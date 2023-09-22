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
from pydantic import BaseModel, Field, StrictInt

class PriceInfoPriceExpireTime(BaseModel):
    """
    PriceInfoPriceExpireTime
    """
    seconds: Optional[StrictInt] = Field(None, description="Timestamp seconds.")
    nanos: Optional[StrictInt] = Field(None, description="Timestamp nanos.")
    __properties = ["seconds", "nanos"]

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
    def from_json(cls, json_str: str) -> PriceInfoPriceExpireTime:
        """Create an instance of PriceInfoPriceExpireTime from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PriceInfoPriceExpireTime:
        """Create an instance of PriceInfoPriceExpireTime from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PriceInfoPriceExpireTime.parse_obj(obj)

        _obj = PriceInfoPriceExpireTime.parse_obj({
            "seconds": obj.get("seconds"),
            "nanos": obj.get("nanos")
        })
        return _obj


