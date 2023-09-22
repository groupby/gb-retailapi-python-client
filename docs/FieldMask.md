# FieldMask

Retrievable fields.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paths** | **List[str]** | Paths for retrievable fields (array). | [optional] 

## Example

```python
from gb_retailapi_client.models.field_mask import FieldMask

# TODO update the JSON string below
json = "{}"
# create an instance of FieldMask from a JSON string
field_mask_instance = FieldMask.from_json(json)
# print the JSON string representation of the object
print FieldMask.to_json()

# convert the object into a dict
field_mask_dict = field_mask_instance.to_dict()
# create an instance of FieldMask from a dict
field_mask_form_dict = field_mask.from_dict(field_mask_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


