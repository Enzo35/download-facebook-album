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
        
        #WebDriverWait(driver, 30)
        #button_quit = driver.find_element(By.XPATH("//div[@role = 'button']"))
        button_quit = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div")
        button_quit.click()
        
        WebDriverWait(driver, 25).until(
                EC.visibility_of_all_elements_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[1]/a/div/img")))

        lSoup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.close()
        del driver
        return lSoup
    except Exception as e:
        print(e)
        return None