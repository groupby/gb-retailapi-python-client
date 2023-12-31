# coding: utf-8

"""
    GroupBy Retail

    GroupBy Retail API

    The version of the OpenAPI document: 0.0.0
    Contact: ops@groupbyinc.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from gb_retailapi_client.models.fulfillment_info import FulfillmentInfo
from gb_retailapi_client.models.image import Image
from gb_retailapi_client.models.product_custom_attribute import ProductCustomAttribute
from gb_retailapi_client.models.product_dto_audience import ProductDtoAudience
from gb_retailapi_client.models.product_dto_available_time import ProductDtoAvailableTime
from gb_retailapi_client.models.product_dto_color_info import ProductDtoColorInfo
from gb_retailapi_client.models.product_dto_price_info import ProductDtoPriceInfo
from gb_retailapi_client.models.product_dto_publish_time import ProductDtoPublishTime
from gb_retailapi_client.models.product_dto_rating import ProductDtoRating
from gb_retailapi_client.models.product_dto_retrievable_fields import ProductDtoRetrievableFields
from gb_retailapi_client.models.promotion import Promotion

class ProductDto(BaseModel):
    """
    Product representation.  # noqa: E501
    """
    name: Optional[StrictStr] = Field(None, description="Relative path to product in Google Retail system.")
    id: Optional[StrictStr] = Field(None, description="Product id in Google Retail system.")
    type: Optional[StrictStr] = Field(None, description="Product type. Possible values: PRIMARY, VARIANT. If the product has variant list and the request specifies the variantIds, requested variants will be the first in the response.")
    primary_product_id: Optional[StrictStr] = Field(None, alias="primaryProductId", description="Product ID that is primary in relation to the current one")
    collection_member_ids: Optional[conlist(StrictStr)] = Field(None, alias="collectionMemberIds", description="The of the collection members when product type is COLLECTION")
    gtin: Optional[StrictStr] = Field(None, description="Global Trade Item Number can be used by a company to uniquely identify all of its trade items.GTIN defines trade items as products or services that are priced, ordered or invoiced at any point in the supply chain.")
    categories: Optional[conlist(StrictStr)] = Field(None, description="Product categories (array).")
    title: Optional[StrictStr] = Field(None, description="Product title.")
    brands: Optional[conlist(StrictStr)] = Field(None, description="Product brands.")
    description: Optional[StrictStr] = Field(None, description="Product description.")
    language_code: Optional[StrictStr] = Field(None, alias="languageCode", description="Language of the title/description and other string attributes. Use language tags defined by [BCP 47][https://www.rfc-editor.org/rfc/bcp/bcp47.txt]. For product search this field is in use. It defaults to 'en-US' if unset.")
    attributes: Optional[Dict[str, ProductCustomAttribute]] = Field(None, description="Highly encouraged. Extra product attributes to be included. For example, for products, this could include the store name, vendor, style, color, etc. These are very strong signals for recommendation model, thus we highly recommend providing the attributes here. Features that can take on one of a limited number of possible values. Two types of features can be set are: Textual features. some examples would be the brand/maker of a product, or country of a customer. Numerical features. Some examples would be the height/weight of a product, or age of a customer.  Max entries count: 200. Length limit of 128 characters.")
    tags: Optional[conlist(StrictStr)] = Field(None, description="Product tags (array).")
    price_info: Optional[ProductDtoPriceInfo] = Field(None, alias="priceInfo")
    rating: Optional[ProductDtoRating] = None
    available_time: Optional[ProductDtoAvailableTime] = Field(None, alias="availableTime")
    availability: Optional[StrictStr] = Field(None, description="The online availability of the product. Default to IN_STOCK")
    available_quantity: Optional[StrictInt] = Field(None, alias="availableQuantity", description="The available quantity of the item.")
    fulfillment_infos: Optional[conlist(FulfillmentInfo)] = Field(None, alias="fulfillmentInfos", description="Fulfillment information, such as the store IDs for in-store pickup or region IDs for different shipping methods.")
    uri: Optional[StrictStr] = Field(None, description="Link to the appropriate product.")
    images: Optional[conlist(Image)] = Field(None, description="Product Image.")
    audience: Optional[ProductDtoAudience] = None
    color_info: Optional[ProductDtoColorInfo] = Field(None, alias="colorInfo")
    sizes: Optional[conlist(StrictStr)] = Field(None, description="Product sizes (array).")
    materials: Optional[conlist(StrictStr)] = Field(None, description="The material of the product. For example, 'leather', 'wooden'. A maximum of 20 values are allowed. Length limit of 128 characters")
    patterns: Optional[conlist(StrictStr)] = Field(None, description="The pattern or graphic print of the product. For example, 'striped', 'polka dot', 'paisley'. A maximum of 20 values are allowed per product. Length limit of 128 characters.")
    conditions: Optional[conlist(StrictStr)] = Field(None, description="The condition of the product. Strongly encouraged to use the standardvalues: 'new', 'refurbished', 'used'. A maximum of 5 values are allowed per product. Length limit of 128 characters.")
    publish_time: Optional[ProductDtoPublishTime] = Field(None, alias="publishTime")
    retrievable_fields: Optional[ProductDtoRetrievableFields] = Field(None, alias="retrievableFields")
    promotions: Optional[conlist(Promotion)] = Field(None, description="The promotions applied to the product. A maximum of 10 values are allowed per product.")
    variants: Optional[conlist(ProductDto)] = Field(None, description="If the product has variant list and the request specifies the variantIds, requested variants will be the first in the response.")
    __properties = ["name", "id", "type", "primaryProductId", "collectionMemberIds", "gtin", "categories", "title", "brands", "description", "languageCode", "attributes", "tags", "priceInfo", "rating", "availableTime", "availability", "availableQuantity", "fulfillmentInfos", "uri", "images", "audience", "colorInfo", "sizes", "materials", "patterns", "conditions", "publishTime", "retrievableFields", "promotions", "variants"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ProductDto:
        """Create an instance of ProductDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in attributes (dict)
        _field_dict = {}
        if self.attributes:
            for _key in self.attributes:
                if self.attributes[_key]:
                    _field_dict[_key] = self.attributes[_key].to_dict()
            _dict['attributes'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of price_info
        if self.price_info:
            _dict['priceInfo'] = self.price_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rating
        if self.rating:
            _dict['rating'] = self.rating.to_dict()
        # override the default output from pydantic by calling `to_dict()` of available_time
        if self.available_time:
            _dict['availableTime'] = self.available_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in fulfillment_infos (list)
        _items = []
        if self.fulfillment_infos:
            for _item in self.fulfillment_infos:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fulfillmentInfos'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item in self.images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of audience
        if self.audience:
            _dict['audience'] = self.audience.to_dict()
        # override the default output from pydantic by calling `to_dict()` of color_info
        if self.color_info:
            _dict['colorInfo'] = self.color_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of publish_time
        if self.publish_time:
            _dict['publishTime'] = self.publish_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of retrievable_fields
        if self.retrievable_fields:
            _dict['retrievableFields'] = self.retrievable_fields.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in promotions (list)
        _items = []
        if self.promotions:
            for _item in self.promotions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['promotions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in variants (list)
        _items = []
        if self.variants:
            for _item in self.variants:
                if _item:
                    _items.append(_item.to_dict())
            _dict['variants'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProductDto:
        """Create an instance of ProductDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProductDto.parse_obj(obj)

        _obj = ProductDto.parse_obj({
            "name": obj.get("name"),
            "id": obj.get("id"),
            "type": obj.get("type"),
            "primary_product_id": obj.get("primaryProductId"),
            "collection_member_ids": obj.get("collectionMemberIds"),
            "gtin": obj.get("gtin"),
            "categories": obj.get("categories"),
            "title": obj.get("title"),
            "brands": obj.get("brands"),
            "description": obj.get("description"),
            "language_code": obj.get("languageCode"),
            "attributes": dict(
                (_k, ProductCustomAttribute.from_dict(_v))
                for _k, _v in obj.get("attributes").items()
            )
            if obj.get("attributes") is not None
            else None,
            "tags": obj.get("tags"),
            "price_info": ProductDtoPriceInfo.from_dict(obj.get("priceInfo")) if obj.get("priceInfo") is not None else None,
            "rating": ProductDtoRating.from_dict(obj.get("rating")) if obj.get("rating") is not None else None,
            "available_time": ProductDtoAvailableTime.from_dict(obj.get("availableTime")) if obj.get("availableTime") is not None else None,
            "availability": obj.get("availability"),
            "available_quantity": obj.get("availableQuantity"),
            "fulfillment_infos": [FulfillmentInfo.from_dict(_item) for _item in obj.get("fulfillmentInfos")] if obj.get("fulfillmentInfos") is not None else None,
            "uri": obj.get("uri"),
            "images": [Image.from_dict(_item) for _item in obj.get("images")] if obj.get("images") is not None else None,
            "audience": ProductDtoAudience.from_dict(obj.get("audience")) if obj.get("audience") is not None else None,
            "color_info": ProductDtoColorInfo.from_dict(obj.get("colorInfo")) if obj.get("colorInfo") is not None else None,
            "sizes": obj.get("sizes"),
            "materials": obj.get("materials"),
            "patterns": obj.get("patterns"),
            "conditions": obj.get("conditions"),
            "publish_time": ProductDtoPublishTime.from_dict(obj.get("publishTime")) if obj.get("publishTime") is not None else None,
            "retrievable_fields": ProductDtoRetrievableFields.from_dict(obj.get("retrievableFields")) if obj.get("retrievableFields") is not None else None,
            "promotions": [Promotion.from_dict(_item) for _item in obj.get("promotions")] if obj.get("promotions") is not None else None,
            "variants": [ProductDto.from_dict(_item) for _item in obj.get("variants")] if obj.get("variants") is not None else None
        })
        return _obj

ProductDto.update_forward_refs()

