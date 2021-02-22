import codecademylib3

# Import pandas with alias
import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)

print(census.head())

#first_name categorical-nominal string
#last_name categorical-nominal string
#birth_year quantitative-discrete int
#voted categorical-binary nominal bool
#num_children quantitative-sicrete int
#income_year quantitative-continuous float
#higher_tax categorical-ordinal string
#marital_status categorical-ordinal string


#print(census.birth_year.unique())


#replace missing value with 1967

census['birth_year'] = census['birth_year'].replace(['missing'],1967)

print(census.birth_year.unique())

census['birth_year'] = census['birth_year'].astype('int')
print(census.dtypes)

print(census.birth_year.mean())


# set an order to the higher_tax variable so that: strongly disagree < disagree < neutral < agree < strongly agree.

census.higher_tax = pd.Categorical(census.higher_tax,['strongly disagree','disagree','neutral','agree','strongly agree',], ordered = True)

print(census['higher_tax'].unique())

#Using cat.code to tlabel encode the higher_tax variabl
census['higher_tax'] = census['higher_tax'].cat.codes

print(census['higher_tax'].mean())

#One-Hot Encode marital_status to create binary variables of each category.
census = pd.get_dummies(data=census, columns=['marital_status'])

print(census.head())
