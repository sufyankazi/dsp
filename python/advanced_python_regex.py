import csv


types=0
DegreeTypes=[]
TitleTypes=[]
Emails=[]
EmailDomains=[]

with open('/home/sufyan/ds/metis/metisgh/prework/dsp/python/faculty.csv', 'r') as data:
    reader =csv.reader(data, delimiter=',')
    next(reader, None)
    for row in reader:
        CurrentDegree=row[1].replace(".","").strip()
        TitleTypes.append(row[2])
        Emails.append(row[3])
        if " " not in CurrentDegree:
            DegreeTypes.append(CurrentDegree)
        else:
            templist=CurrentDegree.split(" ")
            for i in templist: DegreeTypes.append(i)
        EmailDomains.append(row[3].split('@')[-1])

types=len(set(DegreeTypes))
SetDT=set(DegreeTypes)
print('the number of degree-types is '+str(len(SetDT))+'.')
for degree in SetDT:
    print('the number of '+degree+'\'s is '+str(DegreeTypes.count(degree))+'.')

SetTT=set(TitleTypes)
print('the number of title-types is '+str(len(SetTT))+'.')
for title in SetTT:
    print('the number of \"'+title+'\" is '+str(TitleTypes.count(title))+'.')
print("the list of emails is: ")
print(Emails)
print("the number of unique email domains is "+str(len(set(EmailDomains)))+".")
print("the unique email domains are: ")
print(set(EmailDomains))

FilePath="emails.csv"

csv=open(FilePath, "w")
for email in Emails:
    csv.write(email+"\n")#writes emails and \n creates new line
