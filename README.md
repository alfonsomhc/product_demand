# Forecasting Product Demand
Code for a a product forecast model that is deployed as a web API.

## Content
Developed by the data scientist:
 - ar_model/: model code, in this case implementing a standard interface for the prediction service
 - ar_model_artifact/: model artifact, which could be stored instead in a model manager
 - config.py: configuration to be used by mlops framework
 - requirements.txt: libraries required by the model
 - notebooks/: notebooks developed during data exploration and prototyping

Code developed by the platfom team:
 - mlops/: mlops framework code, in this example a logger and a prediction
   service
 - docker-compose.yaml
 - Dockerfile 
 
This "mlops framework" could be added to the repo through a repo template, or a
custom library.

## Getting Started
1. Clone the repo
2. Either run the web api with uvicorn:
```bash
uvicorn mlops.app:app --host 0.0.0.0 --port 8000
```
or through docker composer:
```bash
docker-compose up --build
```
3. Install httpie (https://httpie.io/docs/cli/installation)
4. Call the web api: 
```bash
http -v POST http://127.0.0.1:8000/ data='{"n_weeks": 2}'
```