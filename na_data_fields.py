#First we import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#load the file
working_on ='M1'
values = pd.read_excel('nadata.xlsx')

values.head()

# get column names
col_names = values.columns[1:]
#print(col_names)
#get rows
rows = values['Κωδικός πεδίου']
print(rows)


#iterate through columns to create a columns with only the universities name, not the SYNOLO ones

universities = []
for i in range(0,len(col_names),2):
    #print(col_names[i])
    universities.append(col_names[i])

#print(len(universities))


def get_sum_of_row_values(index):
    new_sum_uni = 0
    new_sum_total_uni = 0
    for uni in universities:
        new_sum_uni += values[uni][index]
        new_sum_total_uni += values['ΣΥΝΟΛΟ '+uni][index]
    return new_sum_uni,new_sum_total_uni

def get_percentages(value_a,total):
    percent = value_a/total *100
    return percent

sum_of_each_code_freq = [get_sum_of_row_values(i)[0] for i in range(len(rows)) ]
sum_of_total_uni_freq = [get_sum_of_row_values(i)[1] for i in range(len(rows)) ]

print(sum_of_each_code_freq)
print(sum_of_total_uni_freq)


percentages = [ get_percentages(sum_of_each_code_freq[i],sum_of_total_uni_freq[i]) for i in range(len(rows))]
print(percentages)



#combine codes and percentages
final = list(zip(rows,percentages))
print(final)

#sort the list based on the 2nd element, the percentages we make reverse=True because we want descenting order
reverse_sorted = sorted(final, key = lambda x: x[1], reverse=True)
print(reverse_sorted)


#plt.rcParams["figure.figsize"] = (20, 10) for PDS
#plt.rcParams["figure.figsize"] = (40, 10) for PMS
plt.rcParams["figure.figsize"] = (60, 10)


plt.xlabel("Δεδομένα")
plt.ylabel("Percentage %")
plt.title("Συχνότητα Μη διαθέσιμων πεδίων "+working_on )


#if i want to not inlcude the first x elements,
#maybe because the missing fields are dates and make the other values seem irrelevant
#labels, ys = zip(*reverse_sorted[3:])
labels, ys = zip(*reverse_sorted[:36])

xs = np.arange(len(labels))
#plt.bar(xs, ys, 0.8, align='center') for PDS
plt.bar(xs, ys, 0.8, align='center')

plt.xticks(xs, labels) #Replace default x-ticks with xs, then replace xs with labels
plt.yticks(ys)

plt.savefig('graph_' + working_on+'.png')
