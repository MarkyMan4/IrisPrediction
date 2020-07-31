from typing import Optional
from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import numpy as np

# define request payload
class Feature(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

app = FastAPI()
model = joblib.load('model/model.pkl')

# names of classes
target_names = {
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica'
}

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post('/predict/')
def get_prediction(feature: Feature):
    data = np.array([[
        feature.sepal_length,
        feature.sepal_width,
        feature.petal_length,
        feature.petal_width
    ]])
    
    prediction = float(model.predict(data)[0])

    return {'prediction': target_names[prediction]}