# Web Scraping

# ---> Web Scraping is nothing but obtaining large amount of data from a website automatically
#---> Most of this data in Structured data in HTML format .., which is then used as in CSV format or in a data base that is used further

# Requests library is used to get the data from html docs
# we use requests library to get the data from html docs

import requests

url = "https://www.wscubetech.com/"
r = requests.get(url)
print(r.status_code)

# if i run the r.ststus_code., if i get (200), that means successful responses
# if the requests response is success., then only we can scrap the page using buetifulsoup

'''
 HTTP response status codes indicate whether a specific HTTP request has been successfully completed. Responses are grouped in five classes:

    Informational responses (100 – 199)
    Successful responses (200 – 299)
    Redirection messages (300 – 399)
    Client error responses (400 – 499)
    Server error responses (500 – 599)
'''
#eg:2
'''
url2="https://www.hindustantimes.com/"
r2 = requests.get(url2)
print(r2.status_code) #---> we are getting 401 for this response
'''
# for eg:1--> if we want entire html code of a webpage  as text format
#print(r.text)








