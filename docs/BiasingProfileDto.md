# BiasingProfileDto

Inline biasing profile, which should be applied to the search. Takes priority over biasing profile.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**biases** | [**List[BiasDto]**](BiasDto.md) |  | 

## Example

```python
from gb_retailapi_client.models.biasing_profile_dto import BiasingProfileDto

# TODO update the JSON string below
json = "{}"
# create an instance of BiasingProfileDto from a JSON string
biasing_profile_dto_instance = BiasingProfileDto.from_json(json)
# print the JSON string representation of the object
print BiasingProfileDto.to_json()

# convert the object into a dict
biasing_profile_dto_dict = biasing_profile_dto_instance.to_dict()
# create an instance of BiasingProfileDto from a dict
biasing_profile_dto_form_dict = biasing_profile_dto.from_dict(biasing_profile_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


