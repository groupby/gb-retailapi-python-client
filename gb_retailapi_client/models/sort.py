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


from typing import Any, Optional
from pydantic import BaseModel, Field, StrictStr

class Sort(BaseModel):
    """
    Sort
    """
    field: StrictStr = Field(..., description="Field the order will be applied to.")
    order: Optional[Any] = Field(..., description="OrderDto the products will appear in.")
    __properties = ["field", "order"]

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
    def from_json(cls, json_str: str) -> Sort:
        """Create an instance of Sort from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if order (nullable) is None
        # and __fields_set__ contains the field
        if self.order is None and "order" in self.__fields_set__:
            _dict['order'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Sort:
        """Create an instance of Sort from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Sort.parse_obj(obj)

        _obj = Sort.parse_obj({
            "field": obj.get("field"),
            "order": obj.get("order")
        })
        return _obj


