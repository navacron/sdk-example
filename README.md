# SDK-Example

This is an example of how to generate an sdk using openapi-generator and how to add observability hooks to the sdk. The observability hooks are added to the api_client.mustache file. This example demonstrates how to add observability hooks to the sdk and how to run the sdk with console and newrelic observability.

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

For example we have added the following code to the api_client.mustache file in the call_api method. 
```
    {{#asyncio}}async {{/asyncio}}def call_api(
        ..
        ..
            # Call pre request hook if defined
            if hasattr(self, 'pre_request_hook'):
                self.pre_request_hook(method=method, path=url, body=body)
```


Re-generate the sdk
```
openapi-generator-cli generate -i todo-open-api.yaml -g python -o ./todo-sdk  -t ./python-templates-modified \--additional-properties=packageName=todosdk
```

## Common SDK

The common_sdk folder contains libraries to instantiate and configure the telemetry and logging. It has a telemetry.py file that contains the init_console_observability and init_newrelic_observability functions. Each method takes TelemetryConfig as an argument and returns a Telemetry object, which contains a logger, tracer and meter.

```
@dataclass
class TelemetryConfig:
    service_name: str
    newrelic_license_key: Optional[str] = None
    log_level: int = logging.INFO
    otlp_endpoint: str = "https://otlp.nr-data.net:4318"
    enable_traces: bool = True
    enable_metrics: bool = True
     

@dataclass
class Telemetry:
    logger: logging.Logger
    tracer: Optional[trace.Tracer]
    meter: Optional[metrics.Meter]

def init_newrelic_observability(config: TelemetryConfig) -> Telemetry:
    ...

def init_console_observability(config: TelemetryConfig) -> Telemetry:
    ... 
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




