# RuleVariant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**biasing_profile_name** | **str** |  | 
**included_navigations** | **List[str]** |  | 
**template** | [**RuleTemplate**](RuleTemplate.md) |  | 
**boosted_product_buckets** | [**List[BoostedProductBucket]**](BoostedProductBucket.md) |  | 
**pinned_refinements** | [**List[PinnedRefinement]**](PinnedRefinement.md) |  | 
**sort** | [**Sort**](Sort.md) |  | 
**value_filters** | [**List[ValueFilter]**](ValueFilter.md) |  | 
**search_filters** | [**List[SearchFilter]**](SearchFilter.md) |  | 
**range_filters** | [**List[RangeFilter]**](RangeFilter.md) |  | 

## Example

```python
from gb_retailapi_client.models.rule_variant import RuleVariant

# TODO update the JSON string below
json = "{}"
# create an instance of RuleVariant from a JSON string
rule_variant_instance = RuleVariant.from_json(json)
# print the JSON string representation of the object
print RuleVariant.to_json()

# convert the object into a dict
rule_variant_dict = rule_variant_instance.to_dict()
# create an instance of RuleVariant from a dict
rule_variant_form_dict = rule_variant.from_dict(rule_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


