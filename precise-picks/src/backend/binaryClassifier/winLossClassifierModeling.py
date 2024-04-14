import pandas as pd
# Load and manipulate data with pandas.
from sklearn.linear_model import LogisticRegression
# We're predicting outcomes with logistic regression—a go-to model for binary classification.
from sklearn.model_selection import train_test_split, cross_val_score
# Split data into training and testing sets, and evaluate model performance with cross-validation.
from sklearn import preprocessing 
# Prep data for modeling by scaling features, so they're all judged fairly.
from sklearn.metrics import classification_report
# Get a score card for model, showing precision, recall, f1-score, and more.

# Load the data, ditching the first unnamed column.
data = pd.read_csv("...nbaHomeWinLossModelDataset.csv").drop(['Unnamed: 0'], axis=1)
data = data.dropna()  # no incomplete data.

# Separate out validation data (for the '2023-24 season) from the rest.
validation = data[data['SEASON'] == '2023-24']
modelData = data[data['SEASON'] != '2023-24'].sample(frac=1)  # Shuffle the non-validation data.

# Prepare features (X) and target (y), excluding 'SEASON' from features.
X = modelData.drop(['HOME_W', 'SEASON'], axis=1)
y = modelData['HOME_W']

# Split the data into training and test sets, keeping 33% for testing.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.33)

# Scale the features for both training and test sets for consistent magnitude.
scaler = preprocessing.StandardScaler()
scaler.fit(X_train)
scaled_data_train = scaler.transform(X_train)

scaler.fit(X_test)
scaled_data_test = scaler.transform(X_test)

# Create and train the logistic regression model.
model = LogisticRegression()
model.fit(scaled_data_train, y_train)

# Evaluate the model's performance on the test set.
model.score(scaled_data_test, y_test)

# Use cross-validation for a more robust assessment of model performance.
F1Score = cross_val_score(model, scaled_data_test, y_test, cv=12, scoring='f1_macro')
print("Logistic Model F1 Accuracy: %0.2f (+/- %0.2f)" % (F1Score.mean(), F1Score.std() * 2))

# Predict on the test set and report the outcomes.
y_pred = model.predict(scaled_data_test)
print(classification_report(y_test, y_pred))

# Prepare the validation set in a similar manner for final model assessment.
scaler = preprocessing.StandardScaler()
scaler.fit(validation.drop(['HOME_W', 'SEASON'], axis=1))
scaled_val_data = scaler.transform(validation.drop(['HOME_W', 'SEASON'], axis=1))

# Predict and evaluate on the unseen validation data to understand future performance.
y_pred = model.predict(scaled_val_data)
print(classification_report(validation['HOME_W'], y_pred))

