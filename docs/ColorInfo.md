# ColorInfo

Product color info.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color_families** | **List[str]** | Product color families (array). | [optional] 
**colors** | **List[str]** | Product color (array). | [optional] 

## Example

```python
from gb_retailapi_client.models.color_info import ColorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ColorInfo from a JSON string
color_info_instance = ColorInfo.from_json(json)
# print the JSON string representation of the object
print ColorInfo.to_json()

# convert the object into a dict
color_info_dict = color_info_instance.to_dict()
# create an instance of ColorInfo from a dict
color_info_form_dict = color_info.from_dict(color_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


