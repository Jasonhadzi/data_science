import codecademylib3
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
financial_data = pd.read_csv('financial_data.csv')

print(financial_data.head())

month = financial_data['Month']
revenue = financial_data['Revenue']
expenses = financial_data['Expenses']

plt.plot(month,revenue)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')
plt.show()

plt.clf()

plt.plot(month,expenses)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Expenses')

plt.show()


expense_overview = pd.read_csv('expenses.csv')

print(expense_overview.head())

expense_categories = expense_overview['Expense']
expense_proportions = expense_overview['Proportion']

plt.clf()

label_names = expense_categories

plt.pie(expense_proportions, labels=label_names)
plt.axis('equal')
plt.tight_layout()
plt.title('Expense cateories')
plt.show()
#update the pie chart so that all categories making up less than 5% of the overall expenses (Equipment, Utilities, Supplies, and Food) are collapsed into an “Other” category.
expense_categories = ['Salaries', 'Advertising', 'Office Rent', 'Other']

proportions = [0.62, 0.15, 0.15, 0.08]

plt.clf()

label_names = expense_categories

plt.pie(proportions, labels=expense_categories,autopct='%0.1f%%')
plt.axis('equal')
plt.tight_layout()
plt.title('Expense cateories')
plt.show()


employees = pd.read_csv('employees.csv')

print(employees.head())

sorted_productivity = employees.sort_values(by=['Productivity'])
print(sorted_productivity)

employees_cut = sorted_productivity.head(100)
print(employees_cut)

#explore the relationship between Income and Productivity

#productivity is a feature that ranges from 0-100, but income is measured in the thousands of dollars.
#there are outliers in the data that add an additional layer of complexity.


transformation = 'standardization'
#Since there are outliers in the data, Sarah should use standardization in this situation. Unlike normalization, standardization does not have a bounding range.

#Once the standardization is complete, all the features will have a mean of zero, a standard deviation of one, and therefore, the same scale.
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
data_prod = scaler.fit_transform(employees.drop(columns=['Name','Commute Time']))

#print(data_prod)
plt.clf()
plt.plot(data_prod[0],data_prod[1])
plt.show()

commute_times = employees['Commute Time']

print(commute_times)

print(commute_times.describe())

plt.clf()

plt.hist(commute_times)
plt.title("Employee Commute Times")
plt.xlabel("Commute Time")
plt.ylabel("Frequency")
plt.show()

#right skewed
plt.clf()
#we will apply a log transformation

commute_times_log = np.log(commute_times)

plt.hist(commute_times_log)
plt.title("Employee Commute Times Normalized")
plt.xlabel("Commute Time")
plt.ylabel("Frequency")
plt.show()
