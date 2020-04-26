# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
# Load te data set
df=pd.read_csv(path)

# Calculating the probability for the event fio credit score is greeter than 700
p_a = len(df[df['fico']>700])/len(df)
print('Probability of P(A) =',p_a)

# Calculating the probability for the event porpose
p_b = len(df[df['purpose']=='debt_consolidation'])/len(df)
print('Probability of P(B) =',p_b)

# creating new daraframe df1
df1 = df[df['purpose']=='debt_consolidation']

# caluclating the probability for both events 
p_a_b = p_b/p_a

# cheking the independency
result = p_a_b==p_a
print('The indepedency result answer is :',result)

# code ends here



# --------------
# code starts here

# Calculating the probability for event paid.back.loan
prob_lp = len(df[df['paid.back.loan']=='Yes'])/len(df)
print('Probability of P(A) =',prob_lp)

# Calculating the probability for event credit.policy
prob_cs = len(df[df['credit.policy']=='Yes'])/len(df)
print('Probability of P(B) =',prob_cs)

# create new df with condition ['paid.back.loan'] == 'Yes'
new_df = df[df['paid.back.loan'] == 'Yes']

A_n_B = new_df[new_df['credit.policy'] == 'Yes']
prob_pd_n_cs = len(A_n_B) / len(df)

# Calculating the probability P(B/A)
prob_pd_cs = prob_pd_n_cs / prob_lp

# Calculate the conditional probability
bayes = (prob_pd_cs*prob_lp)/prob_cs
print(bayes)


# code ends here


# --------------
# code starts here
import seaborn as sns
df1 = df[df['paid.back.loan'] == 'No']
plt.figure(figsize=[10,7]) 
plt.xticks(rotation=45) 
sns.countplot(df1['purpose']) 
plt.show() 

# code ends here


# --------------
# code starts here
# Calculating median and mean for installment
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()

# Distribution of monthly installments of the borrowers 
plt.figure(figsize=[10,7]) 
df['installment'].plot.hist() 
plt.title('Average monthly installments of the borrowers') 
plt.xlabel('Monthly installments') 
plt.show() 
 
 
# Annual income distribution of the borrowers 
plt.figure(figsize=[10,7]) 
df['log.annual.inc'].plot.hist() 
plt.title('Average annual income of the borrowers') 
plt.xlabel('Annual Income(Lpa)') 
plt.show() 


# code ends here


