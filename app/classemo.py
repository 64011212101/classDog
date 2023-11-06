import numpy as np

classEmo = {0:"angry", 1:"happy", 2:"relaxed",
               3:"sad"}

def predict_Emotion(model,img):
    image=np.expand_dims(img,axis=0)
    emotion = model.predict(image)
    return {"emotion":classEmo[np.argmax([emotion[0]])]}