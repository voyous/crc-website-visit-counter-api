import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="counter_http_trigger")
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
def counter_http_trigger(req: func.HttpRequest, inputDocument: func.DocumentList, outputDocument: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if not inputDocument:
        counterItem = {'id': 'count', 'count': 1}
        outputDocument.set(func.Document(counterItem))
    else:
        counterItem = inputDocument[0]
        counterItem['count'] += 1
        outputDocument.set(func.Document(counterItem))

    return func.HttpResponse(f"This HTTP triggered function executed successfully.")