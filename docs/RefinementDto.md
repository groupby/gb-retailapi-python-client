# RefinementDto

Refinement value or range in the navigation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**NavigationTypeDto**](NavigationTypeDto.md) |  | 
**count** | **int** | Number of products which match this refinement value or range. | [optional] 
**value** | **str** | Value of the refinement. | [optional] 
**low** | **float** | Lower bound of the refinement range. | [optional] 
**high** | **float** | Upper bound  of the refinement range. | [optional] 

## Example

```python
from gb_retailapi_client.models.refinement_dto import RefinementDto

# TODO update the JSON string below
json = "{}"
# create an instance of RefinementDto from a JSON string
refinement_dto_instance = RefinementDto.from_json(json)
# print the JSON string representation of the object
print RefinementDto.to_json()

# convert the object into a dict
refinement_dto_dict = refinement_dto_instance.to_dict()
# create an instance of RefinementDto from a dict
refinement_dto_form_dict = refinement_dto.from_dict(refinement_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


