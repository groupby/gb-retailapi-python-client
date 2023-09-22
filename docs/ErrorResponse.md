# ErrorResponse

Error object returned by the API.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_id** | **str** | Identifier used for tracking purposes. | 
**method** | **str** | HTTP method of the API call which produced the error. | 
**path** | **str** | HTTP path of the API call which produced the error. | 
**message** | **str** | Error message. Ideally human readable string. | 

## Example

```python
from gb_retailapi_client.models.error_response import ErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponse from a JSON string
error_response_instance = ErrorResponse.from_json(json)
# print the JSON string representation of the object
print ErrorResponse.to_json()

# convert the object into a dict
error_response_dict = error_response_instance.to_dict()
# create an instance of ErrorResponse from a dict
error_response_form_dict = error_response.from_dict(error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


