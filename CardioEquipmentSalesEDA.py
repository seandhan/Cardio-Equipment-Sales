#!/usr/bin/env python
# coding: utf-8

# <span style = "font-family: Arial; font-weight:bold;font-size:2.5em;color:blue;">Cardio Equipment Sales EDA

# ![fitness_store.png](attachment:fitness_store.png)

# <span style = "font-family: Arial; font-weight:bold;font-size:2.2em;color:black;"> Introduction

# CardioGood is a leading treadmill manufacturer that offers a range of models to meet varying customer needs. This sales dataset provides insights into CardioGood's customers across three treadmill products - the TM195, TM498 and TM798. It includes customer demographics like age, gender, education level and marital status. Usage information covers the average expected weekly usage frequency and mileage. Customers also provide a self-assessed fitness score.
# 
# The key variables in the data relate to customer demographics and treadmill usage. Demographic data covers each customer's age, gender, education level and marital status. Usage variables indicate how often the customer expects to use the treadmill each week and estimated weekly mileage.Analyzing trends and patterns in this sales data can help CardioGood better understand their customers. Identifying relationships between customer characteristics and product selections can inform marketing strategies. Customer usage and mileage statistics can aid product development. Segmenting customers into groups can enable more targeted sales and promotional campaigns.

# <a id="Objectives"></a>
# <span style = "font-family: Arial; font-weight:bold;font-size:2.2em;color:black;"> Objectives

# 1. <a href="#Question1">How do customer demographics (age, gender, education, marital status) compare across purchasers of the 3 treadmill models?</a>
# 2. <a href="#Question2">Is there a relationship between customer income level and the treadmill model purchased?</a>
# 3. <a href="#Question3">Do trends emerge in the expected usage frequencies and weekly mileage across the 3 product models?</a>

# ---

# # Importing Libraries

# In[1]:


# Basic packages
from scipy.stats import chi2_contingency
import copy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as spy
from scipy import stats
import math
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Suppress warnings
import warnings
warnings.filterwarnings('ignore')


# ---

# # Data ingestion 

# In[3]:


# Load dataset
data = pd.read_csv('CardioEqptSales.csv')


# # Data Inspection

# ## Preview dataset

# In[4]:


# Preview the dataset
# View the first 5, last 5 and random 10 rows
print('First five rows', '--'*55)
display(data.head())

print('Last five rows', '--'*55)
display(data.tail())

print('Random ten rows', '--'*55)
np.random.seed(1)
display(data.sample(n=10))


# **Initial observations**
# * `Product`, `Gender` & `MaritalStatus` are categorical variables.
# * `Age`, `Education`, `Usage`, `Fitness` & `Miles` are numerical variables.

# ---

# ## Variable List

# In[5]:


# Display list of variables in dataset
variable_list = data.columns.tolist()
print(variable_list)


# ---

# ## Dataset shape

# In[6]:


shape = data.shape
n_rows = shape[0]
n_cols = shape[1]
print(f"The Dataframe consists of '{n_rows}' rows and '{n_cols}' columns")


# ---

# ## Data info

# In[7]:


# Get info of the dataframe columns
data.info()


# **Observations**
# * All columns have values as there are `180` rows and each column has `180 non-null` elements
# * `Product`, `Gender` & `MaritalStatus` have the **object** datatype. They should be categorical values.
# * `Usage` & `Fitness` are numerical ordinal variables

# ---

# **Panda Object Variable states**

# In[8]:


# Panda Object Variable states function

def pandas_object_states(data):
    """
    This function checks if the variable type is pandas Object and
    displays the states and counts of each
    """
    # Loop through all variables
    for var in data.columns:
        # Check for pandas Object type
        if data[var].dtypes == "object":
            print('Unique values in', var, 'are :')
            print(data[var].value_counts().sort_index())
            print('--'*55)


# In[9]:


# Check the states of all pandas Object variables
pandas_object_states(data)


# ---

# **Convert Pandas Objects to Category type**

