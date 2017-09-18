def COHEN(Frame1, Frame2):
    CD=(Frame1.mean()-Frame2.mean())
    SD=((Frame1.std()**2+Frame2.std()**2)/2)**.5
    CD=CD/SD
    return CD


import thinkstats2, first

live, firsts, others = first.MakeFrames() #Gets data from dataframe python. taken from solutions obvs

TotalW=live.totalwgt_lb
FirstW=firsts.totalwgt_lb
OtherW=others.totalwgt_lb

MyCohen=COHEN(FirstW, OtherW)
NotMyCohen=thinkstats2.CohenEffectSize(FirstW,OtherW)

FirstPMean=firsts.prglngth.mean()
OtherPMean=others.prglngth.mean()

print("the mean weight of first babies is "+str(FirstW.mean())+" lbs")
print("the mean weight of other babies is "+str(OtherW.mean())+" lbs")
print("the Cohen's d between the two sets is "+str(MyCohen))
print("the mean pregnancy length of first babies was "+str(FirstPMean)+" weeks")
print("the mean pregnancy length of other babies was "+str(OtherPMean)+" weeks")
print("the difference between the pregnancy lengths was "+str(FirstPMean-OtherPMean))