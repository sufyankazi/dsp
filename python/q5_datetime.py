# Hint:  use Google to find python function
from datetime import datetime
####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'

a=datetime.strptime(date_stop, "%m-%d-%Y")
b=datetime.strptime(date_start, "%m-%d-%Y")
c=a-b
print(c.days)

####b)  
date_start = '12312013'  
date_stop = '05282015'  

a=datetime.strptime(date_start, "%m%d%Y")
b=datetime.strptime(date_stop, "%m%d%Y")
c=b-a
print(c.days)


####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'

a=datetime.strptime(date_start, "%d-%b-%Y")
b=datetime.strptime(date_stop, "%d-%b-%Y")
c=b-a
print(c.days)