# ProductDtoPriceInfo


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
from gb_retailapi_client.models.product_dto_price_info import ProductDtoPriceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDtoPriceInfo from a JSON string
product_dto_price_info_instance = ProductDtoPriceInfo.from_json(json)
# print the JSON string representation of the object
print ProductDtoPriceInfo.to_json()

# convert the object into a dict
product_dto_price_info_dict = product_dto_price_info_instance.to_dict()
# create an instance of ProductDtoPriceInfo from a dict
product_dto_price_info_form_dict = product_dto_price_info.from_dict(product_dto_price_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


