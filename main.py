import logging

from JiraFunctions import *
from GenerateData import *

# create logger
logging.basicConfig(filename='example.log',level=logging.INFO)

WriteHeader(("Key","EndTimestamp","Summary","Status"))
#actual code
#key, summary, description = GetIssueFields("EMSPM-14628")
def EnkeleStory(story):
    story = GetStory(story)
    subtasks = GetSubtasks(story)
    result = GetTransitionsList(subtasks)
    for row in result:
        AppendRow(row)

def AlleStories():
    stories = GetStories(2018, maxResults="500")
    for story in stories:
        EnkeleStory(story.key)
AlleStories()
