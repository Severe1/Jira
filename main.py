import logging

from GetIssueFields import *
from GetIssues import *
from ExportCSV import *

# create logger
logging.basicConfig(filename='example.log',level=logging.INFO)

#actual code
key, summary, description = GetIssueFields("EMSPM-14628")
GetIssues(2017)
Export("export",".txt",key)
