import pandas as pd
import numpy as np

from Auth import *


def GetStory (issuenr):
    jc = connect()
    issues_in_proj = jc.search_issues('key = '+issuenr, expand='changelog')
    return issues_in_proj

def GetStories (Year, maxResults):
    jc = connect()
    issues_in_proj = jc.search_issues('project=EMSPM AND createdDate > "'+str(Year)+'-01-01"  AND type =  Story AND assignee != null ORDER BY createdDate DESC  ', expand='changelog',maxResults=maxResults)
    return issues_in_proj

def GetTransitions (stories):
    for issue in stories:
        changelog = issue.changelog
        for history in changelog.histories:
            for item in history.items:
                if item.field == 'status':
                    # TODO: Niet printen maar retourneren als tuple
                    print(issue.key + " Date: "+ history.created + " " + item.fromString+" --> "+ item.toString)

def StripSummary(text):
    text = text.replace("CLONE - ","")
    if text.lower().find("bouw") != -1 or text.find("BE") != -1 or  text.find("TE") != -1:
        text = "Bouw"

    if text.lower().find("done") != -1 or text.lower().find("dod") != -1 :
        text = "Definition of done"

    if text.lower().find("uitvoer") != -1 or text.lower().find("test") != -1 :
        text = "Uitvoeren systeemtest"

    if text.lower().find("voorbereid") != -1 or text.lower().find("voor") != -1 :
        text = "Voorbereiden systeemtest"

    if text.lower().find("pm") != -1 :
        text = "PM-aanpassing"

    return text

def GetTransitionsList (stories):
    row = list()
    for issue in stories:
        changelog = issue.changelog
        for history in changelog.histories:
            for item in history.items:
                if item.field == 'status':
                    # TODO: Niet printen maar retourneren als tuple
                    row.append((issue.key, history.created, StripSummary(issue.fields.summary), item.fromString))
    return row
def GetSubtasks (stories):
    jc = connect()
    for issue in stories:
        subtasks = jc.search_issues('parent = '+issue.key+' AND issuetype = Sub-task ', expand='changelog')
    return subtasks
