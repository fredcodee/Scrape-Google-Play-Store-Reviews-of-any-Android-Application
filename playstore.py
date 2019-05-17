from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#chromedriver
browser = webdriver.Chrome("C:\\Users\\Windows 10 Pro\\Downloads\\chromedriver")

#google playstore app id url here
#read readme files to learn how to get any app id url
browser.get("https://play.google.com/store/apps/details?id=com.tencent.ig")
