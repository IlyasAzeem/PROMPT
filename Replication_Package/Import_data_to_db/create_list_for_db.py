import pandas as pd
import csv
import re
import nltk.data

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')


accept_data = pd.read_csv("accept.csv", sep=",", encoding="ISO-8859-1")
response_data = pd.read_csv("response.csv", sep=',', encoding='ISO-8859-1')

lists_path = "E:\Research Work\Sentiment Analysis Project\Dataset\\Title_Body"

Project = ['Project_Name', 'Project_Age', 'Project_Accept_Rate', 'Language', 'Watchers', 'Stars', 'Team_Size', 'Additions_Per_Week',
               'Deletions_Per_Week', 'Comments_Per_Merged_PR', 'Contributor_Num', 'Churn_Average',
               'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Close_Latency',
               'Comments_Per_Closed_PR', 'Forks_Count', 'File_Touched_Average', 'Merge_Latency']

Comments = ['Pull_Request_ID', 'Participants_Count', 'Comments_Embedding', 'Comments_Count', 'Last_Comment_Mention', 'Comments_Sentiment']

Pull_Request = ['Pull_Request_ID','Project_Name', 'Title', 'Body', 'Rebaseable', 'Mergeable', 'Intra_Branch', 'Additions',
                    'Deletions', 'Day', 'Mergeable_State', 'Commits_PR', 'Wait_Time', 'Contain_Fix_Bug', 'PR_Latency',
                    'Files_Changed', 'Label_Count', 'url', 'Title_Body_Sentiment', 'Maintenance_And_Evolution_Category',
                    'Assignees_Count', 'Workload', 'Commits_Average', 'Label']

Contributor = ['Pull_Request_ID', 'Contributor', 'Private_Repos', 'Followers', 'Closed_Num', 'Public_Repos',
                   'Organization_Core_Member', 'Accept_Num', 'User_Accept_Rate', 'Contributions', 'Closed_Num_Rate',
                   'Following', 'Prev_PRs']

Reviews = ['Pull_Request_ID', 'Review_Comments_Embedding', 'Review_Comments_Count', 'Reviews_Sentiment']

Issue = ['Pull_Request_ID', 'Point_To_IssueOrPR', 'Open_Issues']

Response = ['Pull_Request_ID', 'response_label']


def Create_List(df ,columns_list, file_name):
    # Select the columns for project list
    my_list = df[columns_list]
    # print(my_list.shape)
    # print(my_list.columns)
    # print(my_list.dropna().shape)
    # Save the list
    my_list.dropna().to_csv(lists_path+"\\"+file_name+".csv", sep=',',
               encoding='utf-8', index=True)


def Remove_Extra_Whitespaces(text):
    text = ' '.join(str(text).split())
    return text

def clean_text (text):
    text = re.sub('#\d+', 'ISSUE NUMBER', text)
    text = re.sub('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', 'EMAIL', text)
    text = re.sub('\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', 'URL', text, flags=re.MULTILINE)
    text = re.sub('@\w+', 'CONTRIBUTOR', text)
    text = re.sub(',', '', text)
    pattern = re.compile('^[a-zA-Z0-9\'-]+$')
    raw_statements = tokenizer.tokenize(text.strip())
    text_list = ""
    for statement in raw_statements:
        # print(statement[:-1])
        # print(statement[-1])
        statement_without_end_char = statement[:-1]
        end_char = statement[-1]
        for word in statement_without_end_char.split():
            if pattern.match(word):
                text_list += " " + word
        text_list += end_char
    text_list = re.sub('^\s+', '', text_list, flags=re.UNICODE)
    return text_list

def Create_Project_List(df, columnslist, filename):
    project_list = df[columnslist]
    # Assign a name ID to the index
    # Select the latest statistics of the project e.g. forks, watchers etc.
    project_list = project_list.groupby(['Project_Name']).max()
    project_list.index.rename('ID', inplace=True)
    project_list.to_csv(lists_path + "\\" + filename + ".csv", sep=',',
                            encoding='utf-8', index=True)

