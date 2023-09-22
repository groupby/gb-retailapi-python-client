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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from gb_retailapi_client.models.navigation_type_dto import NavigationTypeDto

class RefinementDto(BaseModel):
    """
    Refinement value or range in the navigation.  # noqa: E501
    """
    type: NavigationTypeDto = Field(...)
    count: Optional[StrictInt] = Field(None, description="Number of products which match this refinement value or range.")
    value: Optional[StrictStr] = Field(None, description="Value of the refinement.")
    low: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Lower bound of the refinement range.")
    high: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Upper bound  of the refinement range.")
    __properties = ["type", "count", "value", "low", "high"]

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
    def from_json(cls, json_str: str) -> RefinementDto:
        """Create an instance of RefinementDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RefinementDto:
        """Create an instance of RefinementDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RefinementDto.parse_obj(obj)

        _obj = RefinementDto.parse_obj({
            "type": obj.get("type"),
            "count": obj.get("count"),
            "value": obj.get("value"),
            "low": obj.get("low"),
            "high": obj.get("high")
        })
        return _obj

