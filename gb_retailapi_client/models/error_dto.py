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
from pydantic import BaseModel, Field, StrictStr

class ErrorDto(BaseModel):
    """
    Error returned by the API.  # noqa: E501
    """
    tracking_id: Optional[StrictStr] = Field(None, alias="trackingId", description="Identifier used for tracking purposes.")
    method: Optional[StrictStr] = Field(None, description="HTTP method of the API call which produced the error.")
    path: Optional[StrictStr] = Field(None, description="HTTP path of the API call which produced the error.")
    message: Optional[StrictStr] = Field(None, description="Error message.")
    __properties = ["trackingId", "method", "path", "message"]

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
    def from_json(cls, json_str: str) -> ErrorDto:
        """Create an instance of ErrorDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ErrorDto:
        """Create an instance of ErrorDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ErrorDto.parse_obj(obj)

        _obj = ErrorDto.parse_obj({
            "tracking_id": obj.get("trackingId"),
            "method": obj.get("method"),
            "path": obj.get("path"),
            "message": obj.get("message")
        })
        return _obj


