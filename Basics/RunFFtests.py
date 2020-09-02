from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(executable_path =r'C:\Users\VINAY\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\selenium\webdriver\common\geckodriver.exe')
driver.get("https://letskodeit.teachable.com/p/practice")
driver.implicitly_wait(10)
