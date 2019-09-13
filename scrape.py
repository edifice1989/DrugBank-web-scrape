import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get("https://www.drugbank.ca/drugs/DB09061")
soup = BeautifulSoup(page.content, 'html.parser')
hugo=pd.read_table('/Users/e32659/Desktop/grant/hugo',sep='\t')
period_tags = soup.select('dd.col-md-7.col-sm-6')
periods = [pt.get_text() for pt in period_tags]
for ele in periods:
    if ele in hugo['Approved symbol'].values:
        print(ele, end=',')
