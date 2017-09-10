# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> most importantly, lists are dynamically sized while tuples are fixed. elements can therefore be added to or deleted from lists. tuples can work as keys in dictionaries. because lists are mutable, their hash values will not let the user find their dictionary keys even if they are modified to be visibly identical.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> both lists and sets are mutable. however, set require items to be hashable, does not allow duplicates, and takes constant time to find an item. list takes N time to find an item, but can be ordered and can contain duplicates. I would use list when the position of an item is important and set when the existence of an item is important.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> lambda is a single expression function that does not have a name in namespace. It can be very easy to read because they are short and can be combined with other functions. to create a function that returns the sum of two numbers I can write:
mysum = lambda a,b: a+b
This will return a+b
to use lambda with sorted you can write something like:
sorted ([(5,6,2),(1,5,1),(3,4,3)], key=lambda x: x[2])
This would sort the list by the 3rd element of each object.
---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> list comprehensions are ways to pythonically use list elements to efficiently create new lists. For example:
Ex1:
MyList=[1,2,3,4,5,6]
MyFirstList=[x+2 for x in MyList]

MySecondList=list(map(lambda x:x+2,MyList))

MyThirdList=list(filter(lambda x:x>4,MySecondList))

map executes a certain action on all elements of a list. filter filters elements of a list. a list comprehension is more pythonic, but can do both types of actions efficiently.

mySet=set(MyList)
myNewSet={x**3 for x in mySet}

myDict={'apples':5,'oranges':2,'monkeys':999}
myNewDict={x:y*2 for x,y in myDict.items()}
---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> a=datetime.strptime(date_stop, "%m-%d-%Y")
b=datetime.strptime(date_start, "%m-%d-%Y")
c=a-b
print(c.days)

```
date_start = '12312013'  
date_stop = '05282015'  
```

>> a=datetime.strptime(date_start, "%m%d%Y")
b=datetime.strptime(date_stop, "%m%d%Y")
c=b-a
print(c.days)

c.  
```
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
```

>> a=datetime.strptime(date_start, "%d-%b-%Y")
b=datetime.strptime(date_stop, "%d-%b-%Y")
c=b-a
print(c.days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





