# coding: utf-8

"""
    GroupBy Retail

    GroupBy Retail API

    The version of the OpenAPI document: 0.0
    Contact: ops@groupbyinc.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist

class ProductCustomAttribute(BaseModel):
    """
    A custom attribute that is not explicitly modeled in product.  # noqa: E501
    """
    text: Optional[conlist(StrictStr)] = Field(None, description="The textual values of this custom attribute. At most 400 values are allowed. Empty values are not allowed. Length limit of 256 characters. Exactly one of text or numbers should be set.")
    numbers: Optional[conlist(Union[StrictFloat, StrictInt])] = Field(None, description="The numerical values of this custom attribute. At most 400 values are allowed. Exactly one of text or numbers should be set.")
    searchable: Optional[StrictBool] = Field(None, description="If true, custom attribute values are searchable by text queries in. search. Only set if type text set.")
    indexable: Optional[StrictBool] = Field(None, description="If true, custom attribute values are indexed, so that it can be filtered, faceted or boosted in search.")
    __properties = ["text", "numbers", "searchable", "indexable"]

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
    def from_json(cls, json_str: str) -> ProductCustomAttribute:
        """Create an instance of ProductCustomAttribute from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProductCustomAttribute:
        """Create an instance of ProductCustomAttribute from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProductCustomAttribute.parse_obj(obj)

        _obj = ProductCustomAttribute.parse_obj({
            "text": obj.get("text"),
            "numbers": obj.get("numbers"),
            "searchable": obj.get("searchable"),
            "indexable": obj.get("indexable")
        })
        return _obj