# In[10]:


# Convert variables with "object" type to "category" type
for i in data.columns:
    if data[i].dtypes == "object":
        data[i] = data[i].astype("category") 

# Confirm if there no variables with "object" type
data.info()


# **Missing value summary function**

# In[11]:


def missing_val_chk(data):
    """
    This function to checks for missing values 
    and generates a summary.
    """
    if data.isnull().sum().any() == True:
        # Number of missing in each column
        missing_vals = pd.DataFrame(data.isnull().sum().sort_values(
            ascending=False)).rename(columns={0: '# missing'})

        # Create a percentage missing
        missing_vals['percent'] = ((missing_vals['# missing'] / len(data)) *
                                   100).round(decimals=3)

        # Remove rows with 0
        missing_vals = missing_vals[missing_vals['# missing'] != 0].dropna()

        # display missing value dataframe
        print("The missing values summary")
        display(missing_vals)
    else:
        print("There are NO missing values in the dataset")


# **Missing Values Check**

# In[12]:


#Applying the missing value summary function
missing_val_chk(data)


# ---

# **Duplicate row check function**

# In[13]:


def df_duplicate_removal(data):
    """
    This function checks if there are any duplicated rows in the dataframe.
    If any, it displays the rows, keep the first occurence and drops the 
    duplicates.

    The new dataframe shape is calculated and returned
    """
    # Check if duplicated rows exist
    if any(data.duplicated() == True):
        print("The following is/are the duplicated row(s) in the dataframe")
        # Displays the duplicated row(s)
        display(data[data.duplicated() == True])
        # Drops the duplicates inplace while keeping the first occurence
        data.drop_duplicates(keep="first", inplace=True)

        # Check and returns the shape of the new dataframe
        new_df_shape = data.shape
        n_rows = new_df_shape[0]
        n_cols = new_df_shape[1]
        print(
            f"The new dataframe  consists of '{n_rows}' rows and '{n_cols}' columns")
    else:
        print("There is/are no duplicated row(s) in the dataframe")


# In[14]:


df_duplicate_removal(data)


# ---

# ## 5 Point Summary

# **Numerical type Summary**

# In[15]:


# Five point summary of all numerical type variables in the dataset
data.describe().T


# **Categorical type Summary**

# In[16]:


data.describe(include=['category']).T


# **Observations**
# * `Product` has **3** unique categories.  
#     * `TM195` has the highest frequency in the `Product` column.  
#     
#     
# * `Gender` has **2** unique categories.  
#     * `Male` has the highest frequency in the `Gender` column.  
#     
#     
# * `MaritalStatus` has **2** unique categories.  
#     * `Partnered` has the highest frequency in the `MaritalStatus` column.  

# ---

# **Create independent sub-lists to separate Numerical and Categorical variables for EDA**

# In[17]:


# Select numeric variables
numeric_columns = data.select_dtypes(include=['int', 'float']).columns.tolist()
# Select categorical variables
categorical_columns = data.select_dtypes(include=['category']).columns.tolist()


# ---

# ## Numerical data

# **Skew Summary**

# In[18]:


# Display the skew summary for the numerical variables
for var in data[numeric_columns].columns:
    var_skew = data[var].skew()
    if var_skew > 1:
        print(f"The '{var}' distribution is highly right skewed.\n")
    elif var_skew < -1:
        print(f"The '{var}' distribution is highly left skewed.\n")
    elif (var_skew > 0.5) & (var_skew < 1):
        print(f"The '{var}' distribution is moderately right skewed.\n")
    elif (var_skew < -0.5) & (var_skew > -1):
        print(f"The '{var}' distribution is moderately left skewed.\n")
    else:
        print(f"The '{var}' distribution is fairly symmetrical.\n")


# **Outlier check function**

# In[19]:


