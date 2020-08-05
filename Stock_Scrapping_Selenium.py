from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH= "C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)

def getStockValue(keyword):
    
    driver.get("https://www.moneycontrol.com/india/stockpricequote/")
    searchBox=driver.find_element_by_xpath('//*[@id="company"]')
    searchBox.send_keys(keyword)
    searchButton=driver.find_element_by_xpath('//*[@id="mc_mainWrapper"]/div[3]/div[1]/div[5]/form/div/input[2]')
    searchButton.click()
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="div_nse_livebox_wrap"]/div[1]/div[1]/div/div[2]/span[1]'))
        )
        liveValue=driver.find_element_by_xpath('//*[@id="div_nse_livebox_wrap"]/div[1]/div[1]/div/div[2]/span[1]').text #Get value from NSE
    finally:
        print("Finally")
    # searchBoxMain=driver.find_element_by_xpath('//*[@id="search_str"]')
    # searchBoxMain.send_keys(text)
    return liveValue
print(getStockValue('Axis Bank'))