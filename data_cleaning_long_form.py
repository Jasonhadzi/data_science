## Libraries
import pandas as pd

## Create Long Dataframe
data = pd.DataFrame({"participant": [1,2,3,1,2,3],
                      "attribute": ["age", "age", "age", "income", "income", "income"],
                      "value": [24, 57, 23, 30, 60, 28]})
## Print Dataframe
print(data)

#The pivot method in the pandas package will allow us to reshape the dataset based on the values of a column.
data_tidy = data.pivot(index="participant",
                         columns="attribute",
                         values="value").reset_index()
data_tidy.columns.name = None

 print(data_tidy)

 print(data_tidy[data_tidy["participant"] == 1])
