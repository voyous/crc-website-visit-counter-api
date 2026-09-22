import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="visits", methods=["POST"])
@app.cosmos_db_input(arg_name="inputDocument",
                     database_name="visit-counter-db",
                     container_name="counter-container",
                     id="count",
                     partition_key="count",
                     connection="connection_key")
@app.cosmos_db_output(arg_name="outputDocument",
                      database_name="visit-counter-db",
                      container_name="counter-container",
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