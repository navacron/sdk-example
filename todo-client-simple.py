from todosdk import Configuration, ApiClient
from todosdk.api.default_api import DefaultApi
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# Configure and create API client
config = Configuration(host="http://localhost:5001")
api_client = ApiClient(configuration=config)

# Create API instance
api = DefaultApi(api_client)

# Use the API
todos = api.todos_get()
logging.info(f"Received todos: {todos}")

# Create a new todo
new_todo = api.todos_post({"title": "Test todo"})
logging.info(f"Created new todo: {new_todo}") 