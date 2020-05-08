from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import re




driver = webdriver.Chrome()

x_ = 'https://www.cars.com/for-sale/searchresults.action/?page=1&perPage=20&prMx=60000&rd=30&searchSource=GN_REFINEMENT&sort=relevance&stkTypId=28881&yrId=20141%2C20197%2C20142%2C20198%2C20143%2C20199%2C20144%2C20200%2C20145%2C20201%2C27381%2C34923%2C39723%2C47272%2C51683%2C56007%2C58487%2C30031936%2C35797618%2C36362520%2C36620293&zc=10001'

driver.get(x_)


csv_file = open('cars.csv','w',encoding ='utf-8',newline = '')
writer = csv.writer(csv_file)

listings_per_page = driver.find_elements_by_xpath("//div[@class = 'listing-row__details']")

for i in range(len(listings_per_page)):
    cars_dict = {}


    each_listing = listings_per_page[i]
    title = each_listing.find_element_by_xpath(".//h2[@class='listing-row__title']").text
    print(title)






#prices = [el.text for el in driver.find_elements_by_xpath("//span[contains(@class,'listing-row__price')]")]
#milage = [el.text for el in driver.find_elements_by_xpath("//span[contains(@class, 'listing-row__mileage')]")]
#title = [el.text for el in driver.find_elements_by_xpath("//h2[contains(@class,'listing-row__title')]")]
#info = [el.text for el in driver.find_elements_by_xpath("//ul[contains(@class, 'listing-row__meta')]")]
#listing = [el.text for el in driver.find_elements_by_xpath("//div[contains(@class,'listing-row__details')]")]
#test = driver.find_element_by_xpath("//div[@class = 'listing-row__details']//ul[@class='listing-row__meta']//li[1]").text




# #these works
# test = driver.find_elements_by_xpath("//div[@class = 'listing-row__details']")
# y_ = test[8]
# #this works test2= y_.find_element_by_xpath(".//ul[@class='listing-row__meta']//li[1]").text
# #this works test2=y_.find_elements_by_xpath(".//div[@class='payment-section']")[0].text
# test2 = y_.find_element_by_xpath(".//h2[@class='listing-row__title']").text

#test3 = test2.find_element_by_xpath(".//span[@class='listing-row__price ']").text
#testest = driver.find_elements_by_xpath("//div[@class = 'listing-row__details']//div[@class='payment-section']//span[@class='listing-row__price']").text

#print(prices)
#print(test2)
#print(milage)
#print(title)
#print(len(title))
#print(type(listing[1]))
#next_button = driver.find_element_by_xpath('//a[@class="button next-page"]/div')

