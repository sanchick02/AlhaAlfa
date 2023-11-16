# Import Dataset

import pandas as pd

df2 = pd.read_csv('datasets/OrderReport_archive.csv')

df = pd.read_csv('datasets/MalaysianNames.csv')

# remove rows with missing values
df = df.dropna()

# print(df.isnull().sum())
df = df.drop(['country_code'], axis=1)

# save to csv
df.to_csv('datasets/MalaysianNames_clean.csv', index=False)

# load clean dataset
df = pd.read_csv('datasets/MalaysianNames_clean.csv')
# print(df.head())
# df = df[:100000]

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
import warnings

warnings.filterwarnings("ignore")

name_vectorizer = CountVectorizer(analyzer='char', ngram_range=(2, 3))
name_features = name_vectorizer.fit_transform(df['name'])

label_encoder = LabelEncoder()
df["gender"] = label_encoder.fit_transform(df["gender"])

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(name_features, df["gender"], test_size=0.2, random_state=42)

# # Decision Tree
# from sklearn.tree import DecisionTreeClassifier
# model = DecisionTreeClassifier()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
#
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Model Accuracy: {accuracy}")
#
# # test the model with new names from name column in OrderReport_archive.csv
# new_names = df2['Customer'].tolist()
# new_name_features = name_vectorizer.transform(new_names)
# new_name_features = new_name_features.toarray()
#
# # predict gender of new names
# new_names_pred = model.predict(new_name_features)
# new_names_pred = label_encoder.inverse_transform(new_names_pred)
# print(new_names_pred)
#
# #print total number of M and F in the list
# print("Total number of M: ", new_names_pred.tolist().count('M'))
# print("Total number of F: ", new_names_pred.tolist().count('F'))

# SVM (Takes Years)
#
# from sklearn.svm import SVC
#
# model = SVC(kernel='linear')
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
#
# accuracy = accuracy_score(y_test, y_pred)
#
# print(f"Model Accuracy: {accuracy}")
#
# # test the model with new names from name column in OrderReport_archive.csv
# new_names = df2['Customer'].tolist()
# new_name_features = name_vectorizer.transform(new_names)
# new_name_features = new_name_features.toarray()
#
# # predict gender of new names
# new_names_pred = model.predict(new_name_features)
# new_names_pred = label_encoder.inverse_transform(new_names_pred)
# print(new_names_pred)
#
# #print total number of M and F in the list
# print("Total number of M: ", new_names_pred.tolist().count('M'))
# print("Total number of F: ", new_names_pred.tolist().count('F'))
#

# Naive Bayes
# from sklearn.naive_bayes import MultinomialNB
#
# model = MultinomialNB()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
#
# accuracy = accuracy_score(y_test, y_pred)
#
# print(f"Model Accuracy: {accuracy}")
#
# # test the model with new names from name column in OrderReport_archive.csv
# new_names = df2['Customer'].tolist()
# new_name_features = name_vectorizer.transform(new_names)
# new_name_features = new_name_features.toarray()
#
# # predict gender of new names
# new_names_pred = model.predict(new_name_features)
# new_names_pred = label_encoder.inverse_transform(new_names_pred)
# print(new_names_pred)
#
# #print total number of M and F in the list
# print("Total number of M: ", new_names_pred.tolist().count('M'))
# print("Total number of F: ", new_names_pred.tolist().count('F'))

# Logistic Regression

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy}")

new_names = df2['Customer'].tolist()
# new_names = ['Lee Mann Heyy']
new_name_features = name_vectorizer.transform(new_names)
new_name_features = new_name_features.toarray()

# predict gender of new names
new_names_pred = model.predict(new_name_features)
new_names_pred = label_encoder.inverse_transform(new_names_pred)
print(new_names_pred)

#print total number of M and F in the list
print("Total number of M: ", new_names_pred.tolist().count('M'))
print("Total number of F: ", new_names_pred.tolist().count('F'))

# create a column for gender in OrderReport_archive.csv and put in the gender for respective names and save as new csv

df2.to_csv()


















