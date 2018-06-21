import logging

from JiraFunctions import *
from GenerateData import *

# create logger
logging.basicConfig(filename='example.log',level=logging.INFO)

WriteHeader(("Key","EndTimestamp","Status"))
#actual code
#key, summary, description = GetIssueFields("EMSPM-14628")
def EnkeleStory():
    story = GetStory("EMSPM-14847")
    subtasks = GetSubtasks(story)
    result = GetTransitionsList(subtasks)
    for row in result:
        AppendRow(row)

def AlleStories():
    stories = GetStories(2018, maxResults="50")
    Key, EndTimestamp, Status =  GetTransitions(stories)

EnkeleStory()
