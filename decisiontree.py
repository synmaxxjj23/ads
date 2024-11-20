###   Loading Modules/Packages :: Necessary Libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report,accuracy_score

import seaborn as sns
import matplotlib.pyplot as plt

# Load and display top 2 records of the Soybean dataset
df=pd.read_csv("/content/Soybean.csv")
print(df.head(2))

# DATA EXPLORATION
#Data set details/info
print(df.info())
print(df.describe())

#### DATA PRE-PROCESSING
# Missing Values , Duplicated and Outliers Handling

# Handling Missing Values

#Verify Missing Values
#print(df.isna().sum())

#Fill Missing Values with mean value of the respective feature/column
cols=list(df.columns)

print("Before Pre-Processing - Total Missing Values",df.isna().sum().sum())

for i in range(0,len(cols)-1):
  #print(cols[i])
  if(df[cols[i]].isna().sum()>0):
    df[cols[i]].fillna(df[cols[i]].mean(),inplace=True)

print("After Pre-Processing - Total Missing Values",df.isna().sum().sum())

# Handling Duplicate Values
#Verify Duplicate Values/records


print("BEFORE DROP :: DATA SIZE", df.shape)

df.drop_duplicates(keep="first",inplace=True)

#Verify Duplicate Values/records
print("AFTER DROP :: DATA SIZE", df.shape)

# Handling Outliers

#verify Outliers

#Plotting the box plot
plt.figure(figsize=(20, 8))
sns.boxplot(data=df, orient="v", palette="Set2")
plt.title("Box Plot of Soybean Dataset Features")
plt.show()

''' NOTE:: DATA HAS OUTLIERS BUT THEY ARE VALID RESPONSES , HENCE WE ARE NOT DROPPING THE OUTLIERS.
IF THEY ARE REALLY OUTLERS THEN WE SHOULD DROP THE OUTLIERS USING THE BELOW CODE

# #DROP Outliers
# def remove_outliers_iqr(df, column):
#     Q1 = df[column].quantile(0.25)
#     Q3 = df[column].quantile(0.75)
#     IQR = Q3 - Q1
#     lower_bound = Q1 - 1.5 * IQR
#     upper_bound = Q3 + 1.5 * IQR
#     print(column,":","lower_bound :",lower_bound,"upper_bound:",upper_bound)
#     return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

# # Remove outliers from the 'sepal_width' column

# print("BOX PLOT - B4", df.shape)

# for i in range(0,len(cols)-1):
#   df = remove_outliers_iqr(df, cols[i])

# print("BOX PLOT - AFTER", df.shape)

'''

### MACHINE LEANING MODEL DESIGN AND EVALUATION

#Feature Set
X= df.iloc[:, :-1] #"Input Features

#Target Variable/ Classs variable
Y=df.iloc[:, [-1]]

# print("Input Features (X) : \n" , X)
# print("Target Variable/Class Variable (Y) : \n" , Y)

# Split data into train and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Initialising Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(X_train,Y_train)

# Train the model
# Y_train array Should be flatten into a 1D array
clf.fit(X_train, np.array(Y_train).ravel())

# Predict on the test data
Y_pred = clf.predict(X_test)

# Print accuracy
accuracy = accuracy_score(Y_test, Y_pred)
print(f"Accuracy: {accuracy:.2f}")

# # Print detailed classification report
# report = classification_report(Y_test, Y_pred)
# print("Classification Report:")
# print(report)

#Predict the class of the new observation

new_observation= pd.DataFrame([[6,0,2,1,0,3,0,1,1,1,1,1,0,2,2,0,0,0,1,0,3,1,1,1,0,0,0,0,4,0,0,0,0,0,0]], columns=X.columns)

predicted_class = clf.predict(new_observation)

print("Predicted Class of NEW OBSERVATION :: ", predicted_class[0])
