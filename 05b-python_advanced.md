# Advanced Python    

### Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.  Note:  Do not use Pandas library to complete this section.  

For Part 1, use of regular expressions is optional.  

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

### Part I - Regular Expressions  


#### Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>> the number of degree-types is 9
the number of 0's is 1. #Assuming '0' means no degree.
the number of PhD's is 31.
the number of ScD's is 6.
the number of BSEd's is 1.
the number of MS's is 2.
the number of MA's is 1.
the number of MD's is 1.
the number of JD's is 1.
the number of MPH's is 2.


#### Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>> the number of title-types is 4
the number of "Assistant Professor is Biostatistics" is 1.
the number of "Associate Professor of Biostatistics" is 12.
the number of "Professor of Biostatistics" is 13.
the number of "Assistant Professor of Biostatistics" is 11.


#### Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

>> ['bellamys@mail.med.upenn.edu', 'warren@upenn.edu', 'bryanma@upenn.edu', 'jinboche@upenn.edu', 'sellenbe@upenn.edu', 'jellenbe@mail.med.upenn.edu', 'ruifeng@upenn.edu', 'bcfrench@mail.med.upenn.edu', 'pgimotty@upenn.edu', 'wguo@mail.med.upenn.edu', 'hsu9@mail.med.upenn.edu', 'rhubb@mail.med.upenn.edu', 'whwang@mail.med.upenn.edu', 'mjoffe@mail.med.upenn.edu', 'jrlandis@mail.med.upenn.edu', 'liy3@email.chop.edu', 'mingyao@mail.med.upenn.edu', 'hongzhe@upenn.edu', 'rlocalio@upenn.edu', 'nanditam@mail.med.upenn.edu', 'knashawn@mail.med.upenn.edu', 'propert@mail.med.upenn.edu', 'mputt@mail.med.upenn.edu', 'sratclif@upenn.edu', 'michross@upenn.edu', 'jaroy@mail.med.upenn.edu', 'msammel@cceb.med.upenn.edu', 'shawp@upenn.edu', 'rshi@mail.med.upenn.edu', 'hshou@mail.med.upenn.edu', 'jshults@mail.med.upenn.edu', 'alisaste@mail.med.upenn.edu', 'atroxel@mail.med.upenn.edu', 'rxiao@mail.med.upenn.edu', 'sxie@mail.med.upenn.edu', 'dxie@upenn.edu', 'weiyang@mail.med.upenn.edu']



#### Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>> the number of unique email domains is 4.
the unique email domains are: 
{'mail.med.upenn.edu', 'cceb.med.upenn.edu', 'email.chop.edu', 'upenn.edu'}

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

### Part II - Write to CSV File

#### Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

#### Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
```
Print the first 3 key and value pairs of the dictionary:

>> Ellenberg
['Ph.D.', 'Professor', 'sellenbe@upenn.edu']
['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
Li
['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu']

#### Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
```

Print the first 3 key and value pairs of the dictionary:

>> ('Susan', 'Ellenberg')
Ph.D.
Professor
sellenbe@upenn.edu

#### Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

>> ('Susan', 'Ellenberg')
['Ph.D.', 'Professor', 'sellenbe@upenn.edu']
('Jonas', 'Ellenberg')
['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
('Yimei', 'Li')
['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu']
('Mingyao', 'Li')
['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu']
('Hongzhe', 'Li')
['Ph.D.', 'Professor', 'hongzhe@upenn.edu']

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

