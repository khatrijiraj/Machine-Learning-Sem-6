# -*- coding: utf-8 -*-
"""ML lab 3 linear regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hJQdsWhd741lktQgCNsTGXmCn4dHUk7C

# Q3)(a) Implement Simple Linear Regression Model on a Dataset
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""# Linear Regression"""

df = pd.read_excel('/content/linear reg.xlsx')
df

dep= df.iloc[:,-1].values #dependent
dep

inp= df.iloc[:,:-1].values #indepent
inp

"""## Checking Nan values"""

df.isna().sum() #no null values

"""##Splitting"""

from sklearn.model_selection import train_test_split
inp_train, inp_test, dep_train, dep_test = train_test_split(inp, dep, test_size = 0.2, random_state = 1)

dep_train

dep_test

inp_train

inp_test

"""##Training"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(inp_train, dep_train)

dep_pred = regressor.predict(inp_test)
dep_pred

"""## train visualise"""

plt.scatter(inp_train, dep_train, color = 'red')
dep_tpred = regressor.predict(inp_train)
plt.plot(inp_train, dep_tpred, color = 'blue')

plt.xlabel("Age")
plt.ylabel("price")

plt.show()

"""## Visualise test"""

plt.scatter(inp_test, dep_test, color = 'red')

plt.plot(inp_test, dep_pred, color = 'blue')

plt.xlabel("Age")
plt.ylabel("Price")

plt.show()

"""## Prediction"""

regressor.predict([[32]])

"""## Coefficient and intercept"""

print(regressor.coef_)
print(regressor.intercept_)