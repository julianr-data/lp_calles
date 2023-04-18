
from fastapi import FastAPI
from funcs import decision, is_number
from math import trunc

app = FastAPI()

@app.get("/")
def index():
    return {"message": "hi! this is the root of the api"}

@app.get('/predict')
def predict(street, number):
    concat = street + number
    if is_number(concat):
        if len(number) > 4:
            return {"error3": "no hay domicilios con más de 4 cifras"}  # mejorar esto, hay casos de cuatro cifras no validos

        x = decision(trunc(float(street)), trunc(float(number)))
        if x != 0:
            return {"ok": (x, x+1)}
        else:
            return {"error1": "calle no contenida dentro del algoritmo"}
    else:
        return {"error2": "input invalido, por favor ingrese solo números"}
