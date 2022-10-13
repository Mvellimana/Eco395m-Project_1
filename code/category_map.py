import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point, Polygon
import os
from PIL import Image 
import glob


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

#plot a graph fr every food category and save them using a loop
list_of_categories = ["American",
                      "Mexican_South_American",
                      "Bars_Pubs",
                      "Asian",
                      "Cafes_Juice_bars_Desserts",
                      "Middle-eastern_Indian_African",
                      "Pizza_European",
                      "Food_Trucks_Food_Stands",
                      "Specification_(Vegan_Glutenfree)",
                      "food_delivery_services_groceries_venues_cafeterias"]

def plot_foodcategory(category):
    fig,ax = plt.subplots(figsize = (15,15))
    austin_map.plot(ax=ax, alpha=0.4, color="k")
    plot = geo_df[geo_df["Categories_merged"] == category].plot(ax=ax, markersize=100, color="m", marker="p", label=str(category))
    ax.set_title("Food Category = " + str(category))
    return ax,fig

#run a for loop to save plots for individual categories
for category in list_of_categories:
    ax, fig = plot_foodcategory(category)
    fig.savefig("artifacts/figures/{}.png".format(category), 
              dpi=100, format="png", 
              bbox_inches="tight")
    plt.close()

#write a code to merge the individual graph images into a gif
frames = []
imgs = glob.glob("artifacts/figures/*.png")
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)
 
frames[0].save("artifacts/figures/category.gif", format="GIF",
               append_images=frames[1:],
               save_all=True,
               duration=1000, loop=0)
