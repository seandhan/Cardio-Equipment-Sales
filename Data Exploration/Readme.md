# Importing Libraries


```python
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
%matplotlib inline
```


```python
# Suppress warnings
import warnings
warnings.filterwarnings('ignore')
```

---

# Data ingestion 


```python
# Load dataset
data = pd.read_csv('CardioEqptSales.csv')
```

# Data Inspection

## Preview dataset


```python
# Preview the dataset
# View the first 5, last 5 and random 10 rows
print('First five rows', '--'*55)
display(data.head())

print('Last five rows', '--'*55)
display(data.tail())

print('Random ten rows', '--'*55)
np.random.seed(1)
display(data.sample(n=10))
```

    First five rows --------------------------------------------------------------------------------------------------------------
    


<div>

*Output:*


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Product</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Education</th>
      <th>MaritalStatus</th>
      <th>Usage</th>
      <th>Fitness</th>
      <th>Income</th>
      <th>Miles</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>TM195</td>
      <td>18</td>
      <td>Male</td>
      <td>14</td>
      <td>Single</td>
      <td>3</td>
      <td>4</td>
      <td>29562</td>
      <td>112</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TM195</td>
      <td>19</td>
      <td>Male</td>
      <td>15</td>
      <td>Single</td>
      <td>2</td>
      <td>3</td>
      <td>31836</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2</th>
      <td>TM195</td>
      <td>19</td>
      <td>Female</td>
      <td>14</td>
      <td>Partnered</td>
      <td>4</td>
      <td>3</td>
      <td>30699</td>
      <td>66</td>
    </tr>
    <tr>
      <th>3</th>
      <td>TM195</td>
      <td>19</td>
      <td>Male</td>
      <td>12</td>
      <td>Single</td>
      <td>3</td>
      <td>3</td>
      <td>32973</td>
      <td>85</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TM195</td>
      <td>20</td>
      <td>Male</td>
      <td>13</td>
      <td>Partnered</td>
      <td>4</td>
      <td>2</td>
      <td>35247</td>
      <td>47</td>
    </tr>
  </tbody>
</table>
</div>


    Last five rows --------------------------------------------------------------------------------------------------------------
    


<div>

*Output:*


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Product</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Education</th>
      <th>MaritalStatus</th>
      <th>Usage</th>
      <th>Fitness</th>
      <th>Income</th>
      <th>Miles</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>175</th>
      <td>TM798</td>
      <td>40</td>
      <td>Male</td>
      <td>21</td>
      <td>Single</td>
      <td>6</td>
      <td>5</td>
      <td>83416</td>
      <td>200</td>
    </tr>
    <tr>
      <th>176</th>
      <td>TM798</td>
      <td>42</td>
      <td>Male</td>
      <td>18</td>
      <td>Single</td>
      <td>5</td>
      <td>4</td>
      <td>89641</td>
      <td>200</td>
    </tr>
    <tr>
      <th>177</th>
      <td>TM798</td>
      <td>45</td>
      <td>Male</td>
      <td>16</td>
      <td>Single</td>
      <td>5</td>
      <td>5</td>
      <td>90886</td>
      <td>160</td>
    </tr>
    <tr>
      <th>178</th>
      <td>TM798</td>
      <td>47</td>
      <td>Male</td>
      <td>18</td>
      <td>Partnered</td>
      <td>4</td>
      <td>5</td>
      <td>104581</td>
      <td>120</td>
    </tr>
    <tr>
      <th>179</th>
      <td>TM798</td>
      <td>48</td>
      <td>Male</td>
      <td>18</td>
      <td>Partnered</td>
      <td>4</td>
      <td>5</td>
      <td>95508</td>
      <td>180</td>
    </tr>
  </tbody>
</table>
</div>


    Random ten rows --------------------------------------------------------------------------------------------------------------
    


<div>

