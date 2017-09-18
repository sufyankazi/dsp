import nsfg
import thinkstats2
import thinkplot

#from thinkstats2
def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf

nk=nsfg.ReadFemResp().numkdhh
nkpmf=thinkstats2.Pmf(nk, label='actual')

nkpmfbias=BiasPmf(nkpmf, label='biased')


thinkplot.Pmfs([nkpmf,nkpmfbias])
thinkplot.show(xlabel='num kids',ylabel='Probability')

print("the mean of the actual pmf is "+str(nkpmf.Mean()))
print("the mean of the biased pmf is "+str(nkpmfbias.Mean()))