# FulfillmentInfo

Fulfillment information, such as the store IDs for in-store pickup or region IDs for different shipping methods.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Fulfillment type. Place where product fulfilled. | [optional] 
**place_ids** | **List[str]** | Place ids where product fulfilled (array). | [optional] 

## Example

```python
from gb_retailapi_client.models.fulfillment_info import FulfillmentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FulfillmentInfo from a JSON string
fulfillment_info_instance = FulfillmentInfo.from_json(json)
# print the JSON string representation of the object
print FulfillmentInfo.to_json()

# convert the object into a dict
fulfillment_info_dict = fulfillment_info_instance.to_dict()
# create an instance of FulfillmentInfo from a dict
fulfillment_info_form_dict = fulfillment_info.from_dict(fulfillment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


