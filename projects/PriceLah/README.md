# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 2: Singapore Housing Data and Kaggle Challenge

## Overview

In project 2, each group is tasked with creating a regression model based on Singapore Housing Dataset. This model will predict the price of a house at sale. The Dataset is an exceptionally detailed one with over 70 columns of different features relating to houses.

*Primary Learning Objectives:*

1. Creating and iteratively refining a regression model
2. Using Kaggle to practice the modeling process
3. Providing business insights through reporting and presentation.

---
## Problem Statement
Leveraging Data-Technology to reliably provide a Data-Driven prediction of HDB housing prices.

---
## Datasets
|Data File|Description|Source|
|---|---|---|
|[`train.csv`](./data/train.csv)|HDB housing resale transaction from 2012 to 2021. This is the dataset for training the model|[`Kaggle`](https://www.kaggle.com/competitions/dsi-sg-project-2-regression-challenge-hdb-price/)|
|[`test.csv`](./data/test.csv)|HDB housing resale transaction from 2012 to 2021. This is the dataset for generating predicted transcation price for Kaggle submission|[`Kaggle`](https://www.kaggle.com/competitions/dsi-sg-project-2-regression-challenge-hdb-price/)|

---
## Data Dictionary

|Feature|Type|Description|
|---|---|---|
|resale_price|integer|the property's sale price in Singapore dollars. This is the target variable.|
|Tranc_YearMonth|String|year and month of the resale transaction, e.g. 2015-02|
|town|String|HDB township where the flat is located, e.g. BUKIT MERAH|
|region|String|The town is grouped into west, north, east, north-east and central region|
|flat_type|String|type of the resale flat unit, e.g. 3 ROOM|
|flat_model|String|HDB model of the resale flat, e.g. Multi Generation|
|mid_storey|integer|median value of storey_range|
|floor_area_sqft|float|floor area of the resale flat unit in square feet|
|hdb_age|integer|number of years from lease_commence_date to present year|
|max_floor_lvl|integer|highest floor of the resale flat|
|Mall_Nearest_Distance|float|distance (in metres) to the nearest mall|
|Ammennities_same_block|integer|number of malls and hawker in the same block|
|Ammennities_Within_500m|integer|number of malls within 500 metres|
|Ammennities_Within_1km|integer|number of malls within 1 kilometre|
|Ammennities_Within_2km|integer|number of malls within 2 kilometres|
|mrt_nearest_distance|float|distance (in metres) to the nearest MRT station|
|bus_interchange|integer|boolean value if the nearest MRT station is also a bus interchange|
|mrt_interchange|integer|boolean value if the nearest MRT station is a train interchange station|
|pri_sch_nearest_distance|float|distance (in metres) to the nearest primary school|
|vacancy|integer|number of vacancies in the nearest primary school|
|sec_sch_nearest_dist|float|distance (in metres) to the nearest secondary school|
|cutoff_point|integer|PSLE cutoff point of the nearest secondary school|

---
## Notebooks
1. group_01_cleaning: Data Cleaning, EDA and Feature Engineering
2. group_02_visualisation: Visualisation
3. group_03_model_benchmarks: Model preparation, Cross Validation, Model Fitting and Training, Evaluation
4. group_06_kaggle: running test data through all the previous steps in the earlier notebooks 
---
## Preprocessing and Feature Engineering

### Data Import & Cleaning
Import all the selected datasets and perform data cleaning, including but not limited to, check for missing values and datatype, fill up missing value with "0", and drop the columns that are not relevant for the analysis (for example - all longitude and latitude data is not required as there is no geolocation analysis involved). 

### Exploratory Data Analysis
Explore the data through assessing the summary statistic and investigating trend.

### Data Visualization 
Visualizing the data can greatly enhance findings and reveal additional trends. Data visualization tool applied include Box plot, Bar plot, Histogram, Heatmap, and Scatter plot.

### Feature Engineering
- New features were derived from existing data, for example the `town` are grouped into `region`
- Interaction terms
- Standard scalar
- one-hot-encoding

---
## Modeling and Prediction
- Fit the data into Linear Regression
- Apply regularization techniques - Ridge and Lasso
- Train-Test-Split the data into 5-fold cross validation
- Linear Regression model is selected. Perform LINE+M assumption validation to confirm Linear Regression model is the appropriate for the data set. 

---
## Findings
- RMSE & R2 scores for Linear Regression, Ridge Regression and Lasso Regression were very similar. Hence regularisation tools like Lasso and Ridge are not required for this model. Our Linear Regression model has a RMSE of 52497.81 and a R2 score of 0.865. This means that 86.5% of the variability in house prices is accounted for by the model. 


---
## Recommendations
Include data from before 2012, as 2012 is around the time government introduced cooling measures like ABSD. Overall, HDB prices have been increasing for the past 20 years. 

--- 
