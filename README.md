# Eco395m-Project_1(UPDATE TITLE)
                                                            

Objective
- Provide recommendations on XXX to a potential restaurant owner/investor by anlyzing Austin restaurant data from Yelp.

Dataset
Data from Yelp website was used for our study. An API scraping of the Austin area was done to extract restaurant details such as name, address, coordinates, rating, review count, restaurant category, price level and transaction types (pickup, delivery and/or restaurant reservation). This produced a result containing 1000 different resturants in Austin city.

Methodology

- API Scraping

- Data Cleaning
  The API dataset needed to be cleaned and reformatted for analysis purposes. Pandas library was primarily used for data pre processing. Records with 
  missing price level data were dropped. To remove rating bias due to low number reviews, records with reviews count less than 10 were also dropped. This 
  threshold of 10 was selected based on a review count CDF plot.
  The Yelp scraped dataset included 124 different categories for restaurants. These were aggregated into 10 broader groups. Zipcodes were separated from 
  address data, and latitude and longitude values were extracted from cooridinate information. Transaction types were separated to indivdual columns with 
  binary values for each unique type. Ratings and review counts were standized using the z-score formula. 

- Analysis

Results

Conclusion

Limitation and Future work

- Further analysis is recommended to estimate missing price data. Due to time constraints records with missing data were dropped. 





