# RecommendationsRequest

Object to wrap all recommendation request configs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | **str** |  | 
**visitor_id** | **str** |  | [optional] 
**limit** | **str** |  | [optional] 
**page_size** | **str** |  | [optional] 
**event_type** | **str** |  | [optional] 
**login_id** | **str** |  | [optional] 
**product_id** | **List[str]** |  | [optional] 
**fields** | **List[str]** |  | [optional] 
**filters** | [**List[Filter]**](Filter.md) |  | [optional] 
**raw_filter** | **str** |  | [optional] 
**placement** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**strict_filtering** | **bool** | The default is true. If strictFiltering true only products that are within the scope of the filter specified. If false, relax the filtering so that the response may contain other products that are outside the scope of the filtering. | [optional] 

## Example

```python
from gb_retailapi_client.models.recommendations_request import RecommendationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationsRequest from a JSON string
recommendations_request_instance = RecommendationsRequest.from_json(json)
# print the JSON string representation of the object
print RecommendationsRequest.to_json()

# convert the object into a dict
recommendations_request_dict = recommendations_request_instance.to_dict()
# create an instance of RecommendationsRequest from a dict
recommendations_request_form_dict = recommendations_request.from_dict(recommendations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


