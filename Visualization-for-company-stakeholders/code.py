# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Code start here

data=pd.read_csv(path)
loan_status=data['Loan_Status'].value_counts()
loan_status.plot(kind='bar', stacked=True,figsize=(14,8))
plt.xlabel('Loan approvals' or 'Loan disapprovals')
plt.ylabel('Applications')
plt.title('Loan Status Distribution')
plt.show()


#Code starts here


# --------------
#Code starts here

property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()


#ploting an unstacked bar plot of property_and_loan

property_and_loan.plot(kind='bar',stacked=False,figsize=(14,8))
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.title('Loan Status Distribution')
plt.show()

#Code end here


# --------------
#Code starts here

education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True,figsize=(14,8))
plt.xlabel('Education Status')
plt.ylabel('Applications')
plt.title('Loan Status')
plt.xticks(rotation=45)
plt.show()

#Code end here


# --------------
#Code starts here

#creating dataframe for graduate 
graduate = data[data['Education']=='Graduate']

#creating dataframe for non_graduate
not_graduate = data[data['Education']=='Not Graduate']

#ploting density graph LoanAmount of 'graduate'
graduate.plot(kind='density',label='Graduate')

#ploting density graph LoanAmount of 'not_graduate'
not_graduate.plot(kind='density',label='Not Graduate')

#For automatic legend display
plt.legend()








#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig,(ax_1,ax_2,ax_3)=plt.subplots(3,1,figsize=[14,8])

plt.scatter(data['ApplicantIncome'], data['LoanAmount'])
ax_1.set_title('Applicant Income')

plt.scatter(data['CoapplicantIncome'], data['LoanAmount'])
ax_2.set_title('Coapplicant Income')

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
plt.scatter(data['TotalIncome'], data['LoanAmount'])
ax_3.set_title('Total Income')


