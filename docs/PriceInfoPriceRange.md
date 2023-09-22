# PriceInfoPriceRange


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | [**PriceInfoPriceRangePrice**](PriceInfoPriceRangePrice.md) |  | [optional] 
**original_price** | [**PriceInfoPriceRangeOriginalPrice**](PriceInfoPriceRangeOriginalPrice.md) |  | [optional] 

## Example

```python
from gb_retailapi_client.models.price_info_price_range import PriceInfoPriceRange

# TODO update the JSON string below
json = "{}"
# create an instance of PriceInfoPriceRange from a JSON string
price_info_price_range_instance = PriceInfoPriceRange.from_json(json)
# print the JSON string representation of the object
print PriceInfoPriceRange.to_json()

# convert the object into a dict
price_info_price_range_dict = price_info_price_range_instance.to_dict()
# create an instance of PriceInfoPriceRange from a dict
price_info_price_range_form_dict = price_info_price_range.from_dict(price_info_price_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


