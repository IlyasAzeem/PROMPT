import mysql.connector

mydb = mysql.connector.connect(
    host = "your host name",
    user = "your user",
    passwd = "your password",
    database = "your db name"
)

my_cursor = mydb.cursor()


# Create a table in testdb

# my_cursor.execute("CREATE TABLE students (student_id INTEGER(10), name VARCHAR(50), nationality VARCHAR(50), contract_expiry_date DATETIME)")

def create_table(query):
    my_cursor.execute(query)
    mydb.commit()
    my_cursor.close()
    print("Table created...")



def create_product_table():
    query = "CREATE TABLE project (ID INT, Project_Name VARCHAR(45) NOT NULL PRIMARY KEY UNIQUE, Project_Age DOUBLE, " \
            "Project_Accept_Rate DOUBLE, Language VARCHAR(45), Watchers INT , Stars INT, Team_Size INT, Forks_Count INT, " \
            "Additions_Per_Week DOUBLE, Deletions_Per_Week DOUBLE, Comments_Per_Merged_PR DOUBLE, Contributor_Num INT, " \
            "Churn_Average DOUBLE, Sunday DOUBLE, Monday DOUBLE, Tuesday DOUBLE, Wednesday DOUBLE, Thursday DOUBLE, " \
            "Friday DOUBLE, Saturday DOUBLE, Close_Latency DOUBLE, Comments_Per_Closed_PR DOUBLE, File_Touched_Average DOUBLE, Merge_Latency DOUBLE)"
    create_table(query)
    # query = "CREATE TABLE product3 (prod_id INT NOT NULL UNIQUE, cat_id INT NOT NULL, prod_name VARCHAR(50), price DOUBLE, " \
    #         "PRIMARY KEY (prod_id), CONSTRAINT cat_id_fk2 FOREIGN KEY (cat_id) REFERENCES testdb.category(cat_id) ON DELETE NO ACTION ON UPDATE NO ACTION)"


def create_pull_request_table():
    query = "CREATE TABLE pull_request (ID INT, Pull_Request_ID VARCHAR(45) NOT NULL PRIMARY KEY UNIQUE, Project_Name VARCHAR(45), " \
            "Title TEXT, Body LONGTEXT, Rebaseable TINYINT(4), Mergeable TINYINT(4), Intra_Branch INT, " \
            "Additions INT, Deletions INT, Day INT, Mergeable_State TINYINT(4), Commits_PR INT, Wait_Time DOUBLE, " \
            "Contain_Fix_Bug INT, PR_Latency DOUBLE, Files_Changed INT, Label_Count INT, url TEXT, Title_Body_Sentiment VARCHAR(30)," \
            " Maintenance_And_Evolution_Category VARCHAR(30), Assignees_Count INT, Workload INT, Commits_Average DOUBLE, Label TINYINT(4)," \
            "CONSTRAINT project_name_fk FOREIGN KEY (Project_Name) REFERENCES project(Project_Name) ON DELETE NO ACTION ON UPDATE NO ACTION)"
    create_table(query)


def create_comments_table():
    query = "CREATE TABLE comments (ID INT NOT NULL PRIMARY KEY, Pull_Request_ID VARCHAR(45) NOT NULL, Participants_Count INT, " \
            "Comments_Embedding LONGTEXT, Comments_Count INT, Last_Comment_Mention TINYINT(4), Comments_Sentiment VARCHAR(30),"\
            "CONSTRAINT PR_ID_fk FOREIGN KEY (Pull_Request_ID) REFERENCES pull_request(Pull_Request_ID) ON DELETE NO ACTION ON UPDATE NO ACTION)"
    create_table(query)


def create_reviews_table():
    query = "CREATE TABLE reviews (ID INT NOT NULL PRIMARY KEY, Pull_Request_ID VARCHAR(45) NOT NULL, " \
            "Review_Comments_Embedding LONGTEXT, Review_Comments_Count INT, Reviews_Sentiment VARCHAR(30),"\
            "CONSTRAINT PR_ID_fk1 FOREIGN KEY (Pull_Request_ID) REFERENCES pull_request(Pull_Request_ID) ON DELETE NO ACTION ON UPDATE NO ACTION)"
    create_table(query)

def create_issue_table():
    query = "CREATE TABLE issue (ID INT NOT NULL PRIMARY KEY, Pull_Request_ID VARCHAR(45) NOT NULL, " \
            "Point_To_IssueOrPR TINYINT(4), Open_Issues INT,"\
            "CONSTRAINT PR_ID_fk2 FOREIGN KEY (Pull_Request_ID) REFERENCES pull_request(Pull_Request_ID) ON DELETE NO ACTION ON UPDATE NO ACTION)"
    create_table(query)


def create_response_table():
    query = "CREATE TABLE response (ID INT NOT NULL PRIMARY KEY, Pull_Request_ID VARCHAR(45) NOT NULL, " \
            "response_label TINYINT(4),"\
            "CONSTRAINT PR_ID_fk3 FOREIGN KEY (Pull_Request_ID) REFERENCES pull_request(Pull_Request_ID) ON DELETE NO ACTION ON UPDATE NO ACTION)"
    create_table(query)


def create_contributor_table():
    query = "CREATE TABLE contributor (ID INT NOT NULL PRIMARY KEY, Pull_Request_ID VARCHAR(45) NOT NULL, " \
            "Contributor INT, Private_Repos INT, Followers INT, Closed_Num INT, Public_Repos INT, " \
            "Organization_Core_Member TINYINT(4), Accept_Num INT, User_Accept_Rate DOUBLE, Contributions INT, " \
            "Closed_Num_Rate DOUBLE, Following INT, Prev_PRs INT,"\
            "CONSTRAINT PR_ID_fk4 FOREIGN KEY (Pull_Request_ID) REFERENCES pull_request(Pull_Request_ID) ON DELETE NO ACTION ON UPDATE NO ACTION)"
    create_table(query)





if __name__ == '__main__':
    print("Create Tables")

    create_product_table()
    create_pull_request_table()
    create_comments_table()
    create_reviews_table()
    create_issue_table()
    create_response_table()
    create_contributor_table()
