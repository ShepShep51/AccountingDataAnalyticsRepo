import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



df = pd.read_excel(io='C:\\Users\\Shepard\\Desktop\\Life\\School\\Fall_2020\\ACC575\\Week 3\\Lab_2-5.xlsx')
new_header = df.iloc[0]
df = df[1:]
df.columns =new_header
df = df[['SAT_AVG','RET_FT4']]
df = df.dropna(0,how='any')
X = df.iloc[:, 0].values.reshape(-1, 1)
Y = df.iloc[:, 1].values.reshape(-1, 1)

linear_regressor = LinearRegression()
linear_regressor.fit(X,Y)
Y_pred = linear_regressor.predict(X)
plt.scatter(X,Y)
plt.plot(X,Y_pred, color='red')
plt.xlabel("Average SAT Score")
plt.ylabel("Completion Rate")
plt.show()