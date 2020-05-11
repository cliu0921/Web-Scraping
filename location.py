import pandas as pd
import numpy as np
import math
from sklearn import linear_model
import csv

csv_file = open('city_coefs.csv','w',encoding ='utf-8',newline = '')
writer = csv.writer(csv_file)
writer.writerow(['City','Age_coef','Milage_coef','Intercept'])

cars = pd.read_csv('cars_df.csv')
cars['Year_model'] = pd.to_numeric(cars.Year_model)
cars['Age'] = 2020- cars['Year_model'] 

car_reg = linear_model.LinearRegression()
cars = cars.dropna(axis = 0, how = 'any')
cars.reset_index(drop = True)

cities = cars.City.unique()

city_coefs ={}

for i in range(len(cities)):
    city_ = cities[i]
    car_reg.fit(cars[cars['City'] == city_][['Age','Milage']],cars[cars['City']==city_].Price)
    city_coefs['City'] = city_
    city_coefs['Age_coef'] = car_reg.coef_[0]
    city_coefs['Milage_coef'] = car_reg.coef_[1]
    city_coefs['Intercept'] = car_reg.intercept_

    writer.writerow(city_coefs.values())

csv_file.close()
