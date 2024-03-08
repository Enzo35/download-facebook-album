import sys

import requests
from bs4 import BeautifulSoup

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


htmlStr = response.text
soup = BeautifulSoup(htmlStr, 'html.parser')
if str(soup.html.get("id")) != "facebook":
    print("Page not recognized as Facebook, problems may occuor.")
    print("Stoping script...")
    sys.exit(0)

links = len(soup.find_all('img'))

for a in soup.find_all('img'):
    print(a)

print("Hello World")
print(links)