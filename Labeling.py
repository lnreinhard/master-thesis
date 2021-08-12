# Import library
import pandas as pd

# Read in FactSet data (stock returns) and news
df_factset = pd.read_excel('data/factset/factset_data.xlsx', sheet_name = "data")
df_news = pd.read_csv('data/adhoc_clean.csv')

# Join dataframes 
df_final = df_news.join(df_factset, rsuffix='_f' )

# Remove line breaks, duplicate columns, records with NA cells and reset index
df_final = df_final.replace('\n',' ', regex=True)
df_final = df_final.drop(columns=['datetime_f', 'identifier_f'])
df_final.dropna(inplace=True)
df_final.reset_index(inplace=True, drop=True)

# Check if lengths of input dataframes are equal and how many records remain after joining
print("Length factset:", len(df_factset))
print("   Length news:", len(df_news))
print("  Length final:", len(df_final))

# Replacement function for labeling
def three_labels(x):
    if x <= -1:
        return 'negative'
    if x >= 1:
        return 'positive'
    if x > -1:
        return 'neutral'

# Create subset for headlines, 3 classes, 24 hour market-adjusted return
# Remove unnecessary columns
df_headline_3_24_return_adj = df_final.drop(columns=['datetime', 'identifier', 'text', '24_return','48_return','48_return_adj','72_return','72_return_adj'])

# Apply replacement function
df_headline_3_24_return_adj['24_return_adj'] = df_headline_3_24_return_adj['24_return_adj'].apply(three_labels)

# Rename columns and save
df_headline_3_24_return_adj = df_headline_3_24_return_adj.rename(columns={"24_return_adj": "label", "headline": "text"})
df_headline_3_24_return_adj.to_csv('data/finbert_input/headline_3_24_return_adj.csv', index=False, header=False, sep='}')