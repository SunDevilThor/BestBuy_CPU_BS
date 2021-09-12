# Best Buy AMD Ryzen Processor Webscraper
# Python - Beautiful Soup 

import requests
from bs4 import BeautifulSoup
from requests.models import Response
import pandas as pd

def extract():
    url = 'https://www.bestbuy.com/site/searchpage.jsp?cp=1&id=pcat17071&qp=category_facet%3Dname~abcat0507010&st=ryzen+processor'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def transform(soup):
    products = soup.find_all('li', class_='sku-item')
    #print(len(products))
    for item in products:
        title = item.find('h4', class_ = 'sku-header').text
        #print(title)
        price = item.find('div', class_= 'priceView-hero-price')
        for dollars in price:
            dollars = item.find('span', class_='sr-only').text
            #print(dollars)
            words = dollars.split(' ')
            currency = (words[-1])
            #print(currency)
            try:
                status = item.find('button', class_='c-button').text
                #print(status)
            except Exception:
                status = 'Unavailable Nearby'
                #print(status)
        link = item.find('a', href=True)
        product_url = 'http://www.bestbuy.com/' + link['href']
        #print(product_url)

        cpu = {
            'title': title,
            'price': currency,
            'status': status,
            'link': product_url, 
        }

        CPUs.append(cpu)

    return 

CPUs = []

c = extract()
transform(c)

df = pd.DataFrame(CPUs)
print(df)
df.to_csv('BestBuy_CPU_BS.csv')
df.to_json('BestBuy_CPU_BS.json')