import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point, Polygon
import os
from PIL import Image 
import glob

%matplotlib inline

"""further cleaning f the raw data to suit analysis for mapping purpose"""
df = pd.read_csv('Yelp_API_Data_Cleaned.csv')
df.columns = [c.replace(' ', '_') for c in df.columns]
df['price_level'] = df['price_level'].replace('$', 1)
df['price_level'] = df['price_level'].replace('$$', 2)
df['price_level'] = df['price_level'].replace('$$$', 3)
df.Categories_merged = [c.replace(' ', '_') for c in df.Categories_merged]
df.Categories_merged = [c.replace('/', '_') for c in df.Categories_merged]
df = df.loc[df["Longitude"] < -95]

"""read the austin city map in shapefile format to establish a base for the points to be plotted on"""
austin_map = gpd.read_file(os.path.join(os.getcwd(), 'austin_shapefile/geo_export_1ee4a6f6-dd8c-49f2-9aa6-8630506ef412.shp'))

"""convert the requisite dataframe into a geopandas compatible dataframe with long and lat"""
crs = {'init': 'epsg:4326'}
geometry = [Point(xy) for xy in zip(df["Longitude"],df["Latitude"])]
geo_df = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)