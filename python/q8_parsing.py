# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


import csv
MinDiff=9000
with open('football.csv', 'r') as data:
    reader =csv.reader(data, delimiter=',')
    next(reader, None)
    for row in reader:
        if (int(row[5])-int(row[6]))<MinDiff:
            Team=row[0]
            MinDiff=(int(row[5])-int(row[6]))
print('The team with the smallest difference between for and against goals was '+Team)