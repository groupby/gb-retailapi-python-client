# BiasDto

Biases the search results to either increase or decrease product relevancy for products that match the given field and content.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | The field the bias refers to. | 
**content** | **str** | The content the field must match for the bias to be applied. | [optional] 
**strength** | [**BiasDtoStrengthDto**](BiasDtoStrengthDto.md) |  | 

## Example

```python
from gb_retailapi_client.models.bias_dto import BiasDto

# TODO update the JSON string below
json = "{}"
# create an instance of BiasDto from a JSON string
bias_dto_instance = BiasDto.from_json(json)
# print the JSON string representation of the object
print BiasDto.to_json()

# convert the object into a dict
bias_dto_dict = bias_dto_instance.to_dict()
# create an instance of BiasDto from a dict
bias_dto_form_dict = bias_dto.from_dict(bias_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


