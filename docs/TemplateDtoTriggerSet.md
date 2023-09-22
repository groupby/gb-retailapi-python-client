# TemplateDtoTriggerSet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_pattern_triggers** | [**List[QueryPatternTrigger]**](QueryPatternTrigger.md) | Query pattern triggers. | 
**selected_refinement_triggers** | [**List[SelectedRefinementTrigger]**](SelectedRefinementTrigger.md) | Selected refinement triggers. | 
**custom_parameter_triggers** | [**List[CustomParameterTrigger]**](CustomParameterTrigger.md) | Custom parameter triggers. | 

## Example

```python
from gb_retailapi_client.models.template_dto_trigger_set import TemplateDtoTriggerSet

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDtoTriggerSet from a JSON string
template_dto_trigger_set_instance = TemplateDtoTriggerSet.from_json(json)
# print the JSON string representation of the object
print TemplateDtoTriggerSet.to_json()

# convert the object into a dict
template_dto_trigger_set_dict = template_dto_trigger_set_instance.to_dict()
# create an instance of TemplateDtoTriggerSet from a dict
template_dto_trigger_set_form_dict = template_dto_trigger_set.from_dict(template_dto_trigger_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


