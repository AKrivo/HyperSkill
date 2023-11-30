import os
import requests

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error as mape


# checking ../Data directory presence
if not os.path.exists('../Data'):
    os.mkdir('../Data')

# download data if it is unavailable
if 'data.csv' not in os.listdir('../Data'):
    url = "https://www.dropbox.com/s/3cml50uv7zm46ly/data.csv?dl=1"
    r = requests.get(url, allow_redirects=True)
    open('../Data/data.csv', 'wb').write(r.content)

# read data
data = pd.read_csv('../Data/data.csv')

# write your code here
# Stage 1/5

# Assigning the linear regression model
model = LinearRegression()

# Extraction the data from DataFrame (X cannot be a series so shaping it back to frame)
X, y = data['rating'].to_frame(), data['salary']

# Splitting the data to test and train samples
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)

# Training the model
model.fit(X_train, y_train)

# Predictions, on test and training data
Y_predict_train = model.predict(X_train)
Y_predict_test = model.predict(X_test)

# Calculation of the "mean absolute percentage error"
task_mape = mape(y_test, Y_predict_test)

# Extraction of the coefficients and intercept
a_coef = model.coef_
b_coef = model.intercept_

# Visualizing
fig, axes = plt.subplots(figsize=(8, 8))
axes.scatter(data['rating'], data['salary'], s=10,  c='g', label='Core Data')
axes.scatter(X_test, Y_predict_test, c='b', label='Basic linear prediction')
axes.plot(X_test, [a_coef * X_test.iloc[i] + b_coef for i in range(len(X_test))],
          c='m',
          label='Basic linear prediction: function a*x+b')
axes.set_ylabel("Player's salary", fontsize=12)
axes.set_xlabel("Player's rating", fontsize=12)
axes.grid()
# plt.show()

# Stage 2/5

# Transformation of the predictor (in powers: 2, 3, 4)
X_p2 = X**2
X_p3 = X**3
X_p4 = X**4

# Splitting the data to test and train samples
X_train_p2, X_test_p2, y_train_p2, y_test_p2 = train_test_split(X_p2, y, test_size=0.3, random_state=100)
X_train_p3, X_test_p3, y_train_p3, y_test_p3 = train_test_split(X_p3, y, test_size=0.3, random_state=100)
X_train_p4, X_test_p4, y_train_p4, y_test_p4 = train_test_split(X_p4, y, test_size=0.3, random_state=100)

# Training the model
model_p2 = LinearRegression()
model_p3 = LinearRegression()
model_p4 = LinearRegression()
model_p2.fit(X_train_p2, y_train_p2)
model_p3.fit(X_train_p3, y_train_p3)
model_p4.fit(X_train_p4, y_train_p4)

# Predictions:
Y_predict_test_p2 = model_p2.predict(X_test_p2)
Y_predict_test_p3 = model_p3.predict(X_test_p3)
Y_predict_test_p4 = model_p4.predict(X_test_p4)

# Calculation of the "mean absolute percentage error"
mape_p2 = mape(y_test_p2, Y_predict_test_p2)
mape_p3 = mape(y_test_p3, Y_predict_test_p3)
mape_p4 = mape(y_test_p4, Y_predict_test_p4)

# Visualizing
axes.scatter(X_test, Y_predict_test_p2, c='k', label='Quadratic  predictor')
axes.scatter(X_test, Y_predict_test_p3, c='y', label='Cubic  predictor')
axes.scatter(X_test, Y_predict_test_p4, c='c', label='Quartic  predictor')
axes.legend()
plt.show()

print(mape_p3.round(5))