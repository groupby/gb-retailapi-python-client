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



from pydantic import BaseModel, Field
from gb_retailapi_client.models.navigation_dto import NavigationDto
from gb_retailapi_client.models.search_request_dto import SearchRequestDto

class FacetSearchResponseDto(BaseModel):
    """
    Facet search response representation.  # noqa: E501
    """
    original_request: SearchRequestDto = Field(..., alias="originalRequest")
    available_navigation: NavigationDto = Field(..., alias="availableNavigation")
    __properties = ["originalRequest", "availableNavigation"]

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
    def from_json(cls, json_str: str) -> FacetSearchResponseDto:
        """Create an instance of FacetSearchResponseDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of original_request
        if self.original_request:
            _dict['originalRequest'] = self.original_request.to_dict()
        # override the default output from pydantic by calling `to_dict()` of available_navigation
        if self.available_navigation:
            _dict['availableNavigation'] = self.available_navigation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FacetSearchResponseDto:
        """Create an instance of FacetSearchResponseDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FacetSearchResponseDto.parse_obj(obj)

        _obj = FacetSearchResponseDto.parse_obj({
            "original_request": SearchRequestDto.from_dict(obj.get("originalRequest")) if obj.get("originalRequest") is not None else None,
            "available_navigation": NavigationDto.from_dict(obj.get("availableNavigation")) if obj.get("availableNavigation") is not None else None
        })
        return _obj


