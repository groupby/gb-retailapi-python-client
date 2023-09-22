# PriceInfoPriceExpireTime


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds** | **int** | Timestamp seconds. | [optional] 
**nanos** | **int** | Timestamp nanos. | [optional] 

## Example

```python
from gb_retailapi_client.models.price_info_price_expire_time import PriceInfoPriceExpireTime

# TODO update the JSON string below
json = "{}"
# create an instance of PriceInfoPriceExpireTime from a JSON string
price_info_price_expire_time_instance = PriceInfoPriceExpireTime.from_json(json)
# print the JSON string representation of the object
print PriceInfoPriceExpireTime.to_json()

# convert the object into a dict
price_info_price_expire_time_dict = price_info_price_expire_time_instance.to_dict()
# create an instance of PriceInfoPriceExpireTime from a dict
price_info_price_expire_time_form_dict = price_info_price_expire_time.from_dict(price_info_price_expire_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


