import pandas as pd
import openpyxl as pip

# read the excel & filter the region
df1 = pd.read_excel(r"C:\Users\LENOVO\Documents\DEG\- Applied scripting\ASP project\project_file.xlsx",  usecols = 'A, AE, AF, AG, AH, AI')
print(df1)

# filter the region
df2 = df1.loc[360:479]
print(df2)

print(df2.columns)

# rename the blank column
df3 = df2.rename(columns={'   ':'Date'})
print(df3)

# split the column
date = df3["Date"].str.split(' ', n=2, expand = True)
df3["Year"] = date[1]
df3["Month"] = date[2]
print(df3.head())

# remove unnecessary column
df3.pop('Date')
df3.pop('Month')
print(df3)

# change columns' datatypes
df3[[ ' USA ', ' Canada ', ' Australia ', ' New Zealand ', ' Africa ']].apply(pd.to_numeric)
print(df3.dtypes)

# sum the regions over 10 yrs
sum_df = df3.groupby('Year').sum()
print(sum_df)
