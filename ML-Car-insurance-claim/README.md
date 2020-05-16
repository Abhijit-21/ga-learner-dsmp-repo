### Project Overview

 As we are working in the insurance company. Company wants to know the reason why claim was not made. Doing so would allow insurance company to improve there policy for giving loan to the customer. In this project you are dealing with various feature such as age, occupation etc. based on that let's get back to the final conculsion.

About the Dataset : The Data folder contains the dataset with details of 10302 Insurance claim and the 25 features.


### Learnings from the project

 This is imbalanced dataset . Here 0 - Claim was not made, 1 - Claim made. After completing this project, you will have the better understanding of how to build deal with imbalanced dataset. In this project, you will apply the following concepts.

- Train-test split
- Standard scaler
- Logistic Regression
- SMOTE
- feature scaling


### Challenges faced

 We load the data set and found $ and , symbols present in some column data , so remove them from data set.As we can see that because of the $ symbol most of the features are consider as object type. All the values are numeric so we need to convert it into numeric type. So we are going to change the type of the object features to floating type. Also checked there is any null values in the X_train and X_test.We have some column which is textual in nature but any prediction model only work well in the numerical data so we need to convert that features into the numerical format using label encoding.
After applying  logistic regression model we got the accuracy of 74%.One might think that it is a good score but even if the model always predicts 0, you will still get 74% accuracy(The target value distribution is 74% 0s and 26% 1s).So if you applied model on this dataset it will give us a bad prediction. To overcome we need to use the technic Oversampling or Undersampling technic. Oversampling in data analysis is techniques used to adjust the class distribution of an imbalanced dataset. In this task, you are going to apply the SMOTE to adjust the class distribution of the data set. While working with the learning model, it is important to scale the features to a range which is centered around zero so that the variance of the features are in the same range. If the feature’s variance is orders of magnitude more than the variance of other features, that particular feature might dominate other features in the dataset and our model will not train well which gives us bad model.


