from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_squared_error

X = np.array([[1,2,3,4],[2,3,5,6]])
#representing feature as row
print(f"Training data {X}")
X = X.T
#represening features as col
print(f"Training data {X}")

y = np.array([30,40,55,60]) 

model = LinearRegression()

model.fit(X,y) #learn realtionship between x and y , finding best values for w and b

print(f"W {model.coef_}")
print(f"b {model.intercept_}")
y_pred = model.predict(np.array(X))

mse = mean_squared_error(y,y_pred)
print(mse) #convergence



