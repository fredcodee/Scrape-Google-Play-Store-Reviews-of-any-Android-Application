from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import pandas as pd
#chromedriver
browser = webdriver.Chrome("C:\\Users\\Windows 10 Pro\\Downloads\\chromedriver")

#google playstore app id url here
#read readme files to learn how to get any app id url
app_url_id ="https://play.google.com/store/apps/details?id=com.tencent.ig"
review_list = []

def scrape_reviews():
    browser.get(app_url_id+"&showAllReviews=true")
    sleep(3)
    #navigate to BeautifulSoup
    source = soup(browser.page_source,"html.parser")
    user_data = source.find_all("div", class_="zc7KVe")
    for items in user_data:
        d={}
        d["names"] = items.find("span", {"class":"X43Kjb"}).text
        #rate = items.find("div", class_ = "pf5lIe").text
        d["date"] = items.find("span", class_="p2TkOb").text
        try:
            d["reviews"]= items.find("div", class_="UD7Dzf").find("span").text
        except:
            d["reviews"] = None
        review_list.append(d)

scrape_reviews()
#remove duplicates
for n in review_list:
    for k,v in n.items():
        if v == None:
            review_list.remove(n)

#convert to csv
df1 = pd.DataFrame(review_list)
df1.to_csv('reviews_list.csv', encoding='utf-8')
