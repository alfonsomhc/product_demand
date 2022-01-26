"""
prediction.py

Prediction service. Platform independent. 
"""
from importlib import import_module

import mlops.logger as logger
from config import artifact_folder, model_id, model_import_path

model_module = import_module(model_import_path)
predict = model_module.predict
_initialization = model_module.initialization
ModelException = model_module.ModelException

logging = logger.get_logger("prediction_service")


def initialization():
    """
    Read initialization object required by `predict`.
    Avoid loading the artifact for every prediction.
    """
    if "init_object" not in globals():
        global init_object
        init_object = _initialization(artifact_folder)
        logging.debug(f"Loaded initialization object")


def service(data):
    """
    Generate prediction for an input
    Inputs:
        data: input to the model (sent by a user through the API)
    Output:
        Dictionary with a status field ('ok' or 'error'). If status is 'ok',
         there is a 'prediction' field as well. If status is 'error', there is
         a 'message' field as well.
    """
    try:
        initialization()
        logging.debug(f"Predict {data=}")
        y = predict(data, init_object)
        logging.debug(f"Prediction is {y=}")
        return dict(status="ok", prediction=y, model_id=model_id)
    except ModelException as error:
        error_message = f"Could not get a prediction. Message: {error}"
        logging.error(error_message)
        return dict(status="error", message=error_message, model_id=model_id)
