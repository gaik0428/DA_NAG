import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read excel
whole_df = pd.read_excel(r"C:\Users\Gaik Hwa\PycharmProjects\DA_NAG\Project_File.xlsx")

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
array = total_summed_df.to_numpy()
print(array)

fig = plt.figure(facecolor = 'white', figsize = (10,10))
country = np.array([ ' USA ', ' Canada ', ' Australia ', ' New Zealand ', ' Africa '])
print(country)

plt.bar(country, array)
plt.show()