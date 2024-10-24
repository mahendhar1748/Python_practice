# using Beutiful Soup

import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
r = requests.get(url)
print(r.status_code)
print(r) #--> still we get response

#getting html text format
soup = BeautifulSoup(r.text,"lxml")
#print(soup)

# We can use different functions of Beautifulsoup to extract data from webpage