def Create_Comments_List(df, columnslist, filename):
    pd.options.mode.chained_assignment = None
    comments_list = df[columnslist]
    # Assign a name ID to the index
    comments_list.index.rename('ID', inplace=True)
    # Remove extra whitespaces from the comments
    comments_list['Comments_Embedding'] = comments_list.astype(str).apply(lambda x: Remove_Extra_Whitespaces(x['Comments_Embedding']), axis=1)
    comments_list.dropna().to_csv(lists_path + "\\" + filename + ".csv", sep=',',
                            encoding='utf-8', index=True)

def Create_Reviews_List(df, columnslist, filename):
    pd.options.mode.chained_assignment = None
    reviews_list = df[columnslist]
    # Assign a name ID to the index
    reviews_list.index.rename('ID', inplace=True)
    # Remove extra whitespaces from the comments
    reviews_list['Review_Comments_Embedding'] = reviews_list.astype(str).apply(lambda x: Remove_Extra_Whitespaces(x['Review_Comments_Embedding']), axis=1)
    reviews_list.dropna().to_csv(lists_path + "\\" + filename + ".csv", sep=',',
                            encoding='utf-8', index=True)


def Create_Pull_Request_List(df, columnslist, filename):
    pd.options.mode.chained_assignment = None
    Pull_Request_list = df[columnslist]
    # Assign a name ID to the index
    Pull_Request_list.index.rename('ID', inplace=True)
    # Remove extra whitespaces from the comments
    Pull_Request_list['Body'] = Pull_Request_list.astype(str).apply(lambda x: Remove_Extra_Whitespaces(x['Body']), axis=1)
    Pull_Request_list.to_csv(lists_path + "\\" + filename + ".csv", sep=',',
                            encoding='utf-8', index=True)


def Create_Contributor_List(df, columnslist, filename):
    pd.options.mode.chained_assignment = None
    Contributor_list = df[columnslist]
    # Assign a name ID to the index
    Contributor_list.index.rename('ID', inplace=True)
    print(Contributor_list.shape)
    print(Contributor_list.dropna().shape)
    # Remove extra whitespaces from the comments
    Contributor_list.to_csv(lists_path + "\\" + filename + ".csv", sep=',',
                            encoding='utf-8', index=True)


def Create_Issue_List(df, columnslist, filename):
    pd.options.mode.chained_assignment = None
    Issue_list = df[columnslist]
    # Assign a name ID to the index
    Issue_list.index.rename('ID', inplace=True)
    # Remove extra whitespaces from the comments
    Issue_list.to_csv(lists_path + "\\" + filename + ".csv", sep=',',
                            encoding='utf-8', index=True)


def Create_Response_List(df, rep_df, columnslist, filename):
    pd.options.mode.chained_assignment = None
    Response_list = rep_df[columnslist]
    # Select daily responses of those pull requests which are presnt in pull request table
    ID_list = df['Pull_Request_ID']
    final_response_list = Response_list.loc[Response_list.Pull_Request_ID.isin(ID_list)]
    # Assign a name ID to the index
    final_response_list.index.rename('ID', inplace=True)
    # Remove extra whitespaces from the comments
    final_response_list.head(5).to_csv(lists_path + "\\" + filename + ".csv", sep=',',
                            encoding='utf-8', index=True)




if __name__ == '__main__':
    print("Welcome to PR sentiment analysis")

    # The following method call creates a list for project table
    # Create_Project_List(accept_data, Project, 'file_name')

    # The following method call creates a list for comments table
    # Create_Comments_List(accept_data, Comments, 'file_name')

    # The following method call creates a list for reviews table
    # Create_Reviews_List(accept_data, Reviews, 'temp')

    # The following method call creates a list for Pull request table
    # Create_Pull_Request_List(accept_data, Pull_Request, 'file_name')

    # The following method call creates a list for contributor table
    # Create_Contributor_List(accept_data, Contributor, 'temp')

    # The following method call creates a list for issue table
    # Create_Issue_List(accept_data, Issue, 'temp')

    # The following method call creates a list for response table
    # Create_Response_List(accept_data, response_data, Response, 'file_name')

