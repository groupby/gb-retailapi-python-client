# ProductDtoAudience


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genders** | **List[str]** | The genders of the audience. Strongly encouraged to use the standard values: &#39;male&#39;, &#39;female&#39;, &#39;unisex&#39;. At most 5 values are allowed. Length limit of 128 characters. | [optional] 
**age_groups** | **List[str]** | The age groups of the audience. Strongly encouraged to use the standard values: &#39;newborn&#39; (up to 3 months old), &#39;infant&#39; (3-12 months old), &#39;toddler&#39; (1-5 years old), &#39;kids&#39; (5-13 years old), &#39;adult&#39; (typically teens or older). At most 5 values are allowed. Length limit of 128 characters. | [optional] 

## Example

```python
from gb_retailapi_client.models.product_dto_audience import ProductDtoAudience

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDtoAudience from a JSON string
product_dto_audience_instance = ProductDtoAudience.from_json(json)
# print the JSON string representation of the object
print ProductDtoAudience.to_json()

# convert the object into a dict
product_dto_audience_dict = product_dto_audience_instance.to_dict()
# create an instance of ProductDtoAudience from a dict
product_dto_audience_form_dict = product_dto_audience.from_dict(product_dto_audience_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


