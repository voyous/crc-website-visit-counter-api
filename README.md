# Website Visit Counter

An Azure Functions Python application that counts website visits using an HTTP-triggered function.

## Features

- HTTP endpoint for recording visits
- Returns the current visit count
- Designed for deployment to Azure Functions

## Prerequisites

- Python 3.12
- Azure Functions App
- Azure Cosmosdb database
- An Azure subscription for deployment
- Azure Functions Core Tools (for running locally/testing)

## Run locally

1. Create and activate a virtual environment:

	```bash
	python -m venv .venv
	source .venv/bin/activate
	```

2. Install dependencies:

	```bash
	pip install -r requirements.txt
	```

3. Start the Functions host:

	```bash
	func start
	```

The local HTTP endpoint is typically available at `http://localhost:7071`.

## API

Send a request to the deployed function endpoint to register a visit and retrieve the count:

```bash
curl http://localhost:7071/api/visits -X POST
```

or send a GET request to retrieve the count with no increment to database:

```bash
curl http://localhost:7071/api/get_visits
```

The response contains the current number of visits. The exact route and response format depend on the function implementation.

## Deploy to Azure

Create an Azure Function App configured for Python, then deploy from the project directory:

```bash
az login
func azure functionapp publish <FUNCTION_APP_NAME> --python
```

Replace `<FUNCTION_APP_NAME>` with the name of your Azure Function App.

## Configuration

Store connection strings, storage settings, and other secrets in Azure Function App settings or local `local.settings.json`. Do not commit secrets to source control.
