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


from typing import Optional
from pydantic import BaseModel, Field
from gb_retailapi_client.models.price_info_price_range_original_price import PriceInfoPriceRangeOriginalPrice
from gb_retailapi_client.models.price_info_price_range_price import PriceInfoPriceRangePrice

class PriceInfoPriceRange(BaseModel):
    """
    PriceInfoPriceRange
    """
    price: Optional[PriceInfoPriceRangePrice] = None
    original_price: Optional[PriceInfoPriceRangeOriginalPrice] = Field(None, alias="originalPrice")
    __properties = ["price", "originalPrice"]

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
    def from_json(cls, json_str: str) -> PriceInfoPriceRange:
        """Create an instance of PriceInfoPriceRange from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['price'] = self.price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of original_price
        if self.original_price:
            _dict['originalPrice'] = self.original_price.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PriceInfoPriceRange:
        """Create an instance of PriceInfoPriceRange from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PriceInfoPriceRange.parse_obj(obj)

        _obj = PriceInfoPriceRange.parse_obj({
            "price": PriceInfoPriceRangePrice.from_dict(obj.get("price")) if obj.get("price") is not None else None,
            "original_price": PriceInfoPriceRangeOriginalPrice.from_dict(obj.get("originalPrice")) if obj.get("originalPrice") is not None else None
        })
        return _obj


