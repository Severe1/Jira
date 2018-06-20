# This module connect to the jira database
# Takes a config.txt file with line
# server=username=password
#
#

from jira import JIRA
from Auth import connect_jira

def connect():
    file = open("config.txt", "r").read();
    server,user,passw = file.split("=")
    # create a connection object, jc
    return connect_jira(server, user, passw)

connect()
