# PinnedRefinement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**navigation** | **str** |  | 
**refinements** | [**List[Refinement]**](Refinement.md) |  | 

## Example

```python
from gb_retailapi_client.models.pinned_refinement import PinnedRefinement

# TODO update the JSON string below
json = "{}"
# create an instance of PinnedRefinement from a JSON string
pinned_refinement_instance = PinnedRefinement.from_json(json)
# print the JSON string representation of the object
print PinnedRefinement.to_json()

# convert the object into a dict
pinned_refinement_dict = pinned_refinement_instance.to_dict()
# create an instance of PinnedRefinement from a dict
pinned_refinement_form_dict = pinned_refinement.from_dict(pinned_refinement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


