import pandas as pd


print('Writing to a new csv:')
data = pd.read_csv('add your csv file here')
filtered_data = data.dropna(axis='columns', how='all')
#print(filtered_data)
filtered_data.to_csv('sortedData_new.csv', index=False)
# return true
