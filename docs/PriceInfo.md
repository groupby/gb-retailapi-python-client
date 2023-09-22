# PriceInfo

Price info representation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | Currency code. | [optional] 
**price** | **float** | Price value. | [optional] 
**original_price** | **float** | Original price value. | [optional] 
**cost** | **float** | Cost | [optional] 
**price_effective_time** | [**PriceInfoPriceEffectiveTime**](PriceInfoPriceEffectiveTime.md) |  | [optional] 
**price_expire_time** | [**PriceInfoPriceExpireTime**](PriceInfoPriceExpireTime.md) |  | [optional] 
**price_range** | [**PriceInfoPriceRange**](PriceInfoPriceRange.md) |  | [optional] 

## Example

```python
from gb_retailapi_client.models.price_info import PriceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PriceInfo from a JSON string
price_info_instance = PriceInfo.from_json(json)
# print the JSON string representation of the object
print PriceInfo.to_json()

# convert the object into a dict
price_info_dict = price_info_instance.to_dict()
# create an instance of PriceInfo from a dict
price_info_form_dict = price_info.from_dict(price_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


