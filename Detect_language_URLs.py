# Import libraries
import pandas as pd
from langdetect import detect 

# Reading the list containing all URLs
df = pd.read_csv(r'C:\Users\lucas\OneDrive\Desktop\url_list.csv')

# Copying the column, removing the URL stem and hyphens
df['text'] = df['0'].str.strip("https://www.dgap.de/dgap/News/adhoc/")
df['text'] = df['text'].str.replace("-"," ")

# Detecting the language
df['lang'] = df['text'].apply(detect)

# Filtering only URLs for English disclosures and delete unneeded columns
df = df[df['lang'] == "en"]
del df['text']
del df['lang']

# Writing the list containing English URLs to CSV
df.to_csv(r'C:\Users\lucas\OneDrive\Desktop\final_url_list.csv', index=False, sep=';')