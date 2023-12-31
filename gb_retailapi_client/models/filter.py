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
from pydantic import BaseModel, Field, StrictBool, StrictStr, constr

class Filter(BaseModel):
    """
    Filter
    """
    field: constr(strict=True, min_length=1) = Field(...)
    value: Optional[StrictStr] = None
    exclude: StrictBool = Field(...)
    derived_from_product: StrictBool = Field(..., alias="derivedFromProduct")
    __properties = ["field", "value", "exclude", "derivedFromProduct"]

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
    def from_json(cls, json_str: str) -> Filter:
        """Create an instance of Filter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if value (nullable) is None
        # and __fields_set__ contains the field
        if self.value is None and "value" in self.__fields_set__:
            _dict['value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Filter:
        """Create an instance of Filter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Filter.parse_obj(obj)

        _obj = Filter.parse_obj({
            "field": obj.get("field"),
            "value": obj.get("value"),
            "exclude": obj.get("exclude"),
            "derived_from_product": obj.get("derivedFromProduct")
        })
        return _obj


