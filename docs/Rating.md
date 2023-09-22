# Rating

The rating of this product.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rating_count** | **int** | The total number of ratings. This value is independent of the value of histogram.This value must be nonnegative. | [optional] 
**average_rating** | **float** | The average rating of the product. The rating is scaled at 1-5. | [optional] 
**rating_histogram** | **List[int]** | List of rating counts per rating value (index &#x3D; rating - 1). The list is empty if there is no rating. If the list is non-empty, its size is always 5. For example, [41, 14, 13, 47, 303]. It means that the product got 41 ratings with 1 star, 14 ratings with 2 star, and so on. | [optional] 

## Example

```python
from gb_retailapi_client.models.rating import Rating

# TODO update the JSON string below
json = "{}"
# create an instance of Rating from a JSON string
rating_instance = Rating.from_json(json)
# print the JSON string representation of the object
print Rating.to_json()

# convert the object into a dict
rating_dict = rating_instance.to_dict()
# create an instance of Rating from a dict
rating_form_dict = rating.from_dict(rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


