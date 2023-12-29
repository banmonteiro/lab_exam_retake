import pandas as pd 
df = pd.read_csv('input_file.csv')
df['Location'] = df['Location'].str.replace(',','-')
df["HRID"] = df['Location'].astype(str) + "-" + df['Site'].astype(str) + "-" + df['Replicate'].astype(str)
df.to_csv('b6_output1.csv', index=False)