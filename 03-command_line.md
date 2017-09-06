# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > show current working directory path: **pwd**
 creating a directory: **mkdir**
 deleting a directory: **rmdir**
 creating a file using `touch` command: **touch mytextfile.txt**
 deleting a file: **rm**
 renaming a file: **mv originalpath__filename new_path_filename**
 listing hidden files: **ls -a**
 copying a file from one directory to another: **mv filepath/name newfilepath/name**
 
 remove a directory with files: **rm -t directoryname**
 list files and sort by size: **ls -lS**

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls`  : lists visible files in working directory
`ls -a`  : lists hidden files and visible files in wd
`ls -l`  : lists visible files with persmissions in wd
`ls -lh`  : lists visible files with sizes in human readable formats
`ls -lah`  : lists visible and hidden files with sizes in human readable formats
`ls -t`  : lists visible files sorted by date modified 
`ls -Glp`  : lists visible files in long format with slashes added to directories without group names

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -R **lists files displays subdirectories**
 ls -lu **lists files ordered by order accessed**
 ls  -m **lists files as a comma separated list**
 ls -F **lists files with flags**
 ls -i **lists files with inodes**

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs uses text from a standard text input and executes it as a command. For example: **xargs find -name
*.py** would find files that ended with file extension py. 

 

