# AttributeSuggestion

Object with one single attribute and associated properties.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggestions** | **List[str]** | Suggestion itself. | [optional] 

## Example

```python
from gb_retailapi_client.models.attribute_suggestion import AttributeSuggestion

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeSuggestion from a JSON string
attribute_suggestion_instance = AttributeSuggestion.from_json(json)
# print the JSON string representation of the object
print AttributeSuggestion.to_json()

# convert the object into a dict
attribute_suggestion_dict = attribute_suggestion_instance.to_dict()
# create an instance of AttributeSuggestion from a dict
attribute_suggestion_form_dict = attribute_suggestion.from_dict(attribute_suggestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


