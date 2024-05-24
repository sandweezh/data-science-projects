# Capstone: Activity planner

Author: Cher Wee Zheng

## Overview

This project aims to creata a recommender system to recommend a list of restaurants and activities in Singapore based on a user's inputted preferences of cuisine, budget and activity type preference. By leveraging on techniques such as content-based and collaborative filtering, this system seeks to assist individuals like Wee Zack in quickly recommending a list of restaurants and activiities for his date, reducing the research and effort he needs to put in to planning the date. 

## Persona

Wee Zack, a 26 year old man, is wondering where to take his girlfriend out for a date. He is a homebody and does not know much about the different restaraunts and activities in Singapore. He wants to plan an enjoyable date which is customised to his and his girlfriend's preferences, but to do the research manually would be very time consuming as there are many restaurants and activities in Singapore to choose from. He seeks a solution to quickly help him narrow down the choices.

## Data Sources

Secret Singapore: https://secretsingapore.co/things-to-do-singapore/
The Smart Local: https://thesmartlocal.com/read/things-to-do-singapore/
Yelp: https://www.yelp.com/search?find_desc=Restaurants&find_loc=Singapore&attrs=RestaurantsPriceRange2.1

## Problem Statement

How might we help individuals to plan out their date quickly to ensure the best experience possible, taking into account their budget, location, food preferences and activity preferences?

## Python Version and Libraries
- ScrapingBee
- Scikit-learn
- Pandas
- Numpy
- Matplotlib
- Seaborn
- OpenCV
- Plotly
- Surpise
- Geopy
- json
- Googlemaps


## Scraping

The data for this project was scraped from various websites including TheSmartLocal, Yelp, Google Places, Secret Singapore. They were then compiled into 2 datasets, one for restaurants and one for activities, and their coordinates were extracted for distance computation later on. 

## Modelling

This recommender system is a hybrid model comprising of content-based filtering and collaborative filtering. Due to lack of data, dummy data of 150 users and their interactions with the restaurants and activities in the dataset were created. Several matrix factorisation techniques were tested in this model, such as Alternating Least Squares, Non-negative Matrix Factorisation, SlopeOne and Singular Vector Decomposition. 

## Model Selection

Due to the randomness of the data, the results of the matrix factorisation were poor and they were not incorporated into the final model. Instead, the model has 3 layers:

1. Collaborative filtering - where the recommendations were made based on the new user's similarity to existing dummy users, and the highly rated items of the dummy users were recommended.

2. Content-based filtering - where items which were similar to the user's inputted preferences were recommended. 

3. Comparing the two sets of recommendations from the first 2 layers, a score was given to the overlapping items based on weights of the user's inputted preferences and distance. 



## Training Results

| Algorithm             |     RMSE | MAAE   | 
|-----------------------|----------|--------|
| SVD                   |   1.531  | 1.305  |      
| NMF                   |   1.459  |  1.26  |      
| SlopeOne              |   1.425  |  1.228 |       
| ALS                   |   1.464  |  1.27  |       
| SVDpp                 |   1.535  | 1.303  |       





## Conclusion

In response to the problem statement, this project has developed a recommender system that is capable of recommending restaurants and activities in Singapore based on the user's input preferences. However, as there is no existing user interaction data available, the model is limited in providing recommendations which take into account latent factors or items which other users verify. However, this problem is expected to diminish over time as more users use the system and their data is collected and trained on. 

# Recommendations

Moving forward, as more real user interaction data is gathered, the model can incorporate more collaborative filtering where the inputted user can have predicted ratings for restaurants/activities he has not visited before, based on similar users who have. The database of restaurants and activities will also increase, giving users more options. Currently the existing database is limited due to scraping limits for free users and time constraint. 