# Outlier check
def outlier_count(data):
    """
    This function checks the lower and upper 
    outliers for all numerical variables.

    Outliers are found where data points exists either:
    - Greater than `1.5*IQR` above the 75th percentile
    - Less than `1.5*IQR` below the 25th percentile
    """
    numeric = data.select_dtypes(include=np.number).columns.to_list()
    for i in numeric:
        # Get name of series
        name = data[i].name
        # Calculate the IQR for all values and omit NaNs
        IQR = spy.stats.iqr(data[i], nan_policy="omit")
        # Calculate the boxplot upper fence
        upper_fence = data[i].quantile(0.75) + 1.5 * IQR
        # Calculate the boxplot lower fence
        lower_fence = data[i].quantile(0.25) - 1.5 * IQR
        # Calculate the count of outliers above upper fence
        upper_outliers = data[i][data[i] > upper_fence].count()
        # Calculate the count of outliers below lower fence
        lower_outliers = data[i][data[i] < lower_fence].count()
        # Check if there are no outliers
        if (upper_outliers == 0) & (lower_outliers == 0):
            continue
        print(
            f"The '{name}' distribution has '{lower_outliers}' lower outliers and '{upper_outliers}' upper outliers.\n"
        )


# In[20]:


#Applying the Outlier check function for the sub-dataframe of numerical variables
outlier_count(data[numeric_columns])


# ---

# ## Categorical data

# **Unique states**

# In[21]:


# Display the unique values for all categorical variables
for i in categorical_columns:
    print('Unique values in', i, 'are :')
    print(data[i].value_counts())
    print('--'*55)


# ---

# # Feature Engineering

# The Age and Education variables can be categorized to improve data analysis

# **Categorizing Age**

# In[22]:


# Define the age bins and labels
age_bins = [18, 24, 34, 44, 50]  # Define your age range boundaries
age_labels = ['YoungAdults', 'EarlyAdults', 'Adults', 'SeniorAdults']

# Create a new column with age categories
data['AgeGroup'] = pd.cut(
    data['Age'], bins=age_bins, labels=age_labels, include_lowest=True)


# **Categorizing Education**

# In[23]:


# Define the Education bins and labels
education_bins = [12, 13, 15, 17, float("inf")]  # Define your education years range boundaries
education_labels = ['HighSchool', 'AssocDegree', 'Undergraduate', 'Graduate']

# Create a new column with Education categories
data['EducationLevel'] = pd.cut(
    data['Education'], bins=education_bins, labels=education_labels, include_lowest=True)


# ---

# # Heat Map

# Create sub-dataframe removing binned numerical variables

# In[24]:


data_binned = data.drop(columns=["Age", 'Education'])


# In[25]:


onehot = pd.get_dummies(data_binned,
                        columns=data_binned.select_dtypes(include=['category']).columns.tolist())
oh_corr = onehot.corr()

annot_kws = {"fontsize": 12}

symmetric_matrix = (oh_corr + oh_corr.T) / 2

# Create a mask for the upper half of the matrix
mask = np.triu(np.ones_like(symmetric_matrix), k=1)

plt.figure(figsize=(16, 12))
sns.heatmap(oh_corr, annot=True, fmt=".2f", mask=mask,
            cmap='coolwarm', square=True, annot_kws=annot_kws)
plt.yticks(rotation=0)
plt.show()


# ---

# # Business Questions

# <a id="Question1"></a>
# ## How do customer demographics (age, gender, education, marital status) compare across purchasers of the 3 treadmill models?

# **Treadmill model vs Customer Age**

# In[26]:


# Plot of Treadmill model against customer age

sns.catplot(x='Age',
            y='Product',
            kind="box",
            data=data,
            showmeans=True, 
            meanprops={"markerfacecolor": "red", "markeredgecolor": "red"},
            height=4,
            aspect=2,
            orient='h')
plt.title("Treadmill model across Age")
plt.show()


# **Treadmill model vs Customer Age Group**

# In[27]:


# Plot of treadmill model count against Age Group
sns.set_style("darkgrid")
plt.figure(figsize=(10, 6))
sns.countplot(x="Product", data=data, hue="AgeGroup")
plt.title("Treadmill model across Age Group")
plt.show()


