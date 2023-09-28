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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class SearchMetadataDto(BaseModel):
    """
    Metadata relating to the search results, or how they were generated.  # noqa: E501
    """
    search_attribution_token: Optional[StrictStr] = Field(None, alias="searchAttributionToken", description="Token to assist beacon collectors in correlating searches to user events.")
    cached: Optional[StrictBool] = Field(None, description="Were the search results from a previous call.")
    total_time: Optional[StrictInt] = Field(None, alias="totalTime", description="Total time spent performing the Google search in milliseconds.")
    __properties = ["searchAttributionToken", "cached", "totalTime"]

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
    def from_json(cls, json_str: str) -> SearchMetadataDto:
        """Create an instance of SearchMetadataDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if search_attribution_token (nullable) is None
        # and __fields_set__ contains the field
        if self.search_attribution_token is None and "search_attribution_token" in self.__fields_set__:
            _dict['searchAttributionToken'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SearchMetadataDto:
        """Create an instance of SearchMetadataDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SearchMetadataDto.parse_obj(obj)

        _obj = SearchMetadataDto.parse_obj({
            "search_attribution_token": obj.get("searchAttributionToken"),
            "cached": obj.get("cached"),
            "total_time": obj.get("totalTime")
        })
        return _obj


