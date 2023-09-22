# RuleTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**enable_exact_matching** | **bool** |  | 
**sections** | [**List[RuleTemplateSection]**](RuleTemplateSection.md) |  | 

## Example

```python
from gb_retailapi_client.models.rule_template import RuleTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of RuleTemplate from a JSON string
rule_template_instance = RuleTemplate.from_json(json)
# print the JSON string representation of the object
print RuleTemplate.to_json()

# convert the object into a dict
rule_template_dict = rule_template_instance.to_dict()
# create an instance of RuleTemplate from a dict
rule_template_form_dict = rule_template.from_dict(rule_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


