# Todo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**title** | **str** |  | 
**completed** | **bool** |  | 

## Example

```python
from todosdk.models.todo import Todo

# TODO update the JSON string below
json = "{}"
# create an instance of Todo from a JSON string
todo_instance = Todo.from_json(json)
# print the JSON string representation of the object
print(Todo.to_json())

# convert the object into a dict
todo_dict = todo_instance.to_dict()
# create an instance of Todo from a dict
todo_from_dict = Todo.from_dict(todo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


