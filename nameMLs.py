# Import Dataset
import pandas as pd
df = pd.read_csv('datasets/MalaysianNames.csv')
# print(df.head())
# Data Preprocessing
# remove rows with missing values
df = df.dropna()
# print(df.isnull().sum())
df = df.drop(['country_code'], axis=1)

# save to csv
df.to_csv('datasets/MalaysianNames_clean.csv', index=False)

# load clean dataset
df = pd.read_csv('datasets/MalaysianNames_clean.csv')
# print(df.head())

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings("ignore")


name_vectorizer = CountVectorizer(analyzer='char', ngram_range=(2, 3))
name_features = name_vectorizer.fit_transform(df['name'])

label_encoder = LabelEncoder()
df["gender"] = label_encoder.fit_transform(df["gender"])

from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(name_features, df["gender"], test_size=0.2, random_state=42)


model = DecisionTreeClassifier()


model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy}")

# test the model with new names
new_names = ['AINAA SYAFIQAH ABD RAHMAN ABD RAHMAN', 'Ja Hasim', 'NIK SRI RAHAYU NIK ARIFFIN']
new_name_features = name_vectorizer.transform(new_names)
new_name_features = new_name_features.toarray()

# predict gender of new names
new_names_pred = model.predict(new_name_features)
new_names_pred = label_encoder.inverse_transform(new_names_pred)
print(new_names_pred)




