# CustomParameterTrigger


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from gb_retailapi_client.models.custom_parameter_trigger import CustomParameterTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of CustomParameterTrigger from a JSON string
custom_parameter_trigger_instance = CustomParameterTrigger.from_json(json)
# print the JSON string representation of the object
print CustomParameterTrigger.to_json()

# convert the object into a dict
custom_parameter_trigger_dict = custom_parameter_trigger_instance.to_dict()
# create an instance of CustomParameterTrigger from a dict
custom_parameter_trigger_form_dict = custom_parameter_trigger.from_dict(custom_parameter_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


