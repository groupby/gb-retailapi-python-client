# AdditionalInfo

Object which is contains brands and categories associated with this suggestion.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brands** | **List[str]** |  | 
**categories** | **List[str]** |  | 

## Example

```python
from gb_retailapi_client.models.additional_info import AdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalInfo from a JSON string
additional_info_instance = AdditionalInfo.from_json(json)
# print the JSON string representation of the object
print AdditionalInfo.to_json()

# convert the object into a dict
additional_info_dict = additional_info_instance.to_dict()
# create an instance of AdditionalInfo from a dict
additional_info_form_dict = additional_info.from_dict(additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


