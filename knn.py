# Import necessary libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,accuracy_score

import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
df=pd.read_csv("/content/sample_data/Iris.csv")

# DATA EXPLORATION
print(df.head())
print(df.info())
print(df.describe())

#Verify Missing Values
print(df.isna().sum())

#Verify Duplicate Values/records
print("BEFORE", df[df.duplicated()])

df.drop_duplicates(keep="first",inplace=True)

#Verify Duplicate Values/records
print("AFTER",df[df.duplicated()])


#verify Outliers

#Plotting the box plot
plt.figure(figsize=(12, 8))
sns.boxplot(data=df, orient="v", palette="Set2")
plt.title("Box Plot of Iris Dataset Features")
plt.show()

#DROP Outliers
def remove_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    print("lower_bound :",lower_bound,"upper_bound:",upper_bound)
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

# Remove outliers from the 'sepal_width' column
df_no_outliers_sepal_width = remove_outliers_iqr(df, 'sepal_width')
print("\nDataFrame after Removing Outliers in 'sepal_width':")
print(df_no_outliers_sepal_width)

df=df_no_outliers_sepal_width

#verify Outliers

#Plotting the box plot
plt.figure(figsize=(12, 8))
sns.boxplot(data=df, orient="v", palette="Set2")
plt.title("Box Plot of Iris Dataset Features AFTER OULIERS DROPPED")
plt.show()


### MACHINE LEANING MODEL DESIGN AND EVALUATION

#Feature Set
X= df.iloc[:, :-1]

#Target Variable/ Classs variable
Y=df.iloc[:, [-1]]

print("Input Features (X) : \n" , X)
print("Target Variable/Class Variable (Y) : \n" , Y)

# Split data into train and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Initialize KNN classifier
k = 3  # Define the number of neighbors
knn = KNeighborsClassifier(n_neighbors=k)

# Train the model
# Y_train array Should be flatten into a 1D array
knn.fit(X_train, np.array(Y_train).ravel())

# Predict on the test data
Y_pred = knn.predict(X_test)

# Print accuracy
accuracy = accuracy_score(Y_test, Y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Print detailed classification report
report = classification_report(Y_test, Y_pred)
print("Classification Report:")
print(report)

#Predict the class of the new observation

#new_observation with sepal_length  sepal_width  petal_length  petal_width
new_observation= pd.DataFrame([[5.1, 3.5, 1.4, 0.2]], columns=X.columns)

predicted_class = knn.predict(new_observation)

print("Predicted Class of NEW OBSERVATION :: ", predicted_class[0])