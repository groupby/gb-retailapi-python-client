# ProductDtoAvailableTime


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds** | **int** | Timestamp seconds. | [optional] 
**nanos** | **int** | Timestamp nanos. | [optional] 

## Example

```python
from gb_retailapi_client.models.product_dto_available_time import ProductDtoAvailableTime

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDtoAvailableTime from a JSON string
product_dto_available_time_instance = ProductDtoAvailableTime.from_json(json)
# print the JSON string representation of the object
print ProductDtoAvailableTime.to_json()

# convert the object into a dict
product_dto_available_time_dict = product_dto_available_time_instance.to_dict()
# create an instance of ProductDtoAvailableTime from a dict
product_dto_available_time_form_dict = product_dto_available_time.from_dict(product_dto_available_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


