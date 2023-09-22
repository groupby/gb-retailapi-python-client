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
from pydantic import BaseModel, Field, conint

class PageInfoDto(BaseModel):
    """
    Information regarding where the page of results starts and ends.  # noqa: E501
    """
    record_start: Optional[conint(strict=True, ge=0)] = Field(None, alias="recordStart", description="Where in the list of products the page begins.")
    record_end: Optional[conint(strict=True, ge=1)] = Field(None, alias="recordEnd", description="Where in the list of products the page ends.")
    __properties = ["recordStart", "recordEnd"]

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
    def from_json(cls, json_str: str) -> PageInfoDto:
        """Create an instance of PageInfoDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PageInfoDto:
        """Create an instance of PageInfoDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PageInfoDto.parse_obj(obj)

        _obj = PageInfoDto.parse_obj({
            "record_start": obj.get("recordStart"),
            "record_end": obj.get("recordEnd")
        })
        return _obj


