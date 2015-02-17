#encoding: utf-8
import sys
sys.path.append("selenium-2.44.0-py2.7.egg")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import getpass

email = raw_input("Username or Email for Facebook:")
password = getpass.getpass()
i=input("num: ")
driver = webdriver.Firefox()
person ="groups/300906943348830/"

driver.get("http://www.facebook.com")
print "facebook connect"
elem = driver.find_element_by_id("email")
elem.send_keys(email)
elem = driver.find_element_by_id("pass")
elem.send_keys(password)
elem.send_keys(Keys.RETURN)
print "login Sucess"
time.sleep(1)

driver.get("http://m.facebook.com/"+person)

time.sleep(1)
c=0
while c<i:


	try:
		elem = driver.find_element_by_link_text("ถูกใจ")
		elem.click()
		c+=1
		print "like = " + str(c)
	except:
		elem = driver.find_element_by_link_text("ดูโพสต์เพิ่มเติม")
		elem.click()
		print "next"

	
	time.sleep(3)
print "  _________"
print " |         |"
print " |Enddddddd|"
print " |_________|"
