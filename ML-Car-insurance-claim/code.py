# --------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Code starts here
# Load the dataset
df = pd.read_csv(path)
print(df.head(5))
print(df.info)

# Remove the $ and , from columns
cols = ['INCOME','HOME_VAL','BLUEBOOK','OLDCLAIM','CLM_AMT']
for i in cols:
    df[i] = df[i].str.replace('$','')
    df[i] = df[i].str.replace(',','')

# Spli the data 
X = df.drop('CLAIM_FLAG',1)
y = df['CLAIM_FLAG']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = 6)

# Calculating count for target feature
count = y.value_counts()
# Code ends here


# --------------
# Code starts here
# Apply the fir loop for type conversion
columns = ['INCOME','HOME_VAL','BLUEBOOK','OLDCLAIM','CLM_AMT']
for col in columns:
    X_train[col]=X_train[[col]].astype(float)
    X_test[col]=X_test[[col]].astype(float)

# Check the null value for X_train
X_train.isnull()

# Check the null value for X_test
X_test.isnull()

# Code ends here


# --------------
from sklearn.preprocessing import Imputer

# Code starts here

# Drop the rows from 'YOJ','OCCUPATION' column
X_train.dropna(subset=['YOJ','OCCUPATION'],inplace=True)
X_test.dropna(subset=['YOJ','OCCUPATION'],inplace=True)
print(X_train.shape)

# Update the index
y_train = y_train[X_train.index]
y_test = y_test[X_test.index]

# Filling the missing values with mean with 
col1 = ['AGE','CAR_AGE','INCOME','HOME_VAL']
for i in col1:
    X_train[i].fillna(X_train[i].mean(),inplace=True)
    X_test[i].fillna(X_test[i].mean(),inplace=True)
print(X_train.shape)
# Code ends here


# --------------
from sklearn.preprocessing import LabelEncoder
columns = ["PARENT1","MSTATUS","GENDER","EDUCATION","OCCUPATION","CAR_USE","CAR_TYPE","RED_CAR","REVOKED"]

# Code starts here
for i in columns:

    le = LabelEncoder()
    X_train[i]=le.fit_transform(X_train[i])
    X_test[i]=le.fit_transform(X_test[i])
    x_train = pd.get_dummies(X_train[i].astype('category'))
    x_test = pd.get_dummies(X_test[i].astype('category'))
# Code ends here



# --------------
from sklearn.metrics import precision_score 
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

# code starts here

# Initialise the model
model = LogisticRegression(random_state = 6) 

# Fit the model
model.fit(X_train,y_train)

# Make Prediction
y_pred = model.predict(X_test)

# Calculating the accuracy
score = accuracy_score(y_test,y_pred)
print('Accuracy score of the model : ',score)



# Code ends here


# --------------
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

# code starts here
smote = SMOTE(random_state = 9)
X_train,y_train = smote.fit_sample(X_train,y_train)

# Initialise the standard scalar
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)


# Code ends here


# --------------
# Code Starts here

# Initialise the model
model =  LogisticRegression()

#Fit the model
model.fit(X_train,y_train)

# Prediction on test
y_pred = model.predict(X_test)

# Calculating the score
score = accuracy_score(y_test,y_pred)
print('Accuarcy of model after using SMOTE : ',score)

# Code ends here


