import logging
from connect import *

def GetIssueFields (issue):
    # find an issue
    jc = connect()
    issue = jc.issue(issue)

    key = issue.key
    logging.info("The key found equals "+ key)

    summary = issue.fields.summary
    logging.info("Summary found "+ summary)

    description = issue.fields.description
    logging.info("Description found: "+ description)

    return key, summary, description
