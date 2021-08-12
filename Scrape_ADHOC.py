# Import libraries
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pandas as pd
import csv
from tqdm.auto import tqdm

# Read URL list 
final_list = []
with open(r'C:\Users\lucas\OneDrive\Desktop\final_url_list.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        final_list.append(row[0])

# Create empty list
data = []

# Loop over each URL in the final list and retrieve date, identifier, headline and text
for i in tqdm(range(0,len(final_list))):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path=r'C:\Program Files\geckodriver-v0.29.1-win64\geckodriver.exe')
    url = final_list[i]  
    driver.get(url)    
    sleep(randint(3,7))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    try:
        date = soup.find('div', {'class': 'column left_col'}).find('h2')
        data.append(date.text.strip())  
    except:
        date = 0
        data.append('NA')

    try:
        identifier = soup.find("strong", text="ISIN:").next_sibling
        data.append(identifier.strip())
    except:
        identifier = 'NA'
        data.append('NA')

    try:
        header = soup.find(class_='news_header')
        data.append(header.text.strip())
    except:
        header = 'NA'
        data.append('NA')

    try:
        news = soup.find(class_='break-word news_main')
        data.append(news.text.strip()) 
    except:
        news = 'NA'
        data.append('NA')
    
    driver.close()
        

# Create datafrane    
df = pd.DataFrame()

# Assign data to dataframe columns
df['datetime'] = data[0::4]
df['identifier'] = data[1::4]
df['headline'] = data[2::4]
df['news'] = data[3::4]

# Remove new line spaces and records containing NA cells
df['news'] = df['news'].str.replace('\n',' ')
df = df[df.datetime != 'NA']

#Convert datetime column to datetime format
df['datetime']  = df['datetime'].str[14:25] + "" + df['datetime'].str[27:32]
df['datetime'] = pd.to_datetime(df['datetime'])

df.to_csv(r'C:\Users\lucas\OneDrive\Desktop\final\adhoc_messages.csv', index=False, sep='|')