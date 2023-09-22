# DebugDto

Contains debug info associated to response.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_search_request** | **List[object]** | Search request in raw format executed internally against search engine. | [optional] 
**raw_search_response** | **List[object]** | Search response in raw format received internally from search engine. | [optional] 

## Example

```python
from gb_retailapi_client.models.debug_dto import DebugDto

# TODO update the JSON string below
json = "{}"
# create an instance of DebugDto from a JSON string
debug_dto_instance = DebugDto.from_json(json)
# print the JSON string representation of the object
print DebugDto.to_json()

# convert the object into a dict
debug_dto_dict = debug_dto_instance.to_dict()
# create an instance of DebugDto from a dict
debug_dto_form_dict = debug_dto.from_dict(debug_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


