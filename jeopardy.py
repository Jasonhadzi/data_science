import pandas as pd
pd.set_option('display.max_colwidth', -1)

df =  pd.read_csv('jeopardy.csv')

df.rename(columns= lambda title: title[1:] if title[0] == ' ' else title, inplace=True)

#print(df['Question'])
list_of_words = ["King", "England"]


def search_words(data,words):
#lambda function uses the all function to check if all elements of the input list are in the question.
#Returns true if all of the words in the list appear in the question.
  filter = lambda x: all( word.lower() in x.lower() for word in words)

  return data.loc[data['Question'].apply(filter)]

filtered_df = search_words(df,list_of_words)

#print(filtered_df['Question'])

#print(df['Value'].unique())
# Adding a new column. If the value of the float column is not "None", then we cut off the first character (which is a dollar sign), and replace all commas with nothing, and then cast that value to a float. If the answer was "None", then we just enter a 0.

df['float value'] = df['Value'].apply(lambda  x: float(x[1:].replace(',','') ) if x!= 'None' else 0)

filtered_df = search_words(df,'King')

print(filtered_df['float value'].mean())


def get_unique_answers(data):
  return data['Answer'].value_counts()


print(get_unique_answers(filtered_df))
