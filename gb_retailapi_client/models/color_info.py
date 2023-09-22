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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist

class ColorInfo(BaseModel):
    """
    Product color info.  # noqa: E501
    """
    color_families: Optional[conlist(StrictStr)] = Field(None, alias="colorFamilies", description="Product color families (array).")
    colors: Optional[conlist(StrictStr)] = Field(None, description="Product color (array).")
    __properties = ["colorFamilies", "colors"]

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
    def from_json(cls, json_str: str) -> ColorInfo:
        """Create an instance of ColorInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ColorInfo:
        """Create an instance of ColorInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ColorInfo.parse_obj(obj)

        _obj = ColorInfo.parse_obj({
            "color_families": obj.get("colorFamilies"),
            "colors": obj.get("colors")
        })
        return _obj


