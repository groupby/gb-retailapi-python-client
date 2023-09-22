# Stats

Object with base response information. Contains count of returned suggestions and time spent to handle the request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_count** | **int** | Count of suggested sentences in response. | [optional] 
**autocomplete_response** | **int** | Time in milliseconds taken by autocomplete service to handle request and send response. | [optional] 
**extended_attributes_count** | **int** | Count of extended attributes in autocomplete response. | [optional] 
**extended_attributes_response** | **int** | Time in milliseconds taken by application to enrich response with extended attributes. | [optional] 

## Example

```python
from gb_retailapi_client.models.stats import Stats

# TODO update the JSON string below
json = "{}"
# create an instance of Stats from a JSON string
stats_instance = Stats.from_json(json)
# print the JSON string representation of the object
print Stats.to_json()

# convert the object into a dict
stats_dict = stats_instance.to_dict()
# create an instance of Stats from a dict
stats_form_dict = stats.from_dict(stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


