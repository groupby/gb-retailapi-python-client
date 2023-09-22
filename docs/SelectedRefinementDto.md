# SelectedRefinementDto

Refinement the shopper has selected for filtering.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**navigation_name** | **str** | The name of the navigation the refinement is for. | 
**type** | [**NavigationTypeDto**](NavigationTypeDto.md) |  | 
**value** | **str** | Value of selected refinement, if type is value. | [optional] 
**low** | **float** | The lowest end or value of the range, if applicable. | [optional] 
**high** | **float** | The highest end or value of the range, if applicable. | [optional] 
**source** | **str** | Field which is indicated that it is dynamic navigation. | [optional] 
**var_or** | **bool** | Navigation multiselect. Indicate that it is possibly to select more than one navigation value due to search request. | [optional] 

## Example

```python
from gb_retailapi_client.models.selected_refinement_dto import SelectedRefinementDto

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedRefinementDto from a JSON string
selected_refinement_dto_instance = SelectedRefinementDto.from_json(json)
# print the JSON string representation of the object
print SelectedRefinementDto.to_json()

# convert the object into a dict
selected_refinement_dto_dict = selected_refinement_dto_instance.to_dict()
# create an instance of SelectedRefinementDto from a dict
selected_refinement_dto_form_dict = selected_refinement_dto.from_dict(selected_refinement_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


