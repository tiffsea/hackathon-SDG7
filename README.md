# hackathon-SDG7
The code in this repository was developed in July 2020 during a University of Sussex HackEvent. The purpose of the HackEvent was to develop tools that assist in the aggregation of SDG7 data from a variety of sources including but not limited to a Web of Science (WoS) data source file from 2018. More information about SDGs and specifically SDG7 can be found on the [UN Goal 7](https://sdgs.un.org/goals/goal7) site.

### Summary
Our approach stores the WoS2018.csv data to a pandas.DataFrame data structure for the purpose of iterating though the Journal_Names and Abstracts. The idea is that given a list of computer-informed journal names, find the journal names that are more valuable for a SDG7 query. To do this, we ask the user for some PDF documents (could be publications, or in our case SDG7 indicator documentation), then we scrap those documents leveraging python scrapping libraries, pre-process the PDF document text, and perform a TFIDF analysis on the tokenised text from those documents. The TFIDF function we developed returns a list of tokens with their TFIDF scores and this list can be sorted in ascending or descending order. The tokens are then evaluated numerically using f-score, recall, and precision. 

Given more time, we would have extended this approach by then selecting the Journal_Names which contain terms from the list of sorted (highest to lowest) TFIDF tokens. Once the computer-informed Journal_Names are selected, we would then perform pre-processing on the Abstract text from those informed Journal_Names to get the highest scores and perform the same evaluation as mentioned before - TFIDF on the tokens, and numerical evaluation using f-score, recall, and precision.

### Using Git cloned repo

##### Installation
- Git installation required
- Python 3+ installation required
- Jupyter Notebook (or alternatively you can use Google Colab) / conda installation required

##### Useful commands
- clone the repo locally: 
  - `git clone https://github.com/tiffsea/hackathon-SDG7.git`
- change directory to new cloned repo: 
  - `cd hackathon-SDG7`
- you will want to make changes to the files, first, create a branch to work with - would be useful to use your name as the branch
  - `git branch` - checks which branch you are currently in (would be `*master`)
  - `git checkout -b YOUR-NAME` - creates a branch called YOUR-NAME (no spaces)
- after you make some changes to the files, you will want to add all your changed files, commit those files, and push to base (web) repo: 
  - `git add --all` - adds all changed files
  - `git commit --all -m "TYPE SOME SHORT MESSAGE HERE"` - commits all files with message "TYPE SOME SHORT MESSAGE HERE"
  - `git push -u origin YOUR-BRANCH-NAME` -pushes upstream to origin changes from YOUR-BRANCH-NAME

##### Usage
- download the `2018_WoS.csv` data
- clone repo
- open `SDG7 Group 3 Code and Documentation.ipynb` jupyter notebook from command line
  - `jupyter notebook`

### Slack
https://app.slack.com/client/T017N7JG7JQ/C017ULZ0WAD

### Docs
- Shared folder: https://sussex.box.com/s/mvj6ffs1sbre1y64drg92yle025x6dlz
- HackMD: https://hackmd.io/JRwBajagRTiEbgjVf0vltw
- Resources: https://sussex.box.com/s/5e4930lgph9m9kw8r9hvo1k73apuo0i9
