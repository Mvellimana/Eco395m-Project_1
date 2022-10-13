# How to Find Market Niche for your Business
## Introduction

Have you thought about using web scraping for your potential dish scraping business? If yes, this report would give you an applicable method to follow, which would pay off in the future. The goal of the project is to provide an insghit to potential investors in food & beverage industry. The idea here is to scrape Yelp resturants data, clean it, then analyze it by finding out which cusine has a market niche, and where it locates in Austin?

We don't recommend taking a decsison based on only these results since it requires deep-dive in market validation and market research. However, the analysis would be helpful for pleminary purposes.


## API Scraping

First of all, we extracted dataset data from Yelp website which was used for our methdology. Basically, we utilized [Yelp API documentation](https://www.yelp.com/developers/documentation/v3) to scrape resturants in Austin. We were able to extract restaurant details such as name, address, coordinates, rating, review count, restaurant category, price level and transaction types (pickup, delivery and/or restaurant reservation). Yelp has a cap of scrapped data from API, so we were only able to get results of 1000 different resturants in Austin city. However, we still think that's a big sample which could test our approach. 



## Data Cleaning

The API dataset needed to be cleaned and reformatted for analysis purposes. `Pandas` library was primarily used for data pre processing. First, we dropped records with missing price level data, so we could get a an overview of the average price per category. Second, to remove rating bias due to low number reviews, records with reviews count less than 10 were also dropped. This threshold of 10 was selected based on a review count CDF plot. 

The Yelp scraped dataset included 124 different categories for restaurants. That was a lot! So, these were aggregated into 10 broader groups to analyze which category would be best to invest in. Then, we used coding magic to seperate (strip) Zipcodes from address data, and latitude and longitude values from cooridinate information. In addition, transaction types were separated to indivdual columns with binary values for each unique type.

Also, ratings and review counts were standarized using by z-scoring to have them within the same scale for the anlatical part. Finally, we converted the price level from `$` to numbers from 1-4 for averaging analysis.



## Analysis

First we had 


