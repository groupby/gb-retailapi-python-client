# Experiment

Information about Rule based Experiment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment_id** | **str** | Experiment id. | [optional] 
**experiment_variant** | **str** | Experiment variant. | [optional] 

## Example

```python
from gb_retailapi_client.models.experiment import Experiment

# TODO update the JSON string below
json = "{}"
# create an instance of Experiment from a JSON string
experiment_instance = Experiment.from_json(json)
# print the JSON string representation of the object
print Experiment.to_json()

# convert the object into a dict
experiment_dict = experiment_instance.to_dict()
# create an instance of Experiment from a dict
experiment_form_dict = experiment.from_dict(experiment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


