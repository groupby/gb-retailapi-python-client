# ProductDtoColorInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color_families** | **List[str]** | Product color families (array). | [optional] 
**colors** | **List[str]** | Product color (array). | [optional] 

## Example

```python
from gb_retailapi_client.models.product_dto_color_info import ProductDtoColorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDtoColorInfo from a JSON string
product_dto_color_info_instance = ProductDtoColorInfo.from_json(json)
# print the JSON string representation of the object
print ProductDtoColorInfo.to_json()

# convert the object into a dict
product_dto_color_info_dict = product_dto_color_info_instance.to_dict()
# create an instance of ProductDtoColorInfo from a dict
product_dto_color_info_form_dict = product_dto_color_info.from_dict(product_dto_color_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


