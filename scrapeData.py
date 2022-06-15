
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import json
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import random


# prox = Proxy()
# prox.proxy_type = ProxyType.MANUAL
# prox.http_proxy = "68.183.185.62:80"
# prox.socks_proxy = "ip_addr:port"
# prox.ssl_proxy = "ip_addr:port"

# capabilities = webdriver.DesiredCapabilities.CHROME
# prox.add_to_capabilities(capabilities)

# chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),desired_capabilities=capabilities)
chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

search_query = 'Singapore'
SITE = 'https://food.grab.com/sg/en/'


with chrome_driver as driver:
    # set timeout time
    wait = WebDriverWait(driver, 15)

    # retrieve url 
    driver.get(SITE)


    # find search box
    search_bar = driver.find_element_by_id('location-input')
    search_bar.send_keys(search_query)
    
    # dictionary appears
    wait.until(presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div/ul/li[1]')))
    list_element = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[1]')
    time.sleep(2)
    list_element.click()

    # find the search button
    search_button = driver.find_element_by_xpath('//*[@id="page-content"]/div[2]/div/button')
    search_button.click()
    time.sleep(random.randint(5,10))

    wait.until(presence_of_element_located((By.XPATH,'//*[@id="page-content"]/div[4]//div/button/span[text()="Load More"]')))

    load_more = driver.find_element_by_xpath('//*[@id="page-content"]/div[4]//div/button')
    props = ''
    i = 1
    
    # props_script_element = driver.find_element_by_css_selector('#__NEXT_DATA__')
    # print(props_script_element)
    # props = props_script_element.get_attribute('innerHTML')
    # print(props)

    # with open('props.json','w') as file:
        # file.write(props)

        
    while load_more:
        try:
            props_script_element = driver.find_element_by_id('__NEXT_DATA__')
            props = props_script_element.get_attribute('innerHTML')
            
            print(f'Writing times {i}')
            with open(f'data/props_{i}.json','w',encoding='utf-8') as file:
                file.write(props)
            i+=1
        except:
            print('Done Scraping!')
            exit()
        load_more.click()
        
        try:
            wait.until(presence_of_element_located((By.XPATH,'//*[@id="page-content"]/div[4]//div/button/span[text()="Load More"]')))
            time.sleep(random.randint(6,12))
            load_more = driver.find_element_by_xpath('//*[@id="page-content"]/div[4]//div/button')
        except:
            print("Reached end of the page")



