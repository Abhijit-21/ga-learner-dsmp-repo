# --------------
#Importing header files

import pandas as pd
from sklearn.model_selection import train_test_split

# Code starts here
# loading the data set
data =  pd.read_csv(path)

#split X and Y into trainning and testing data set
X = data.drop(axis=1,columns=['customer.id','paid.back.loan'])
y = data['paid.back.loan']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = 0)

# Code ends here


# --------------
#Importing header files
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here

fully_paid  = y_train.value_counts()
print(fully_paid)

#plotting the graph to look at the distribution of 'paid.back.loan'

plt.plot(fully_paid)
plt.xlabel('count of paid back loans')
plt.ylabel('frequency')
plt.legend()
plt.title('value counts of paid back loan')
plt.show()


# Code ends here


# --------------
#Importing header files
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pandas as pd


# Code starts here

# convert the int.rate into float
X_train['int.rate'] = X_train['int.rate'].str[:-1].astype(float)
X_train['int.rate'] = X_train['int.rate']/100


X_test['int.rate'] = X_test['int.rate'].str[:-1].astype(float)
X_test['int.rate'] = X_test['int.rate']/100


num_df = X_train.select_dtypes('number')
print(num_df)

cat_df = X_train.select_dtypes(exclude = 'number')
print(cat_df)

# Code ends here


# --------------
#Importing header files
import seaborn as sns
import matplotlib.pyplot as plt


# Code starts here
cols = list(num_df.columns)
n = len(cols)

fig,axes = plt.subplots(nrows=9,ncols=1)

for i in range(n):
    X = y_train
    y = num_df[cols[i]]
    ax = axes[i]
    sns.boxplot(X,y)
    plt.show()

# Code ends here


# --------------
import seaborn as sns
import matplotlib.pyplot as plt

#Categorical Features Visualisation

#Code starts here
cols = list(cat_df.columns)
n = len(cols)
print(n)
#Plot and see the relation of categorical features with the target variable
fig,axes = plt.subplots(nrows=2,ncols=2)

for i in range(0,2):
    for j in range(0,2):
        sns.countplot(x=X_train[cols[i*2+j]], hue=y_train,ax=axes[i,j])
        plt.show()
        
        





# Code ends here


# --------------
#Importing header files
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Code starts here
cols = cat_df.columns

for i in cols:

    # Fill the X_train null values with NA
    X_train[i].fillna('NA')

    # Initialize label encoder object
    le = LabelEncoder()

    # Transform to labels for X_train
    X_train[i] = le.fit_transform(X_train[i])

for i in cols:

    # Fill the X_test null values with NA
    X_test[i].fillna('NA')

    # Initialize label encoder object
    le1 = LabelEncoder()

    # Transform to labels for X_test
    X_test[i] = le1.fit_transform(X_test[i])
    
y_train = pd.Series(np.where(y_train.values == 'Yes', 1, 0), y_train.index)
y_test = pd.Series(np.where(y_test.values == 'Yes', 1, 0), y_test.index)

# Initialize the model
model = DecisionTreeClassifier(random_state = 0)

# Fit the model
model.fit(X_train,y_train)

# scoring the model
acc = model.score(X_test,y_test)
print('Accuracy score of model : ',acc)

# Code ends here


# --------------
#Importing header files
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

#Parameter grid
parameter_grid = {'max_depth': np.arange(3,10), 'min_samples_leaf': range(10,50,10)}

# Code starts here
model_2 = DecisionTreeClassifier(random_state=0)

p_tree = GridSearchCV(estimator=model_2,param_grid=parameter_grid,cv=5)

p_tree.fit(X_train,y_train)

acc_2 = p_tree.score(X_test,y_test)
print('Accuracy score of model : ',acc_2)

# Code ends here


# --------------
#Importing header files

from io import StringIO
from sklearn.tree import export_graphviz
from sklearn import tree
from sklearn import metrics
from IPython.display import Image
import pydotplus

# Code starts here
dot_data = export_graphviz(decision_tree=p_tree.best_estimator_, out_file=None, feature_names=None, filled = True,class_names=['loan_paid_back_yes','loan_paid_back_no'])

graph_big = pydotplus.graph_from_dot_data(dot_data)

# show graph - do not delete/modify the code below this line
img_path = user_data_dir+'/file.png'
graph_big.write_png(img_path)

plt.figure(figsize=(20,15))
plt.imshow(plt.imread(img_path))
plt.axis('off')
plt.show() 

# Code ends here


