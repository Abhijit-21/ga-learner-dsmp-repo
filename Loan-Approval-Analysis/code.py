# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 



bank=pd.read_csv(path)
print(bank)



# code starts here

categorical_var=bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var=bank.select_dtypes(include = 'number')
print(numerical_var)

# code ends here


# --------------
# code starts here
import numpy as np
import pandas as pd

# from dataframe drop the 'Loan_ID'
banks=bank.drop('Loan_ID',1)

# Null Values in DF
banks.isnull().sum()

# Calculating the mode for the df
col = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
       'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area', 'Loan_Status']
for i in col:
    bank_mode = banks[i].mode()
    banks[i] = banks[i].fillna(banks[i].mode().iloc[0])

# Null Values in DF
banks.isnull().sum()

#code ends here


# --------------
# Code starts here

# generating the pivot table
avg_loan_amount=pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount',aggfunc=np.mean)
print(avg_loan_amount)

# code ends here



# --------------
# code starts here
Loan_Status = 614

loan_approved_se = (banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')
true_count1 = loan_approved_se.sum()
print(true_count1)

loan_approved_nse = (banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')
true_count2 = loan_approved_nse.sum()
print(true_count2)

# calculating the percentage of loan approval for self-employed
percentage_se =  (true_count1 / Loan_Status)*100
print('percentage of loan approval for self-employed = ',percentage_se)
percentage_nse =  (true_count2 / Loan_Status)*100
print('percentage of loan approval for not self-employed = ',percentage_nse)

# code ends here


# --------------
# code starts here

# convert loan amount term in year
loan_term = banks['Loan_Amount_Term'].apply(lambda x : int(x)/12)
print(loan_term)

# applicant having loan amount term is greeter than
big_loan_term = loan_term[loan_term >= 25].count()
print(big_loan_term)
   



# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')

loan_groupby = loan_groupby['ApplicantIncome','Credit_History']

mean_values = loan_groupby.mean()

# code ends here


