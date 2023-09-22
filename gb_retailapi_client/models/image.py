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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class Image(BaseModel):
    """
    Product image  # noqa: E501
    """
    uri: Optional[StrictStr] = Field(None, description="Absolute path to product image.")
    height: Optional[StrictInt] = Field(None, description="Height in pixels")
    width: Optional[StrictInt] = Field(None, description="Width in pixels")
    __properties = ["uri", "height", "width"]

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
    def from_json(cls, json_str: str) -> Image:
        """Create an instance of Image from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Image:
        """Create an instance of Image from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Image.parse_obj(obj)

        _obj = Image.parse_obj({
            "uri": obj.get("uri"),
            "height": obj.get("height"),
            "width": obj.get("width")
        })
        return _obj

