import pandas as pd
import numpy as np
import math
from sklearn import linear_model
import csv


csv_file = open('make_coefs.csv','w',encoding ='utf-8',newline = '')
writer = csv.writer(csv_file)
writer.writerow(['Make','Age_coef','Milage_coef','Intercept'])




#from matplotlib import pyplot as plt
#plt.style.use('ggplot')

cars = pd.read_csv('cars_df.csv')
cars['Year_model'] = pd.to_numeric(cars.Year_model)
cars['Age'] = 2020- cars['Year_model'] 
car_reg = linear_model.LinearRegression()
cars = cars.dropna(axis = 0, how = 'any')
cars.reset_index(drop = True)

unique_makes = cars.Make.unique()
make_coefs = {}

for i in range(len(unique_makes)):
    make = unique_makes[i]
    car_reg.fit(cars[cars['Make']== make][['Age','Milage']],cars[cars['Make']== make].Price)
    make_coefs['make'] = make
    make_coefs['Age_coef'] = car_reg.coef_[0]
    make_coefs['Milage_coef'] = car_reg.coef_[1]
    make_coefs['Intercept'] = car_reg.intercept_
    #make_coefs['make']= [car_reg.coef_[0], car_reg.coef_[1],car_reg.intercept_]

    writer.writerow(make_coefs.values())

csv_file.close()


