from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import re




driver = webdriver.Chrome()

#x_ = 'https://www.cars.com/for-sale/searchresults.action/?page=1&perPage=20&prMx=60000&rd=30&searchSource=GN_REFINEMENT&sort=relevance&stkTypId=28881&yrId=20141%2C20197%2C20142%2C20198%2C20143%2C20199%2C20144%2C20200%2C20145%2C20201%2C27381%2C34923%2C39723%2C47272%2C51683%2C56007%2C58487%2C30031936%2C35797618%2C36362520%2C36620293&zc=10001'







#driver.get(x_)
#new york city area
#link_beginning = 'https://www.cars.com/for-sale/searchresults.action/?page='
#link_end = '&perPage=100&prMx=60000&rd=30&searchSource=PAGINATION&sort=relevance&stkTypId=28881&yrId=20141%2C20197%2C20142%2C20198%2C20143%2C20199%2C20144%2C20200%2C20145%2C20201%2C27381%2C34923%2C39723%2C47272%2C51683%2C56007%2C58487%2C30031936%2C35797618%2C36362520%2C36620293&zc=10001'


#jersey cars
#link_beginning = 'https://www.cars.com/for-sale/searchresults.action/?page='
#link_end = '&perPage=100&prMx=60000&rd=30&searchSource=PAGINATION&sort=relevance&stkTypId=28881&yrId=20141%2C20197%2C20142%2C20198%2C20143%2C20199%2C20144%2C20200%2C20145%2C20201%2C27381%2C34923%2C39723%2C47272%2C51683%2C56007%2C58487%2C30031936%2C35797618%2C36362520%2C36620293&zc=08544'

#san fransisco
#link_beginning = 'https://www.cars.com/for-sale/searchresults.action/?page='
#link_end = '&perPage=100&prMx=60000&rd=30&searchSource=GN_REFINEMENT&sort=relevance&stkTypId=28881&yrId=20141%2C20197%2C20142%2C20198%2C20143%2C20199%2C20144%2C20200%2C20145%2C20201%2C27381%2C34923%2C39723%2C47272%2C51683%2C56007%2C58487%2C30031936%2C35797618%2C36362520%2C36620293&zc=94112'



#chicago
#link_beginning = 'https://www.cars.com/for-sale/searchresults.action/?page='
#link_end = '&perPage=100&prMx=60000&rd=30&searchSource=GN_REFINEMENT&sort=relevance&stkTypId=28881&yrId=20141%2C20197%2C20142%2C20198%2C20143%2C20199%2C20144%2C20200%2C20145%2C20201%2C27381%2C34923%2C39723%2C47272%2C51683%2C56007%2C58487%2C30031936%2C35797618%2C36362520%2C36620293&zc=60525'

#houston
# link_beginning = 'https://www.cars.com/for-sale/searchresults.action/?page='
# link_end = '&perPage=100&prMx=60000&rd=30&searchSource=GN_REFINEMENT&sort=relevance&stkTypId=28881&yrId=20141%2C20197%2C20142%2C20198%2C20143%2C20199%2C20144%2C20200%2C20145%2C20201%2C27381%2C34923%2C39723%2C47272%2C51683%2C56007%2C58487%2C30031936%2C35797618%2C36362520%2C36620293&zc=77030'

#LA
#link_beginning = 'https://www.cars.com/for-sale/searchresults.action/?page='
#link_end = '&perPage=100&prMx=60000&rd=30&searchSource=GN_REFINEMENT&sort=relevance&stkTypId=28881&yrId=20141%2C20197%2C20142%2C20198%2C20143%2C20199%2C20144%2C20200%2C20145%2C20201%2C27381%2C34923%2C39723%2C47272%2C51683%2C56007%2C58487%2C30031936%2C35797618%2C36362520%2C36620293&zc=90012'

#seattle
#link_beginning = 'https://www.cars.com/for-sale/searchresults.action/?page='
#link_end = '&perPage=100&prMx=60000&rd=30&searchSource=GN_REFINEMENT&sort=relevance&stkTypId=28881&yrId=20141%2C20197%2C20142%2C20198%2C20143%2C20199%2C20144%2C20200%2C20145%2C20201%2C27381%2C34923%2C39723%2C47272%2C51683%2C56007%2C58487%2C30031936%2C35797618%2C36362520%2C36620293&zc=98104'

#boston
link_beginning = 'https://www.cars.com/for-sale/searchresults.action/?page='
link_end = '&perPage=100&prMx=60000&rd=30&searchSource=GN_REFINEMENT&sort=relevance&stkTypId=28881&yrId=20141%2C20197%2C20142%2C20198%2C20143%2C20199%2C20144%2C20200%2C20145%2C20201%2C27381%2C34923%2C39723%2C47272%2C51683%2C56007%2C58487%2C30031936%2C35797618%2C36362520%2C36620293&zc=02115'



#list of pages




links = []




for i in range(0,50):
    page_number = str(i)
    single_link = link_beginning + page_number + link_end
    links.append(single_link)



csv_file = open('cars.csv','w',encoding ='utf-8',newline = '')
writer = csv.writer(csv_file)

#add headers
writer.writerow(["Listing","Make","Year_model","Price","Milage","Exterior_color","Interior_color","Transmission","Drivetrain"])




#while True:
#    try:
for i in range(len(links)):
    
    page_ = links[i]
    driver.get(page_) 
    time.sleep(4)

    listings_per_page = driver.find_elements_by_xpath("//div[@class = 'listing-row__details']")

    print("scraping page" + str(i))

    for j in range(len(listings_per_page)):
        cars_dict = {}


        each_listing = listings_per_page[j]

        title = each_listing.find_element_by_xpath(".//h2[@class='listing-row__title']").text
        make = each_listing.find_element_by_xpath(".//h2[@class='listing-row__title']").text.split(' ')[1]
        year_model = each_listing.find_element_by_xpath(".//h2[@class='listing-row__title']").text.split(' ')[0]
        price = each_listing.find_elements_by_xpath(".//div[@class='payment-section']")[0].text.split(' ')[0]
        milage = each_listing.find_elements_by_xpath(".//div[@class='payment-section']")[0].text.split(' ')[-2]
        exterior_color = each_listing.find_element_by_xpath(".//ul[@class='listing-row__meta']//li[1]").text.split(':')[1].strip()
        interior_color = each_listing.find_element_by_xpath(".//ul[@class='listing-row__meta']//li[2]").text.split(':')[1].strip()
        transmission = each_listing.find_element_by_xpath(".//ul[@class='listing-row__meta']//li[3]").text.split(':')[1].strip()
        drivetrain = each_listing.find_element_by_xpath(".//ul[@class='listing-row__meta']//li[4]").text.split(':')[1].strip()



        #add to dictionary
        cars_dict['title'] = title
        cars_dict['make'] = make
        cars_dict['year_model'] = year_model
        cars_dict['price'] = price
        cars_dict['milage'] = milage
        cars_dict['exterior_color']= exterior_color
        cars_dict['interior_color'] = interior_color
        cars_dict['transmission'] = transmission
        cars_dict['drivetrain'] = drivetrain

        writer.writerow(cars_dict.values())

    #except IndexError:

    #    continue
#    break            


csv_file.close()


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

driver.close()

