# How to Find Market Niche for your Business
## Introduction
                                                            
Have you thought about using web scraping for your potential dish scraping business? If yes, this report would give you an applicable method to follow, which would pay off in the future. The goal of the project is to provide an insightt to potential investors in food & beverage industry. The idea here is to scrape Yelp restaurants data, clean it, then analyze it by finding out which cuisine has a market niche, and where it locates in Austin?

We don't recommend taking a decsison based on only these results since it requires deep-dive in market validation and market research. However, the analysis would be helpful for preliminary purposes.

## API Scraping

First of all, we extracted dataset data from Yelp website which was used for our methdology. Basically, we utilized [Yelp API documentation](https://www.yelp.com/developers/documentation/v3) to scrape resturants in Austin. We were able to extract restaurant details such as name, address, coordinates, rating, review count, restaurant category, price level and transaction types (pickup, delivery and/or restaurant reservation). 

The code in the "Learning API" folder is what we used to learn how the API works, how to grab our desired parameters, and test our code. Gathering some of the parameters included extra steps, so we divided the parameters amongst ourselves to learn how to get each one. Once we figured out how to get each parameter we desired, we combined all this knowledge into one python script. We created a list of dictionaries from the results and wrote it to a CSV so the other members of the group can begin cleaning and analyzing the data. We left the "Learning API" folder to show the steps we took figuring out the API and incase we needed a backup.

Yelp has a cap of scrapped data from API, so we were only able to get results of 1000 different resturants in Austin city. However, we still think that's a big sample which could test our approach. 

## Data Cleaning

The API dataset needed to be cleaned and reformatted for analysis purposes. `Pandas` library was primarily used for data preprocessing. First, we dropped records with missing price level data, so we could get a an overview of the average price per category. Second, to remove rating bias due to low number reviews, records with reviews count less than 10 were also dropped. This threshold of 10 was selected based on a review count CDF plot. 

The Yelp scraped dataset included 124 different categories for restaurants. That was a lot! So, these were aggregated into 10 broader groups to analyze which category would be best to invest in. Then, we used coding magic to separate (strip) Zipcodes from address data, and latitude and longitude values from coridinate information. In addition, transaction types were separated to indivdual columns with binary values for each unique type.

Also, ratings and review counts were standardized using by z-scoring to have them within the same scale for the analytical  part. Finally, we converted the price level from `$` to numbers from 1-4 for averaging analysis.

## Analysis

### What does restaurant population in Austin look like

Austin restaurants seem to be popular among for people with a mean rating of 4.1 evaluated from 739 restaurants. Nearly 84% of the restaurants offer delivery. This seems coherent with the busy lifestyle of Austinites. 

|      | Summary Statistics |              |                     |                           |
|------|--------------------|--------------|---------------------|---------------------------|
|      |                    |              |                     |                           |
|      | Rating             | Review count | Standardized Rating | Standardized Review count |
| min  | 2                  | 10           | -4.66E+00           | -6.62E-01                 |
| max  | 5                  | 5560         | 2.00E+00            | 8.46E+00                  |
| std  | 0.45               | 608.26       | 1.00E+00            | 1.00E+00                  |
| mean | 4.10               | 412.49       | -1.82E-16           | 4.03E-17                  |
| var  | 0.20               | 369980.55    | 1.00E+00            | 1.00E+00                  |
|      |                    |              |                     |                           |
|      | Delivery           | Pickup       | Reservation         |                           |
| sum  | 619                | 315          | 6                   |                           |



To start with lets get a visual idea of where the restaurants are located in Austin. Yelpen lists the price range in 3 categories i.e low price, medium price and high price. With help of cordinates obtained from Yelp we plotted them on Austin City map boundaries. Restaurants seem to be uniformly distributed with respect to price. One expected observation is that expensive (more likely fine dining) restaurants are not present in Outskirts of the city like south Austin or Winderson Mill. Most of the restaurants are concentrated in central Austin (Downtown, campus area, east caeser chavez, north loop etc). Most of them are situated along I-35 and Mopac (not surprising). 

![Restaurant Locations in Austin](/artifacts/figures/price_range_map.png)

This map is populated using the script: price_range_map.py

### How do categories vary across Austin?

We observed that there are many categories of food in Austin and so naturally it would be interesting to see how dense these categories are in Austin. For better visualization we have populated this data on Austin map and animated into a gif to showcase the transition between food categories. Quite expectedly American`(`BBQ!!!`)`, Mexican, Asian and everybody's BYOB favourite Pizza seem to top the charts. Funnily enough no taker for vegan food in Austin `(`At least yet`)`

| Categories                                         
|----------------------------------------------------|
| American                                           |
| Asian                                              |
| Mexican/South American                             |
| Pizza/European                                     |
| Bars/Pubs                                          |
| Cafes/Juice bars/Desserts                          |
| Middle-eastern/Indian/African                      |
| Food Trucks/Food Stands                            |
| Food delivery services/groceries/venues/cafeterias |
| Specification (Vegan/Glutenfree)                   |

![Food Categories](/artifacts/figures/category.gif)


This map is populated using the script: category_map.py

### Which Category is the best?

We analyzed the resturants by their category in order to get the averages of price level, review count, rating, Rating_stndized, and the number of resturants per category. Then we plotted the most intresting results which is the average rating, and the number of resturants by category. Since we are looking for the best invesment opportunities in terms of market niche, we would be intrested in the category with the highest average rating and lowest number of resturants. In this case, the investor could get an idea about the gap between the supply and demand. We believe based on our data, that would be a good plimenery result to identify the gap. However, investors should take that with a grain of salt.

As we can see from the graph below, the market is saturated with American, Mexican/South American, and Asian. However, by looking at the Food Truck/Food Stands and Middle Eastern/Indian/African categories, we can see good opportunites there in terms of lack of number of resturants, and their high reviews which reflects the prefrence of the consumers. For the sake of this project we decided to deep-dive into the Food Truck/Food Stands category.

![Best Restaurants Category](/artifacts/best_restaurant.jpeg)

### What Zip Code is optimal?

For this section, we had look into the zip codes of the Food Truck/Food Stands to find which zip codes have the highest customer engagments using Yelp reviewers. We believe this a good method to use since it could give the investor an insight where customers have higher probability to write a comment in Yelp for your restaurant which the investor could leverage on.

Since some of the Food Truks are located within the same zip codes, we had to group them by the zip code and finding the average review counts, number of food trucks in each zip code, and average rating with a zip code.

In order to build a statstical measure for market niche, we created a statstical ratio for that. So basically, we multiplied the average rating by the average number of reviews within a zip code, then divide that by the number of restaurants to penalize the ratio. The idea here is to inflate the number of the average review counts if you have good reviews, and discount it by the number of food trucks to be able to find market niche.

Market Niche = (Average Number of Reviews by the Zip Code * Average Rating by the Zip Code)/Number of Restaurants

We found out that 78741 is the highest by far. One reason is because there is an HEB market in this ZIP Code, with an elementary school which reflects a neighborhood with certain purchasing power.

![Food Trucks in Austin by Zip Code](/artifacts/food_trucks.jpeg)

## Conclusion

So this analysis would be prudent to explore potential restaurant categories in the food and beverage sector. We leveraged our skills in scraping to explore the data in Austin. Then we cleaned it, and analyze it accordingly. This analysis would be helpful to be included in the market validation study within the food and beverage sector.

## Limitation and Scope for Future Developments

Yelp results from API scraping and therefore potentially there could be more data that we could not access. Regardless of the search Yelp would given only 2400 results in one go limiting our opportunity to get more data. Additionally, we also faced that API scrapping limited the number of features we could achieve. Having said that Yelp has built a very sophisticated and user-friendly API system. 
While Yelp has given access to plethora of things, the data could be cleaner. We found 124 food categories across 739 restaurants which hindered any meaningful analysis. The dataset was also not devoid of missing values. 

We dont have the detailed price and sales volume for every restaurant which hindered out chances of doing more granular analysis.

We did find plethora of information on reviewers on Yelp. This can be sufficient to perform a reviewer profiling and ask some useful questions on credibility of reviewers and perhaps quantify how valuable reviews are to a business. 
We also think we can expand the results from our search in terms of geography, food categories etc. 
Furthermore, this offers opportunity  to run multiple prediction models to analyse different aspects like popularity of restaurants, rating accuracy, fraudulent  reviewers etc. 
