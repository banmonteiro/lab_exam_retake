import pandas as pd
df = pd.read_csv('input_file.csv')
filter_df = df[(df['Interval'] == '30-0')]
filter_df.to_csv('b1_output1.csv', index=False)