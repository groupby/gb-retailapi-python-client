# QueryPatternTrigger


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**QueryPatternTriggerType**](QueryPatternTriggerType.md) |  | 
**values** | **List[str]** |  | [optional] 
**patterns** | **List[object]** |  | [optional] 

## Example

```python
from gb_retailapi_client.models.query_pattern_trigger import QueryPatternTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of QueryPatternTrigger from a JSON string
query_pattern_trigger_instance = QueryPatternTrigger.from_json(json)
# print the JSON string representation of the object
print QueryPatternTrigger.to_json()

# convert the object into a dict
query_pattern_trigger_dict = query_pattern_trigger_instance.to_dict()
# create an instance of QueryPatternTrigger from a dict
query_pattern_trigger_form_dict = query_pattern_trigger.from_dict(query_pattern_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


