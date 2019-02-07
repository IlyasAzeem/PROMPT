# PrioRitizatiOn & Management of Pull requesTs (PROMPT) dataset Online Appendix
This repo provides instructions about the schema and use to PROMPT dataset. PROMPT is a MySql database which contains 236514 pull requests, along with their daily resposnes, extracted from GitHub. In the following sections we explained how to replicate your study.

Table of Contents
1. PROMPT Database
2. Enitiy Relationship Diagram
3. Tables
4. Replication Instructions

# PROMPT Database
The PROMPT database is aviable in compressed format here. It is a MySql database and to use it one need to improt the database into MySql Community Server.

# Enitiy Relationship Diagram
The PROMPT database consists for seven entities as shown in the figure and the description of each enitity is given [here](PR_Algorithm.pdf).

![PROMPT Schema](https://github.com/IlyasAzeem/PROMPT_DB/blob/master/ERD.png)

# Tables
###### Project
Project table contains the basic statistical information about a project e.g. watches, forks etc.
###### Pull Request
Pull requets belonging to each project are stored in Pull Request table. The Project_Name column is used as a foreign key to link the pull requests to the corresponding project. The Pull_Requet_ID column serve as a primary key and it is used as a foreign key in the rest of the tables to link a pull requests with its corresponding comments, reviews etc.
###### Contributor
The contrubutors who took part in a pull request are stored into table Contributor. Private_Repos and Public_Repos represent the number of private and public repositories owned by a contributor. 
###### Reviews
All the reviews belonging to each pull request are combined together and put into one record. The Review_Comments_Count column contains the count of the reviews associated to each pull request. 
###### Comments
Similar to to reviews the all the user comments belonging to each pull request are combine together and put into one record. The count of the user comments associated to each pull request is stored in the Comment_Count column.
###### Issue
Issue table provide information related to the number of issues associated with a pull request and whether a given pull request is points to an issue or not. 
###### Response
The response table contains the daily pull requests response information since it is created till the closing time. The column response label is Boolean which indicates either the pull request is responded on a particular day or not.

# Replication Instructions
In the following sub-section we describe the steps how did we crawled the pull requests using GitHub API, extracted features from raw data, and then imported the extracted features into MySql database.
###### Data Crwalers
We used GitHub API V3 to extracted pull requests data from 21 popular GitHub projects since the projects are initiated till February 2018. The data crwaling process has been performed in three steps.
1. Organizations: Popular open source projects are generally tied to organizations. Firstly, we crawled more than 2.4 million organizations on the GitHub using the script [crawler-organizations](Data_Crawlers/crawler-orginizations.py).
2. Projects Selection:  In order to obtain high-quality experiment data and select projects that are developed in strict accordance with the process of the Pull-based development model we used the script [crawler-projects](Data_Crawlers/crawler-projects.py).
3. Pulls Requests Extraction: The last step in the data crwaling was to extract pull requests fromt the selected projects. We used the script [crawler-pull-request-number](Data_Crawlers/crawler-pull-request-number.py) to extracted the pull requests from the selected projects. The extracted pull requests are saved in json format in a text file available [here](Features_Extraction/filter-raw-data.txt). 
###### Features Extraction
In order to extrat features from the raw data used the two scripts [generate_accept](Features_Extraction/generate_accept.py) and [generate_response](Features_Extraction/generate_response.py). The first script extracts all the features of the pull requests mentioned in the schema above (except the sentiment and textual labels) with a label representing whether the pull request is accepted or not. Similarly, the second script extracts all the same features of the pull requests along with their daily responses. The label response_label represents whether a given pull request is responded on a given day or not.
