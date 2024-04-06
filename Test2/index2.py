import pandas as pd

data = pd.read_csv('songs_normalize.csv')

positive_corr = data.corr().unstack().sort_values(ascending=False).drop_duplicates()
negative_corr = data.corr().unstack().sort_values().drop_duplicates()

with open('correlation_results.txt', 'w', encoding='utf-8') as f:
    f.write("Najveća pozitivna korelacija: \n")
    f.write(str(positive_corr.head(1)))
    f.write("\n\nNajveća negativna korelacija: \n")
    f.write(str(negative_corr.head(1)))

