import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, mean_absolute_error, mean_squared_error

df = pd.read_csv('./student_scores.csv')
df.describe()

df.plot(x='Hours', y='Scores', style='o')
plt.show()

x = df.iloc[ :, :-1].values
y = df.iloc[:, :-1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(y_test)

print(f"Intercept: {regressor.intercept_}")
print(f"Coefficient: {regressor.coef_}")

print(f"\nMean absolute error: {mean_absolute_error(y_test, y_pred)}")
print(f"\nMean squared error: {mean_squared_error(y_test, y_pred)}")

# print(type(x_test[0]))
# print(type(x_test[0][0]))
import numpy as np

hour = input("Enter hour: ")
hour = np.float64(hour)
hour = np.asarray(hour)
hour = hour.reshape(1, -1)
pred_score = regressor.predict(hour)
print(f"Predicted score: {pred_score}")