def PrintDict(MyDict):
    NumItems=0
    for key in MyDict:
        if NumItems >= 3: break
        print(key)
        #NumItem=NumItems+1
        for value in MyDict[key]:
            if NumItems >= 3: break
            print(value)
            NumItems = NumItems + 1
            if NumItems >= 3:break
    print("---")

faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
PrintDict(faculty_dict)

professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
PrintDict(professor_dict)

MyList=[]
for key in professor_dict:
    MyList.append(key)
MyList.sort(key=lambda x: x[1])
for item in MyList:
    print(item)
    print(professor_dict[item])