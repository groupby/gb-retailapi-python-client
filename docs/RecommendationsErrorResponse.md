# RecommendationsErrorResponse

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
from gb_retailapi_client.models.recommendations_error_response import RecommendationsErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationsErrorResponse from a JSON string
recommendations_error_response_instance = RecommendationsErrorResponse.from_json(json)
# print the JSON string representation of the object
print RecommendationsErrorResponse.to_json()

# convert the object into a dict
recommendations_error_response_dict = recommendations_error_response_instance.to_dict()
# create an instance of RecommendationsErrorResponse from a dict
recommendations_error_response_form_dict = recommendations_error_response.from_dict(recommendations_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


