# SearchResponseDto

Response of calling the search API, including various elements of the original request context, matching records and general metadata relating to the results.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the search. | [optional] 
**area** | **str** | Area Id the search was performed in. | [optional] 
**query** | **str** | Original search query. | [optional] 
**corrected_query** | **str** | Search query after any changes/corrections are done by the engine. | [optional] 
**biasing_profile** | **str** | Name of the biasing profile which was used to bias products in the search results. | [optional] 
**biasing_profile_applied_id** | **int** | Id of the biasing profile which was used to bias products in the search results. | [optional] 
**filter** | **str** |  | 
**original_request** | [**SearchRequestDto**](SearchRequestDto.md) |  | 
**records** | [**List[RecordDto]**](RecordDto.md) | The list of records that match the search. | [optional] 
**total_record_count** | **int** | The total number of products that match the search. If all products were filtered out on S4R site equals to 0. | [optional] 
**metadata** | [**SearchMetadataDto**](SearchMetadataDto.md) |  | 
**page_info** | [**PageInfoDto**](PageInfoDto.md) |  | 
**available_navigation** | [**List[NavigationDto]**](NavigationDto.md) |  | 
**selected_navigation** | [**List[NavigationDto]**](NavigationDto.md) |  | 
**redirect** | **str** | URL to which the merchandiser should redirect the shopper to. | [optional] 
**experiments** | [**List[Experiment]**](Experiment.md) |  | 
**template** | [**TemplateDto**](TemplateDto.md) |  | 
**empty** | **bool** | True if the search yielded no results, otherwise false. | [optional] 
**site_params** | [**List[Metadata]**](Metadata.md) |  | 
**debug** | [**DebugDto**](DebugDto.md) |  | 
**warnings** | **List[str]** | Warning messages containing information about invalid products, etc. | [optional] 
**include_expanded_results** | **bool** | When a shopper uses an ambiguous or a multi-word search phrase, they can get an empty response. After turning on include expanded results, Retail Search analyzes the request and returns the expanded list of products based on the parsed search query. For example, if you search \&quot;Google Pixel 5\&quot; without query expansion, you might only get \&quot;google_pixel_5\&quot; in the result. With query expansion, you might get \&quot;google_pixel_4a_with_5g\&quot;, \&quot;google_pixel_4a\&quot; and \&quot;google_pixel_5_case\&quot; as well.The default value is configured in the tenant settings or true if there is no such setting | [optional] 
**facet_limit** | **int** | Maximum of facet values that should be returned for this facet. If not specified, defaults to 20. The maximum allowed value is 300. Values above 300 will be coerced to 300.  If this field is negative, an INVALID_ARGUMENT is returned.  This limit (300) is configured on Google side, but Google have an ability to change it for specific project.  | [optional] 
**redirect_metadata** | [**List[Metadata]**](Metadata.md) |  | 

## Example

```python
from gb_retailapi_client.models.search_response_dto import SearchResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResponseDto from a JSON string
search_response_dto_instance = SearchResponseDto.from_json(json)
# print the JSON string representation of the object
print SearchResponseDto.to_json()

# convert the object into a dict
search_response_dto_dict = search_response_dto_instance.to_dict()
# create an instance of SearchResponseDto from a dict
search_response_dto_form_dict = search_response_dto.from_dict(search_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


