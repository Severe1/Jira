import csv

def Export(filename, extension, content):
    file = open(filename+extension, 'w')
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow(content)
