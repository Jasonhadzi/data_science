# Import libraries
import numpy as np
import pandas as pd
import codecademylib3
from scipy.stats import binom_test, f_oneway,chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Import data
dogs = pd.read_csv('dog_data.csv')

# Subset to just whippets, terriers, and pitbulls
dogs_wtp = dogs[dogs.breed.isin(['whippet', 'terrier', 'pitbull'])]

# Subset to just poodles and shihtzus
dogs_ps = dogs[dogs.breed.isin(['poodle', 'shihtzu'])]


print(dogs.head())

#FetchMaker estimates (based on historical data for all dogs) that 8% of dogs in their system are rescue

#They would like to know if whippets are significantly more or less likely than other dogs to be a rescue.

whippet_rescue = dogs.is_rescue[dogs.breed=='whippet']

#print(whippet_rescue)
#How many whippets are rescues?
num_whippet_rescues = np.sum(whippet_rescue==1)

num_whippets = len(whippet_rescue)

#Use a hypothesis test to test the following null and alternative hypotheses:

#Null: 8% of whippets are rescues
#Alternative: more or less than 8% of whippets are rescues

#we have a samlpe of binary data: 0,1 and we want to compare a sample frequency to a population value: whipets

#we will use a binom test

pval = binom_test(num_whippet_rescues,num_whippets, p =0.08 )

print(pval)
#pval more than 0.05 so the null hypothesis is true

#Is there a significant difference in the average weights of these three dog breeds (mid sized dogs)

wt_whippets = dogs_wtp.weight[dogs_wtp.breed == 'whippet']
wt_terriers =dogs_wtp.weight[dogs_wtp.breed == 'terrier']
wt_pitbulls =dogs_wtp.weight[dogs_wtp.breed == 'pitbull']

#Null: whippets, terriers, and pitbulls all weigh the same amount on average

#Alternative: whippets, terriers, and pitbulls do not all weigh the same amount on average (at least one pair of breeds has differing average weights)

fstat, pval = f_oneway(wt_whippets,wt_terriers,wt_pitbulls)
print(pval)
#less than 0.05, so we reject the null hypothesis

#we conduct a Tukey's range test

results = pairwise_tukeyhsd(dogs_wtp.weight,dogs_wtp.breed)

print(results)
#we reject the NH for pitbull-terrier, terrier - whippet

#create a contingency table of dog colors by breed (poodle vs. shihtzu). Save the table as Xtab and print it out.

Xtab = pd.crosstab(dogs_ps.breed, dogs_ps.color)
print(Xtab)

#Null: There is an association between breed (poodle vs. shihtzu) and color.

#Alternative: There is not an association between breed (poodle vs. shihtzu) and color.

#we compare two categorical values -> chi square
chi2,pval,dof,expected = chi2_contingency(Xtab)

print(pval)
#pval less tha 0.05 we reject the null hypothesis
