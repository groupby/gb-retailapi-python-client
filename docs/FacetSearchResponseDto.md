# FacetSearchResponseDto

Facet search response representation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_request** | [**SearchRequestDto**](SearchRequestDto.md) |  | 
**available_navigation** | [**NavigationDto**](NavigationDto.md) |  | 

## Example

```python
from gb_retailapi_client.models.facet_search_response_dto import FacetSearchResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of FacetSearchResponseDto from a JSON string
facet_search_response_dto_instance = FacetSearchResponseDto.from_json(json)
# print the JSON string representation of the object
print FacetSearchResponseDto.to_json()

# convert the object into a dict
facet_search_response_dto_dict = facet_search_response_dto_instance.to_dict()
# create an instance of FacetSearchResponseDto from a dict
facet_search_response_dto_form_dict = facet_search_response_dto.from_dict(facet_search_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


