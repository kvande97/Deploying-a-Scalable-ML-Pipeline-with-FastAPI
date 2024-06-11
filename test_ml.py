
import pytest
import pandas as pd
from ml.data import process_data
from ml.model import train_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

data = pd.read_csv('data/census.csv')
train_data, test_data = train_test_split(data, test_size=0.2, random_state=40)

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]
 
X_train, y_train, encoder, lb = process_data(
    train_data,
    categorical_features=cat_features,
    label="salary",
    training=True,
)

model = train_model(X_train, y_train)

def test_train_model():
    assert isinstance(model, RandomForestClassifier)

def test_data_shapes():
    assert data.shape[1] == 15
    assert train_data.shape[1] == 15
    assert test_data.shape[1] == 15
    assert X_train.shape[0] == y_train.shape[0]

def test_split_percentage():
    perc = train_data.shape[0] / data.shape[0]
    assert abs(perc - 0.8) < 0.01

def test_clean_data():
    assert data.isnull().sum().sum() == 0

    
    






