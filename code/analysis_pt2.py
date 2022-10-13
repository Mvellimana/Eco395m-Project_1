import pandas as pd
import requests
import io
import numpy as np 
import matplotlib.pyplot as plt 
from scipy import stats
from scipy.stats import zscore


url = "https://raw.githubusercontent.com/Mvellimana/Eco395m-Project_1/Data-cleaning-%26-preprocessing_Mai/Yelp_API_Data_Cleaned.csv"

download = requests.get(url).content
df = pd.read_csv(io.StringIO(download.decode('utf-8')))

df_anlz = df[['categories', 
'Categories_merged', 
'price level', 
'review count', 
'Review count_stndized', 
'rating', 
'Rating_stndized', 
'Zipcode']].copy()

