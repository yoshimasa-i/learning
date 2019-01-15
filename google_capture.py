# -*- coding: utf-8 -*-
import time
from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')  
driver.get('https://www.google.co.jp/imghp?hl=ja');
time.sleep(5) 
search_box = driver.find_element_by_name('q')
search_box.send_keys(u'nike sb ピジョン')

search_box.submit()
driver.save_screenshot('sexy.png')
time.sleep(5) 
driver.quit()
