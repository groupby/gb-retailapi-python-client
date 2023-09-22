# PriceInfoPriceRangeOriginalPrice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimum** | **float** | Inclusive lower bound. The lower bound of the interval. If neither of the min fields (minimum or exclusiveMinimum) are set, then the lower bound is negative infinity. This field must be not larger than maximum or exclusiveMaximum. | [optional] 
**exclusive_minimum** | **float** | Exclusive lower bound. The lower bound of the interval. If neither of the min fields (minimum or exclusiveMinimum) are set, then the lower bound is negative infinity. This field must be not larger than maximum or exclusiveMaximum. | [optional] 
**maximum** | **float** | Inclusive upper bound. The upper bound of the interval. If neither of the max fields are set, then the upper bound is positive infinity. This field must be not smaller than minimum or exclusiveMinimum. | [optional] 
**exclusive_maximum** | **float** | Exclusive upper bound. The upper bound of the interval. If neither of the max fields are set, then the upper bound is positive infinity. This field must be not smaller than minimum or exclusiveMinimum. | [optional] 

## Example

```python
from gb_retailapi_client.models.price_info_price_range_original_price import PriceInfoPriceRangeOriginalPrice

# TODO update the JSON string below
json = "{}"
# create an instance of PriceInfoPriceRangeOriginalPrice from a JSON string
price_info_price_range_original_price_instance = PriceInfoPriceRangeOriginalPrice.from_json(json)
# print the JSON string representation of the object
print PriceInfoPriceRangeOriginalPrice.to_json()

# convert the object into a dict
price_info_price_range_original_price_dict = price_info_price_range_original_price_instance.to_dict()
# create an instance of PriceInfoPriceRangeOriginalPrice from a dict
price_info_price_range_original_price_form_dict = price_info_price_range_original_price.from_dict(price_info_price_range_original_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


