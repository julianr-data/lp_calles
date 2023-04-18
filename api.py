
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
            return {"code": "error3", "message": "No hay domicilios de más de 4 cifras"}  # mejorar esto, tb hay casos de cuatro cifras no validos

        x = decision(trunc(float(street)), trunc(float(number)))
        if x != 0:
            return {"code": "ok", "message": (x, x+1)}
        else:
            return {"code": "error1", "message": "Calle no contenida dentro del algoritmo"}
    else:
        return {"code": "error2", "message": "Input invalido, por favor ingrese solo números"}
