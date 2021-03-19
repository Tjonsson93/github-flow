
import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# used to scale the data to fit the Logistic algorithm
sc = StandardScaler()

# random_state=0 means that we don't shuffle the dataset 
classifier = LogisticRegression(random_state=0)

def train_model():
    con = sqlite3.connect('ads_dataset.db')
    # df = dataframe
    df = pd.read_sql_query('SELECT * FROM dataset', con)

    X = df.iloc[:, :-1].values

    y = df.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    classifier.fit(X_train, y_train)

    con.close()






def predict(age, income):

    
    probability_of_click = classifier.predict_proba(sc.transform([[age, income]]))

    #
    #
    probability = probability_of_click[0, 1]

    # classifier.predict() == probability > 0.5
    prediction = True if probability > 0.5 else False

    # return a dict with predicited values
    return { "willClick": prediction, "probability": probability }