*Output:*


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Product</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Education</th>
      <th>MaritalStatus</th>
      <th>Usage</th>
      <th>Fitness</th>
      <th>Income</th>
      <th>Miles</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>116</th>
      <td>TM498</td>
      <td>31</td>
      <td>Female</td>
      <td>16</td>
      <td>Partnered</td>
      <td>2</td>
      <td>3</td>
      <td>51165</td>
      <td>64</td>
    </tr>
    <tr>
      <th>112</th>
      <td>TM498</td>
      <td>29</td>
      <td>Female</td>
      <td>14</td>
      <td>Partnered</td>
      <td>3</td>
      <td>3</td>
      <td>51165</td>
      <td>95</td>
    </tr>
    <tr>
      <th>99</th>
      <td>TM498</td>
      <td>25</td>
      <td>Male</td>
      <td>16</td>
      <td>Partnered</td>
      <td>2</td>
      <td>2</td>
      <td>52302</td>
      <td>42</td>
    </tr>
    <tr>
      <th>161</th>
      <td>TM798</td>
      <td>27</td>
      <td>Male</td>
      <td>21</td>
      <td>Partnered</td>
      <td>4</td>
      <td>4</td>
      <td>90886</td>
      <td>100</td>
    </tr>
    <tr>
      <th>35</th>
      <td>TM195</td>
      <td>26</td>
      <td>Female</td>
      <td>16</td>
      <td>Partnered</td>
      <td>4</td>
      <td>3</td>
      <td>52302</td>
      <td>113</td>
    </tr>
    <tr>
      <th>54</th>
      <td>TM195</td>
      <td>30</td>
      <td>Male</td>
      <td>14</td>
      <td>Single</td>
      <td>3</td>
      <td>3</td>
      <td>54576</td>
      <td>85</td>
    </tr>
    <tr>
      <th>69</th>
      <td>TM195</td>
      <td>38</td>
      <td>Female</td>
      <td>14</td>
      <td>Partnered</td>
      <td>2</td>
      <td>3</td>
      <td>54576</td>
      <td>56</td>
    </tr>
    <tr>
      <th>19</th>
      <td>TM195</td>
      <td>23</td>
      <td>Female</td>
      <td>15</td>
      <td>Partnered</td>
      <td>2</td>
      <td>2</td>
      <td>34110</td>
      <td>38</td>
    </tr>
    <tr>
      <th>110</th>
      <td>TM498</td>
      <td>26</td>
      <td>Male</td>
      <td>16</td>
      <td>Single</td>
      <td>4</td>
      <td>3</td>
      <td>51165</td>
      <td>106</td>
    </tr>
    <tr>
      <th>127</th>
      <td>TM498</td>
      <td>34</td>
      <td>Male</td>
      <td>15</td>
      <td>Single</td>
      <td>3</td>
      <td>3</td>
      <td>67083</td>
      <td>85</td>
    </tr>
  </tbody>
</table>
</div>


**Initial observations**
* `Product`, `Gender` & `MaritalStatus` are categorical variables.
* `Age`, `Education`, `Usage`, `Fitness` & `Miles` are numerical variables.

---

## Variable List


```python
# Display list of variables in dataset
variable_list = data.columns.tolist()
print(variable_list)
```

    ['Product', 'Age', 'Gender', 'Education', 'MaritalStatus', 'Usage', 'Fitness', 'Income', 'Miles']
    

---

## Dataset shape


```python
shape = data.shape
n_rows = shape[0]
n_cols = shape[1]
print(f"The Dataframe consists of '{n_rows}' rows and '{n_cols}' columns")
```

    The Dataframe consists of '180' rows and '9' columns
    

---

## Data info


```python
# Get info of the dataframe columns
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 180 entries, 0 to 179
    Data columns (total 9 columns):
     #   Column         Non-Null Count  Dtype 
    ---  ------         --------------  ----- 
     0   Product        180 non-null    object
     1   Age            180 non-null    int64 
     2   Gender         180 non-null    object
     3   Education      180 non-null    int64 
     4   MaritalStatus  180 non-null    object
     5   Usage          180 non-null    int64 
     6   Fitness        180 non-null    int64 
     7   Income         180 non-null    int64 
     8   Miles          180 non-null    int64 
    dtypes: int64(6), object(3)
    memory usage: 12.8+ KB
    

**Observations**
* All columns have values as there are `180` rows and each column has `180 non-null` elements
* `Product`, `Gender` & `MaritalStatus` have the **object** datatype. They should be categorical values.
* `Usage` & `Fitness` are numerical ordinal variables

---

**Panda Object Variable states**


```python
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
```


```python
# Check the states of all pandas Object variables
pandas_object_states(data)
```

    Unique values in Product are :
    Product
    TM195    80
    TM498    60
    TM798    40
    Name: count, dtype: int64
    --------------------------------------------------------------------------------------------------------------
    Unique values in Gender are :
    Gender
    Female     76
    Male      104
    Name: count, dtype: int64
    --------------------------------------------------------------------------------------------------------------
    Unique values in MaritalStatus are :
    MaritalStatus
    Partnered    107
    Single        73
    Name: count, dtype: int64
    --------------------------------------------------------------------------------------------------------------
    

---

**Convert Pandas Objects to Category type**


```python
# Convert variables with "object" type to "category" type
for i in data.columns:
    if data[i].dtypes == "object":
        data[i] = data[i].astype("category") 

# Confirm if there no variables with "object" type
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 180 entries, 0 to 179
    Data columns (total 9 columns):
     #   Column         Non-Null Count  Dtype   
    ---  ------         --------------  -----   
     0   Product        180 non-null    category
     1   Age            180 non-null    int64   
     2   Gender         180 non-null    category
     3   Education      180 non-null    int64   
     4   MaritalStatus  180 non-null    category
     5   Usage          180 non-null    int64   
     6   Fitness        180 non-null    int64   
     7   Income         180 non-null    int64   
     8   Miles          180 non-null    int64   
    dtypes: category(3), int64(6)
    memory usage: 9.5 KB
    

**Missing value summary function**


```python
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
```

**Missing Values Check**


```python
#Applying the missing value summary function
missing_val_chk(data)
```

    There are NO missing values in the dataset
    

