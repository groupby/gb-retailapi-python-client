# SortDto

Order the returned products should appear on the page.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | Field the order will be applied to. | 
**order** | [**SortDtoOrderDto**](SortDtoOrderDto.md) |  | 

## Example

```python
from gb_retailapi_client.models.sort_dto import SortDto

# TODO update the JSON string below
json = "{}"
# create an instance of SortDto from a JSON string
sort_dto_instance = SortDto.from_json(json)
# print the JSON string representation of the object
print SortDto.to_json()

# convert the object into a dict
sort_dto_dict = sort_dto_instance.to_dict()
# create an instance of SortDto from a dict
sort_dto_form_dict = sort_dto.from_dict(sort_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


