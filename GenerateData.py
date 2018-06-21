import csv

def WriteHeader(Header):
    file = open("data.csv", 'w')
    writer = csv.writer(file)
    writer.writerow(Header)
    file.close();

def AppendRow(row):
    file = open("data.csv", 'a')
    writer = csv.writer(file)
    writer.writerow(row)
    file.close();
