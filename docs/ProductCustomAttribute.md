# ProductCustomAttribute

A custom attribute that is not explicitly modeled in product.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **List[str]** | The textual values of this custom attribute. At most 400 values are allowed. Empty values are not allowed. Length limit of 256 characters. Exactly one of text or numbers should be set. | [optional] 
**numbers** | **List[float]** | The numerical values of this custom attribute. At most 400 values are allowed. Exactly one of text or numbers should be set. | [optional] 
**searchable** | **bool** | If true, custom attribute values are searchable by text queries in. search. Only set if type text set. | [optional] 
**indexable** | **bool** | If true, custom attribute values are indexed, so that it can be filtered, faceted or boosted in search. | [optional] 

## Example

```python
from gb_retailapi_client.models.product_custom_attribute import ProductCustomAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCustomAttribute from a JSON string
product_custom_attribute_instance = ProductCustomAttribute.from_json(json)
# print the JSON string representation of the object
print ProductCustomAttribute.to_json()

# convert the object into a dict
product_custom_attribute_dict = product_custom_attribute_instance.to_dict()
# create an instance of ProductCustomAttribute from a dict
product_custom_attribute_form_dict = product_custom_attribute.from_dict(product_custom_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


