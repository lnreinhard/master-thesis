# Import libraries
from bs4 import BeautifulSoup
import numpy as np
from time import sleep
from random import randint
from selenium import webdriver
import pandas as pd

# Loop: get all URLs from each page
pages = np.arange(0, 7500, 1)
url_collected = []

for page in pages:
    page = "https://www.dgap.de/dgap/News/?newsType=ADHOC&page=" + str(page) + "&limit=20"
    driver = webdriver.Chrome("C:\Program Files\chromedriver_win32\chromedriver.exe")
    driver.get(page)
    sleep(randint(5, 15))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    urls = [item.get("href") for item in soup.find_all("a")]
  
    for u in urls:
        url_collected.append(u)

# Remove empty records
urls_final = list(filter(None, url_collected))

# Only keep records that contain stem
url_final = [x for x in urls_final if x.startswith('/dgap/News/adhoc/')]

# Remove duplicates
url_final = list(dict.fromkeys(url_final))

string = 'https://www.dgap.de'
final_list=[string + s for s in url_final]

df_list = pd.DataFrame(final_list)
df_list.to_csv(r'C:\Users\lucas\OneDrive\Desktop\url_list.csv', index=False)