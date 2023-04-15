
from fastapi import FastAPI
from funcs import decision

app = FastAPI()

@app.get("/")
def index():
    return {"message": "hi! this is the root of the api"}

@app.get('/predict')
def predict(street, number):
    x = decision(int(street), int(number))
    return {"message": f"The address is between: {x} and {x+1}"}
