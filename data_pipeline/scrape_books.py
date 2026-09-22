import requests
from bs4 import beautifulsoup

url= "https://books.toscrape.com/"
response=requests.get(url)

soup= Beautifulsoup(response.text, "html.parser")
print(soup.title.text)
print(soup.find(ol))
