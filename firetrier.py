import selenium
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os, sys, time

# 1- set profile
#profile = os.path.dirname(sys.argv[0]) + "/selenita"
binary = FirefoxBinary('C:/Program Files (x86)/Mozilla Firefox/firefox.exe')
profile = 'dependencies\\1ndsjjut.default'
fp = webdriver.FirefoxProfile(profile)
driver = webdriver.Firefox(firefox_profile=fp, firefox_binary=binary)

# 2- get tmp file location
profiletmp = driver.firefox_profile.path

# but... the current profile is a copy of the original profile :/
print("running profile " + profiletmp)

driver.get("http://httpbin.org")
time.sleep(2)
input("Press a key when finish doing things") # I've installed an extension

# 3- then save back
print("saving profile " + profiletmp + " to \\" + profile)
if os.system("copy " + profiletmp + "\ " + profile ):
    print("files should be copied :/")


driver.quit()
sys.exit(0)