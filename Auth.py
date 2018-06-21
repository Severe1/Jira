# This module connect to the jira database
# Takes a config.txt file with line
# server=username=password
#
#
import logging
from jira.client import JIRA

# create logger
log = logging.getLogger(__name__)

# Defines a function for connecting to Jira
def connect_jira(jira_server, jira_user, jira_password):
    '''
    Connect to JIRA. Return None on error
    '''
    try:
        log.info("Connecting to JIRA: %s" % jira_server)
        jira_options = {'server': jira_server}
        jira = JIRA(options=jira_options, basic_auth=(jira_user, jira_password))
                                        # ^--- Note the tuple
        return jira
    except Exception as e:
        log.error("Failed to connect to JIRA: %s" % e)
        return None

def connect():
    file = open("config.txt", "r").read();
    server,user,passw = file.split("\n")[0].split('=')
    # create a connection object, jc
    return connect_jira(server, user, passw)

connect()
