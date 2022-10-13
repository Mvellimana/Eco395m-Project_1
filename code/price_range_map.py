import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point, Polygon
import os


#further cleaning f the raw data to suit analysis for mapping purpose
df = pd.read_csv("artifacts/Yelp_API_Data_Cleaned.csv")
df.columns = [c.replace(" ", "_") for c in df.columns]
df["price_level"] = df["price_level"].replace("$", 1)
df["price_level"] = df["price_level"].replace("$$", 2)
df["price_level"] = df["price_level"].replace("$$$", 3)
df.Categories_merged = [c.replace(" ", "_") for c in df.Categories_merged]
df.Categories_merged = [c.replace("/", "_") for c in df.Categories_merged]
df = df.loc[df["Longitude"] < -95]

#read the austin city map in shapefile format to establish a base for the points to be plotted on
austin_map = gpd.read_file(os.path.join(os.getcwd(), "data/austin_shapefile/geo_export_1ee4a6f6-dd8c-49f2-9aa6-8630506ef412.shp"))

#convert the requisite dataframe into a geopandas compatible dataframe with long and lat
crs = {"init": "epsg:4326"}
geometry = [Point(xy) for xy in zip(df["Longitude"],df["Latitude"])]
geo_df = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)

#plot a graph showing all locations of restaurants in the dataset and highlight different price levels
fig,ax = plt.subplots(figsize = (15,15))
austin_map.plot(ax=ax, alpha=0.4, color="xkcd:sky blue")
geo_df[geo_df["price_level"] == 1].plot(ax=ax, markersize=20, color="red", marker="o", label="Low Price Level")
geo_df[geo_df["price_level"] == 2].plot(ax=ax, markersize=20, color="green", marker="^", label="Medium Price Level")
geo_df[geo_df["price_level"] == 3].plot(ax=ax, markersize=20, color="yellow", marker="s", label="High Price Level")
ax.set_title("Restaurants in Austin City based on Prices") 
plt.legend(prop={"size": 15})

fig.savefig("artifacts/figures/price_range_map.png", 
              dpi=100, format="png", 
              bbox_inches="tight")
