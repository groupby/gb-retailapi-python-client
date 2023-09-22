# SearchRequestDtoOverwrites


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[RuleConfiguration]**](RuleConfiguration.md) |  | 

## Example

```python
from gb_retailapi_client.models.search_request_dto_overwrites import SearchRequestDtoOverwrites

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequestDtoOverwrites from a JSON string
search_request_dto_overwrites_instance = SearchRequestDtoOverwrites.from_json(json)
# print the JSON string representation of the object
print SearchRequestDtoOverwrites.to_json()

# convert the object into a dict
search_request_dto_overwrites_dict = search_request_dto_overwrites_instance.to_dict()
# create an instance of SearchRequestDtoOverwrites from a dict
search_request_dto_overwrites_form_dict = search_request_dto_overwrites.from_dict(search_request_dto_overwrites_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


