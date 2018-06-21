import pandas as pd
import numpy as np

from Auth import *


def GetStory (issuenr):
    jc = connect()
    issues_in_proj = jc.search_issues('key = '+issuenr, expand='changelog')
    return issues_in_proj

def GetStories (Year, maxResults):
    jc = connect()
    issues_in_proj = jc.search_issues('project=EMSPM AND createdDate > '+str(Year)+'  AND type =  Story ORDER BY createdDate DESC', expand='changelog',maxResults=maxResults)
    return issues_in_proj

def GetTransitions (stories):
    for issue in stories:
        changelog = issue.changelog
        for history in changelog.histories:
            for item in history.items:
                if item.field == 'status':
                    # TODO: Niet printen maar retourneren als tuple
                    print(issue.key + " Date: "+ history.created + " " + item.fromString+" --> "+ item.toString)

def GetTransitionsList (stories):
    row = list()
    for issue in stories:
        changelog = issue.changelog
        for history in changelog.histories:
            for item in history.items:
                if item.field == 'status':
                    # TODO: Niet printen maar retourneren als tuple
                    row.append((issue.key, history.created, item.fromString))
    return row
def GetSubtasks (stories):
    jc = connect()
    for issue in stories:
        subtasks = jc.search_issues('parent = '+issue.key+' AND issuetype = Sub-task ', expand='changelog')
    return subtasks
