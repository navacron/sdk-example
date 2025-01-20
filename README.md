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


Download python templates for openapi-generator
```
openapi-generator-cli author template -g python -o ./python-templates
```