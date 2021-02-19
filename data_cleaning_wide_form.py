## Libraries
import pandas as pd

## Create Data
data = pd.DataFrame({"Name":["Annie", "John", "Min-ji", "Ravi", "Lucas"],
    "Test1" : [85,92,88,86,91],
    "Test2" : [78,86,79,90,93],
    "Test3" : [98,90,95,78,88]})
print(data)


## Tidy data
data_tidy = pd.melt(data, id_vars="Name", var_name="Test", value_name="Score")
print(data_tidy)

#we could use the groupby function to calculate the average for each student
data_tidy.groupby(by = "Name").mean()

#Or we could find the average score of each test
data_tidy.groupby(by = "Test").mean()

#We could also get the information about scores greater than 90
data_tidy[data_tidy["Score"] > 90]
