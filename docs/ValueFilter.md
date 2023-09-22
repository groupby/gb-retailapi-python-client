# ValueFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | Field the value applies to. | 
**value** | **str** | Value to filter on. | 
**number_value** | **float** | Numeric value to filter on. | 
**exclude** | **bool** | Describing whether the filter is negated or not: color that is NOT red. | 
**type** | **object** | Determine which field we need to use - value if &#39;TEXTUAL&#39; type or numberValue if &#39;NUMERIC&#39; type. | 

## Example

```python
from gb_retailapi_client.models.value_filter import ValueFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ValueFilter from a JSON string
value_filter_instance = ValueFilter.from_json(json)
# print the JSON string representation of the object
print ValueFilter.to_json()

# convert the object into a dict
value_filter_dict = value_filter_instance.to_dict()
# create an instance of ValueFilter from a dict
value_filter_form_dict = value_filter.from_dict(value_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


