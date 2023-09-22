# RuleConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_in_experiment** | **bool** |  | [optional] 
**id** | **int** |  | 
**name** | **str** |  | 
**area_id** | **int** |  | 
**priority** | **int** |  | 
**enabled** | **bool** |  | 
**active_hours_enabled** | **bool** |  | 
**active_from** | **int** |  | 
**active_to** | **int** |  | 
**trigger_sets** | [**List[TriggerSet]**](TriggerSet.md) |  | 
**biasing_profile_name** | **str** |  | 
**sort** | [**Sort**](Sort.md) |  | 
**included_navigations** | **List[str]** |  | 
**value_filters** | [**List[ValueFilter]**](ValueFilter.md) |  | 
**search_filters** | [**List[SearchFilter]**](SearchFilter.md) |  | 
**range_filters** | [**List[RangeFilter]**](RangeFilter.md) |  | 
**template** | [**RuleTemplate**](RuleTemplate.md) |  | 
**boosted_product_buckets** | [**List[BoostedProductBucket]**](BoostedProductBucket.md) |  | 
**pinned_refinements** | [**List[PinnedRefinement]**](PinnedRefinement.md) |  | 
**message_type** | [**MessageType**](MessageType.md) |  | 
**type** | [**RuleType**](RuleType.md) |  | 
**variants** | [**List[ExperimentVariant]**](ExperimentVariant.md) |  | 

## Example

```python
from gb_retailapi_client.models.rule_configuration import RuleConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of RuleConfiguration from a JSON string
rule_configuration_instance = RuleConfiguration.from_json(json)
# print the JSON string representation of the object
print RuleConfiguration.to_json()

# convert the object into a dict
rule_configuration_dict = rule_configuration_instance.to_dict()
# create an instance of RuleConfiguration from a dict
rule_configuration_form_dict = rule_configuration.from_dict(rule_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


