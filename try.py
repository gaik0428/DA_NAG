import pandas as pd
import openpyxl as pip
import matplotlib.pyplot as pls

# the regions
others = [[' USA ', ' Canada ', ' Australia ', ' New Zealand ', ' Africa ']]

# read the excel, filter the region & filter the timeframe
whole_df = pd.read_excel(r"C:\Users\Gaik Hwa\PycharmProjects\DA_NAG\Project_File.xlsx")

# rename the blank column
whole_df = whole_df.rename(columns={'   ': 'Date'})

# split the column
date = whole_df["Date"].str.split(' ', n=2, expand=True)
whole_df["Year"] = date[1]
whole_df["Month"] = date[2]
print(whole_df.head())

print(whole_df.columns)

# Filter region & timeframe
whole_df = whole_df.loc[(whole_df['Year'] >= '2008')
                        & (whole_df['Year'] <= '2017')]
relevant_df = whole_df
print(relevant_df)

# remove unnecessary column
relevant_df.pop("Date")
relevant_df.pop("Month")
print(relevant_df)

# change columns' datatypes
relevant_df[[' USA ', ' Canada ', ' Australia ', ' New Zealand ', ' Africa ']].apply(pd.to_numeric)
print(relevant_df.dtypes)

country_df = relevant_df("others")
print(country_df)