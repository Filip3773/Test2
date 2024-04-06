import pandas as pd


data = pd.read_csv('songs_normalize.csv' )

max_values = data.max()
min_values = data.min()

average_values = data.mean()

percentage_difference = ((max_values - average_values) / average_values) * 100


selected_column = 'duration_ms'  
normalized_column = (data[selected_column] - data[selected_column].min()) / (data[selected_column].max() - data[selected_column].min())


data[selected_column] = normalized_column

data.to_csv('updated_dataset.csv', index=False)
