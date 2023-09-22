# RecordDto

Information regarding a product in the proprietary Group By API format.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the record as an MD5 hash. | [optional] 
**u** | **str** | Logical URL of the record. | [optional] 
**t** | **str** | Title of the record. | [optional] 
**collection** | **str** | Collection the record was queried from or resides. | [optional] 
**all_meta** | **Dict[str, object]** | All other metadata, read fields, the record has. | [optional] 

## Example

```python
from gb_retailapi_client.models.record_dto import RecordDto

# TODO update the JSON string below
json = "{}"
# create an instance of RecordDto from a JSON string
record_dto_instance = RecordDto.from_json(json)
# print the JSON string representation of the object
print RecordDto.to_json()

# convert the object into a dict
record_dto_dict = record_dto_instance.to_dict()
# create an instance of RecordDto from a dict
record_dto_form_dict = record_dto.from_dict(record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


