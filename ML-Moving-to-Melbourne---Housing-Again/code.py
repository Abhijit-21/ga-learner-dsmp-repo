# --------------
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# path- variable storing file path
df = pd.read_csv(path)
print(df.head(5))

# split the data into train and test data
X = df.drop(axis=1,columns='Price')
y = df['Price']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=6)

# calculating correlation between featurs of the variable
corr = X_train.corr()
print('the correlation between the features of the trainning data is :',corr)
#Code starts here


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Code starts here

# Instantiate a linear regression model
regressor = LinearRegression()

# fit the model on the trainning data
regressor.fit(X_train,y_train)
y_pred = regressor.predict(X_test)

# check the model performance using r^2 score
r2 = r2_score(y_test,y_pred)
print('r2_score = ',round(r2,2))


# --------------
from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score

# Code starts here
lasso = Lasso()
lasso.fit(X_train,y_train)
lasso_pred = lasso.predict(X_test)
r2_lasso = r2_score(y_test,lasso_pred)
print('r2_score = ',round(r2_lasso,2))


# --------------
from sklearn.linear_model import Ridge

# Code starts here
ridge = Ridge()
ridge.fit(X_train,y_train)
ridge_pred = ridge.predict(X_test)
r2_ridge = r2_score(y_test,ridge_pred)
print('r2_score = ',round(r2_ridge,2))


# Code ends here


# --------------
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

#Code starts here
regressor = LinearRegression()
regressor.fit(X_test,y_test)
score = cross_val_score(regressor,X_train,y_train,cv=10)
mean_score = np.mean(score)
print(mean_score)


# --------------
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression

#Code starts here

poly = PolynomialFeatures(2)
model = LinearRegression()
model = make_pipeline(poly,model)
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
r2_poly = r2_score(y_test,y_pred)
print(round(r2_poly,2))



