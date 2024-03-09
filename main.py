import sys
import requests
from bs4 import BeautifulSoup

from getFacebookPage import linkToSoup_selenium

BASE_FACEBOOK_URL = "https://www.facebook.com/"

url = input("Input Facebook Album URL: \n")
if url[:len(BASE_FACEBOOK_URL)] != BASE_FACEBOOK_URL:
    print("Page not recognized as Facebook, problems may occuor.")
    print("Stoping script...")
    sys.exit(0)

print("\n")

response = requests.get(url)
if response.status_code != 200:
    response.raise_for_status()
    sys.exit(0)


#soup = linkToSoup_selenium(url, '//h2//span//*[contains(text(),"Intro")]')
soup = linkToSoup_selenium(url, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div')
if soup == None:
    print("Page not recognized.")
    print("Stoping script...")
    sys.exit(0)

links = soup.find_all('img')
'''
for a in soup.find_all('img'):
    print("\n")
    print(a)
'''
print(len(links))