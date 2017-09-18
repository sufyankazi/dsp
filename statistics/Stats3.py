import random
import thinkstats2
import thinkplot

randlist=[]
for x in range(0,1000):
    randlist.append(random.random())

pmf=thinkstats2.Pmf(randlist, label='Pmf')
cdf=thinkstats2.Cdf(randlist, label='Cdf')


thinkplot.Pmf(pmf)
thinkplot.show(xlabel='num',ylabel='Pmf')
thinkplot.Cdf(cdf)
thinkplot.show(xlabel='num',ylabel='Cdf')
