import sys
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


l = input("Input Facebook Album URL: \n")

ecx_login = "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div"

ecx_album = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[1]/a/div/img"

ecx_photo = "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div/div/img"

ecx_next_photo = "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[3]/div/div/div/i"


try:
    cService = webdriver.ChromeService(executable_path='chromedriver.exe')
    driver = webdriver.Chrome(service = cService)
    # I copy chromedriver.exe to every folder with py file that will need to scrape with selenium

    driver.get(l)
    if ecx_login:
        WebDriverWait(driver, 25).until(EC.visibility_of_all_elements_located((By.XPATH, ecx_login)))
    
    button_quit = driver.find_element(By.XPATH, ecx_login)
    button_quit.click()
    
    WebDriverWait(driver, 25).until(EC.visibility_of_all_elements_located((By.XPATH, ecx_album)))
    
    button_photo = driver.find_element(By.XPATH, ecx_album)
    button_photo.click()

    WebDriverWait(driver, 25).until(EC.visibility_of_all_elements_located((By.XPATH, ecx_photo)))
    
    WebDriverWait(driver, 25).until(EC.visibility_of_all_elements_located((By.XPATH, ecx_next_photo)))

    button_next_photo = driver.find_element((By.XPATH, ecx_next_photo))
    button_next_photo.click()

    WebDriverWait(driver, 25).until(EC.visibility_of_all_elements_located((By.XPATH, ecx_photo)))

    #lSoup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.close()
    del driver
except Exception as e:
    print(e)




"""
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

links = soup.find_all('img', href=True)
'''
for a in soup.find_all('img'):
    print( '\n')
    print(a)
'''
print(len(links))

"""