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
from gb_retailapi_client.models.bias_dto_strength_dto import BiasDtoStrengthDto

class BiasDto(BaseModel):
    """
    Biases the search results to either increase or decrease product relevancy for products that match the given field and content.  # noqa: E501
    """
    field: StrictStr = Field(..., description="The field the bias refers to.")
    content: Optional[StrictStr] = Field(None, description="The content the field must match for the bias to be applied.")
    strength: BiasDtoStrengthDto = Field(...)
    __properties = ["field", "content", "strength"]

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
    def from_json(cls, json_str: str) -> BiasDto:
        """Create an instance of BiasDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if content (nullable) is None
        # and __fields_set__ contains the field
        if self.content is None and "content" in self.__fields_set__:
            _dict['content'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BiasDto:
        """Create an instance of BiasDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BiasDto.parse_obj(obj)

        _obj = BiasDto.parse_obj({
            "field": obj.get("field"),
            "content": obj.get("content"),
            "strength": obj.get("strength")
        })
        return _obj


