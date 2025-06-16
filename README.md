# Census Income Prediction Project

## Overview
This project aims to predict median household income at the county level using data from the U.S. Census Bureau's American Community Survey (ACS). The goal is to explore socioeconomic factors and develop a regression model to estimate median income based on demographic and housing variables.

The project uses the Census API to download the data, processes and cleans it, then applies a linear regression model to predict median income. The model's performance is evaluated on both training and testing sets, with results visualized to compare actual vs predicted incomes.

## Data Source
* **Data**: 2022 American Community Survey 5-Year Estimates (ACS 5)
* **API**: U.S. Census Bureau API
* **Variables used**: Median household income; Total population; % of population with a bachelor's degree; % of population with a high school diploma; Median gross rent; Median home value

## Setup Instructions
1. Register for a Census API Key
* Visit the [Census Bureau's API page](https://www.census.gov/data/developers/guidance/api-user-guide.html) and register for an API key.

2. Store your API Key
* Create a file named ```api_key.py``` in your project directory.
* Add the following line, replacing ```YOUR_KEY_HERE``` with your actual API key:
```CENSUS_API_KEY = "YOUR_KEY_HERE"```

## How to Run
1. Run the main script in ```main.py```
2. The script will:
* Import and clean Census data from the API.
* Train a linear regression model to predict median household income.
* Output training and testing R-squared scores.
* Display a scatter plot comparing actual vs. predicted median incomes.

## Code in Repo
```api_key.py```: Stores your Census API key.

```data_collection.py```: Contains get_census_data() function that pulls and cleans data from the Census API.

```model.py```: Contains train_model() function that trains a linear regression model and evaluates it.

```main.py```: Main script to conduct data fetching and modeling.