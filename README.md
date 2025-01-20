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

Generate the sdk
```
openapi-generator-cli generate -i todo-open-api.yaml -g python -o ./todosdk-python --additional-properties=packageName=todosdk
```

Update requirements.txt and install generated sdk. Do not forget to pip install everytime the sdk is updated.
```
Add ./todosdk-python to requirements.txt
pip install -r requirements.txt
```
## Run the Service and Client

Run the api service app compliant to the openapi spec
```
python todo-service-flask.py
```

Run the client that that demonstrate the usage of the generated sdk
```
python todo-client-simple.py
```
