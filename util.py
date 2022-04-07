import subprocess
import sys

# Install all packages
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

import pandas as pd
import plotly.express as px
from sklearn.metrics import accuracy_score, make_scorer

# Constant
STATE_DICT = {1:'Alabama',2:'Alaska',4:'Arizona', 5:'Arkansas',6:'California',8:'Colorado',9:'Connecticut',
              10:'Delaware', 11:'District of Columbia', 12:'Florida', 13:'Georgia', 15:'Hawaii', 16:'Idaho', 
              17:'Illinois', 18:'Indiana', 19:'Iowa', 20:'Kansas', 21:'Kentucky', 22:'Louisiana', 23:'Maine', 
              24:'Maryland', 25:'Massachusetts', 26:'Michigan', 27:'Minnesota', 28:'Mississippi', 29:'Missouri',
              30:'Montana', 31:'Nebraska', 32:'Nevada', 33:'New Hampshire', 34:'New Jersey', 35:'New Mexico', 
              36:'New York', 37:'North Carolina', 38:'North Dakota', 39:'Ohio', 40:'Oklahoma', 42:'Pennsylvania',
              44:'Rhode Island', 45:'South Carolina', 46:'South Dakota', 47:'Tennessee', 48:'Texas', 49:'Utah',
              50:'Vermont', 51:'Virginia', 55:'Wisconsin', 56:'Wyoming', 72:'Puerto Rico'}

REASON_DICT = {1:'1 - Treatment Completed', 
               2:'2 - Dropped out of treatment', 
               3:'3 - Terminated by facility', 
               4:'4 - Transferred to another treatment/facility',
               5:'5 - Incarcerated',
               6:'6 - Death',
               7:'7 - Other'}

def read_csv(path):
    return pd.read_csv(path)

def preprocess(df, features, scaler):
    """
    Normalize the features in the dataframe with a given scaler function.
    :param df: DataFrame
    :param features: List[String]
    :param scaler: A function from https://scikit-learn.org/stable/modules/classes.html#module-sklearn.preprocessing
    """
    df[features] = scaler.fit_transform(df[features])
    return df

def unsupervised_model(df, X, model):
    """
    Run a unsupervised model from sklearn
    :param df: DataFrame
    :param X: List[String]
    :param y: String
    :param model: A model function from sklearn i.e. PCA()
    """
    result = model.fit(df[X])
    transformed = model.transform(df[X])
    return result, transformed

def supervised_model(df, X, y, model, scoring_method=accuracy_score):
    """
    Run a supervised model from sklearn, return the model, predicted_y and the score (accuracy by default)
    :param df: DataFrame
    :param X: List[String]
    :param y: String
    :param model: A model function from sklearn i.e. LogisticRegression()
    :param scoring_method: Evaluation method such as accuracy_score()
    """
    y_true = df[[y]]
    model = model.fit(df[X], y_true)
    y_predicted = model.predict(df[X])
    score = scoring_method(y_true, y_predicted)
    return model, y_predicted, score

def pca_scatter_plot(df, pc1, pc2, color):
    labels={
        pc1: "Principal Component 1",
        pc2: "Principal Component 2"
    }
    fig = px.scatter(df, 
                     x=pc1, 
                     y=pc2, 
                     color=df[color].astype(str), 
                     labels=labels,
                     title="2 component PCA")
    config = {'staticPlot': True}

    fig.show(config=config)
    