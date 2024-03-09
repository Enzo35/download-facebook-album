# Code credits to Driftr95, at https://stackoverflow.com/questions/74100308/facebook-scraping-python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def linkToSoup_selenium(l, ecx=None):
    try:
        cService = webdriver.ChromeService(executable_path='chromedriver.exe')
        driver = webdriver.Chrome(service = cService)
        # I copy chromedriver.exe to every folder with py file that will need to scrape with selenium

        driver.get(l)
        if ecx:
            WebDriverWait(driver, 25).until(
                EC.visibility_of_all_elements_located((By.XPATH, ecx)))

        lSoup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.close()
        del driver
        print("\ndone")
        return lSoup
    except Exception as e:
        print(e)
        return None