import pandas as pd
import numpy as np

car_eval = pd.read_csv('car_eval_dataset.csv')
#print(car_eval.head())

index = car_eval.manufacturer_country.value_counts()[3]
print(index)

print(car_eval.manufacturer_country.value_counts(normalize=True))

# Convert buying_cost to type 'category' using the list you created in the previous exercise.
possible_vls =car_eval.buying_cost.unique()
buying_cost_categories = ['low','med','high','vhigh']


# Calculate the median category of the buying_cost variable and print the result.
car_eval.buying_cost = pd.Categorical(car_eval.buying_cost, buying_cost_categories, ordered=True)

median_index = np.median(car_eval.buying_cost.cat.codes)
median = buying_cost_categories[int(median_index)]

print(median)

luggage_prop = car_eval.luggage.value_counts(normalize=True)
print(luggage_prop)

luggage_prop_drop_na= car_eval.luggage.value_counts(dropna=False,normalize=True)
print(luggage_prop_drop_na)
#no missing values

five_or_more_cars = (car_eval.doors == '5more').sum()
five_or_more_cars_prop = (car_eval.doors == '5more').mean()

print(five_or_more_cars)
print(five_or_more_cars_prop)
