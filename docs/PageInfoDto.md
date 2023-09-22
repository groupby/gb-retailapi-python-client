# PageInfoDto

Information regarding where the page of results starts and ends.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_start** | **int** | Where in the list of products the page begins. | [optional] 
**record_end** | **int** | Where in the list of products the page ends. | [optional] 

## Example

```python
from gb_retailapi_client.models.page_info_dto import PageInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of PageInfoDto from a JSON string
page_info_dto_instance = PageInfoDto.from_json(json)
# print the JSON string representation of the object
print PageInfoDto.to_json()

# convert the object into a dict
page_info_dto_dict = page_info_dto_instance.to_dict()
# create an instance of PageInfoDto from a dict
page_info_dto_form_dict = page_info_dto.from_dict(page_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


