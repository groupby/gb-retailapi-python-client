# TemplateDto

Template to assist the front end application in rendering the UI. Currently only the triggered rule name will be included, or the 'default' template name to indicate no rule was triggered. This is to mainly compatibility with the Searchandiser API and the addition of templates in the future. Template is search agnostic and do not affect search request or result. Templated selected only by triggered rule.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the template. | [optional] 
**rule_name** | **str** | Name of the rule which may have triggered. | [optional] 
**trigger_set** | [**TemplateDtoTriggerSet**](TemplateDtoTriggerSet.md) |  | [optional] 
**zones** | [**List[ZoneDto]**](ZoneDto.md) | Zones for linked template. | [optional] 

## Example

```python
from gb_retailapi_client.models.template_dto import TemplateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDto from a JSON string
template_dto_instance = TemplateDto.from_json(json)
# print the JSON string representation of the object
print TemplateDto.to_json()

# convert the object into a dict
template_dto_dict = template_dto_instance.to_dict()
# create an instance of TemplateDto from a dict
template_dto_form_dict = template_dto.from_dict(template_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


