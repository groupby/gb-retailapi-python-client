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

class Stats(BaseModel):
    """
    Object with base response information. Contains count of returned suggestions and time spent to handle the request.  # noqa: E501
    """
    search_count: Optional[StrictInt] = Field(None, alias="searchCount", description="Count of suggested sentences in response.")
    autocomplete_response: Optional[StrictInt] = Field(None, alias="autocompleteResponse", description="Time in milliseconds taken by autocomplete service to handle request and send response.")
    extended_attributes_count: Optional[StrictInt] = Field(None, alias="extendedAttributesCount", description="Count of extended attributes in autocomplete response.")
    extended_attributes_response: Optional[StrictInt] = Field(None, alias="extendedAttributesResponse", description="Time in milliseconds taken by application to enrich response with extended attributes.")
    __properties = ["searchCount", "autocompleteResponse", "extendedAttributesCount", "extendedAttributesResponse"]

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
    def from_json(cls, json_str: str) -> Stats:
        """Create an instance of Stats from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Stats:
        """Create an instance of Stats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Stats.parse_obj(obj)

        _obj = Stats.parse_obj({
            "search_count": obj.get("searchCount"),
            "autocomplete_response": obj.get("autocompleteResponse"),
            "extended_attributes_count": obj.get("extendedAttributesCount"),
            "extended_attributes_response": obj.get("extendedAttributesResponse")
        })
        return _obj


