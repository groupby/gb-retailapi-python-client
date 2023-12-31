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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint, conlist, constr

class Request(BaseModel):
    """
    Object which is represent autocomplete request and encapsulate all passed parameters.   # noqa: E501
    """
    area: constr(strict=True, max_length=80) = Field(..., description="Area i.e. 'Production' Will not be used immediately. This will be useful when we eventually need to support a US area vs a Canada area. But this would require using the custom dataset instead of user-generated.")
    collection: constr(strict=True, max_length=80, min_length=1) = Field(..., description="Name of the collection used to determine the retail backend to use. Usually it is name which is associated with retail project in command center (project configuration).")
    search_items: conint(strict=True, le=20, ge=1) = Field(..., alias="searchItems", description="Completion max suggestions. The maximum allowed max suggestions is 20.")
    query: constr(strict=True, max_length=255, min_length=1) = Field(..., description="String. Required. The query used to generate suggestions. The maximum number of allowed characters is 255.")
    enable_attribute_suggestion: Optional[StrictBool] = Field(None, alias="enableAttributeSuggestion", description="Enable attribute suggestions, by setting the field enableAttributeSuggestion=true in the API request. Then in response, there will be an additional field attributeResults to show direct match results on brands/categories  Note that attribute results directly come from the products we import and Google does not apply any cleaning on them. ")
    extended_suggestions: Optional[StrictBool] = Field(None, alias="extendedSuggestions", description="Optional param which is define if extended suggestions will be returned in autocomplete response or not. Possibly values: true, false, not specified (If not specified default collection setting will be used). ")
    extended_attributes: Optional[conlist(StrictStr, min_items=1)] = Field(None, alias="extendedAttributes", description="    List with extended attributes which are would be returned in autocomplete response.     Requires extendedSuggestions to be enabled using search param or on collection layer. ")
    visitor_id: Optional[constr(strict=True, max_length=128)] = Field(None, alias="visitorId", description="String. Not required field. A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor logs in or out of the website. The field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned. ")
    site: Optional[StrictStr] = Field(None, description="Name of site filter. If not specified, the specified area's default site will be applied if configured in Command Center. To not use default specify empty value i.e.\"\".  If the site doesn't exist then the search will execute without the site filter.")
    __properties = ["area", "collection", "searchItems", "query", "enableAttributeSuggestion", "extendedSuggestions", "extendedAttributes", "visitorId", "site"]

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
    def from_json(cls, json_str: str) -> Request:
        """Create an instance of Request from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if extended_suggestions (nullable) is None
        # and __fields_set__ contains the field
        if self.extended_suggestions is None and "extended_suggestions" in self.__fields_set__:
            _dict['extendedSuggestions'] = None

        # set to None if extended_attributes (nullable) is None
        # and __fields_set__ contains the field
        if self.extended_attributes is None and "extended_attributes" in self.__fields_set__:
            _dict['extendedAttributes'] = None

        # set to None if visitor_id (nullable) is None
        # and __fields_set__ contains the field
        if self.visitor_id is None and "visitor_id" in self.__fields_set__:
            _dict['visitorId'] = None

        # set to None if site (nullable) is None
        # and __fields_set__ contains the field
        if self.site is None and "site" in self.__fields_set__:
            _dict['site'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Request:
        """Create an instance of Request from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Request.parse_obj(obj)

        _obj = Request.parse_obj({
            "area": obj.get("area"),
            "collection": obj.get("collection"),
            "search_items": obj.get("searchItems"),
            "query": obj.get("query"),
            "enable_attribute_suggestion": obj.get("enableAttributeSuggestion"),
            "extended_suggestions": obj.get("extendedSuggestions"),
            "extended_attributes": obj.get("extendedAttributes"),
            "visitor_id": obj.get("visitorId"),
            "site": obj.get("site")
        })
        return _obj


