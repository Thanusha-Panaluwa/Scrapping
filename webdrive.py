# -*- coding: utf-8 -*-
import mechanize
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(executable_path=r'C:\Python27\Scripts\chromedriver.exe')
browser.get("http://aiproducts.com/index.html") 
#time.sleep(10)
search_input = browser.find_element_by_name("TextSearch")

search_input.send_keys("A-AH146786")
search_attempt = browser.find_element_by_xpath("//*[@type='submit']")
search_attempt.submit()


#br = mechanize.Browser()
#br.set_handle_robots(False)
#br.addheaders = [("User-agent", "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
  #reading the page body that is redirected after successful login

browser.get('https://www.allpartsstore.com/ItemList.htm')
#accessing other url(s) after login is done this way 

req = browser.page_source
soup = BeautifulSoup(req)

print soup
