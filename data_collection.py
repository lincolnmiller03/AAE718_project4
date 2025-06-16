import requests
import pandas as pd
import os
from api_key import CENSUS_API_KEY

def get_census_data():
    url = "https://api.census.gov/data/2022/acs/acs5"
    variables = [
        "B19013_001E",  # Median household income
        "B01003_001E",  # Total population
        "B15003_022E",  # Bachelor's degree
        "B15003_017E",  # High school graduate
        "B25064_001E",  # Median gross rent
        "B25077_001E",  # Median home value
    ]
    var_str = ",".join(variables)
    params = {
        "get": var_str,
        "for": "county:*",
        "key": CENSUS_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data[1:], columns=data[0])
    df = df.apply(pd.to_numeric, errors='coerce')
    
    df["pct_bachelors"] = df["B15003_022E"] / df["B01003_001E"]
    df["pct_highschool"] = df["B15003_017E"] / df["B01003_001E"]
    df = df.drop(columns=["B15003_022E", "B15003_017E"])
    
    df.dropna(inplace=True)
    df.rename(columns={"B19013_001E": "median_income"}, inplace=True)
    return df