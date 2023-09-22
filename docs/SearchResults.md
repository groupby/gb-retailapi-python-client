# SearchResults

SAYT response. Contains list of suggestions ad base response information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stats** | [**SearchResultsStats**](SearchResultsStats.md) |  | [optional] 
**search_terms** | [**List[SearchTerms]**](SearchTerms.md) |  | 
**extended_attributes** | **Dict[str, List[str]]** | Map with extended attributes which are returned in autocomplete response.  | [optional] 
**attribute_results** | [**Dict[str, AttributeSuggestion]**](AttributeSuggestion.md) | SAYT response attributes. Contains list of direct matching attributes. | [optional] 
**site_filter** | **str** | SiteFilter object used with request. | [optional] 

## Example

```python
from gb_retailapi_client.models.search_results import SearchResults

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResults from a JSON string
search_results_instance = SearchResults.from_json(json)
# print the JSON string representation of the object
print SearchResults.to_json()

# convert the object into a dict
search_results_dict = search_results_instance.to_dict()
# create an instance of SearchResults from a dict
search_results_form_dict = search_results.from_dict(search_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


