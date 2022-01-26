"""
app.py

Web API layer. Platform specific.
"""

from importlib import import_module

from fastapi import FastAPI
from pydantic import Json, BaseModel

import mlops.logger as logger
from config import service_type

logging = logger.get_logger(f"api")

service = import_module(f"mlops.{service_type}").service

app = FastAPI()


class Data(BaseModel):
    data: Json


@app.post("/")
def api(input: Data):
    data = input.data
    logging.debug(f"{data=}")
    try:
        return service(data)
    except Exception as error:
        error_type = type(error).__name__
        error_message = f"Service failed. {error_type}: {error}"
        logging.critical(error_message)
        return dict(status="error", error_message=error_message)
