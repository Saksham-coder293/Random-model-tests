from bs4 import BeautifulSoup
import os
import pandas as pd
d = {'title':[1,2], 'price': [3,4],'link': [1,2]}

for file in os.listdir("data"):
  try : 
    with open(f"data/{file}") as f:
        html_doc = f.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    t = soup.find("h2")
    title = t.get_text()
    print(title)
     


    l =t.find("a")
    link ="https://amazon.in/" +  l['href']
    p = soup.find("span",attr = {"class": 'a-price-whole'})
    d['title'].append(title)
    d['price'].append(title)
    d['link'].append(link)
    price = p.get_text
    print(title,link,price)
    break 
  except Exception as e:
     print(e)



df = pd.DataFrame(data = d)
df.to_csv("data.csv")