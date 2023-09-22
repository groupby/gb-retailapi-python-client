# FacetSearchRequestDto

Request that should be populated to configure a search API call, made by the client on behalf of a shopper. Contains original request and information about facet for which extra keys requested.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facet** | [**Facet**](Facet.md) |  | 
**original_request** | [**SearchRequestDto**](SearchRequestDto.md) |  | 

## Example

```python
from gb_retailapi_client.models.facet_search_request_dto import FacetSearchRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of FacetSearchRequestDto from a JSON string
facet_search_request_dto_instance = FacetSearchRequestDto.from_json(json)
# print the JSON string representation of the object
print FacetSearchRequestDto.to_json()

# convert the object into a dict
facet_search_request_dto_dict = facet_search_request_dto_instance.to_dict()
# create an instance of FacetSearchRequestDto from a dict
facet_search_request_dto_form_dict = facet_search_request_dto.from_dict(facet_search_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


