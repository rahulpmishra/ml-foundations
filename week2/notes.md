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