import pandas as pd
df = pd.read_csv('input_file.csv')
filter = df['Scientific Name'].unique()
filter_df = pd.DataFrame({'Scientific Name': filter})
filter_df.to_csv('b3_output1.csv', index=False)