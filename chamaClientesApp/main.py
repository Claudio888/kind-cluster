import requests
import os
import log_config

from fastapi import FastAPI
from pydantic import BaseModel
from logging.config import dictConfig
from prometheus_fastapi_instrumentator import Instrumentator


dictConfig(log_config.sample_logger)
 

app = FastAPI()

Instrumentator().instrument(app).expose(app)

@app.get("/")
async def root():
    return {"message": "Aplicacao para testes de deployment DevOps - Request - getClientes"}


@app.get("/getclientes")
def get_clientes():
    endpoint = os.getenv("CLIENTES_URL")
    response = requests.get("{clientes_url}/clientes".format(clientes_url=endpoint))
    return response.json()

@app.get("/getclientes/{id_number}")
def get_clientes_id(id_number: int):
    endpoint = os.getenv("CLIENTES_URL")
    response = requests.get("{clientes_url}/clientes/{id_number}".format(clientes_url=endpoint, id_number=id_number))
    return response.json()