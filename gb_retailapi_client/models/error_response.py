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



from pydantic import BaseModel, Field, StrictStr

class ErrorResponse(BaseModel):
    """
    Error object returned by the API.  # noqa: E501
    """
    tracking_id: StrictStr = Field(..., alias="trackingId", description="Identifier used for tracking purposes.")
    method: StrictStr = Field(..., description="HTTP method of the API call which produced the error.")
    path: StrictStr = Field(..., description="HTTP path of the API call which produced the error.")
    message: StrictStr = Field(..., description="Error message. Ideally human readable string.")
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
    def from_json(cls, json_str: str) -> ErrorResponse:
        """Create an instance of ErrorResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ErrorResponse:
        """Create an instance of ErrorResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ErrorResponse.parse_obj(obj)

        _obj = ErrorResponse.parse_obj({
            "tracking_id": obj.get("trackingId"),
            "method": obj.get("method"),
            "path": obj.get("path"),
            "message": obj.get("message")
        })
        return _obj


