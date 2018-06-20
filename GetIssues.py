from connect import *

def GetIssues (Year):
    jc = connect()
    issues_in_proj = jc.search_issues('project=EMSPM')
    all_proj_issues_but_mine = jc.search_issues('project=EMSPM and assignee != currentUser()')
    print(issues_in_proj)
    # Summaries of my last 3 reported issues
    for issue in jc.search_issues('assignee = currentUser() order by created desc', maxResults=3):
        print('{}: {}'.format(issue.key, issue.fields.summary))
