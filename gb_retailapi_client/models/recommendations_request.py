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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, constr
from gb_retailapi_client.models.filter import Filter

class RecommendationsRequest(BaseModel):
    """
    Object to wrap all recommendation request configs.  # noqa: E501
    """
    collection: constr(strict=True, max_length=80, min_length=1) = Field(...)
    visitor_id: Optional[constr(strict=True, max_length=128)] = Field(None, alias="visitorId")
    limit: Optional[StrictStr] = None
    page_size: Optional[StrictStr] = Field(None, alias="pageSize")
    event_type: Optional[StrictStr] = Field(None, alias="eventType")
    login_id: Optional[StrictStr] = Field(None, alias="loginId")
    product_id: Optional[conlist(StrictStr)] = Field(None, alias="productID")
    fields: Optional[conlist(StrictStr)] = None
    filters: Optional[conlist(Filter)] = None
    raw_filter: Optional[StrictStr] = Field(None, alias="rawFilter")
    placement: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    strict_filtering: Optional[StrictBool] = Field(None, alias="strictFiltering", description="The default is true. If strictFiltering true only products that are within the scope of the filter specified. If false, relax the filtering so that the response may contain other products that are outside the scope of the filtering.")
    __properties = ["collection", "visitorId", "limit", "pageSize", "eventType", "loginId", "productID", "fields", "filters", "rawFilter", "placement", "name", "strictFiltering"]

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
    def from_json(cls, json_str: str) -> RecommendationsRequest:
        """Create an instance of RecommendationsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in filters (list)
        _items = []
        if self.filters:
            for _item in self.filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['filters'] = _items
        # set to None if visitor_id (nullable) is None
        # and __fields_set__ contains the field
        if self.visitor_id is None and "visitor_id" in self.__fields_set__:
            _dict['visitorId'] = None

        # set to None if limit (nullable) is None
        # and __fields_set__ contains the field
        if self.limit is None and "limit" in self.__fields_set__:
            _dict['limit'] = None

        # set to None if page_size (nullable) is None
        # and __fields_set__ contains the field
        if self.page_size is None and "page_size" in self.__fields_set__:
            _dict['pageSize'] = None

        # set to None if event_type (nullable) is None
        # and __fields_set__ contains the field
        if self.event_type is None and "event_type" in self.__fields_set__:
            _dict['eventType'] = None

        # set to None if login_id (nullable) is None
        # and __fields_set__ contains the field
        if self.login_id is None and "login_id" in self.__fields_set__:
            _dict['loginId'] = None

        # set to None if product_id (nullable) is None
        # and __fields_set__ contains the field
        if self.product_id is None and "product_id" in self.__fields_set__:
            _dict['productID'] = None

        # set to None if fields (nullable) is None
        # and __fields_set__ contains the field
        if self.fields is None and "fields" in self.__fields_set__:
            _dict['fields'] = None

        # set to None if filters (nullable) is None
        # and __fields_set__ contains the field
        if self.filters is None and "filters" in self.__fields_set__:
            _dict['filters'] = None

        # set to None if raw_filter (nullable) is None
        # and __fields_set__ contains the field
        if self.raw_filter is None and "raw_filter" in self.__fields_set__:
            _dict['rawFilter'] = None

        # set to None if placement (nullable) is None
        # and __fields_set__ contains the field
        if self.placement is None and "placement" in self.__fields_set__:
            _dict['placement'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if strict_filtering (nullable) is None
        # and __fields_set__ contains the field
        if self.strict_filtering is None and "strict_filtering" in self.__fields_set__:
            _dict['strictFiltering'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RecommendationsRequest:
        """Create an instance of RecommendationsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RecommendationsRequest.parse_obj(obj)

        _obj = RecommendationsRequest.parse_obj({
            "collection": obj.get("collection"),
            "visitor_id": obj.get("visitorId"),
            "limit": obj.get("limit"),
            "page_size": obj.get("pageSize"),
            "event_type": obj.get("eventType"),
            "login_id": obj.get("loginId"),
            "product_id": obj.get("productID"),
            "fields": obj.get("fields"),
            "filters": [Filter.from_dict(_item) for _item in obj.get("filters")] if obj.get("filters") is not None else None,
            "raw_filter": obj.get("rawFilter"),
            "placement": obj.get("placement"),
            "name": obj.get("name"),
            "strict_filtering": obj.get("strictFiltering")
        })
        return _obj


