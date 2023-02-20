
import pandas as pd
import openpyxl as pip

df1 = pd.read_excel(r"C:\Users\Gaik Hwa\PycharmProjects\DA_NAG\Project_File.xlsx",  usecols = 'A, AE, AF, AG, AH, AI')
print(df1)

df2 = df1.loc[360:479]
print(df2)

print(df2.columns)

df2.rename(columns = {'   ':'Date'}, inplace = True)
print(df2)

date = df2["Date"].str.split(' ', n=2, expand = True)
df2["year"] = date[1]
df2["month"] = date[2]
print(df2.head())
