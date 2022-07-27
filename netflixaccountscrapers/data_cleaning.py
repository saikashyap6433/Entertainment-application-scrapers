import pandas as pd
f = 'netflix.csv'
df = pd.read_csv(f, sep=";")

vector_not_null = df['Email'].notnull()
df_not_null = df[vector_not_null]


df_not_null.to_csv ('test_file_without_null_rows.csv', index = None, header=True, sep=';', encoding='utf-8-sig')
