<p align="center">
  <img src="https://forthebadge.com/images/badges/made-with-python.svg" />&nbsp;&nbsp;&nbsp;
  <img src="https://forthebadge.com/images/badges/made-with-markdown.svg" />&nbsp;&nbsp;&nbsp;
  <img src="https://forthebadge.com/images/badges/powered-by-oxygen.svg" />&nbsp;&nbsp;
</p>



<h1 align="center"> Cardio Equipment Sales 🏃</h1>

<p align="center">The primary objective of this analysis is to better understand CardioGood's customers by examining customer demographics, identifying relationships between customer characteristics and product selections, and studying customer usage and mileage statistics to aid marketing and product development strategies.</p>

---

## 📝 Table of Contents

- [🤓 Description](#description)
- [💻 Dataset Overview](#dataset-overview)
- [📊 Exploratory Data Analysis](#exploratory-data-analysis)
- [🚀 Business Questions](#business-questions)
- [✨ Recommendations](#recommendations)
- [📗 Notebooks](#notebooks)
- [📧 Contact Information](#contact-information)

## 🤓 Description <a name = "description"></a>

CardioGood is a leading treadmill manufacturer offering a range of models to meet varying customer needs. This sales dataset provides insights into CardioGood's customers across three treadmill products: TM195, TM498, and TM798. It includes customer demographics such as age, gender, education level, and marital status, along with usage information covering the average expected weekly usage frequency and mileage. Customers also provide a self-assessed fitness score.

`Objectives`

1. **How do customer demographics (age, gender, education, marital status) compare across purchasers of the 3 treadmill models?**
2. **Is there a relationship between customer income level and the treadmill model purchased?**
3. **Do trends emerge in the expected usage frequencies and weekly mileage across the 3 product models?**
----


## 💻 Dataset Overview <a name = "dataset-overview"></a>

The dataset source file can found through the following link:
### Click to view 👇:

[![Data_link](https://github.com/seandhan/image_database/blob/main/Data-LINK-.svg)](https://github.com/seandhan/Cardio-Equipment-Sales/blob/main/CardioEqptSales.csv)

The cardio fitness dataset contains 9 variables. The data dictionary and key observations are shown below:

<details>
<summary>Data Dictionary</summary>
<br>
  
1. **Product** - the model no. of the treadmill
2. **Age** - in no of years, of the customer
3. **Gender** - of the customer
4. **Education** - in no. of years, of the customer
5. **Marital Status** - of the customer
6. **Usage** - Avg. # times the customer wants to use the treadmill every week
7. **Fitness** - Self rated fitness score of the customer (5 - very fit, 1 - very unfit)
8. **Income** - of the customer
9. **Miles** - expected to run

</details>


<details>
<summary>Key Observations</summary>
<br>

- The dataset is well-structured with 180 rows and 9 columns, including categorical and numerical variables.
- All columns have complete data with no missing values.

</details>


### Click to view 👇:

[![Data Exploration](https://github.com/seandhan/image_database/blob/main/Solution-Dataset%20Exploration-.svg)](https://github.com/seandhan/Cardio-Equipment-Sales/blob/main/Data%20Exploration/Readme.md)



----

## 📊 Exploratory Data Analysis <a name = "exploratory-data-analysis"></a>

The main observations from the dataset are depicted below

<details>
<summary>Main Observations</summary>
<br>

Product Preferences:
* The "TM195" treadmill is the most popular choice among customers, followed by TM498 and TM798.
* Male customers are more frequent purchasers than females, and those in partnered relationships show a higher buying frequency.

Income and Demographics:
* Older customers tend to have higher incomes.
* Higher education is strongly correlated with higher incomes, indicating greater earning potential.
* Gender differences: Male customers generally earn more income than female customers.

Usage Patterns:
* Customers planning to use treadmills more frequently tend to rate themselves as fitter.
* The TM798 model is preferred by fitness enthusiasts, while the TM195 is chosen by those planning lighter usage.
* Partnered customers plan to use their treadmills more often than single customers.

Correlations:
* Several meaningful correlations exist, such as a positive relationship between age and income and positive correlations between education, income, fitness, usage, and miles with the TM798 model.
* Male customers have a preference for the TM798 model.

Product Sales and Gender:
* Male customers are more likely to purchase the TM798 model than females.
* The TM195 model is equally distributed among male and female customers.

Product Preferences by Gender:
* Female customers who buy the TM798 model expect to run more miles on average compared to male customers

</details>

Data visualisation played a vital role in understanding the data. We employed various charts, plots, and graphs to visually represent distributions, trends, and relationships. These visualisations made complex data more accessible and enhanced our ability to derive insights. These visualizations can be seen here.

### Click to view 👇:

[![Exploratory Data Analysis](https://github.com/seandhan/image_database/blob/main/Solution-Exploratory%20Data%20Analysis-.svg)](https://github.com/seandhan/Cardio-Equipment-Sales/blob/main/Exploratory%20Data%20Analysis/Readme.md)


----

## 🚀 Business Questions <a name = "business-questions"></a>

The following business questions will be addressed in the analysis

1. **How do customer demographics (age, gender, education, marital status) compare across purchasers of the 3 treadmill models?**
2. **Is there a relationship between customer income level and the treadmill model purchased?**
3. **Do trends emerge in the expected usage frequencies and weekly mileage across the 3 product models?**

### Click to view 👇:

[![Solution-Business Questions](https://github.com/seandhan/image_database/blob/main/Solution-Business%20Questions-.svg)](https://github.com/seandhan/Cardio-Equipment-Sales/blob/main/Business%20Questions/Readme.md)

----

## ✨ Recommendations <a name = "recommendations"></a>

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
---


## 📗 Notebooks <a name = "notebooks"></a>

The Notebook for the "Data Exploration" can be accessed below:

### Click to view 👇:

[![DataExp Notebook](https://github.com/seandhan/image_database/blob/main/Notebook-Dataset%20Exploration-.svg)](https://github.com/seandhan/Cardio-Equipment-Sales/blob/main/Notebooks/Data%20Exploration.ipynb)


The Notebook for the "Exploratory Data Analysis" can be accessed below:

### Click to view 👇:

[![Exploratory Data Analysis](https://github.com/seandhan/image_database/blob/main/Notebook-Exploratory%20Data%20analysis-.svg)](https://github.com/seandhan/Cardio-Equipment-Sales/blob/main/Notebooks/EDA.ipynb)

The Notebook for the "Business Questions" can be accessed below:

[![Business Questions](https://github.com/seandhan/image_database/blob/main/Notebook-Business%20Questions-.svg)](https://github.com/seandhan/Cardio-Equipment-Sales/blob/main/Notebooks/Business%20Questions.ipynb)

---

## 📧 Contact Information <a name = "contact-information"></a>

- Email: [sean_dhanasar@msn.com](mailto:sean_dhanasar@msn.com)
- LinkedIn: [Sean Dhanasar](https://www.linkedin.com/in/sdhanasar)


