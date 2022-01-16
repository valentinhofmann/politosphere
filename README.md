# The Reddit Politosphere

This repository contains documentation and scripts for the Reddit Politosphere, a large-scale text and network resource of online political discourse
based on the [Pushshift Reddit Dataset](https://doi.org/10.5281/zenodo.3608135).
The Reddit Politosphere can be downloaded from [Zenodo](https://doi.org/10.5281/zenodo.5851729).

# Scripts
 We provide scripts for easy data access:
 
 - `load_comments.py`: load comments 
 - `load_networks.py`: load comments 


# Comments

The comment files contain all comments posted to the 
political subreddits between 2008 and 2019.


# Networks

The network files contain the weighted and unweighted 
networks between between 2008 and 2019. For the weighted networks, 
the edge weights correspond to the number of users that posted at least 10 comments
in both subreddits. The unweighted networks 
are created by applying statistical network backboning, 
specifically the noise-corrected filter, to the 
weighted networks.

- 

# Subreddit Metadata

# User Metadata

