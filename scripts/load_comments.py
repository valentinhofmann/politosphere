import argparse

import pandas as pd


def main():

    # Read file name
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default=None, type=str, required=True, help='Path to comments file')
    args = parser.parse_args()

    # Define large number to make chunking work
    n_r = 2 ** 100

    for c in pd.read_json(args.file, compression='bz2', lines=True, dtype=False, chunksize=10000, nrows=n_r):
        # Process comments here
        pass


if __name__ == '__main__':
    main()
