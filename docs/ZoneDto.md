# ZoneDto

UI zones, that may contain code snippets, sub-searches and etc.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for the zone, ideally human-readable. | [optional] 
**type** | [**ZoneDtoType**](ZoneDtoType.md) |  | [optional] 
**content** | **str** | Zone content - it is can be any data, HTML - code, usual text or etc | [optional] 
**rich_content** | **str** | Zone content - it is can be any data, HTML - code, usual text or etc | [optional] 

## Example

```python
from gb_retailapi_client.models.zone_dto import ZoneDto

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneDto from a JSON string
zone_dto_instance = ZoneDto.from_json(json)
# print the JSON string representation of the object
print ZoneDto.to_json()

# convert the object into a dict
zone_dto_dict = zone_dto_instance.to_dict()
# create an instance of ZoneDto from a dict
zone_dto_form_dict = zone_dto.from_dict(zone_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


