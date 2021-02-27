# import libraries
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp, binom_test

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

#investigate cholesterol levels for patients with heart disease. Use the dataset yes_hd to save cholesterol levels for patients with heart disease as a variable named chol_hd.
chol_hd = yes_hd.chol

print(chol_hd)
#find the mean
chol_mean = np.mean(chol_hd)

print(chol_mean)

#Do people with heart disease have high cholesterol levels (greater than or equal to 240 mg/dl) on average?

#Null: People with heart disease have an average cholesterol level equal to 240 mg/dl

#Alternative: People with heart disease have an average cholesterol level that is greater than 240 mg/dl

tstat, pval= ttest_1samp(chol_hd,240)
#divide the p-value by two (in order to run the one-sided test)
print(pval/2)

#less than 0.05, suggesting that heart disease patients have an average cholesterol level significantly higher than 240 mg/dl.


#repeat above steps but with patients who were not diagnosed with heart disease

no_chol_hd = no_hd.chol
print(np.mean(no_chol_hd))


tstat, pval= ttest_1samp(no_chol_hd,240)
print(pval/2)


num_patients = len(heart)
print(num_patients)
#Calculate the number of patients with fasting blood sugar greater than 120.
num_highfbs_patients = np.sum(heart.fbs == 1)

print(num_highfbs_patients)

print(0.08*num_patients)

#Does this sample come from a population in which the rate of fbs > 120 mg/dl is equal to 8%?

#Null: This sample was drawn from a population where 8% of people have fasting blood sugar > 120 mg/dl

#Alternative: This sample was drawn from a population where more than 8% of people have fasting blood sugar > 120 mg/dl

p_value = binom_test(num_highfbs_patients, n=num_patients, p=0.08, alternative='greater')

print(p_value)
#less than 0.05, indicating that this sample likely comes from a population where more than 8% of people have fbs > 120 mg/dl.
