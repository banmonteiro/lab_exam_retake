import pandas as pd
df = pd.read_csv('input_file.csv')
filter_df = df[(df['Genus'].str.startswith('St'))]
filter_df.to_csv('b2_output1.csv', index=False)