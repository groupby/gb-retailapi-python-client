# CustomParameterDto

A key=value combination to allow for further triggering of rules or redirects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key of the custom parameter. | 
**value** | **str** | Value of the custom parameter | 

## Example

```python
from gb_retailapi_client.models.custom_parameter_dto import CustomParameterDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomParameterDto from a JSON string
custom_parameter_dto_instance = CustomParameterDto.from_json(json)
# print the JSON string representation of the object
print CustomParameterDto.to_json()

# convert the object into a dict
custom_parameter_dto_dict = custom_parameter_dto_instance.to_dict()
# create an instance of CustomParameterDto from a dict
custom_parameter_dto_form_dict = custom_parameter_dto.from_dict(custom_parameter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


