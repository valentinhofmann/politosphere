# The Reddit Politosphere

This repository contains documentation and scripts for the [Reddit Politosphere](https://doi.org/10.5281/zenodo.5851729), a large-scale text and network resource of online political discourse
based on the [Pushshift Reddit Dataset](https://doi.org/10.5281/zenodo.3608135). 

The Reddit Politosphere covers 605 [political subreddits](data/subreddits.txt) between 2008 to 2019.
For each year, it contains:

- all comments posted in the political subreddits together with metadata such as creation time
- networks with the political subreddits as nodes and edges computed on the basis of user overlap

We also release metadata for subreddits and users.

# Scripts

 We provide two scripts for easy data access:
 
 - `load_comments.py`: load comments for specific years and subreddits
 - `load_networks.py`: load networks for specific years

# Comments

The comment files contain all comments posted in the 
political subreddits between 2008 and 2019. The data fields are identical to the 
Pushshift Reddit Dataset. We add the following two data fields:

- `body_cleaned`: a tokenized, lower-cased, and cleaned version of the comment body 
- `language`: the language of the comment as detected by [CLD2](https://github.com/CLD2Owners/cld2)


# Networks

The network files contain the weighted and unweighted 
networks between between 2008 and 2019. The weighted networks
have edge weights corresponding to the number of users that posted at least 10 comments
in both subreddits. The unweighted networks 
are created by applying statistical network backboning, 
specifically the [noise-corrected filter](https://www.michelecoscia.com/?pageid=287), to the 
weighted networks. The files have the following data fields:

- `node_1`, `node_2`: nodes incident to the undirected edge
- `weighted`: edge weight in weighted network
- `unweighted`: edge status in unweighted network (1: edge, 0: no edge)

# Subreddit Metadata

# User Metadata

