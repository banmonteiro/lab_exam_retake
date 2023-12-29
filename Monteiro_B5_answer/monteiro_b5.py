import pandas as pd
df = pd.read_csv('input_file.csv')
filter_df = df[(df['Scientific Name'] == 'Pomacentrus adelus')]
average_count = filter_df['Count'].mean()
pd.DataFrame({'Average Count':[average_count]}).to_csv('b5_output1.csv', index=False)