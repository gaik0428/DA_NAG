import pandas as pd
import openpyxl as pip
import matplotlib.pyplot as plt

# read excel
whole_df = pd.read_excel(r"C:\Users\LENOVO\Documents\DEG\- Applied scripting\ASP project\project_file.xlsx")

# rename blank column
whole_df = whole_df.rename(columns={'   ':'Date'})

# split Date column to make life easier
date = whole_df["Date"].str.split(' ', n=2, expand = True)
whole_df["Year"] = date[1]
whole_df["Month"] = date[2]
print(whole_df.head())

# filter the regions & timeframe
whole_df = whole_df.loc[(whole_df['Year'] >= '2008')
                        & (whole_df['Year'] <= '2017')]
whole_df = whole_df[[ ' USA ', ' Canada ', ' Australia ', ' New Zealand ', ' Africa ', 'Year']]
relevant_df = whole_df
print(relevant_df)

# change datatypes
relevant_df = relevant_df.astype(int)
print(relevant_df.dtypes)

# find the total over 10 yrs
relevant_df.pop('Year')
total_summed_df = relevant_df.sum().sort_values(ascending=False)
print(total_summed_df)

# Top 3 countries
print(total_summed_df.head(3))

# Visualization
Top_countries_bc = total_summed_df.plot(kind="bar", title = 'International Monthly Visitors for 2008 to 2017', stacked = False ,figsize=(10,10),fontsize=12)
plt.show()
