# NavigationDto

Navigation available for the shopper to refine the results on.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the field the navigation in on. | [optional] 
**display_name** | **str** | Name of the navigation for display purposes. | [optional] 
**type** | [**NavigationTypeDto**](NavigationTypeDto.md) |  | 
**refinements** | [**List[RefinementDto]**](RefinementDto.md) |  | 
**var_or** | **bool** | Flag if this navigation supports or queries. | [optional] 
**source** | **str** |  | 
**metadata** | [**List[Metadata]**](Metadata.md) |  | 
**place_id** | **str** | Place id for inventory navigations. | 

## Example

```python
from gb_retailapi_client.models.navigation_dto import NavigationDto

# TODO update the JSON string below
json = "{}"
# create an instance of NavigationDto from a JSON string
navigation_dto_instance = NavigationDto.from_json(json)
# print the JSON string representation of the object
print NavigationDto.to_json()

# convert the object into a dict
navigation_dto_dict = navigation_dto_instance.to_dict()
# create an instance of NavigationDto from a dict
navigation_dto_form_dict = navigation_dto.from_dict(navigation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


