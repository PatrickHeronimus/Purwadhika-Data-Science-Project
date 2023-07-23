# Purwadhika-Data-Science-Project

## `Background`

#### Housebiz is a prominent real estate company operating in various regions across the United States. With a focus on providing high-quality services to homebuyers and sellers, Housebiz relies on data-driven insights to make informed decisions and offer personalized solutions to their clients. To achieve this, they have collected a comprehensive dataset containing valuable information about housing attributes in California. 
#### This dataset includes features such as longitude, latitude, housing median age, total rooms, total bedrooms, population, households, median income, median house value, and ocean proximity. Leveraging the power of machine learning and regression analysis, Housebiz aims to gain valuable insights into the real estate market dynamics and factors influencing housing prices, helping them better serve their clients and make strategic business decisions.

## `Problem Statement`
#### Being competitive in the real estate business means we should generate profit to our company but also mantain our real estate prices so we can still compete with other competitors.

## `Goals`
#### Create a predictive tools that can predict the correct price for real estate in California. Because the target variable is continuous, we will use Supervised Machine Learning Regression

## `Metrics Evaluation`
#### The evaluation metrics that will be used are RMSE, MAE, and MAPE. RMSE is the mean value of the square root of the error, MAE is the mean absolute value of the error, MAPE is the average percentage error generated by the regression model. The smaller the RMSE, MAE, and MAPE values, the more accurate the model is in predicting the house price according to the features limitations.

## `The dataset consist a number of columns that is displayed below`

**Attributes Information**

| **ATTRIBUTE** | **DESCRIPTION** |
| --- | --- |
| longitude | The longitude coordinate of the location of the housing property |
| latitude | The latitude coordinate of the location of the housing property |
| housing_median_age | The median age of houses in the area |
| total_rooms | The total number of rooms in all housing units in the area |
| total_bedrooms | The total number of bedrooms in all housing units in the area |
| population | The total population of the area |
| households | The total number of households in the area |
| median_income | The median income of households in the area |
| median_house_value | The median value of houses in the area |
| ocean_proximity | The proximity of the housing area to the ocean or other bodies of water |

## `Analytic Approach`
#### Data Understanding :
Data Understanding is the initial step in the data analysis process, where the primary goal is to gain a comprehensive understanding of the dataset's characteristics, contents, and structure.
#### Data Preprocessing :
The primary goal of data preprocessing is to clean, preprocess, and prepare the data to improve the performance and accuracy of machine learning algorithms.
Checking null values, duplicate and outliers.
#### Data Split, Train and Test :
The dataset is divided into two or more subsets: the training set and the testing set. The training set is used to train the machine learning model, while the testing set is used to evaluate the model's performance.
#### We use 5 different testing models which is :
#### - Linear Regression
#### - KNN Regression
#### - Decision Tree Regression
#### - Random Forest Regression
#### - XGBoost Regression 

## `Conclusion`

#### According to the modelling that has been done, we can conclude that the location of the house is the most influental features on the price and the median_income came second. 
#### At first, our prediction would be a house near the ocean will have a higher affection towards the price rather than a house that is away from the ocean. But after some modelling, it is shown that unexpectedly, a house that located away from the ocean affects the price more rather than a house located near the ocean. 
#### The second most influental features to the price is none other than the income influence or median_income. For this data, it is not very surprising because as areas with higher income levels often have higher housing prices. 
#### The evaluation metrics used are RMSE, MAE & MAPE. From the MAPE value produced by the XGBoost Model after hyperparameter tuning is 17.91% which is better than before hyperparameter tuning although the increase is slightly. Which means that our model estimated price will be missed about 17.91% from the actual price of the house. 

## `Recommendations`

#### For things that could be done to improve the model are :
#### - Collecting More Data
Gather more data to increase the size of the dataset. More data can help the model learn better patterns and improve performance. Such as crime rate in each area. 
#### - Update the Data Frequently
If the housing dataset changes overtime, update the dataset regularly to keep the model up-to-date and relevant so it can generate a more suitable and reasonable value for the real estate. 