from jira import JIRA
jira = JIRA('https://ims.everest.nl')
issue = jira.issue('JRA-9')
print(issue.fields.project.key) # 'JRA'
print(issue.fields.issuetype.name) # 'New Feature'
print(issue.fields.reporter.displayName) # 'Mike Cannon-Brookes [Atlassian]'


jira = JIRA(basic_auth=(un, pwd), options={'server': server})
