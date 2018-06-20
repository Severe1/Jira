from GetIssueFields import *
import logging
from ExportCSV import *

# create logger
logging.basicConfig(filename='example.log',level=logging.INFO)

#actual code
key, summary, description = GetIssueFields()

print(key +" "+ summary)
print(description)

Export("export",".txt",key)
