import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.DataFrame({"X": [1,2,3,4,5], "y": [1,4,9,16,25]});
print(df);

model = LinearRegression();

yhat = model.fit(df[['X']], df['y']);

print(yhat.coef_);
print(yhat.intercept_);

ypred = model.predict(df[['X']]);

# print(ypred);

print(mean_squared_error(df['y'], ypred));