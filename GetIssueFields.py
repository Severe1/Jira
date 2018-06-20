from jira import JIRA
from Auth import connect_jira
import logging

def GetIssueFields ():
    # create a connection object, jc
    jc = connect_jira("https://ims.everest.nl", "", "")

    # find an issue
    issue = jc.issue("EMSPM-14268")

    key = issue.key
    logging.info("The key found equals "+ key)

    summary = issue.fields.summary
    logging.info("Summary found "+ summary)

    description = issue.fields.description
    logging.info("Description found: "+ description)

    return key, summary, description
