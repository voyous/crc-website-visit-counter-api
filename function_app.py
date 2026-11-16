import azure.functions as func
import logging
import json
import os

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# Increments the visit count in Cosmos DB and returns the updated count.
@app.route(route="visits", methods=["POST"])
@app.cosmos_db_input(arg_name="inputDocument",
                     database_name=os.environ['DATABASE_NAME'],
                     container_name=os.environ['DB_CONTAINER_NAME'],
                     id="count",
                     partition_key="count",
                     connection="connection_key")
@app.cosmos_db_output(arg_name="outputDocument",
                      database_name=os.environ['DATABASE_NAME'],
                      container_name=os.environ['DB_CONTAINER_NAME'],
                      connection="connection_key")
def visits(req: func.HttpRequest, inputDocument: func.DocumentList, outputDocument: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if not inputDocument:
        countItem = {'id': 'count', 'count': 1}
        outputDocument.set(func.Document(countItem))
    else:
        countItem = inputDocument[0]
        countItem['count'] += 1
        outputDocument.set(func.Document(countItem))

    return func.HttpResponse(body=json.dumps({"count": countItem['count']}), status_code=200)

# Retrieves the current visit count from Cosmos DB and returns it.
@app.route(route="get_visits", methods=["GET"])
@app.cosmos_db_input(arg_name="inputDocument",
                     database_name=os.environ['DATABASE_NAME'],
                     container_name=os.environ['DB_CONTAINER_NAME'],
                     id="count",
                     partition_key="count",
                     connection="connection_key")
def get_visits(req: func.HttpRequest, inputDocument: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if not inputDocument:
        return func.HttpResponse(body=json.dumps({"count": 0}), status_code=200)
    else:
        countItem = inputDocument[0]
    
    return func.HttpResponse(body=json.dumps({"count": countItem['count']}), status_code=200)