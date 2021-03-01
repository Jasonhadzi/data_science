# Import libraries
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp, ttest_ind, chi2_contingency
# Load datasets
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')

print(lifespans.head())

#The first thing we want to know is whether Familiar’s most basic package, the Vein Pack, actually has a significant impact on the subscribers

vein_pack_lifespans = lifespans.lifespan[lifespans.pack=='vein']

average_lifespan_vein_pack = np.mean(vein_pack_lifespans)
print(average_lifespan_vein_pack)

#We have a single sample of lifespans and we want to compare the mean of this sample to a hypothetical population value of 73 years.
# Lifespans are a quantitative variable.
# we will use one sample t-test

#Null: The average lifespan of a Vein Pack subscriber is 73 years.
#Alternative: The average lifespan of a Vein Pack subscriber is NOT 73 years.

tstat, pval = ttest_1samp(vein_pack_lifespans, 73)
print(pval)
#pval is less than 0.05, we reject the null hypothesis

#compare this lifespan data between our different packages. Our next step up from the Vein Pack is the Artery Pack

artery_pack_lifespans = lifespans.lifespan[lifespans.pack=='artery']

print(np.mean(artery_pack_lifespans))

#find out if the average lifespan of a Vein Pack subscriber is significantly different from the average life expectancy for the Artery Pack.

#Null: The average lifespan of a Vein Pack subscriber is equal to the average lifespan of an Artery Pack subscriber.

#Alternative: The average lifespan of a Vein Pack subscriber is NOT equal to the average lifespan of an Artery Pack subscriber.

#looking at an association between two variables: whether a subscriber got the Vein Pack or Artery Pack (a binary categorical variable) and their lifetime (a quantitative variable).

#we will conduct a two sample t test

ttest,pval = ttest_ind(vein_pack_lifespans,artery_pack_lifespans)
print(pval)
#output is 0.0558 larger than 0.05 so it is not significantly different. We keep the null hypothesis


print(iron.head())


#Is there an association between the pack that a subscriber gets (Vein vs. Artery) and their iron level?

#create contigency table
Xtab = pd.crosstab(iron.pack,iron.iron)
print(Xtab)
#Null: There is NOT an association between which pack (Vein vs. Artery) someone subscribes to and their iron level.

#Alternative: There is an association between which pack (Vein vs. Artery) someone subscribes to and their iron level.
chi2,pval,dof,expected = chi2_contingency(Xtab)

print(pval)
#pval is lower than 0.05 so we reject the null hypothesis, there is a significant association
