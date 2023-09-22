# ExperimentVariant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**rule_variant** | [**RuleVariant**](RuleVariant.md) |  | 
**variant_trigger_percentage** | **int** |  | 

## Example

```python
from gb_retailapi_client.models.experiment_variant import ExperimentVariant

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentVariant from a JSON string
experiment_variant_instance = ExperimentVariant.from_json(json)
# print the JSON string representation of the object
print ExperimentVariant.to_json()

# convert the object into a dict
experiment_variant_dict = experiment_variant_instance.to_dict()
# create an instance of ExperimentVariant from a dict
experiment_variant_form_dict = experiment_variant.from_dict(experiment_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


