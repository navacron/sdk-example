from common_sdk import init_newrelic_observability
from common_sdk.telemetry.instrumentation import TelemetryConfig
from todosdk import Configuration, ApiClient
from todosdk.api.default_api import DefaultApi
import os

# New Relic configuration
NEWRELIC_LICENSE_KEY = os.getenv('NEW_RELIC_LICENSE_KEY')
NEWRELIC_ENDPOINT = "https://otlp.nr-data.net:4318"

# Initialize telemetry
telemetry = init_newrelic_observability(TelemetryConfig(
    service_name='todo-client',
    enable_traces=True,
    enable_metrics=True,
    newrelic_license_key=NEWRELIC_LICENSE_KEY,
    otlp_endpoint=NEWRELIC_ENDPOINT
))

counter = telemetry.meter.create_counter(
        name="demo.requests",
        description="Number of requests processed",
        unit="1"
    )

# Configure and create API client
config = Configuration(host="http://localhost:5001")
api_client = ApiClient(configuration=config)

# Define pre and post request hooks
def pre_request_hook(method, path, body):
    with telemetry.tracer.start_as_current_span("api_request") as span:
        span.set_attribute("http.method", method)
        span.set_attribute("http.path", path)
        telemetry.logger.info(f"About to make {method} request to {path}")
        # Record a metric
        counter.add(1, {"request.status": "success"})

def post_request_hook(method, path, response):
    telemetry.logger.info(f"Received response from {method} {path}: {response.status}")

# ... rest of your code ...
# Set the hooks
api_client.pre_request_hook = pre_request_hook
api_client.post_request_hook = post_request_hook

# Create API instance
api = DefaultApi(api_client)

# Use the API
todos = api.todos_get()
telemetry.logger.info(f"Received todos: {todos}")
#print(f"Received todos: {todos}")

# Create a new todo
new_todo = api.todos_post({"title": "Test todo"})
telemetry.logger.info(f"Created new todo: {new_todo}") 