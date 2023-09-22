# ProductDtoRetrievableFields


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paths** | **List[str]** | Paths for retrievable fields (array). | [optional] 

## Example

```python
from gb_retailapi_client.models.product_dto_retrievable_fields import ProductDtoRetrievableFields

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDtoRetrievableFields from a JSON string
product_dto_retrievable_fields_instance = ProductDtoRetrievableFields.from_json(json)
# print the JSON string representation of the object
print ProductDtoRetrievableFields.to_json()

# convert the object into a dict
product_dto_retrievable_fields_dict = product_dto_retrievable_fields_instance.to_dict()
# create an instance of ProductDtoRetrievableFields from a dict
product_dto_retrievable_fields_form_dict = product_dto_retrievable_fields.from_dict(product_dto_retrievable_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


