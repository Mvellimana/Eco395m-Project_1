import pandas as pd
import requests
import io
import numpy as np 
import matplotlib.pyplot as plt 
from scipy import stats
from scipy.stats import zscore

#Cleaned Data URL from Mai branch
url = "https://raw.githubusercontent.com/Mvellimana/Eco395m-Project_1/Data-cleaning-%26-preprocessing_Mai/Yelp_API_Data_Cleaned.csv"

download = requests.get(url).content
df = pd.read_csv(io.StringIO(download.decode('utf-8')))


#Select needed variables

df_anlz = df[[
'categories', 
'Categories_merged', 
'price level', 
'review count', 
'Review count_stndized', 
'rating', 
'Rating_stndized', 
'Zipcode']].copy()


#Replace dollar signs to use it later for price avg/category

df_anlz['price level'] = df_anlz['price level'].replace("$", 1)
df_anlz['price level'] = df_anlz['price level'].replace("$$", 2)
df_anlz['price level'] = df_anlz['price level'].replace("$$$", 3)
df_anlz['price level'] = df_anlz['price level'].replace("$$$$", 4)

#group variables by category to find their mean

df_anlz_sum = df_anlz[[
'Categories_merged', 
'price level', 
'review count', 
'rating', 
'Rating_stndized']].groupby(["Categories_merged"]).mean()


#findng number of resturants by category and standarized them

df_anlz_sum2 = df_anlz.groupby(["Categories_merged"])["Categories_merged"].count().reset_index(name="rest_count")
df_anlz_sum2['rest_count_standarized'] = df_anlz_sum2.rest_count.transform(zscore, ddof=1)



#merge the standarized and non-standarized ones

df_anlz_final = pd.merge(df_anlz_sum, df_anlz_sum2, on = "Categories_merged")

df_anlz_final = df_anlz_final.sort_values(by=['Rating_stndized',], ascending= False)








