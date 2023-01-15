from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import requests
import json
import os
import sys
import configparser

url = sys.argv[1]

config = configparser.ConfigParser()
config.read('python.ini')

webhook_url = config['Discord']['webhook_url']
nom_webhook = config['Discord']['nom']
image_webhook = config['Discord']['image']

driver = webdriver.Chrome()
driver.set_window_size(10, 10)
driver.get(url)

#debug for test
avis = "avis"

article = driver.find_element(By.XPATH,'/html/body/main/div[1]/section/div/div[2]/main/div/nav/ul/li[4]/a/span').text

article = article.replace("Baskets", "👟")
article = article.replace("Pantalons", "👖")
article = article.replace("Shorts", "👖")
article = article.replace("Jeans", "👖")
article = article.replace("Manteaux & vestes", "🥼")
article = article.replace("Hauts & t-shirts", "👕")
article = article.replace("Costumes & blazers", "🧥")
article = article.replace("Sweats & pulls", "👕")
article = article.replace("Sous-vêtements & chaussettes", "🧦")
article = article.replace("Maillots de bain", "👙")
article = article.replace("Vêtements de sport & accessoires", "🏅")
article = article.replace("Vêtements spécialisés & costumes", "👒")
if "Autre" in article:
    article = "❄️"



evaluation = driver.find_element(By.XPATH,"/html/body/main/div[1]/section/div/div[2]/main/aside/div[3]/a/div[2]/div[2]/div")
evall = evaluation.get_attribute("aria-label")

noteval = driver.find_element(By.XPATH,"/html/body/main/div[1]/section/div/div[2]/main/aside/div[3]/a/div[2]/div[2]/div/div").text

if "Pas encore d'évaluation" in noteval:
    evall = "Member rated 0.24 out of 5"
else:
    pass
    
try:
    avis = driver.find_element(By.XPATH,'/html/body/main/div[1]/section/div/div[2]/main/aside/div[3]/a/div[2]/div[2]/div/div[6]/h4').text
except NoSuchElementException:
    avis = "0"


evall = evall.replace("Member rated ", "")
evall = evall.replace("out of 5", "")

evall = float(evall)

if 0 <= evall <= 0.5:
    evall = "<:nostar:1063935179426639923><:nostar:1063935179426639923><:nostar:1063935179426639923><:nostar:1063935179426639923><:nostar:1063935179426639923>"
elif 0.5 <= evall <= 1:
    evall = "<:halfstar:1063957819025539133> <:nostar:1063935179426639923><:nostar:1063935179426639923><:nostar:1063935179426639923><:nostar:1063935179426639923>"
elif 1 <= evall <= 1.5:
    evall = ":star:<:nostar:1063935179426639923><:nostar:1063935179426639923><:nostar:1063935179426639923><:nostar:1063935179426639923>"
elif 1.5 <= evall <= 2:
    evall = ":star:<:halfstar:1063957819025539133> <:nostar:1063935179426639923><:nostar:1063935179426639923><:nostar:1063935179426639923>"
elif 2 <= evall <= 2.5:
    evall = ":star::star:<:nostar:1063935179426639923><:nostar:1063935179426639923><:nostar:1063935179426639923>"
elif 2.5 <= evall <= 3:
    evall = ":star::star:<:halfstar:1063957819025539133> <:nostar:1063935179426639923><:nostar:1063935179426639923>"
elif 3 <= evall <= 3.5:
    evall = ":star::star::star:<:nostar:1063935179426639923><:nostar:1063935179426639923>"
elif 3.5 <= evall <= 4:
    evall = ":star::star::star:<:halfstar:1063957819025539133> <:nostar:1063935179426639923>"
elif 4 <= evall <= 4.5:
    evall = ":star::star::star::star:<:nostar:1063935179426639923>"
elif 4.5 <= evall <= 5:
    evall = ":star::star::star::star:<:halfstar:1063957819025539133> "
elif 5 == evall:
    evall = ":star::star::star::star::star:"






description = driver.find_element(By.XPATH, '/html/body/main/div[1]/section/div/div[2]/main/aside/div[1]/div[2]/div[1]/div/div/div/div[3]/span').text

name = driver.find_element(By.XPATH, '/html/body/main/div[1]/section/div/div[2]/main/aside/div[1]/div[2]/div[1]/div/div/div/div[1]/h2').text

prix = driver.find_element(By.XPATH, '/html/body/main/div[1]/section/div/div[2]/main/aside/div[1]/div[1]/div[1]/div[1]/div/div/h1').text

auteur = driver.find_element(By.XPATH,'/html/body/main/div[1]/section/div/div[2]/main/aside/div[3]/a/div[2]/div[1]/div/div/span').text

marque = driver.find_element(By.XPATH,'/html/body/main/div[1]/section/div/div[2]/main/aside/div[1]/div[1]/div[2]/div[2]/div[2]/a/span').text

etat = driver.find_element(By.XPATH,'/html/body/main/div[1]/section/div/div[2]/main/aside/div[1]/div[1]/div[2]/div[4]/div[2]').text
verif_etat = driver.find_element(By.XPATH,'/html/body/main/div[1]/section/div/div[2]/main/aside/div[1]/div[1]/div[2]/div[4]/div[1]').text

if "ÉTAT" in verif_etat:
    verif_etat = etat
else:
    etat = "Non trouvé <a:non:978232182088798208>"

taille = driver.find_element(By.XPATH,'/html/body/main/div[1]/section/div/div[2]/main/aside/div[1]/div[1]/div[2]/div[3]/div[2]').text
verif_taille = driver.find_element(By.XPATH,'/html/body/main/div[1]/section/div/div[2]/main/aside/div[1]/div[1]/div[2]/div[3]/div[1]').text

if "TAILLE" in verif_taille:
    verif_taille = taille
else:
    taille = "Non trouvé <a:non:978232182088798208>"
    

meta_image = driver.find_element(By.XPATH,"//meta[@property='og:image']")
image = meta_image.get_attribute("content")

taille = taille.replace("SIZE INFORMATION", "").strip()
etat = etat.replace("CONDITION INFORMATION", "").strip()

driver.quit()

data = {
  "content": None,
  "embeds": [
    {
      "description": description + "\n⠀",
      "color": 30594,
      "fields": [
        {
          "name": "\📦 • Auteur",
          "value": auteur,
          "inline": True
        },
        {
          "name": "\📋 • Avis",
          "value": evall + "(" + avis + " Avis)",
          "inline": True
        },
        {
          "name": "\💸 • Prix",
          "value": prix,
          "inline": True
        },
        {
          "name": "\💼 • Marque",
          "value": marque,
          "inline": True
        },
        {
          "name": "\📏 • Taille",
          "value": taille,
          "inline": True
        },
        {
          "name": "\📌 • État",
          "value": etat,
          "inline": True
        }
      ],
      "author": {
        "name": article + " • " + name,
        "url": url
      },
      "image": {
        "url": image
      }
    }
  ],
  "username": nom_webhook,
  "avatar_url": image_webhook,
  "attachments": []
}

headers = {'Content-Type': 'application/json'}
requests.post(webhook_url, json=data, headers=headers)
