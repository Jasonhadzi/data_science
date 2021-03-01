# Import libraries
import codecademylib3
import pandas as pd
import numpy as np
from scipy.stats import binom_test, f_oneway,chi2_contingency

# Read in the `clicks.csv` file as `abdata`
abdata = pd.read_csv('clicks.csv')

print(abdata.head())

# We are interested in whether visitors are more likely to make a purchase if they are in any one group compared to the others.

Xtab = pd.crosstab(abdata.group, abdata.is_purchase)

print(Xtab)

pval = chi2_contingency(Xtab)[1]
print(pval)
#pval less than 0.05 so there is significant difference between A,B,C

#What we really want to know is whether each price point allows us to make enough money that we can exceed some target goal. Brian, how much do you think it cost to build this feature?

# we need to generate a minimum of $1000 in revenue per week in order to justify this project.

#In order to justify this feature, we will need to calculate the necessary purchase rate for each price point. Let’s start by calculating the number of visitors to the site this week.

num_visits = len(abdata)
print(num_visits)

#we need to calculate the number of visitors who would need to purchase the upgrade package at each price point ($0.99, $1.99, $4.99) in order to generate Brian’s minimum revenue target of $1,000 per week.

#calculate the number of sales that would be needed to reach $1,000 dollars of revenue at each price point

num_sales_needed_099 = np.ceil(1000/0.99)
print(num_sales_needed_099)
num_sales_needed_199 = np.ceil(1000/1.99)
print(num_sales_needed_199)
num_sales_needed_499 = np.ceil(1000/4.99)
print(num_sales_needed_499)

#Now that we know how many sales we need at each price point, calculate the proportion of weekly visitors who would need to make a purchase in order to meet that goal.

p_sales_needed_099 = num_sales_needed_099/num_visits
print(p_sales_needed_099)
p_sales_needed_199 = num_sales_needed_199/num_visits
print(p_sales_needed_199)
p_sales_needed_499 = num_sales_needed_499/num_visits
print(p_sales_needed_499)

#To start, we want to know if the percent of Group A (the $0.99 price point) that purchased an upgrade package is significantly greater than p_sales_needed_099 (the percent of visitors who need to buy an upgrade package at $0.99 in order to make our minimum revenue target of $1,000).

#To answer this question, we want to focus on just the visitors in group A. Then, we want to compare the number of purchases in that group to p_sales_needed_099.

#Since we have a single sample of categorical data and want to compare it to a hypothetical population value, a binomial test is appropriate.

#we need to know two pieces of information:
#The number of visitors in group A (the number of visitors who were offered the $0.99 price point)
#The number of visitors in Group A who made a purchase

samp_size_099 = len(abdata[abdata.group=='A'])
sales_099 = np.sum((abdata.group=='A')&(abdata.is_purchase=='Yes'))

print(samp_size_099)
print(sales_099)

samp_size_199 = len(abdata[abdata.group=='B'])
sales_199 = np.sum((abdata.group=='B')&(abdata.is_purchase=='Yes'))

samp_size_499 = len(abdata[abdata.group=='C'])
sales_499 = np.sum((abdata.group=='C')&(abdata.is_purchase=='Yes'))

#in this case, we want to know if the observed purchase rate is significantly 'greater' than the purchase rate that results in the minimum revenue target.
pvalueA = binom_test(sales_099,samp_size_099, p=p_sales_needed_099, alternative = 'greater')
print(pvalueA)
pvalueB = binom_test(sales_199,samp_size_199, p=p_sales_needed_199, alternative = 'greater')
print(pvalueB)
pvalueC = binom_test(sales_499,samp_size_499, p=p_sales_needed_499, alternative = 'greater')
print(pvalueC)

#only pvalue C is less than 0.05 so only for group C the purchase rate was significantly higher than the target

#Brian should charge $4.99 for the upgrade.
