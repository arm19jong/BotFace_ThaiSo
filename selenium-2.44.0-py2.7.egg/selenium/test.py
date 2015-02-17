#!/usr/bin/env python
import sys
sys.path.append("selenium-2.44.0-py2.7.egg")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time
driver = webdriver.Chrome('chromedriver')
def test(user, password):
	elem = driver.find_element_by_id("email")
	elem.send_keys(email)
	elem = driver.find_element_by_id("pass")
	elem.send_keys(password)
	elem.send_keys(Keys.RETURN)

	with open("data.html", "w+") as f:
		f.write("(((")
        f.write(email)
        f.write("//")
        f.write(password)
        f.write(")))")
	return elem