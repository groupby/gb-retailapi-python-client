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


from typing import Any, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr

class ValueFilter(BaseModel):
    """
    ValueFilter
    """
    field: StrictStr = Field(..., description="Field the value applies to.")
    value: StrictStr = Field(..., description="Value to filter on.")
    number_value: Union[StrictFloat, StrictInt] = Field(..., alias="numberValue", description="Numeric value to filter on.")
    exclude: StrictBool = Field(..., description="Describing whether the filter is negated or not: color that is NOT red.")
    type: Optional[Any] = Field(..., description="Determine which field we need to use - value if 'TEXTUAL' type or numberValue if 'NUMERIC' type.")
    __properties = ["field", "value", "numberValue", "exclude", "type"]

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
    def from_json(cls, json_str: str) -> ValueFilter:
        """Create an instance of ValueFilter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ValueFilter:
        """Create an instance of ValueFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ValueFilter.parse_obj(obj)

        _obj = ValueFilter.parse_obj({
            "field": obj.get("field"),
            "value": obj.get("value"),
            "number_value": obj.get("numberValue"),
            "exclude": obj.get("exclude"),
            "type": obj.get("type")
        })
        return _obj


