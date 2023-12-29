import pandas as pd 
df = pd.read_csv('input_file.csv')
transposed_df = df.transpose()
transposed_df.to_csv('b7_output1.csv', header=False)