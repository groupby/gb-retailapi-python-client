# SearchMetadataDto

Metadata relating to the search results, or how they were generated.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_attribution_token** | **str** | Token to assist beacon collectors in correlating searches to user events. | [optional] 
**cached** | **bool** | Were the search results from a previous call. | [optional] 
**total_time** | **int** | Total time spent performing the Google search in milliseconds. | [optional] 

## Example

```python
from gb_retailapi_client.models.search_metadata_dto import SearchMetadataDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchMetadataDto from a JSON string
search_metadata_dto_instance = SearchMetadataDto.from_json(json)
# print the JSON string representation of the object
print SearchMetadataDto.to_json()

# convert the object into a dict
search_metadata_dto_dict = search_metadata_dto_instance.to_dict()
# create an instance of SearchMetadataDto from a dict
search_metadata_dto_form_dict = search_metadata_dto.from_dict(search_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


