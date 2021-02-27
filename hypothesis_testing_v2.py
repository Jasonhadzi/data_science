# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind, f_oneway, chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# load data
heart = pd.read_csv('heart_disease.csv')

print(heart.head())

#Is thalach associated with whether or not a patient will ultimately be diagnosed with heart disease?
sns.boxplot(data=heart, x='heart_disease',y='thalach')
plt.show()
plt.clf()
#patients diagnosed with heart disease generally had a lower maximum heart rate during their exercise test.
thalach_hd = heart.thalach[heart.heart_disease=='presence']
thalach_no_hd= heart.thalach[heart.heart_disease=='absence']
mean_diff = np.mean(thalach_no_hd) - np.mean(thalach_hd)
print('`thalach` mean Difference: ', mean_diff)

# run two-sample t-test
#Null: The average thalach for a person with heart disease is equal to the average thalach for a person without heart disease.
#Alternative: The average thalach for a person with heart disease is NOT equal to the average thalach for a person without heart disease.
tstat, pval = ttest_ind(thalach_hd, thalach_no_hd)
print('p-value for `thalach` two-sample t-test: ', pval)
#pval less than 0.05 we reject the null hypothesisand conclude that there is a significant difference in thalach for people with heart disease compared to people without heart disease.

#investigate at least one other quantitative variable
sns.boxplot(x=heart.heart_disease, y=heart.age)
plt.show()
plt.clf()

#Create a set of side-by-side box plots of thalach for each chest pain type in the data
sns.boxplot(data=heart,x=heart.cp, y=heart.thalach)
plt.show()
plt.clf()

thalach_typical = heart.thalach[heart.cp == "typical angina"]
thalach_asymptom = heart.thalach[heart.cp == "asymptomatic"]
thalach_nonangin = heart.thalach[heart.cp == "non-anginal pain"]
thalach_atypical = heart.thalach[heart.cp == "atypical angina"]
#Run a single hypothesis test to address the following null and alternative hypotheses:
#Null: People with typical angina, non-anginal pain, atypical angina, and asymptomatic people all have the same average thalach.
#Alternative: People with typical angina, non-anginal pain, atypical angina, and asymptomatic people do not all have the same average thalach.

pval = f_oneway(thalach_typical,thalach_asymptom,thalach_nonangin,thalach_atypical)[1]

print(pval)

#Run another hypothesis test to determine which of those pairs are significantly different.
#Use an overall type I error rate of 0.05 for all six comparisons.

turkey_results = pairwise_tukeyhsd(heart.thalach,heart.cp, 0.05)
print(turkey_results)
#we reject the null hypothesis for asymptomatic   atypical angina, asymptomatic   non-anginal pain, asymptomatic    typical angina

Xtab = pd.crosstab(heart.cp, heart.heart_disease,)
print(Xtab)

#Run a hypothesis test for the following null and alternative hypotheses:
#Null: There is NOT an association between chest pain type and whether or not someone is diagnosed with heart disease.

#Alternative: There is an association between chest pain type and whether or not someone is diagnosed with heart disease.

pval = chi2_contingency(Xtab)[1]
print(pval)
#there is a significant association between these variables.
