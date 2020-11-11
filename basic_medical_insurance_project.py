# Create calculate_insurance_cost() function below:
def calculate_insurance_cost(name,age,sex,bmi,num_of_children,smoker):
  cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost for "+ name+ " is " + str(cost) + " dollars.")
  return cost

# Estimate Maria's insurance cost
insurance_cost = calculate_insurance_cost('Maria',28,0 ,26.2,3,0)

# Initial variables for Omar
name = 'Omar'
age = 35
sex = 1
bmi = 22.2
num_of_children = 0
smoker = 1

# Estimate Omar's insurance cost
insurance_cost = calculate_insurance_cost(name, age,sex,bmi,num_of_children,smoker)
