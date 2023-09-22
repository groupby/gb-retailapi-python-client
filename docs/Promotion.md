# Promotion

The promotions applied to the product. A maximum of 10 values are allowed per product.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promotion_id** | **str** | ID of the promotion. For example, &#39;free gift&#39;. Length limit of 128 characters. | [optional] 

## Example

```python
from gb_retailapi_client.models.promotion import Promotion

# TODO update the JSON string below
json = "{}"
# create an instance of Promotion from a JSON string
promotion_instance = Promotion.from_json(json)
# print the JSON string representation of the object
print Promotion.to_json()

# convert the object into a dict
promotion_dict = promotion_instance.to_dict()
# create an instance of Promotion from a dict
promotion_form_dict = promotion.from_dict(promotion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


