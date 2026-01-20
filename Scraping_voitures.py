from bs4 import BeautifulSoup
import requests
import csv

# request the webpage
rsp=requests.get("https://globaloccaz.com/acheter-une-voiture")
print (rsp.status_code)
# parse the content
soup=BeautifulSoup(rsp.text,"html.parser")

lien_cards = soup.find_all("div",class_='search-content')

for card in lien_cards:
    print(len(card.find_all("div",class_="card")))
    #link=card.find("a")
    #href=link.get('href')
    #print(href) 
    

