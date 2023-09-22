# ErrorDto

Error returned by the API.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_id** | **str** | Identifier used for tracking purposes. | [optional] 
**method** | **str** | HTTP method of the API call which produced the error. | [optional] 
**path** | **str** | HTTP path of the API call which produced the error. | [optional] 
**message** | **str** | Error message. | [optional] 

## Example

```python
from gb_retailapi_client.models.error_dto import ErrorDto

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDto from a JSON string
error_dto_instance = ErrorDto.from_json(json)
# print the JSON string representation of the object
print ErrorDto.to_json()

# convert the object into a dict
error_dto_dict = error_dto_instance.to_dict()
# create an instance of ErrorDto from a dict
error_dto_form_dict = error_dto.from_dict(error_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