# **One way ANOVA for statistical significance of Customer Age across models**

# In[28]:


# Group your data by 'Product' and select the 'Usage' column
grouped_age_data = [group['Age']
                    for name, group in data.groupby('Product')]

# Perform ANOVA test
f_statistic, p_value = stats.f_oneway(*grouped_age_data)

# Display the results
print("F-statistic:", f_statistic)
print("P-value:", p_value)

# Interpret the results
alpha = 0.05  # Set your significance level
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference in mean age of customers.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference in mean age of customers.")


# ---

# **Treadmill model across Gender**

# In[29]:


# Plot of treadmill model count against gender
sns.set_style("darkgrid")
plt.figure(figsize=(10, 6))
sns.countplot(x="Product", data=data, hue="Gender")
plt.title("Treadmill model across Gender")
plt.show()


# In[30]:


# Group your data by 'Product' and 'Gender' and count occurrences
grouped_gender_data = pd.crosstab(data['Product'], data['Gender'])

# Perform the chi-square test
chi2, p, _, _ = chi2_contingency(grouped_gender_data)

# Display the results
print("Chi-squared statistic:", chi2)
print("P-value:", p)

# Interpret the results
alpha = 0.05  # Set your significance level
if p < alpha:
    print("Reject the null hypothesis. There is a significant relationship between Product and Gender.")
else:
    print("Fail to reject the null hypothesis. There is no significant relationship between Product and Gender.")


# ---

# **Treadmill model vs Customer Education**

# In[31]:


# Plot of Treadmill model against customer education

sns.catplot(x='Education',
            y='Product',
            kind="box",
            data=data,
            showmeans=True,
            meanprops={"markerfacecolor": "red", "markeredgecolor": "red"},
            height=4,
            aspect=2,
            orient='h')
plt.title("Treadmill model across Education")
plt.show()


# **Treadmill model vs Customer Education Level**

# In[32]:


# Plot of treadmill model count against Education Level
sns.set_style("darkgrid")
plt.figure(figsize=(10, 6))
sns.countplot(x="Product", data=data, hue="EducationLevel")
plt.title("Treadmill model across Education Level")
plt.show()


# In[33]:


# Group your data by 'Product' and 'Education' and count occurrences
grouped_education_data = pd.crosstab(data['Product'], data['Education'])

# Perform the chi-square test
chi2, p, _, _ = chi2_contingency(grouped_education_data)

# Display the results
print("Chi-squared statistic:", chi2)
print("P-value:", p)

# Interpret the results
alpha = 0.05  # Set your significance level
if p < alpha:
    print("Reject the null hypothesis. There is a significant relationship between Product and Education.")
else:
    print("Fail to reject the null hypothesis. There is no significant relationship between Product and Education.")


# ---

# **Treadmill model vs Customer Marital Status**

# In[34]:


# Group your data by 'Product' and 'MaritalStatus' and count occurrences
grouped_marital_data = data.groupby(
    by=['Product', 'MaritalStatus']).size().unstack(fill_value=0)

# Determine the number of rows and columns for your subplot grid
num_rows = 1  # You can change this as needed
num_cols = len(grouped_marital_data.index)

# Create a figure and subplot grid
# Adjust the figure size as needed
fig, axes = plt.subplots(num_rows, num_cols, figsize=(18, 6))

# Increase the font sizes
title_fontsize = 22
label_fontsize = 18

# Create a pie chart for each 'Product' group and place them side by side
for i, (product, counts) in enumerate(grouped_marital_data.iterrows()):
    ax = axes[i]
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%',
           textprops={'fontsize': label_fontsize})
    ax.set_title(
        f'MaritalStatus distribution across {product} ', fontsize=title_fontsize)
    ax.axis('equal')  # Equal aspect ratio ensures that the pie is circular

# Adjust the layout to prevent overlapping titles
plt.tight_layout()

