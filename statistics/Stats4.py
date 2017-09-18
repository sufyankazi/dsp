import scipy.stats as stats

mu=178
sig=7.7
lbound=stats.norm.cdf(177.8, loc=mu, scale=sig)
ubound=stats.norm.cdf(185.42, loc=mu, scale=sig)
print(str((ubound-lbound)*100)+'% of the US male population is height-eligible to apply to blue man group')