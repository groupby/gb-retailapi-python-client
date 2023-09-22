# ProductDto

Product representation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Relative path to product in Google Retail system. | [optional] 
**id** | **str** | Product id in Google Retail system. | [optional] 
**type** | **str** | Product type. Possible values: PRIMARY, VARIANT. If the product has variant list and the request specifies the variantIds, requested variants will be the first in the response. | [optional] 
**primary_product_id** | **str** | Product ID that is primary in relation to the current one | [optional] 
**collection_member_ids** | **List[str]** | The of the collection members when product type is COLLECTION | [optional] 
**gtin** | **str** | Global Trade Item Number can be used by a company to uniquely identify all of its trade items.GTIN defines trade items as products or services that are priced, ordered or invoiced at any point in the supply chain. | [optional] 
**categories** | **List[str]** | Product categories (array). | [optional] 
**title** | **str** | Product title. | [optional] 
**brands** | **List[str]** | Product brands. | [optional] 
**description** | **str** | Product description. | [optional] 
**language_code** | **str** | Language of the title/description and other string attributes. Use language tags defined by [BCP 47][https://www.rfc-editor.org/rfc/bcp/bcp47.txt]. For product search this field is in use. It defaults to &#39;en-US&#39; if unset. | [optional] 
**attributes** | [**Dict[str, ProductCustomAttribute]**](ProductCustomAttribute.md) | Highly encouraged. Extra product attributes to be included. For example, for products, this could include the store name, vendor, style, color, etc. These are very strong signals for recommendation model, thus we highly recommend providing the attributes here. Features that can take on one of a limited number of possible values. Two types of features can be set are: Textual features. some examples would be the brand/maker of a product, or country of a customer. Numerical features. Some examples would be the height/weight of a product, or age of a customer.  Max entries count: 200. Length limit of 128 characters. | [optional] 
**tags** | **List[str]** | Product tags (array). | [optional] 
**price_info** | [**ProductDtoPriceInfo**](ProductDtoPriceInfo.md) |  | [optional] 
**rating** | [**ProductDtoRating**](ProductDtoRating.md) |  | [optional] 
**available_time** | [**ProductDtoAvailableTime**](ProductDtoAvailableTime.md) |  | [optional] 
**availability** | **str** | The online availability of the product. Default to IN_STOCK | [optional] 
**available_quantity** | **int** | The available quantity of the item. | [optional] 
**fulfillment_infos** | [**List[FulfillmentInfo]**](FulfillmentInfo.md) | Fulfillment information, such as the store IDs for in-store pickup or region IDs for different shipping methods. | [optional] 
**uri** | **str** | Link to the appropriate product. | [optional] 
**images** | [**List[Image]**](Image.md) | Product Image. | [optional] 
**audience** | [**ProductDtoAudience**](ProductDtoAudience.md) |  | [optional] 
**color_info** | [**ProductDtoColorInfo**](ProductDtoColorInfo.md) |  | [optional] 
**sizes** | **List[str]** | Product sizes (array). | [optional] 
**materials** | **List[str]** | The material of the product. For example, &#39;leather&#39;, &#39;wooden&#39;. A maximum of 20 values are allowed. Length limit of 128 characters | [optional] 
**patterns** | **List[str]** | The pattern or graphic print of the product. For example, &#39;striped&#39;, &#39;polka dot&#39;, &#39;paisley&#39;. A maximum of 20 values are allowed per product. Length limit of 128 characters. | [optional] 
**conditions** | **List[str]** | The condition of the product. Strongly encouraged to use the standardvalues: &#39;new&#39;, &#39;refurbished&#39;, &#39;used&#39;. A maximum of 5 values are allowed per product. Length limit of 128 characters. | [optional] 
**publish_time** | [**ProductDtoPublishTime**](ProductDtoPublishTime.md) |  | [optional] 
**retrievable_fields** | [**ProductDtoRetrievableFields**](ProductDtoRetrievableFields.md) |  | [optional] 
**promotions** | [**List[Promotion]**](Promotion.md) | The promotions applied to the product. A maximum of 10 values are allowed per product. | [optional] 
**variants** | [**List[ProductDto]**](ProductDto.md) | If the product has variant list and the request specifies the variantIds, requested variants will be the first in the response. | [optional] 

## Example

```python
from gb_retailapi_client.models.product_dto import ProductDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDto from a JSON string
product_dto_instance = ProductDto.from_json(json)
# print the JSON string representation of the object
print ProductDto.to_json()

# convert the object into a dict
product_dto_dict = product_dto_instance.to_dict()
# create an instance of ProductDto from a dict
product_dto_form_dict = product_dto.from_dict(product_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


