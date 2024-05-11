import pandas as pd
import numpy as np
import math

def process(df):
    df['Gender'] = df['Gender'].replace({'Male': 1, 'Female': 0})
    df['Has a car'] = df['Has a car'].replace({'Yes': 1, 'No': 0})
    df['Has a mobile phone'] = df['Has a mobile phone'].replace({'Yes': 1, 'No': 0})
    df['Has a work phone'] = df['Has a work phone'].replace({'Yes': 1, 'No': 0})
    df['Has an email'] = df['Has an email'].replace({'Yes': 1, 'No': 0})
    df['Has a property'] = df['Has a property'].replace({'Yes': 1, 'No': 0})
    df['Education level'] = df['Education level'].astype('category')
    df['Marital status'] = df['Marital status'].replace({'Single / not married': 0, 'Married': 1, 'Separated': 2})
    df['Education level'] = df['Education level'].replace({'Secondary / secondary special': 0, 'Incomplete higher': 1, 'Higher education': 2})
    df.drop('Employment status', inplace=True, axis=1)
    # df['Dwelling'].replace({'House / apartment', 'With parents'})
    # df['Dwelling'] = df['Dwelling'].astype('category')
    df['Dwelling'] = df['Dwelling'].replace({'House / apartment': 1, 'With parents': 0})

    # for col in ['Income', 'Age', 'Employment length']:
    #     df[col] = df[col].apply(lambda x: math.log(abs(x)))
    
    return df