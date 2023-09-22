# SelectedRefinementTrigger


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** |  | 
**value** | **str** |  | 
**range** | [**Range**](Range.md) |  | 
**type** | [**SelectedRefinementTriggerType**](SelectedRefinementTriggerType.md) |  | 

## Example

```python
from gb_retailapi_client.models.selected_refinement_trigger import SelectedRefinementTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedRefinementTrigger from a JSON string
selected_refinement_trigger_instance = SelectedRefinementTrigger.from_json(json)
# print the JSON string representation of the object
print SelectedRefinementTrigger.to_json()

# convert the object into a dict
selected_refinement_trigger_dict = selected_refinement_trigger_instance.to_dict()
# create an instance of SelectedRefinementTrigger from a dict
selected_refinement_trigger_form_dict = selected_refinement_trigger.from_dict(selected_refinement_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