plt.show()


# In[35]:


# Group your data by 'Product' and 'MaritalStatus' and count occurrences
grouped_marital_data = pd.crosstab(data['Product'], data['MaritalStatus'])

# Perform the chi-square test
chi2, p, _, _ = chi2_contingency(grouped_marital_data)

# Display the results
print("Chi-squared statistic:", chi2)
print("P-value:", p)

# Interpret the results
alpha = 0.05  # Set your significance level
if p < alpha:
    print("Reject the null hypothesis. There is a significant relationship between Product and MaritalStatus.")
else:
    print("Fail to reject the null hypothesis. There is no significant relationship between Product and MaritalStatus.")


# ---

# **Observations:**
# 
# CardioGood should take an inclusive approach in marketing that avoids targeting narrow age ranges or lifestyles. Messaging and imagery for all models should appeal to a wide cross-section of adults across generations and relationship statuses. However, the data indicates opportunities to fine-tune brand positioning and partnerships by model based on core customer segments.
# 
# The TM195 treadmill should be promoted toward younger millennial fitness enthusiasts entering the category, highlighting introductory pricing and features. For the premium TM798 model, marketing should focus on performance-driven male runners based on their significant representation in this segment. Tactics like in-gym promotions and running event sponsorships can effectively reach this group. Additionally, TM798 messaging should highlight productivity features and advanced training data to align with educated professionals drawn to this top-tier model. In summary, while taking an inclusive approach, targeted outreach to align with the core demographics of each customer segment can help strengthen treadmill model positioning and marketing effectiveness.

# <a href="#Objectives">Go to Objectives</a>

# ---

# <a id="Question2"></a>
# ## Is there a relationship between customer income level and the treadmill model purchased?

# **Treadmill model vs Customer Income**

# In[36]:


# Plot of Treadmill model against customer income

sns.catplot(x='Income',
            y='Product',
            kind="box",
            data=data,
            showmeans=True,
            meanprops={"markerfacecolor": "red", "markeredgecolor": "red"},
            height=4,
            aspect=2,
            orient='h')
plt.title("Treadmill model across Income")
plt.show()


# **Mean Income across Treadmill models**

# In[37]:


# Mean of Income across Treadmill models
data.groupby(by='Product').Income.mean()


# **One way ANOVA for statistical significance of Customer Income across models**

# In[38]:


# Group your data by 'Product' and select the 'Usage' column
grouped_income_data = [group['Income']
                       for name, group in data.groupby('Product')]

# Perform ANOVA test
f_statistic, p_value = stats.f_oneway(*grouped_income_data)

# Display the results
print("F-statistic:", f_statistic)
print("P-value:", p_value)

# Interpret the results
alpha = 0.05  # Set your significance level
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference in mean customer income.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference in mean customer income.")


# **Observations:**
# 
# This analysis found income level strongly correlates with treadmill model selection. Specifically, the data showed customers with higher incomes overwhelmingly prefer the premium TM798 model.
# 
# To leverage this, CardioGood should make income a key factor in shaping TM798 marketing strategy and targeting. Messaging and partnerships should focus on highlighting the superior quality, performance, and prestige of the TM798. This positions it as an aspirational product for high-income earners. Tactics like digital ads geo-targeted by income levels can help reach affluent professionals identified as top prospects. Additionally, brand sponsorships of luxury events popular with wealthy consumers can further strengthen TM798's premium branding. In summary, showcasing the TM798 as a top-of-the-line model will resonate with high income customers and drive growth in this profitable segment.

# <a href="#Objectives">Go to Objectives</a>

# ---

# <a id="Question3"></a>
# ## Do trends emerge in the expected usage frequencies and weekly mileage across the 3 product models?

# **Usage distribution across treadmill models**

# In[39]:


# Create a list of unique products in your data
Tmodels = data['Product'].unique()

# Determine the number of rows and columns for your subplot grid
num_rows = 1
num_cols = len(Tmodels)

