# BoostedProductBucket


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | **List[str]** |  | 

## Example

```python
from gb_retailapi_client.models.boosted_product_bucket import BoostedProductBucket

# TODO update the JSON string below
json = "{}"
# create an instance of BoostedProductBucket from a JSON string
boosted_product_bucket_instance = BoostedProductBucket.from_json(json)
# print the JSON string representation of the object
print BoostedProductBucket.to_json()

# convert the object into a dict
boosted_product_bucket_dict = boosted_product_bucket_instance.to_dict()
# create an instance of BoostedProductBucket from a dict
boosted_product_bucket_form_dict = boosted_product_bucket.from_dict(boosted_product_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