---

**Duplicate row check function**


```python
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
```


```python
df_duplicate_removal(data)
```

    There is/are no duplicated row(s) in the dataframe
    

---

## 5 Point Summary

**Numerical type Summary**


```python
# Five point summary of all numerical type variables in the dataset
data.describe().T
```




<div>

*Output:*


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Age</th>
      <td>180.0</td>
      <td>28.788889</td>
      <td>6.943498</td>
      <td>18.0</td>
      <td>24.00</td>
      <td>26.0</td>
      <td>33.00</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>Education</th>
      <td>180.0</td>
      <td>15.572222</td>
      <td>1.617055</td>
      <td>12.0</td>
      <td>14.00</td>
      <td>16.0</td>
      <td>16.00</td>
      <td>21.0</td>
    </tr>
    <tr>
      <th>Usage</th>
      <td>180.0</td>
      <td>3.455556</td>
      <td>1.084797</td>
      <td>2.0</td>
      <td>3.00</td>
      <td>3.0</td>
      <td>4.00</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>Fitness</th>
      <td>180.0</td>
      <td>3.311111</td>
      <td>0.958869</td>
      <td>1.0</td>
      <td>3.00</td>
      <td>3.0</td>
      <td>4.00</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>Income</th>
      <td>180.0</td>
      <td>53719.577778</td>
      <td>16506.684226</td>
      <td>29562.0</td>
      <td>44058.75</td>
      <td>50596.5</td>
      <td>58668.00</td>
      <td>104581.0</td>
    </tr>
    <tr>
      <th>Miles</th>
      <td>180.0</td>
      <td>103.194444</td>
      <td>51.863605</td>
      <td>21.0</td>
      <td>66.00</td>
      <td>94.0</td>
      <td>114.75</td>
      <td>360.0</td>
    </tr>
  </tbody>
</table>
</div>



**Categorical type Summary**


```python
data.describe(include=['category']).T
```




<div>

*Output:*


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>unique</th>
      <th>top</th>
      <th>freq</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Product</th>
      <td>180</td>
      <td>3</td>
      <td>TM195</td>
      <td>80</td>
    </tr>
    <tr>
      <th>Gender</th>
      <td>180</td>
      <td>2</td>
      <td>Male</td>
      <td>104</td>
    </tr>
    <tr>
      <th>MaritalStatus</th>
      <td>180</td>
      <td>2</td>
      <td>Partnered</td>
      <td>107</td>
    </tr>
  </tbody>
</table>
</div>



**Observations**
* `Product` has **3** unique categories.  
    * `TM195` has the highest frequency in the `Product` column.  
    
    
* `Gender` has **2** unique categories.  
    * `Male` has the highest frequency in the `Gender` column.  
    
    
* `MaritalStatus` has **2** unique categories.  
    * `Partnered` has the highest frequency in the `MaritalStatus` column.  

---

**Create independent sub-lists to separate Numerical and Categorical variables for EDA**


```python
# Select numeric variables
numeric_columns = data.select_dtypes(include=['int', 'float']).columns.tolist()
# Select categorical variables
categorical_columns = data.select_dtypes(include=['category']).columns.tolist()
```

---

## Numerical data

**Skew Summary**


```python
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
```

    The 'Age' distribution is moderately right skewed.
    
    The 'Education' distribution is moderately right skewed.
    
    The 'Usage' distribution is moderately right skewed.
    
    The 'Fitness' distribution is fairly symmetrical.
    
    The 'Income' distribution is highly right skewed.
    
    The 'Miles' distribution is highly right skewed.
    
    

**Outlier check function**


```python
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
```


```python
#Applying the Outlier check function for the sub-dataframe of numerical variables
outlier_count(data[numeric_columns])
```

    The 'Age' distribution has '0' lower outliers and '5' upper outliers.
    
    The 'Education' distribution has '0' lower outliers and '4' upper outliers.
    
    The 'Usage' distribution has '0' lower outliers and '9' upper outliers.
    
    The 'Fitness' distribution has '2' lower outliers and '0' upper outliers.
    
    The 'Income' distribution has '0' lower outliers and '19' upper outliers.
    
    The 'Miles' distribution has '0' lower outliers and '13' upper outliers.
    
    

---

## Categorical data

**Unique states**


```python
# Display the unique values for all categorical variables
for i in categorical_columns:
    print('Unique values in', i, 'are :')
    print(data[i].value_counts())
    print('--'*55)
```

    Unique values in Product are :
    Product
    TM195    80
    TM498    60
    TM798    40
    Name: count, dtype: int64
    --------------------------------------------------------------------------------------------------------------
    Unique values in Gender are :
    Gender
    Male      104
    Female     76
    Name: count, dtype: int64
    --------------------------------------------------------------------------------------------------------------
    Unique values in MaritalStatus are :
    MaritalStatus
    Partnered    107
    Single        73
    Name: count, dtype: int64
    --------------------------------------------------------------------------------------------------------------
    

---
