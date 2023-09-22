# SearchTerms

Object with one single suggestion and associated info (brands and categories).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Suggestion itself. | [optional] 
**additional_info** | [**AdditionalInfo**](AdditionalInfo.md) |  | 

## Example

```python
from gb_retailapi_client.models.search_terms import SearchTerms

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTerms from a JSON string
search_terms_instance = SearchTerms.from_json(json)
# print the JSON string representation of the object
print SearchTerms.to_json()

# convert the object into a dict
search_terms_dict = search_terms_instance.to_dict()
# create an instance of SearchTerms from a dict
search_terms_form_dict = search_terms.from_dict(search_terms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


