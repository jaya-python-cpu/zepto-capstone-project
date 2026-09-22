import requests
from bs4 import beautifulsoup
import pandas as pd

books_data=[]

url= "https://books.toscrape.com/"
response=requests.get(url)
response.raise_for_satus()

soup= Beautifulsoup(response.text, "html.parser")
print(soup.title.text)
print(soup.find(ol))

books= soup.select("article.product_pod")
print(len(books))

for book in books:
   title=book.h3.a["title"]
   print(title)
  
   price=
book.select_one(".price_color").
  text
  print(price)
  rating=
book.select_one(".star-rating")
["class"][1]
  print(rating)
availability=
book.select_one(".availability")
.text.strip()
print(availability)
books_data.append({"title": title,"price": price, "rating": rating,"availability": availability})
df=pd.DataFrame(books_data)
  print(df.head())

