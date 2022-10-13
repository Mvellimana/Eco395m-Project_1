import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""Load in csv with Yelp API scraped data"""
url = "https://raw.githubusercontent.com/Mvellimana/Eco395m-Project_1/main/results.csv"

download = requests.get(url).content
Yelp_scrape = pd.read_csv(io.StringIO(download.decode("utf-8")))


"""Merging categroies to create 10 bins"""

temp_catg = np.zeros(np.shape(Yelp_scrape.categories))

mexican = (Yelp_scrape.categories == "Mexican")|(Yelp_scrape.categories == "Tex-Mex")|(Yelp_scrape.categories == "Tacos")|(Yelp_scrape.categories == "Tapas/Small Plates")|(Yelp_scrape.categories == "Tapas Bars")|(Yelp_scrape.categories == "Empanadas")|(Yelp_scrape.categories == "Caribbean")|(Yelp_scrape.categories == "Venezuelan")|(Yelp_scrape.categories == "Colombian")|(Yelp_scrape.categories == "Latin American")|(Yelp_scrape.categories == "Brazilian")|(Yelp_scrape.categories == "Cuban")|(Yelp_scrape.categories == "Salvadoran")|(Yelp_scrape.categories == "Peruvian")|(Yelp_scrape.categories == "Puerto Rican")|(Yelp_scrape.categories == "Honduran")|(Yelp_scrape.categories == "Argentine")|(Yelp_scrape.categories == "Trinidadian")
foodtrucks = (Yelp_scrape.categories == "Food Trucks")|(Yelp_scrape.categories == "Food Stands")
american = (Yelp_scrape.categories == "Bagels")|(Yelp_scrape.categories == "Sandwiches")|(Yelp_scrape.categories == "Steakhouses")|(Yelp_scrape.categories == "American (New)")|(Yelp_scrape.categories == "Breakfast & Brunch")|(Yelp_scrape.categories == "American (Traditional)")|(Yelp_scrape.categories == "Burgers")|(Yelp_scrape.categories == "Chicken Wings")|(Yelp_scrape.categories == "Salad")|(Yelp_scrape.categories == "Cajun/Creole")|(Yelp_scrape.categories == "Delis")|(Yelp_scrape.categories == "Diners")|(Yelp_scrape.categories == "Fast Food")|(Yelp_scrape.categories == "Hot Dogs")|(Yelp_scrape.categories == "Soul Food")|(Yelp_scrape.categories == "Cheesesteaks")|(Yelp_scrape.categories == "Smokehouse")|(Yelp_scrape.categories == "Supper Clubs")|(Yelp_scrape.categories == "Southern")|(Yelp_scrape.categories == "Barbeque")|(Yelp_scrape.categories == "Seafood")|(Yelp_scrape.categories == "Poke")|(Yelp_scrape.categories == "Hawaiian")|(Yelp_scrape.categories == "Polynesian")|(Yelp_scrape.categories == "Tiki Bars")
euro = (Yelp_scrape.categories == "Pizza")|(Yelp_scrape.categories == "Italian")|(Yelp_scrape.categories == "Tuscan")|(Yelp_scrape.categories == "Creperies")|(Yelp_scrape.categories == "French")|(Yelp_scrape.categories == "German")|(Yelp_scrape.categories == "Modern European")|(Yelp_scrape.categories == "Greek")|(Yelp_scrape.categories == "Basque")
bars = (Yelp_scrape.categories == "Bars") | (Yelp_scrape.categories == "Cocktail Bars") | (Yelp_scrape.categories == "Lounges") | (Yelp_scrape.categories == "Sports Bars") | (Yelp_scrape.categories == "Pubs") | (Yelp_scrape.categories == "Breweries") | (Yelp_scrape.categories == "Wine Bars") | (Yelp_scrape.categories == "Gastropubs") | (Yelp_scrape.categories == "Dive Bars") | (Yelp_scrape.categories == "Beer Gardens") | (Yelp_scrape.categories == "Brewpubs") | (Yelp_scrape.categories == "Irish Pub") | (Yelp_scrape.categories == "Izakaya") | (Yelp_scrape.categories == "Beer Bar") | (Yelp_scrape.categories == "Irish") 
asian = (Yelp_scrape.categories == "Sushi Bars") | (Yelp_scrape.categories == "Japanese") | (Yelp_scrape.categories == "Vietnamese") | (Yelp_scrape.categories == "Korean") | (Yelp_scrape.categories == "Thai") | (Yelp_scrape.categories == "Chinese") | (Yelp_scrape.categories == "Asian Fusion") | (Yelp_scrape.categories == "Ramen") | (Yelp_scrape.categories == "Dim Sum") | (Yelp_scrape.categories == "Noodles") | (Yelp_scrape.categories == "Szechuan") | (Yelp_scrape.categories == "Filipino") | (Yelp_scrape.categories == "Japanese Curry") | (Yelp_scrape.categories == "Singaporean") | (Yelp_scrape.categories == "Laotian") | (Yelp_scrape.categories == "Hainan") | (Yelp_scrape.categories == "Cambodian") | (Yelp_scrape.categories == "Indonesian") | (Yelp_scrape.categories == "Conveyor Belt Sushi")
mid_ind_af = (Yelp_scrape.categories == "Mediterranean") | (Yelp_scrape.categories == "Halal") | (Yelp_scrape.categories == "Middle Eastern") | (Yelp_scrape.categories == "Turkish") | (Yelp_scrape.categories == "Lebanese") | (Yelp_scrape.categories == "Kebab") | (Yelp_scrape.categories == "Indian") | (Yelp_scrape.categories == "Himalayan/Nepalese") | (Yelp_scrape.categories == "Ethiopian") | (Yelp_scrape.categories == "South African") 
cafe_jui_dess = (Yelp_scrape.categories == "Coffee & Tea") | (Yelp_scrape.categories == "Cafes") | (Yelp_scrape.categories == "Juice Bars & Smoothies") | (Yelp_scrape.categories == "Bubble Tea") | (Yelp_scrape.categories == "Coffee Roasteries") | (Yelp_scrape.categories == "Bakeries") | (Yelp_scrape.categories == "Desserts") 
speci = (Yelp_scrape.categories == "Vegan") | (Yelp_scrape.categories == "Vegetarian") | (Yelp_scrape.categories == "Gluten-Free") 
misc = (Yelp_scrape.categories == "Chicken Shop") | (Yelp_scrape.categories == "Venues & Event Spaces") | (Yelp_scrape.categories == "Food Court") | (Yelp_scrape.categories == "Grocery") | (Yelp_scrape.categories == "Caterers") | (Yelp_scrape.categories == "Restaurants") | (Yelp_scrape.categories == "Comfort Food") | (Yelp_scrape.categories == "Butcher") | (Yelp_scrape.categories == "Buffets") | (Yelp_scrape.categories == "Personal Chefs") | (Yelp_scrape.categories == "Music Venues") | (Yelp_scrape.categories == "Dance Clubs") | (Yelp_scrape.categories == "Do-It-Yourself Food") | (Yelp_scrape.categories == "Cafeteria") | (Yelp_scrape.categories == "Art Galleries") | (Yelp_scrape.categories == "Food Delivery Services") 

temp_catg[mexican.values] = 1
temp_catg[foodtrucks.values] = 2
temp_catg[american.values] = 3
temp_catg[euro.values] = 4
temp_catg[bars.values] = 5
temp_catg[asian.values] = 6
temp_catg[mid_ind_af.values] = 7
temp_catg[cafe_jui_dess.values] = 8
temp_catg[speci.values] = 9
temp_catg[misc.values] = 10

Yelp_scrape["Categories_merged"] = temp_catg

Yelp_scrape["Categories_merged"] = Yelp_scrape["Categories_merged"].replace(1,"Mexican/South American")
Yelp_scrape["Categories_merged"] = Yelp_scrape["Categories_merged"].replace(2,"Food Trucks/Food Stands")
Yelp_scrape["Categories_merged"] = Yelp_scrape["Categories_merged"].replace(3,"American")
Yelp_scrape["Categories_merged"] = Yelp_scrape["Categories_merged"].replace(4,"Pizza/European")
Yelp_scrape["Categories_merged"] = Yelp_scrape["Categories_merged"].replace(5,"Bars/Pubs")
Yelp_scrape["Categories_merged"] = Yelp_scrape["Categories_merged"].replace(6,"Asian")
Yelp_scrape["Categories_merged"] = Yelp_scrape["Categories_merged"].replace(7,"Middle-eastern/Indian/African")
Yelp_scrape["Categories_merged"] = Yelp_scrape["Categories_merged"].replace(8,"Cafes/Juice bars/Desserts")
Yelp_scrape["Categories_merged"] = Yelp_scrape["Categories_merged"].replace(9,"Specification (Vegan/Glutenfree)")
Yelp_scrape["Categories_merged"] = Yelp_scrape["Categories_merged"].replace(10,"food delivery services/groceries/venues/cafeterias")

"""Create coordinate columns"""

Yelp_scrape["Latitude"] = Yelp_scrape["coordinates"].apply(lambda st: st[st.find(""latitude": ")+11:st.find(", "lon")])
Yelp_scrape["Longitude"] = Yelp_scrape["coordinates"].apply(lambda st: st[st.find(""longitude": ")+12:st.find("}")])


Yelp_scrape["Latitude"]= Yelp_scrape["Latitude"].astype(float)
Yelp_scrape["Longitude"]= Yelp_scrape["Longitude"].astype(float)

"""Remove square brackets in address and create new column for zipcode"""

Yelp_scrape["Address_mod"]= Yelp_scrape["address"].str.strip("[]")
Yelp_scrape["Zipcode"] = Yelp_scrape["Address_mod"].apply(lambda st: st[st.find(", TX ")+5:-1])
Yelp_scrape["Zipcode"]=Yelp_scrape["Zipcode"].str.strip()

"""Create binary transc columns"""

Yelp_scrape["Delivery"]= Yelp_scrape["transaction types"].str.contains("delivery")
Yelp_scrape["Delivery"]= Yelp_scrape["Delivery"].astype(int)

Yelp_scrape["Pickup"]= Yelp_scrape["transaction types"].str.contains("pickup")
Yelp_scrape["Pickup"]= Yelp_scrape["Pickup"].astype(int)

Yelp_scrape["Reservation"]= Yelp_scrape["transaction types"].str.contains("restaurant_reservation")
Yelp_scrape["Reservation"]= Yelp_scrape["Reservation"].astype(int)

"""Dropping records with no price data"""
Yelp_scrape["price level"]=Yelp_scrape["price level"].str.strip().replace("",np.nan)
Yelp_scrape["price level"].replace("", np.nan, inplace=True)
Yelp_scrape.dropna(subset=["price level"], inplace=True)

"""Finding review threshold"""
Yelp_scrape.sort_values("review count")
plt.rcParams["figure.figsize"] = (20,10)
review_ct = pd.Series(Yelp_scrape["review count"].values, index=Yelp_scrape["id"])

review_ct.hist(cumulative=True, density=1, bins=500)

plt.xticks(np.arange(0, 6000, 200))

plt.show()

"""Dropping records with review less than 10"""

Yelp_scrape = Yelp_scrape.drop(Yelp_scrape[(Yelp_scrape["review count"] <10) ].index)

"""Create std rating and review count"""

Yelp_scrape["Rating_stndized"] =( Yelp_scrape["rating"] - Yelp_scrape["rating"].mean() ) / Yelp_scrape["rating"].std()
Yelp_scrape["Review count_stndized"] =( Yelp_scrape["review count"] - Yelp_scrape["review count"].mean() ) / Yelp_scrape["review count"].std()

"""standard deviation by category"""
Yelp_scrape["Stnd_dev_by_catg"] =Yelp_scrape.groupby("Categories_merged")["review count"].transform("std")


"""summary stat"""
Yelp_scrape[["rating","review count","Rating_stndized","Review count_stndized"]].agg(["min", "max", "std", "mean","var"])

Yelp_scrape[["Delivery","Pickup","Reservation"]].agg(["sum"])  

"""Save to csv"""
Yelp_scrape.to_csv("Yelp_API_Data_Cleaned.csv", index = False)  
