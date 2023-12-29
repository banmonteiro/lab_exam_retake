import pandas as pd
df = pd.read_csv('input_file.csv')
filter = df[['Scientific Name', 'Size Est (cm)']].drop_duplicates()
filter.to_csv('b4_output1.csv', index=False)