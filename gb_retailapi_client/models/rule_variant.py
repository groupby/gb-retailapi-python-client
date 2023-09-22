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


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist
from gb_retailapi_client.models.boosted_product_bucket import BoostedProductBucket
from gb_retailapi_client.models.pinned_refinement import PinnedRefinement
from gb_retailapi_client.models.range_filter import RangeFilter
from gb_retailapi_client.models.rule_template import RuleTemplate
from gb_retailapi_client.models.search_filter import SearchFilter
from gb_retailapi_client.models.sort import Sort
from gb_retailapi_client.models.value_filter import ValueFilter

class RuleVariant(BaseModel):
    """
    RuleVariant
    """
    biasing_profile_name: StrictStr = Field(..., alias="biasingProfileName")
    included_navigations: conlist(StrictStr) = Field(..., alias="includedNavigations")
    template: RuleTemplate = Field(...)
    boosted_product_buckets: conlist(BoostedProductBucket) = Field(..., alias="boostedProductBuckets")
    pinned_refinements: conlist(PinnedRefinement) = Field(..., alias="pinnedRefinements")
    sort: Sort = Field(...)
    value_filters: conlist(ValueFilter) = Field(..., alias="valueFilters")
    search_filters: conlist(SearchFilter) = Field(..., alias="searchFilters")
    range_filters: conlist(RangeFilter) = Field(..., alias="rangeFilters")
    __properties = ["biasingProfileName", "includedNavigations", "template", "boostedProductBuckets", "pinnedRefinements", "sort", "valueFilters", "searchFilters", "rangeFilters"]

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
    def from_json(cls, json_str: str) -> RuleVariant:
        """Create an instance of RuleVariant from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of template
        if self.template:
            _dict['template'] = self.template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in boosted_product_buckets (list)
        _items = []
        if self.boosted_product_buckets:
            for _item in self.boosted_product_buckets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['boostedProductBuckets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in pinned_refinements (list)
        _items = []
        if self.pinned_refinements:
            for _item in self.pinned_refinements:
                if _item:
                    _items.append(_item.to_dict())
            _dict['pinnedRefinements'] = _items
        # override the default output from pydantic by calling `to_dict()` of sort
        if self.sort:
            _dict['sort'] = self.sort.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in value_filters (list)
        _items = []
        if self.value_filters:
            for _item in self.value_filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['valueFilters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in search_filters (list)
        _items = []
        if self.search_filters:
            for _item in self.search_filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['searchFilters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in range_filters (list)
        _items = []
        if self.range_filters:
            for _item in self.range_filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rangeFilters'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RuleVariant:
        """Create an instance of RuleVariant from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RuleVariant.parse_obj(obj)

        _obj = RuleVariant.parse_obj({
            "biasing_profile_name": obj.get("biasingProfileName"),
            "included_navigations": obj.get("includedNavigations"),
            "template": RuleTemplate.from_dict(obj.get("template")) if obj.get("template") is not None else None,
            "boosted_product_buckets": [BoostedProductBucket.from_dict(_item) for _item in obj.get("boostedProductBuckets")] if obj.get("boostedProductBuckets") is not None else None,
            "pinned_refinements": [PinnedRefinement.from_dict(_item) for _item in obj.get("pinnedRefinements")] if obj.get("pinnedRefinements") is not None else None,
            "sort": Sort.from_dict(obj.get("sort")) if obj.get("sort") is not None else None,
            "value_filters": [ValueFilter.from_dict(_item) for _item in obj.get("valueFilters")] if obj.get("valueFilters") is not None else None,
            "search_filters": [SearchFilter.from_dict(_item) for _item in obj.get("searchFilters")] if obj.get("searchFilters") is not None else None,
            "range_filters": [RangeFilter.from_dict(_item) for _item in obj.get("rangeFilters")] if obj.get("rangeFilters") is not None else None
        })
        return _obj

