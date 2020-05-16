# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#path of the data file- path
# Load the data set
data = pd.read_csv(path)
print(data.head(5))

# Replace '-' with 'Agender' for Gender column
data['Gender'].replace('-','Agender',inplace=True)
print('Data set after replacement ',data.head(5))
gender_count = data['Gender'].value_counts()
print('gender_count: ' ,gender_count)
plt.plot(kind='barh')
plt.show()

#Code starts here 




# --------------
#Code starts here

alignment = data['Alignment'].value_counts()
alignment.plot(kind='pie', subplots=True)
plt.title('Character Alignment')
plt.show()


# --------------
#Code starts here

# craete the subset of data
sc_df = data[['Strength','Combat']]

# Covariance between Strength and Combat
sc_covariance = sc_df.cov().iloc[0,1]

# Standard Deviation
sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()

# Pearson's Correlation between Strength and Combat
sc_pearson = (sc_covariance) / (sc_strength * sc_combat)
print("Pearson's Correlation for Strength and Combat :", sc_pearson)

# Subsetting Intelligence and Combat points from data
ic_df = data[['Intelligence','Combat']]

# Covariance between Intelligence and Combat
ic_covariance = ic_df.cov().iloc[0,1]

# Standard Deviation
ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()

#  Pearson's Correlation between Intelligence and Combat
ic_pearson = (ic_covariance) / (ic_intelligence * ic_combat)
print("Pearson's Correlation for Intelligence and Combat :", ic_pearson)



# --------------
#Code starts here

# Calculate the value of quantile=0.99 for the column Total
total_high =  data['Total'].quantile(0.99)

# Subsetting the data quantile
super_best = data[data['Total']>total_high]

# Listing the names of the superheroes
super_best_names = list(super_best['Name'])
print('Best superheroes in the superhero universe :\n', super_best_names)  

# Code end here


# --------------
#Code starts here
# Subplotting
fig, (ax_1,ax_2,ax_3) = plt.subplots(nrows=1,ncols=3,figsize=[20,8])

# Boxplot for Intelligence
ax_1.boxplot(data['Intelligence'])
ax_1.set_title('Intelligence')

# Boxplot for Speed
ax_2.boxplot(data['Speed'])
ax_2.set_title('Speed')

# Boxplot for Power
ax_3.boxplot(data['Power'])
ax_3.set_title('Power')

plt.show()

# Code end here


