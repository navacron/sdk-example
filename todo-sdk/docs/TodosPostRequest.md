# TodosPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 

## Example

```python
from todosdk.models.todos_post_request import TodosPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TodosPostRequest from a JSON string
todos_post_request_instance = TodosPostRequest.from_json(json)
# print the JSON string representation of the object
print(TodosPostRequest.to_json())

# convert the object into a dict
todos_post_request_dict = todos_post_request_instance.to_dict()
# create an instance of TodosPostRequest from a dict
todos_post_request_from_dict = TodosPostRequest.from_dict(todos_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


