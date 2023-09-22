# SearchResultsStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_count** | **int** | Count of suggested sentences in response. | [optional] 
**autocomplete_response** | **int** | Time in milliseconds taken by autocomplete service to handle request and send response. | [optional] 
**extended_attributes_count** | **int** | Count of extended attributes in autocomplete response. | [optional] 
**extended_attributes_response** | **int** | Time in milliseconds taken by application to enrich response with extended attributes. | [optional] 

## Example

```python
from gb_retailapi_client.models.search_results_stats import SearchResultsStats

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultsStats from a JSON string
search_results_stats_instance = SearchResultsStats.from_json(json)
# print the JSON string representation of the object
print SearchResultsStats.to_json()

# convert the object into a dict
search_results_stats_dict = search_results_stats_instance.to_dict()
# create an instance of SearchResultsStats from a dict
search_results_stats_form_dict = search_results_stats.from_dict(search_results_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


