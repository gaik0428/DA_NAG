import pandas as pd
df1 = pd.read_excel("Project_File.xlsx", usecols = 'A, AE, AF, AG, AH, AI')
df2 = df1.loc[360:480]
df2 
