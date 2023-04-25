from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.EdgeOptions()
options.add_experimental_option("debuggerAddress","127.0.0.1:9527")

browser = webdriver.Edge(options = options)
browser.get("https://gartic.io/theme")
it = browser.find_elements(By.TAG_NAME,'input')

for el in it:
    print(el.id)
#cur = browser.find_element(By.TAG_NAME,'Input').send_keys("123")
