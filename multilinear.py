#DATA SET DESCRIPTION ::

#Income (in $1000s): Represents the individual's annual income.
#Education Level (Years): Number of years of formal education completed.
#Years of Experience: Number of years in the workforce.
#Age: Target variable to predict.

### USING MACHINE LEARNING APPROACH

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split

# Sample data
df=pd.read_csv("/content/AgeData.csv")
#print(df.describe())

x = df[['Income (in $1000s)', 'Education Level (Years)', 'Years of Experience']]
y= df['Age']

#print(x)
#print(y)

x_train, x_test, y_train, y_test=train_test_split(x, y, test_size = 0.3)

#Fitting the Multiple Linear Regression model
mlr = LinearRegression()
mlr.fit(x_train, y_train)

#Intercept and Coefficient
print("Intercept: (Beta 0) ", mlr.intercept_)

#print("Coefficients:")
#print(list(zip(x, mlr.coef_)))

print("\nCoefficients:\n Beta 1:",mlr.coef_[0])
print("\n Beta 2:",mlr.coef_[1])
print("\n Beta 3:",mlr.coef_[2])

print("\nRegression Equation:",mlr.intercept_,"+",mlr.coef_[0],"*Income (in $1000s)+"
,mlr.coef_[1],"*Education Level (Years)+",mlr.coef_[2],"*Years of Experience")

#Prediction of test set
y_pred_mlr= mlr.predict(x_test)

meanAbErr = metrics.mean_absolute_error(y_test, y_pred_mlr)
meanSqErr = metrics.mean_squared_error(y_test, y_pred_mlr)
rootMeanSqErr = np.sqrt(metrics.mean_squared_error(y_test, y_pred_mlr))
#print('\nR squared: {:.2f}'.format(mlr.score(x,y)*100))
print('\nR squared: {:.2f}'.format(mlr.score(x,y)))
print('Mean Absolute Error:', meanAbErr)
print('Mean Square Error:', meanSqErr)
print('Root Mean Square Error:', rootMeanSqErr)


#### PREDICTING AGE BASED ON TEST/NEW OBSERVATION
newobs_df=pd.DataFrame([[38,15,12]], columns=x.columns)

y_pred_new= mlr.predict(newobs_df)
print("PREDICTED AGE OF NEW RESPONDENT",y_pred_new[0])