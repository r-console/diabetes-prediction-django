from rest_framework.response import Response
from rest_framework.decorators import api_view
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from django.conf import settings
import os


@api_view(['GET'])
def getData(request):
    person = {'name': 'Ramesh'}
    return Response(person)


@api_view(['POST'])
def PredictData(request):
    # read dataset with pandas
    csv_file_path = os.path.join(settings.STATIC_ROOT, 'diabetes.csv')
    df = pd.read_csv(csv_file_path)
    # split actual outcome from dataset
    X = df.drop("Outcome", axis=1)
    Y = df['Outcome']
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    # training the model
    model = LogisticRegression(max_iter=1000)
    model.fit(x_train, y_train)
    # predict our values
    OURVALUE = request.data
    p = pd.DataFrame([OURVALUE['data']], columns=["Pregnancies", "Glucose", "BloodPressure",
                     "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"])
    res = model.predict(p)
    return Response({"result": res[0]})
