import pandas as pd
import numpy as np
import math
from sklearn import linear_model
import csv

csv_file = open('category_coefs.csv','w',encoding ='utf-8',newline = '')
writer = csv.writer(csv_file)
writer.writerow(['Category','Age_coef','Milage_coef','Intercept'])

cars = pd.read_csv('cars3_df.csv')
cars = cars.dropna(axis = 0, how = 'any')
cars.reset_index(drop = True)

car_reg = linear_model.LinearRegression()

cat = cars.Category.unique()

cat_coefs = {}

for i in range(len(cat)):
    cat_ = cat[i]
    car_reg.fit(cars[cars['Category'] == cat_][['Age','Milage']],cars[cars['Category']==cat_].Price)
    cat_coefs['City'] = cat_
    cat_coefs['Age_coef'] = car_reg.coef_[0]
    cat_coefs['Milage_coef'] = car_reg.coef_[1]
    cat_coefs['Intercept'] = car_reg.intercept_


    writer.writerow(cat_coefs.values())
    

csv_file.close()


