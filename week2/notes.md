#### titanic.csv

## Which columns have missing values? How many?

Age, Cabin, and Embarked have missing values with counts:

Age = 177

Cabin = 687

Embarked = 2


## Which columns are numeric? Which are categorical?

numerical_cols = ['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']

categorical_cols = ['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']


## What is the class balance in Survived? Is this balanced or imbalanced?

Non-survived (0): 549 passengers (~61%)

Survived (1): 342 passengers (~39%)

#### Conclusion:
The dataset is moderately imbalanced.


## Which column has the most missing data? What % is missing?

Cabin has the most missing data.

Missing percentage ≈ 77%


## why does modifying a slice without .copy() cause a bug?

Without .copy(), a sliced DataFrame may be either a view or a copy of the original DataFrame.

So when you modify it, pandas cannot guarantee whether the original DataFrame should also change, leading to unpredictable behavior and SettingWithCopyWarning.


## What are the 3 strategies for handling missing values and when do you use each?

If more than 50% data is missing then drop the column.

If numerical column data is missing then fill with mean or median.

If categorical column data is missing then fill with mode.


## What is the .copy() bug and why does it matter?

When we apply any transformation or add/remove columns from a subpart of DataFrame then sometimes pandas gets confused and makes the changes in original DataFrame too, so that is why always use .copy().


## Why do you fill missing values with median instead of mean for Age?

Median is less affected by outliers compared to mean, so it gives better and more stable filling for Age values.


## What does errors='coerce' do in pd.to_numeric()?

If any non-numeric data is encountered then instead of throwing an error it replaces that value with NaN.


## What columns in Titanic does sklearn refuse to process directly and why?

Columns like Name, Sex, Ticket, Cabin, and Embarked contain string/categorical data, so sklearn models cannot process them directly unless they are converted into numeric format.