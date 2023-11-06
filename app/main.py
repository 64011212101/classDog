from app.classemo import predict_Emotion
from fastapi import FastAPI, Request
import requests
import tensorflow as tf
from tensorflow.keras.models import load_model

app = FastAPI()

emotionModel = load_model('model/dogEmotionModel.h5')

getimage = 'http://172.17.0.1:8080/api/getpreimg'

@app.get("/")
def root():
    return {"message": "This is my api"}

@app.post("/api/emotiondog")
async def read_str(request:Request):
    item = await request.json()
    print(item)
    img = requests.get(getimage,json=item)
    res = predict_Emotion(emotionModel,img.json()['img'])
    return res