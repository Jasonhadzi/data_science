import pandas as pd

country = pd.read_csv("country.csv")

# Extract Country abbreviation and Feature from 'Country_Feature' using regular expressions
sep = country["Country_Feature"].str.extract("(\D{3})(\D{3})")

# Name Columns "Country" and "Feature"
sep.columns = ["Country", "Feature"]

# Merge country and sep
country = pd.concat([country, sep], axis = 1)

# Drop 'Country_Feature' column
country = country.drop(['Country_Feature'], axis = 1)

# Sort Columns to 'Country', 'Feature', and 'Observation'
country = country[["Country", "Feature", "Observation"]]

# Print country
print(country)
