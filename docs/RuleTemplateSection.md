# RuleTemplateSection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_id** | **int** |  | 
**name** | **str** |  | 
**zone_content** | **str** |  | 
**zone_type** | [**ZoneType**](ZoneType.md) |  | 

## Example

```python
from gb_retailapi_client.models.rule_template_section import RuleTemplateSection

# TODO update the JSON string below
json = "{}"
# create an instance of RuleTemplateSection from a JSON string
rule_template_section_instance = RuleTemplateSection.from_json(json)
# print the JSON string representation of the object
print RuleTemplateSection.to_json()

# convert the object into a dict
rule_template_section_dict = rule_template_section_instance.to_dict()
# create an instance of RuleTemplateSection from a dict
rule_template_section_form_dict = rule_template_section.from_dict(rule_template_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


