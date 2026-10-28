#Web Scrapping

#directing to url
from bs4 import BeautifulSoup
import requests
product="doramon"
url="https://www.flipkart.com/search?q="+product
print(url)

# #status code
response=requests.get(url)
# print(response)

# #website frontend code in text
# print(response.text)

#in HTML format
content=BeautifulSoup(response.text,"html.parser")
# print(content)

products = content.find_all("div", {"class": "lvJbLV col-12-12"})
print(len(products))

title=products[0].find("a",{"class":"pIpigb"}).text
print(title)

rating=products.find("div",{"class":"a7saXW WDsrYC"}).text
print(rating)