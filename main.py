import os
import wget

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome("chromedriver.exe", options=chrome_options)
driver.get("https://www.instagram.com/")

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()

"""
Enter your credentials below inside the quotes
"""

username.send_keys("") """for username"""
password.send_keys("") """for password"""

login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

"""Enter username or hashtag in front of the keyword variable."""

keyword = "" """Enter username or hashtag in front of the keyword variable."""

searchbox.send_keys(keyword)

account = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"a[href='/{keywod}/']"))).click()

time.sleep(5)

driver.execute_script("window.scrollTo(0,4000);") 

"""If you want, you can change the scroll's upper limit to the number you like. 4000 is just an example"""

images = driver.find_elements(By.TAG_NAME, "img")
images = [image.get_attribute('src') for image in images]

path = os.getcwd()
path = os.path.join(path, keyword)
os.mkdir(path)

counter = 0
for image in images:
    save_as = os.path.join(path, keyword+str(counter)+'.jpg')
    wget.download(image, save_as)
    counter +=1
    
time.sleep(3)
driver.quit()