# Create a figure and subplot grid
# Adjust the figure size as needed
fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 4))

# Create a separate plot for each product
for i, product in enumerate(Tmodels):
    data[data['Product'] == product]['Usage'].hist(
        ax=axes[i], bins=10, rwidth=0.9, edgecolor='k')
    axes[i].set_title(f'Histogram for {product}')
    axes[i].set_xlabel('Usage')
    axes[i].set_ylabel('Frequency')
    axes[i].set_xticks(range(1, 8, 1))  # Set integer values as x-axis ticks

# Adjust the layout to prevent overlapping titles
plt.tight_layout()

plt.show()


# **Summary statistics of Usage**

# In[40]:


data.groupby(by='Product')['Usage'].describe()


# **One way ANOVA for statistical significance of Customer Usage across models**

# In[41]:


# Group your data by 'Product' and select the 'Usage' column
grouped_usage_data = [group['Usage'] for name, group in data.groupby('Product')]

# Perform ANOVA test
f_statistic, p_value = stats.f_oneway(*grouped_usage_data)

# Display the results
print("F-statistic:", f_statistic)
print("P-value:", p_value)

# Interpret the results
alpha = 0.05  # Set your significance level
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference in mean usage frequency.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference in mean usage frequency.")


# ---

# **Miles distribution across treadmill models**

# In[42]:


# Create a list of unique products in your data
Tmodels = data['Product'].unique()

# Determine the number of rows and columns for your subplot grid
num_rows = 1
num_cols = len(Tmodels)

# Create a figure and subplot grid
# Adjust the figure size as needed
fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 4))

# Create a separate plot for each product
for i, product in enumerate(Tmodels):
    data[data['Product'] == product]['Miles'].hist(
        ax=axes[i], bins=10, rwidth=0.9, edgecolor='k')
    axes[i].set_title(f'Histogram for {product}')
    axes[i].set_xlabel('Miles')
    axes[i].set_ylabel('Frequency')

# Adjust the layout to prevent overlapping titles
plt.tight_layout()

plt.show()


# **Summary statistics of Miles**

# In[43]:


data.groupby(by='Product')['Miles'].describe()


# **One way ANOVA for statistical significance of Customer Miles across models**

# In[44]:


# Group your data by 'Product' and select the 'Usage' column
grouped_miles_data = [group['Miles'] for name, group in data.groupby('Product')]

# Perform ANOVA test
f_statistic, p_value = stats.f_oneway(*grouped_miles_data)

# Display the results
print("F-statistic:", f_statistic)
print("P-value:", p_value)

# Interpret the results
alpha = 0.05  # Set your significance level
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference in mean miles frequency.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference in mean miles frequency.")


# ---

# **Observations:**
# 
# This analysis uncovered distinct usage profiles associated with each treadmill model. For the entry-level TM195, the majority of customers expected to use the treadmill sparingly, with average weekly usage of just 2-3 times. 25% of TM195 buyers plan to use the treadmill only once per week or less, indicating they purchased this model primarily for light or occasional cardio activity.
# 
# In contrast, customers of the mid-range TM498 model averaged 3-4 uses per week - a moderate increase versus TM195. For top-tier TM798, average weekly usage was highest at 3-5 times. The TM798 attracts committed runners looking to use their home treadmill consistently to train throughout the week.
# 
# Similar trends were seen for expected mileage. Average miles per week for TM195 customers peaked at 20-30. TM498 buyers saw a moderate uptick in planned mileage to 30-40 weekly miles. For TM798, average miles jumped substantially to 50+ miles per week, with some customers expecting to log over 100 miles.
# 
# These insights paint a picture of three distinct user profiles attached to each model. The TM195 appeals to casual walkers or light joggers. The TM498 suits users looking for consistency in moderate running. And the TM798 is optimized for enthusiasts training at high mileages.

# ---

# <a href="#Objectives">Go to Objectives</a>

# ---

# ---
