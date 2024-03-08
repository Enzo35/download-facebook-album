import sys

import requests
from bs4 import BeautifulSoup

url = input("Input Facebook Album URL: \n")
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
    
    """cont = input("Continue or Stop? s/n ")
    while cont != "s" and cont != "n":
        print(type(cont))
        cont = input("Continue or Stop? s/n ")
    
    if cont == "n":
        print("Stoping...")
        sys.exit(0)
    print("Continuing script")"""




print("Hello World")
print(type(soup.title))