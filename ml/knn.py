import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing

df = pd.read_csv("./wine-red.csv")

X = np.asarray(df.iloc[:, :-1])

y = np.asarray(df["quality"])

X = preprocessing.StandardScaler().fit(X).transform(X)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=.2)

knn = KNeighborsClassifier(n_neighbors=8)

knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)

print(f"Mean squared error: {mean_squared_error(y_test, y_pred)}")