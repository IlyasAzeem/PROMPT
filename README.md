# PrioRitizatiOn & Management of Pull requesTs (PROMPT) dataset Online Appendix
This repo provides instructions about the schema and use of the PROMPT dataset. PROMPT is a MySql database which contains 236514 pull requests, along with their daily responses, extracted from GitHub. In the following sections, we explained how to replicate your study.

[Table of Contents]
1. [PROMPT Database]
2. [Enitiy Relationship Diagram]
3. [Tables]
4. [Replication Instructions]

## PROMPT Database
The PROMPT database is avialable in compressed format [here](https://github.com/IlyasAzeem/PROMPT/blob/master/Replication_Package/Import_data_to_db). It is a MySql database and to use it one needs to import the database into MySql Community Server.

## Enitiy Relationship Diagram
The PROMPT database consists of seven entities as shown in the figure and the description of each entity is given [here](PR_Algorithm.pdf).

![PROMPT Schema](https://github.com/IlyasAzeem/PROMPT_DB/blob/master/ERD.png)

## Tables
###### Project
Project table contains the basic statistical information about a project e.g. watches, forks etc.
###### Pull_Request
Pull-requests belonging to each project are stored in the Pull_Request table. The Project_Name column is used as a foreign key to link the pull requests to the corresponding project. The Pull_Requet_ID column serves as a primary key and it is used as a foreign key in the rest of the tables to link pull requests with its corresponding comments, reviews etc.
###### Contributor
The contrubutors who took part in a pull request are stored into table Contributor. Private_Repos and Public_Repos represent the number of private and public repositories owned by a contributor. 
###### Reviews
All the reviews belonging to each pull request are combined together and put into one record. The Review_Comments_Count column contains the count of the reviews associated with each pull request. 
###### Comments
Similar to reviews all the user comments belonging to each pull request are combined together and put into one record. The count of the user comments associated with each pull request is stored in the Comment_Count column.
###### Issue
Issue table provides information related to the number of issues associated with a pull request and whether a given pull request is pointing to an issue or not. 
###### Response
The response table contains the daily pull requests response information since it is created until the closing time. The column response label is Boolean which indicates either the pull request is responded on a particular day or not.

## Replication Instructions
In the following sub-section, we describe the steps how did we crawled the pull requests using GitHub API, extracted features from raw data, and then imported the extracted features into the MySql database.
###### Data Crawlers
We used GitHub API V3 to extracted pull requests data from 21 popular GitHub projects since the projects are initiated until February 2018. The data crawling process has been performed in three steps.
1. Organizations: Popular open source projects are generally tied to organizations. Firstly, we crawled more than 2.4 million organizations on the GitHub using the script [crawler-organizations](https://github.com/IlyasAzeem/PROMPT/blob/master/Replication_Package/Data_Crawlers/crawler-organizations.py).
2. Projects Selection:  In order to obtain high-quality experiment data and select projects that are developed in strict accordance with the process of the Pull-based development model we used the script [crawler-projects](https://github.com/IlyasAzeem/PROMPT/blob/master/Replication_Package/Data_Crawlers/crawler-projects.py).
3. Pulls Requests Extraction: The last step in the data crawling was to extract pull requests from the selected projects. We used the script [crawler-PR-features](https://github.com/IlyasAzeem/PROMPT/blob/master/Replication_Package/Data_Crawlers/crawler-PR-features.py) to extracted the pull requests from the selected projects. The extracted pull requests are saved in JSON format in a text file. The zipped file can be found [here](https://github.com/IlyasAzeem/PROMPT/blob/master/Replication_Package/Dataset_CSV_Files/). 
###### Features Extraction
In order to extract features from the raw data used the two scripts [generate_accept_data](https://github.com/IlyasAzeem/PROMPT/blob/master/Replication_Package/Features_Extraction/generate_accept_data.py) and [generate_response_data](https://github.com/IlyasAzeem/PROMPT/blob/master/Replication_Package/Features_Extraction/generate_response_data.py). The first script extracts all the features of the pull requests mentioned in the schema above (except the sentiment and textual labels) with a label representing whether the pull request is accepted or not. Similarly, the second script extracts all the same features of the pull requests along with their daily responses. The label response_label represents whether a given pull request is responded on a given day or not.
###### Sentiment Analysis and Textual Labeling
We used Senti4SD [1], widely applied in Software engineering research, to identify the sentiment of the textual features of the pull requests including title and body together, user comments and review comments.
Pull requests are usually associated with certain maintenance and evolution tasks such as ﬁxing a bug, adding new features, and/or improving existing features. Hence, the type of maintenance and evolution task associated with each PR is crucial to select the set of pull requests to integrate with the next release. For this reason, we used DECA [2], [3], a state-of-the-art tool to categorize development discussions, to classify pull requests title and body according to maintenance and evolution tasks. The final datasets in the csv format with all the features can be found [here](https://github.com/IlyasAzeem/PROMPT/tree/master/Replication_Package/Dataset_CSV_Files) in the zipped format.
###### Import data to MySql
We created a database in MySql Community Server and imported all the pull requests data into the database using python script available [here](https://github.com/IlyasAzeem/PROMPT/blob/master/Replication_Package/Import_data_to_db/import_data_to_db.py). Before importing data to the database we split the accept.csv file into various lists according to the tables in the database. The script used for splitting the accept.csv file is given [here](https://github.com/IlyasAzeem/PROMPT/blob/master/Replication_Package/Import_data_to_db/create_list_for_db.py). For the response table, the daily responses of the pull requests in table Pull_Request are imported from the response.csv. The PROMPT dataset in the database format is avaiable [here](https://github.com/IlyasAzeem/PROMPT/blob/master/Replication_Package/Import_data_to_db).




## References
[1] F.  Calefato,  F.  Lanubile,  F.  Maiorano,  and  N.  Novielli,  “Sentiment polarity  detection  for  software  development,”  Empirical  Softw.  Engg., vol. 23, no. 3, 2018.

[2] A. D. Sorbo, S. Panichella, C. A. Visaggio, M. D. Penta, G. Canfora, and H. C. Gall, “Development emails content analyzer: Intention mining in developer discussions (T),” in International Conference on Automated Software Engineering, ASE 2015, 2015, pp. 12–23.

[3] A. D. Sorbo, S. Panichella, C. A. Visaggio, M. D. Penta, G. Canfora, and  H.  C.  Gall,  “DECA:  development  emails  content  analyzer,”  in International Conference on Software Engineering, 2016, pp. 641–644.
