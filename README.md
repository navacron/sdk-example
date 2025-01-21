# SDK-Example

## Create a virtual environment
```
python -m venv venv
```

Activate the virtual environment
```
source venv/bin/activate
```

Install the requirements
```
pip install -r requirements.txt
```

## Openapi-generator 

Install openapi-generator-cli

```
brew install openapi-generator
```

Download python templates for openapi-generator
```
openapi-generator-cli author template -g python -o ./python-templates
```

Generate the sdk, without using the templates i.e. default templates
```
openapi-generator-cli generate -i todo-open-api.yaml -g python -o ./todo-sdk --additional-properties=packageName=todosdk
```

Update requirements.txt and install generated sdk. Do not forget to pip install everytime the sdk is updated.
```
Add ./todosdk to requirements.txt
pip install -r requirements.txt
```
## Run the Service and Client

Run the api service app compliant to the openapi spec
```
python todo-service-flask.py
```

Run the client that that demonstrate the usage of generated sdk
```
python todo-client-simple.py
```

## Add Observability Hooks


Modify the api_client.mustache file to add pre and post request hooks. Note that the api_client.mustache file is located in the python-templates-modified folder and all other files are deleted for simplicity. The python-templates folder is the original template folder.

Re-generate the sdk
```
openapi-generator-cli generate -i todo-open-api.yaml -g python -o ./todo-sdk  -t ./python-templates-modified \--additional-properties=packageName=todosdk
```

## Run Console Observability

Run the client that that demonstrate the usage of generated sdk with observability that prints to console. This demonstrates trace, span and metrics and logging, directly to the console.

```
python todo-client-observability-console.py
```

## Run NewRelic Observability

Register for a free account at https://newrelic.com/signup

Get API key for NewRelic. Get the Ingest KEY type to be able to send data to NewRelic, using opentelemetry.

In your unix environment, set the following environment variables
```
export NEW_RELIC_LICENSE_KEY=YOUR_NEW_RELIC_INGEST_KEY
```

Run the client that that demonstrate the usage of generated sdk with observability
```
python todo-client-observability-newrelic.py
```

Go to NewRelic and see the traces and metrics and logs




