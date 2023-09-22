# Facet

A facet specification to perform faceted search.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** | Only get facet values that start with the given string prefix. For example, suppose \&quot;categories\&quot; has three values \&quot;Women &gt; Shoe\&quot;, \&quot;Women &gt; Dress\&quot; and \&quot;Men &gt; Shoe\&quot;. If set \&quot;prefixes\&quot; to \&quot;Women\&quot;, the \&quot;categories\&quot; facet will give only \&quot;Women &gt; Shoe\&quot; and \&quot;Women &gt; Dress\&quot;. Only supported on textual fields. Maximum is 10. This field is case-sensitive | [optional] 
**contains** | **str** | Only get facet values that contains the given strings. For example, suppose \&quot;categories\&quot; has three values \&quot;Women &gt; Shoe\&quot;, \&quot;Women &gt; Dress\&quot; and \&quot;Men &gt; Shoe\&quot;. If set \&quot;contains\&quot; to \&quot;Shoe\&quot;, the \&quot;categories\&quot; facet will give only \&quot;Women &gt; Shoe\&quot; and \&quot;Men &gt; Shoe\&quot;. Only supported on textual fields. Maximum is 10. This field is case-sensitive | [optional] 
**display_name** | **str** | Display name of facet | [optional] 
**type** | [**NavigationType**](NavigationType.md) |  | [optional] 
**navigation_name** | **str** | Represents the name of navigation. | [optional] 

## Example

```python
from gb_retailapi_client.models.facet import Facet

# TODO update the JSON string below
json = "{}"
# create an instance of Facet from a JSON string
facet_instance = Facet.from_json(json)
# print the JSON string representation of the object
print Facet.to_json()

# convert the object into a dict
facet_dict = facet_instance.to_dict()
# create an instance of Facet from a dict
facet_form_dict = facet.from_dict(facet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


