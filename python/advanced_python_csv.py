import csv

Emails=[]

with open('/home/sufyan/ds/metis/metisgh/prework/dsp/python/faculty.csv', 'r') as data:
    reader =csv.reader(data, delimiter=',')
    next(reader, None)
    for row in reader:
        Emails.append(row[3])

FilePath="emails.csv"

csv=open(FilePath, "w")
for email in Emails:
    csv.write(email+"\n")#writes emails and \n creates new line
