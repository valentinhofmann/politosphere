# The Reddit Politosphere

This repository contains documentation and scripts for the [Reddit Politosphere](https://doi.org/10.5281/zenodo.5851729), a pseudonymized, 
large-scale text and network resource of online political discourse
based on the [Pushshift Reddit Dataset](https://doi.org/10.5281/zenodo.3608135). 

The Reddit Politosphere covers 605 [political subreddits](data/subreddits.txt) between 2008 to 2019.
For each year, it contains:

- all comments posted in the political subreddits together with metadata such as creation time
- networks with the political subreddits as nodes and edges computed on the basis of user overlap

We also release metadata for subreddits and users.

# Scripts

 We provide scripts for easy data access:
 
 - `load_comments.py`, `load_comments.sh`: load comments for specific years and subreddits
 - `load_networks.py`: load networks for specific years

# Comments

The comment files `comments_YYYY-MM.bz2` contain all comments posted in the 
political subreddits between 2008 and 2019. The data fields are identical to the 
Pushshift Reddit Dataset. The author names are converted to random five-character pseudonyms. We add the following two data fields:

- `body_cleaned`: a tokenized, lower-cased, and cleaned version of the comment body 
- `language`: the language of the comment as detected by [CLD2](https://github.com/CLD2Owners/cld2)


# Networks

The network files `networks_YYYY.csv` contain the weighted and unweighted 
networks between 2008 and 2019. The weighted networks
have edge weights corresponding to the number of users that posted at least 10 comments
in both subreddits, excluding bots and automoderators. The unweighted networks 
are created by applying statistical network backboning, 
specifically the [noise-corrected filter](https://www.michelecoscia.com/?pageid=287), to the 
weighted networks. Intuitively, a large weight between
two _large_ subreddits is less indicative of latent associations between the subreddits
than a large weight between two _small_ subreddits.
The noise-corrected filter takes such effects into account when 
converting the weighted into an unweighted network.
The files have the following data fields:

- `node_1`, `node_2`: nodes incident to the undirected edge
- `weighted`: edge weight in the weighted network
- `unweighted`: whether or not the edge exists in the unweighted network

# Subreddit Metadata

The subreddit metadata file `subreddits_metadata.json` lists selected properties of the 
political subreddits. Specifically, it has the following data fields:

- `subreddit`: name of subreddit
- `banned`: whether or not subreddit has been banned by 2022
- `gun`: subreddit with focus on gun control
- `party`: explicit affiliation with democratic `dem` or republican `rep` party`
- `politician`: subreddit devoted to a politician
- `region`: Canada `ca`, Europe `eu`, Middle East `me`, UK `uk`, US states `us` or other regions `world`


# User Metadata

The subreddit metadata file `users_metadata.json` lists selected properties of the 
users (who otherwise are fully pseudonymized). Specifically, it has the following data fields:

- `author`: pseudonymized username
- `automoderator`: whether or not user is automoderator (for filtering)
- `bot`: whether or not user is bot (for filtering)
- `gender`: username containing male `m` or female `f` given name

It further provides information about the presence of frequent classes of 
lexical elements in the usernames:

- `angry`: negative attitude (_angry_, _rogue_, _troll_, _wtf_)
- `anti`: overt negation (_anti_, _downvote_, _fuck_, _stop_)
- `astro`: astro theme (_astro_, _cosm_, _rocket_, _space_)
- `dangerous`: dangerous animal (_beast_, _gorilla_, _shark_, _tiger_, _wolf_)
- `doom`: doom theme (_dead_, _death_, _doom_, _evil_, _zombie_)
- `military`: military title (_c(a)pt_, _colonel_, _commander_, _major_, _sgt_)
- `nobility`: title of nobility (_duke_, _emperor_, _king_, _lord_, _sir_)
- `trump`: reference to Donald Trump (_trump_)


# Citation

Please cite the following paper when using data from the Reddit Politosphere:

```
@inproceedings{hofmann2022politosphere,
    title = {The {R}eddit {P}olitosphere: A Large-Scale Text and Network Resource of Online Political Discourse},
    author = {Hofmann, Valentin and Sch{\"u}tze, Hinrich and Pierrehumbert, Janet},
    booktitle = {Proceedings of the International AAAI Conference on Web and Social Media 16},
    year = {2022}
}
```
