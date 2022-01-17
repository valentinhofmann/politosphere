import argparse
import re

import pandas as pd


def main():

    # Read arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--comments_file', default=None, type=str, required=True, help='Comments file')
    parser.add_argument('--subreddits_file', default=None, type=str, required=False, help='Subreddits file')
    parser.add_argument('--target_dir', default=None, type=str, required=False, help='Directory to store comments')
    args = parser.parse_args()

    # Read subreddits
    if args.subreddits_file:
        with open(args.subreddits_file, 'r') as f:
            subreddits = set(f.read().strip().split('\n'))

    # Load comments in chunks
    comments = list()
    for c in pd.read_json(args.comments_file, compression='bz2', lines=True, dtype=False, chunksize=10000):
        if args.subreddits_file:
            c = c[c.subreddit.isin(subreddits)]
            # Perform further filtering here
        comments.append(c)
    comments = pd.concat(comments, sort=True)

    # Store extracted comments
    if args.target_dir:
        target_file = '{}/comments_extracted_{}.json'.format(
            args.target_dir, re.findall(r'\d{4}-\d{2}', args.comments_file)[0]
        )
        comments.to_json(
            target_file,
            orient='records',
            lines=True
        )


if __name__ == '__main__':
    main()
