# -*- coding: utf-8 -*-
"""Copy of Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10iwhKZN797VpZcc3ff3E0GCiPdbi21z3
"""



"""# **Samuel Maina Gachuru**

# **Automobile Accident Severity Prediction according to weather condition.**

## Getting started.
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler  # Corrected class name
from sklearn.model_selection import train_test_split
import tensorflow as tf

df = pd.read_csv('https://raw.githubusercontent.com/mishrasarthak/Accident-Casualty-Prediction-System/refs/heads/master/Accident_Dataset_prepared.csv')

df

"""## **Data seperation into x and y**"""

y = df['Weather Conditions']
y

x = df.drop(['Weather Conditions', 'Number of Vehicles', 'Road Surface', 'Lighting Conditions', 'Casualty Victim', 'Sex of Casualty', 'Age of Casualty', 'Type of Vehicle', 'Number of Vehicles'], axis=1)

x

"""### **Data spliting into training and testing**"""

from sklearn.model_selection import train_test_split

x_train, x_test,y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=100)

x_test

x_train

"""## **Model Building**

### **Linear Regression**
"""

from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100)

model = LinearRegression()

"""**Training The model**"""

model.fit(X_train, y_train)

y_lr_test_pred = model.predict(X_test)


lr_test_mse = mean_squared_error(y_test, y_lr_test_pred)
lr_test_r2 = r2_score(y_test, y_lr_test_pred)

"""### **Applying the model to make prediction**"""

from sklearn.metrics import mean_squared_error, r2_score

"""### **Evaluating The model performance**"""

print(f"Test Mean Squared Error: {lr_test_mse}")
print(f"Test R-squared: {lr_test_r2}")

lr_results = pd.DataFrame(['Linear Regression', lr_test_mse,lr_test_r2]).transpose()
lr_results.columns = ['method','TEST MSE','TEST R2']
lr_results

"""## **Data visualization**

Weather condition

# Values                  Weather
   1.           Fine without high winds.
   2.           Raining without high winds
   4.           Raining with high winds.
   3.           snowing without high win 5.            other

Casualty severelity


value   C.severelity
 1.        slight
 2.        sereous

# **END**
"""

