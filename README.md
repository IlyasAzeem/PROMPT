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
## Project
Project table contains the basic statistical information about a project e.g. watches, forks etc.
## Pull Request
Pull requets belonging to each project are stored in Pull Request table. The Project_Name column is used as a foreign key to link the pull requests to the corresponding project. The Pull_Requet_ID column serve as a primary key and it is used as a foreign key in the rest of the tables to link a pull requests with its corresponding comments, reviews etc.
## Contributor
The contrubutors who took part in a pull request are stored into table Contributor. Private_Repos and Public_Repos represent the number of private and public repositories owned by a contributor. 
## Reviews
All the reviews belonging to each pull request are combined together and put into one record. The Review_Comments_Count column contains the count of the reviews associated to each pull request. 
## Comments
Similar to to reviews the all the user comments belonging to each pull request are combine together and put into one record. The count of the user comments associated to each pull request is stored in the Comment_Count column.
## Issue
Issue table provide information related to the number of issues associated with a pull request and whether a given pull request is points to an issue or not. 
## Response
The response table contains the daily pull requests response information since it is created till the closing time. The column response label is Boolean which indicates either the pull request is responded on a particular day or not.

