# Cardio Equipment Sales EDA
---
## Project Description

CardioGood is a leading treadmill manufacturer offering a range of models to meet varying customer needs. This sales dataset provides insights into CardioGood's customers across three treadmill products: TM195, TM498, and TM798. It includes customer demographics such as age, gender, education level, and marital status, along with usage information covering the average expected weekly usage frequency and mileage. Customers also provide a self-assessed fitness score.

The primary objective of this analysis is to better understand CardioGood's customers by examining customer demographics, identifying relationships between customer characteristics and product selections, and studying customer usage and mileage statistics to aid marketing and product development strategies.

----

## Table of Contents

- [Skills and Tools Used](#skills-and-tools-used)
- [Project Overview](#project-overview)
- [Project Objectives](#project-objectives)
- [Data Source](#data-source)
- [Data Dictionary](#data-dictionary)
- [Analysis](#Analysis)
- [Data Exploration and Understanding](#data-exploration-and-understanding)
- [Key Observations](#Key-Observations)
- [Recommendations](#Recommendations)
- [Contact Information](#contact-information)
----
## Skills and Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scipy
- Jupyter Notebook
- Data visualization
- Statistical analysis

----


## Project Overview

CardioGood, a renowned treadmill manufacturer, offers a diversified range of treadmill models tailored to meet the unique needs of its customers. In this comprehensive sales analysis project, we delve into CardioGood's customer data across three distinct treadmill products: the TM195, TM498, and TM798. This dataset encompasses a wealth of invaluable information, including customer demographics such as age, gender, education level, and marital status. Furthermore, it provides insights into usage patterns, including the average expected weekly usage frequency and estimated weekly mileage, while also accounting for customers' self-assessed fitness scores.

----

## Project Objectives

1. **Demographic Insights**: Our primary objective is to gain a deep understanding of CardioGood's diverse customer base. This includes exploring customer demographics, comprising age, gender, education, and marital status, and drawing insightful comparisons across purchasers of the three treadmill models.

2. **Income Level Analysis**: We aim to investigate whether a correlation exists between customer income levels and the specific treadmill model they choose to purchase. This relationship could inform targeted marketing strategies and customer outreach efforts.

3. **Usage Patterns**: We scrutinize usage patterns to identify trends in the expected weekly usage frequencies and weekly mileage across the three treadmill product models. These insights can guide marketing and product development strategies, allowing CardioGood to cater more effectively to customer expectations.


## Data Source

Data Source: [CardioEqptSales.csv](https://github.com/seandhan/Cardio-Equipment-Sales/blob/main/CardioEqptSales.csv)

----

## Data Dictionary

The data contains the following variables:
* Product - the model no. of the treadmill
* Age - in no of years, of the customer
* Gender - of the customer
* Education - in no. of years, of the customer
* Marital Status - of the customer
* Usage - Avg. # times the customer wants to use the treadmill every week
* Fitness - Self rated fitness score of the customer (5 - very fit, 1 - very unfit)
* Income - of the customer
* Miles- expected to run
----
## Analysis
Click [HERE](https://github.com/seandhan/CardioEquipmentSales/blob/main/CardioEquipmentSalesEDA.ipynb) to view the analysis.

----
## Data Exploration and Understanding

In this section, we outline the steps taken to explore and understand the CardioGood sales dataset. A thorough data exploration process is essential to derive meaningful insights and lay the foundation for subsequent data analysis.


### Data Overview

The first step was to gain a comprehensive overview of the dataset. This involved:

- Loading the dataset and performing basic data checks to ensure data integrity.
- Examining the structure of the dataset, including the number of rows and columns.
- Identifying the types of variables, including categorical and numerical, to inform subsequent analysis.

### Univariate Analysis

Univariate analysis focuses on individual variables to understand their distributions, statistics, and characteristics. For the CardioGood dataset, we performed the following:

- **Categorical Variables:** We calculated the frequency distribution for categorical variables, such as Product, Gender, and MaritalStatus, to identify dominant categories.
- **Numerical Variables:** We conducted statistical analysis on numerical variables, including Age, Education, Usage, Fitness, Income, and Miles. This included measures of central tendency and dispersion, as well as visualization to understand their distributions.

### Bivariate Analysis

Bivariate analysis explores relationships and associations between pairs of variables. In our analysis, we examined the relationships between variables with a particular focus on:

- **Demographics vs. Product:** We investigated how demographic variables (age, gender, education, and marital status) related to the choice of treadmill product (TM195, TM498, TM798).
- **Income vs. Product:** We explored the association between customer income levels and the specific treadmill model purchased, providing insights into the income-product relationship.
- **Usage and Mileage:** We analyzed trends in expected usage frequencies and weekly mileage across the three product models to uncover distinct usage profiles associated with each.

### Data Visualization

Data visualization played a vital role in understanding the data. We employed various charts, plots, and graphs to visually represent distributions, trends, and relationships. These visualizations made complex data more accessible and enhanced our ability to derive insights.

### Data Cleaning and Preprocessing

Throughout the exploration process, we identified and addressed any data cleaning and preprocessing tasks. This included handling missing values, removing duplicates, and ensuring data consistency. Clean, reliable data is critical for accurate analysis and interpretation.

By thoroughly exploring and understanding the data, we gained valuable insights into customer demographics, product preferences, and usage patterns. These insights form the foundation for the subsequent data analysis and decision-making processes.

----
## Key Observations

### Data Completeness and Structure:

- The dataset is well-structured with 180 rows and 9 columns, including categorical and numerical variables.
- All columns have complete data with no missing values.

### Product Preferences:

- The "TM195" treadmill is the most popular choice among customers, followed by TM498 and TM798.
- Male customers are more frequent purchasers than females, and those in partnered relationships show a higher buying frequency.

### Income and Demographics:

- Older customers tend to have higher incomes.
- Higher education is strongly correlated with higher incomes, indicating greater earning potential.
- Gender differences: Male customers generally earn more income than female customers.

### Usage Patterns:

- Customers planning to use treadmills more frequently tend to rate themselves as fitter.
- The TM798 model is preferred by fitness enthusiasts, while the TM195 is chosen by those planning lighter usage.
- Partnered customers plan to use their treadmills more often than single customers.

### Correlations:

- Several meaningful correlations exist, such as a positive relationship between age and income and positive correlations between education, income, fitness, usage, and miles with the TM798 model.
- Male customers have a preference for the TM798 model.

### Product Sales and Gender:

- Male customers are more likely to purchase the TM798 model than females.
- The TM195 model is equally distributed between male and female customers.

### Product Preferences by Gender:

- Female customers who buy the TM798 model expect to run more miles on average compared to male customers
----
## Recommendations

### Demographic Insights

>CardioGood should take an inclusive approach in marketing that avoids targeting narrow age ranges or lifestyles. Messaging and imagery for all models should appeal to a wide cross-section of adults across generations and relationship statuses. However, the data indicates opportunities to fine-tune brand positioning and partnerships by model based on core customer segments.
>
>The TM195 treadmill should be promoted toward younger millennial fitness enthusiasts entering the category, highlighting introductory pricing and features. For the premium TM798 model, marketing should focus on performance-driven male runners based on their significant representation in this segment. Tactics like in-gym promotions and running event sponsorships can effectively reach this group. Additionally, TM798 messaging should highlight productivity features and advanced training data to align with educated professionals drawn to this top-tier model. In summary, while taking an inclusive approach, targeted outreach to align with the core demographics of each customer segment can help strengthen treadmill model positioning and marketing effectiveness.


### Income Level Analysis

>This analysis found income level strongly correlates with treadmill model selection. Specifically, the data showed customers with higher incomes overwhelmingly prefer the premium TM798 model.
>
>To leverage this, CardioGood should make income a key factor in shaping TM798 marketing strategy and targeting. Messaging and partnerships should focus on highlighting the superior quality, performance, and prestige of the TM798. This positions it as an aspirational product for high-income earners. Tactics like digital ads geo-targeted by income levels can help reach affluent professionals identified as top prospects. Additionally, brand sponsorships of luxury events popular with wealthy consumers can further strengthen TM798's premium branding. In summary, showcasing the TM798 as a top-of-the-line model will resonate with high income customers and drive growth in this profitable segment.


### Usage Patterns

>This analysis uncovered distinct usage profiles associated with each treadmill model. For the entry-level TM195, the majority of customers expected to use the treadmill sparingly, with average weekly usage of just 2-3 times. 25% of TM195 buyers plan to use the treadmill only once per week or less, indicating they purchased this model primarily for light or occasional cardio activity.
>
>In contrast, customers of the mid-range TM498 model averaged 3-4 uses per week - a moderate increase versus TM195. For top-tier TM798, average weekly usage was highest at 3-5 times. The TM798 attracts committed runners looking to use their home treadmill consistently to train throughout the week.
>
>Similar trends were seen for expected mileage. Average miles per week for TM195 customers peaked at 20-30. TM498 buyers saw a moderate uptick in planned mileage to 30-40 weekly miles. For TM798, average miles jumped substantially to 50+ miles per week, with some customers expecting to log over 100 miles.
>
>These insights paint a picture of three distinct user profiles attached to each model. The TM195 appeals to casual walkers or light joggers. The TM498 suits users looking for consistency in moderate running. And the TM798 is optimized for enthusiasts training at high mileages

----
## Contact Information

- Email: [sean_dhanasar@msn.com](mailto:sean_dhanasar@msn.com)
- LinkedIn: [Sean Dhanasar](https://www.linkedin.com/in/sdhanasar)

[//]: # (Include your contact information and links to your professional profiles)
[//]: # (LinkedIn, portfolio website, email, etc.)

