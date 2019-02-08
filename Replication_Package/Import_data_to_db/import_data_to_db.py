import mysql.connector
import pandas as pd


df = pd.read_csv('Add the lists here one by one',
                         sep=',', encoding='utf-8')


mydb = mysql.connector.connect(
    host = "your host name",
    user = "your user",
    passwd = "your password",
    database = "your db name"
)

my_cursor = mydb.cursor()


def insert_comments():
    query = "INSERT INTO comments (ID, Pull_Request_ID, Participants_Count, Comments_Embedding, Comments_Count, " \
            "Last_Comment_Mention, Comments_Sentiment) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    for index, row in df.iterrows():
        my_cursor.execute(query, (row['ID'], row['Pull_Request_ID'], row['Participants_Count'], row['Comments_Embedding'],
                                  row['Comments_Count'], row['Last_Comment_Mention'], row['Comments_Sentiment']))
        mydb.commit()
        print("Processing record #: %s", row['ID'])
    my_cursor.close()

def insert_reviews():
    query = "INSERT INTO reviews (ID, Pull_Request_ID, Review_Comments_Embedding, Review_Comments_Count, Reviews_Sentiment)" \
            " VALUES (%s, %s, %s, %s, %s)"
    for index, row in df.iterrows():
        my_cursor.execute(query, (row['ID'], row['Pull_Request_ID'], row['Review_Comments_Embedding'],
                                  row['Review_Comments_Count'], row['Reviews_Sentiment']))
        mydb.commit()
        print("Processing record #: ", row['ID'])
    my_cursor.close()

def insert_issue():
    query = "INSERT INTO issue (ID, Pull_Request_ID, Point_To_IssueOrPR, Open_Issues)" \
            " VALUES (%s, %s, %s, %s)"
    for index, row in df.iterrows():
        my_cursor.execute(query, (row['ID'], row['Pull_Request_ID'], row['Point_To_IssueOrPR'],
                                  row['Open_Issues']))
        mydb.commit()
    my_cursor.close()


def insert_response():
    query = "INSERT INTO response (ID, Pull_Request_ID, response_label)" \
            " VALUES (%s, %s, %s)"
    for index, row in df.head(100).iterrows():
        my_cursor.execute(query, (row['ID'], row['Pull_Request_ID'], row['response_label']))
        mydb.commit()
        print("Processing record #: ", row['ID'])
    my_cursor.close()


def insert_project():
    query = "INSERT INTO project (ID, Project_Name, Project_Age, Project_Accept_Rate, Language, Watchers, Stars, " \
            "Team_Size, Forks_Count, Additions_Per_Week, Deletions_Per_Week, Comments_Per_Merged_PR, Contributor_Num, Churn_Average," \
            "Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Close_Latency, Comments_Per_Closed_PR," \
            "File_Touched_Average, Merge_Latency) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
            "%s, %s, %s, %s, %s, %s, %s, %s, %s))"
    for index, row in df.iterrows():
        my_cursor.execute(query, (row['ID'], row['Project_Name'], row['Project_Age'], row['Project_Accept_Rate'], row['Language'],
                                  row['Watchers'], row['Stars'], row['Team_Size'], row['Forks_Count'],
                                  row['Additions_Per_Week'], row['Deletions_Per_Week'], row['Comments_Per_Merged_PR'], row['Contributor_Num'],
                                  row['Churn_Average'], row['Sunday'], row['Monday'], row['Tuesday'], row['Wednesday'],
                                  row['Friday'], row['Thursday'], row['Saturday'], row['Close_Latency'], row['Comments_Per_Closed_PR'],
                                  row['File_Touched_Average'], row['Merge_Latency']))
        print("Processing record #: ", row['ID'])
        mydb.commit()
    my_cursor.close()


def insert_contributor():
    query = "INSERT INTO contributor (ID, Pull_Request_ID, Contributor, Private_Repos, Followers, Closed_Num, Public_Repos, " \
            "Organization_Core_Member, Accept_Num, User_Accept_Rate, Contributions, Closed_Num_Rate, Following, Prev_PRs)" \
            " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    for index, row in df.head(100).iterrows():
        my_cursor.execute(query, (row['ID'], row['Pull_Request_ID'], row['Contributor'], row['Private_Repos'], row['Followers'],
                                  row['Closed_Num'], row['Public_Repos'], row['Organization_Core_Member'], row['Accept_Num'],
                                  row['User_Accept_Rate'], row['Contributions'], row['Closed_Num_Rate'], row['Following'],
                                  row['Prev_PRs']))
        mydb.commit()
        print("Processing record #: ", row['ID'])
    my_cursor.close()


def insert_pull_request():
    query = "INSERT INTO pull_request (ID, Pull_Request_ID, Project_Name, Title, Body, Rebaseable, Mergeable, Intra_Branch, " \
            "Additions, Deletions, Day, Mergeable_State, Commits_PR, Wait_Time, Contain_Fix_Bug, PR_Latency, Files_Changed, " \
            "Label_Count, url, Title_Body_Sentiment, Maintenance_And_Evolution_Category, Assignees_Count, Workload, Commits_Average, Label)" \
            " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
            "%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    for index, row in df.head(100).iterrows():
        my_cursor.execute(query, (row['ID'], row['Pull_Request_ID'], row['Project_Name'], row['Title'], row['Body'],
                                  row['Rebaseable'], row['Mergeable'], row['Intra_Branch'], row['Additions'], row['Deletions'],
                                  row['Day'], row['Mergeable_State'], row['Commits_PR'], row['Wait_Time'], row['Contain_Fix_Bug'],
                                  row['PR_Latency'], row['Files_Changed'], row['Label_Count'], row['url'], row['Title_Body_Sentiment'],
                                  row['Maintenance_And_Evolution_Category'], row['Assignees_Count'], row['Workload'], row['Commits_Average'],
                                  row['Label']))
        mydb.commit()
        print("Processing record #: ", row['ID'])
    my_cursor.close()





if __name__ == '__main__':
    print("MySql Queries")

    # insert_project()

    # insert_pull_request()

    # insert_issue()

    # insert_reviews()

    # insert_comments()

    # insert_response()

    # insert_contributor()


    print("Done ...")