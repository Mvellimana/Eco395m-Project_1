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
df = pd.read_csv(io.StringIO(download.decode("utf-8")))


#Select needed variables

df_anlz = df[[
"categories", 
"Categories_merged", 
"price level", 
"review count", 
"Review count_stndized", 
"rating", 
"Rating_stndized", 
"Zipcode"]].copy()


#Replace dollar signs to use it later for price avg/category

df_anlz["price level"] = df_anlz["price level"].replace("$", 1)
df_anlz["price level"] = df_anlz["price level"].replace("$$", 2)
df_anlz["price level"] = df_anlz["price level"].replace("$$$", 3)
df_anlz["price level"] = df_anlz["price level"].replace("$$$$", 4)

#group variables by category to find their mean

df_anlz_sum = df_anlz[[
"Categories_merged", 
"price level", 
"review count", 
"rating", 
"Rating_stndized"]].groupby(["Categories_merged"]).mean()


#findng number of resturants by category and standarized them

df_anlz_sum2 = df_anlz.groupby(["Categories_merged"])["Categories_merged"].count().reset_index(name="rest_count")
df_anlz_sum2["rest_count_standarized"] = df_anlz_sum2.rest_count.transform(zscore, ddof=1)



#merge the standarized and non-standarized ones

df_anlz_final = pd.merge(df_anlz_sum, df_anlz_sum2, on = "Categories_merged")

df_anlz_final = df_anlz_final.sort_values(by=["Rating_stndized"], ascending= False)



# plot the standarized values of average ratings (more is good) and number of resturants (less is good) by category

x = np.arange(len(df_anlz_final.Categories_merged))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.barh(x - width/2, df_anlz_final.Rating_stndized, width, label="Average Rating", align="center")
rects2 = ax.barh(x + width/2, df_anlz_final["rest_count_standarized"], width, label="Number of Restaurants", align="center")

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel("Restaurant Cateogries")
ax.set_xlabel("Standarized Scale")
ax.set_title("Best Restaurant Category")
ax.set_yticks(x, df_anlz_final.Categories_merged)
ax.legend(loc="best")

fig.tight_layout()



#filter the data by food truks

df_fig3 = df_anlz.query('Categories_merged == "Food Trucks/Food Stands"')


#Get avg review count, resturant numbers by zip code, avg rating by zip code

df_fig3_sum = df_fig3.groupby(["Zipcode"])["review count"].mean().reset_index(name="avg_review_count")
df_fig3_sum2 = df_fig3.groupby(["Zipcode"])["Zipcode"].count().reset_index(name="rest_count_by_zipcode")
df_fig3_sum3 = df_fig3.groupby(["Zipcode"])["rating"].mean().reset_index(name="avg_rating")



#merge all the previous generated columns to one dataframe

df_fig3_final = pd.merge(df_fig3_sum, df_fig3_sum2, on = "Zipcode")
df_fig3_final = pd.merge(df_fig3_final, df_fig3_sum3, on = "Zipcode")


#come up with a stat to measure market niche by multiplying avg number of reviews by zip code by average rating by zip code, and divding that by number of resturants by zip code 


df_fig3_final["marker_niech"] =( df_fig3_final["avg_review_count"] * (df_fig3_final["avg_rating"])) / df_fig3_final["rest_count_by_zipcode"]
df_fig3_final = df_fig3_final.sort_values("marker_niech", ascending= True)


#Plot the market niche stat by zip code and take the highest

x2 = np.arange(len(df_fig3_final.Zipcode))  # the label locations

fig, ax = plt.subplots()
rects1_fig3 = ax.barh(x2 - width/2, df_fig3_final.marker_niech, width, align="center")


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel("Zip Codes")
ax.set_xlabel("Market Niche Value")
ax.set_title("Food Trucks Areas in Austin (Yelp Sample)")
ax.set_yticks(x2, df_fig3_final.Zipcode)




plt.show()

