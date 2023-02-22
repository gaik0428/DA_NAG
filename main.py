import pandas as pd
import openpyxl as pip
import matplotlib.pyplot as pls

# read the excel, filter the region & filter the timeframe
relevant_df = pd.read_excel(r"C:\Users\LENOVO\Documents\DEG\- Applied scripting\ASP project\project_file.xlsx",  usecols = 'A, AE, AF, AG, AH, AI')
relevant_df = relevant_df.loc[360:479]
print(relevant_df)

# to find the column names
print(relevant_df.columns)

# rename the blank column
relevant_df = relevant_df.rename(columns={'   ':'Date'})
print(relevant_df)

# split the column
date = relevant_df["Date"].str.split(' ', n=2, expand = True)
relevant_df["Year"] = date[1]
relevant_df["Month"] = date[2]
print(relevant_df.head())

# remove unnecessary column
relevant_df.pop('Date')
relevant_df.pop('Month')
print(relevant_df)

# change columns' datatypes
relevant_df[[ ' USA ', ' Canada ', ' Australia ', ' New Zealand ', ' Africa ']].apply(pd.to_numeric)
print(relevant_df.dtypes)

# sum the regions over 10 yrs [ separate ] in a new dataframe
yr_summed_df = relevant_df.groupby('Year').sum()
yr_summed_df.loc["Sum"] = yr_summed_df.sum(axis=0)
print(yr_summed_df)

# Only the total sum for visualization
total_summed_df = yr_summed_df.iloc[[10]]
print(total_summed_df)

# visualization for top 3 countries over 10 yrs
Top_countries_bc = total_summed_df.plot(kind="bar", title = 'International Monthly Visitors for 2008 to 2017', stacked = False ,figsize=(10,10), legend =True,fontsize=12)
pls.show()

# Top 3 Countries in order : Australia, USA & New Zealand

