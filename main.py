from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://web.whatsapp.com/')
time.sleep(30)
navigation=driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[4]/header/div[2]/div/span/div[4]/div/span')
navigation.click()
newbut=driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[4]/header/div[2]/div/span/div[4]/span/div/ul/li[1]/div')
newbut.click()
search_box=driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[3]/div[1]/span/div/span/div/div/div[1]/div/div/div[2]/input')
search_box.send_keys('mom')
time.sleep(2)
addperson=driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[3]/div[1]/span/div/span/div/div/div[2]/div/div/div/div/div/div/div[2]')
addperson.click()
time.sleep(2)
nextbutton=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[3]/div[1]/span/div/span/div/div/span/div/span')
nextbutton.click()
time.sleep(5)
nameenter=driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[3]/div[1]/span/div/span/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/p')
nameenter.send_keys('Group Name')
time.sleep(2)
nextbutton2=driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[3]/div[1]/span/div/span/div/div/span/div/div/span')
nextbutton2.click()

