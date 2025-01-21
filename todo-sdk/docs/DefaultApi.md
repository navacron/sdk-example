# todosdk.DefaultApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**todos_get**](DefaultApi.md#todos_get) | **GET** /todos | Get all todos
[**todos_post**](DefaultApi.md#todos_post) | **POST** /todos | Create a new todo
[**todos_todo_id_get**](DefaultApi.md#todos_todo_id_get) | **GET** /todos/{todoId} | Get a specific todo


# **todos_get**
> List[Todo] todos_get()

Get all todos

### Example


```python
import todosdk
from todosdk.models.todo import Todo
from todosdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = todosdk.Configuration(
    host = "http://localhost:5001"
)


# Enter a context with an instance of the API client
with todosdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = todosdk.DefaultApi(api_client)

    try:
        # Get all todos
        api_response = api_instance.todos_get()
        print("The response of DefaultApi->todos_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->todos_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Todo]**](Todo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of todos |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **todos_post**
> Todo todos_post(todos_post_request)

Create a new todo

### Example


```python
import todosdk
from todosdk.models.todo import Todo
from todosdk.models.todos_post_request import TodosPostRequest
from todosdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = todosdk.Configuration(
    host = "http://localhost:5001"
)


# Enter a context with an instance of the API client
with todosdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = todosdk.DefaultApi(api_client)
    todos_post_request = todosdk.TodosPostRequest() # TodosPostRequest | 

    try:
        # Create a new todo
        api_response = api_instance.todos_post(todos_post_request)
        print("The response of DefaultApi->todos_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->todos_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **todos_post_request** | [**TodosPostRequest**](TodosPostRequest.md)|  | 

### Return type

[**Todo**](Todo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created todo |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **todos_todo_id_get**
> Todo todos_todo_id_get(todo_id)

Get a specific todo

### Example


```python
import todosdk
from todosdk.models.todo import Todo
from todosdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = todosdk.Configuration(
    host = "http://localhost:5001"
)


# Enter a context with an instance of the API client
with todosdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = todosdk.DefaultApi(api_client)
    todo_id = 56 # int | 

    try:
        # Get a specific todo
        api_response = api_instance.todos_todo_id_get(todo_id)
        print("The response of DefaultApi->todos_todo_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->todos_todo_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **todo_id** | **int**|  | 

### Return type

[**Todo**](Todo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Todo found |  -  |
**404** | Todo not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

