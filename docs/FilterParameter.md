# FilterParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** |  | 
**value** | **str** |  | [optional] 
**exclude** | **bool** |  | 
**derived_from_product** | **bool** |  | 

## Example

```python
from gb_retailapi_client.models.filter_parameter import FilterParameter

# TODO update the JSON string below
json = "{}"
# create an instance of FilterParameter from a JSON string
filter_parameter_instance = FilterParameter.from_json(json)
# print the JSON string representation of the object
print FilterParameter.to_json()

# convert the object into a dict
filter_parameter_dict = filter_parameter_instance.to_dict()
# create an instance of FilterParameter from a dict
filter_parameter_form_dict = filter_parameter.from_dict(filter_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


