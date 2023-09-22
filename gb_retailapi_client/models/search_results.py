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


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from gb_retailapi_client.models.attribute_suggestion import AttributeSuggestion
from gb_retailapi_client.models.search_results_stats import SearchResultsStats
from gb_retailapi_client.models.search_terms import SearchTerms

class SearchResults(BaseModel):
    """
    SAYT response. Contains list of suggestions ad base response information.  # noqa: E501
    """
    stats: Optional[SearchResultsStats] = None
    search_terms: conlist(SearchTerms) = Field(..., alias="searchTerms")
    extended_attributes: Optional[Dict[str, conlist(StrictStr)]] = Field(None, alias="extendedAttributes", description="Map with extended attributes which are returned in autocomplete response. ")
    attribute_results: Optional[Dict[str, AttributeSuggestion]] = Field(None, alias="attributeResults", description="SAYT response attributes. Contains list of direct matching attributes.")
    site_filter: Optional[StrictStr] = Field(None, alias="siteFilter", description="SiteFilter object used with request.")
    __properties = ["stats", "searchTerms", "extendedAttributes", "attributeResults", "siteFilter"]

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
    def from_json(cls, json_str: str) -> SearchResults:
        """Create an instance of SearchResults from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of stats
        if self.stats:
            _dict['stats'] = self.stats.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in search_terms (list)
        _items = []
        if self.search_terms:
            for _item in self.search_terms:
                if _item:
                    _items.append(_item.to_dict())
            _dict['searchTerms'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in extended_attributes (dict of array)
        _field_dict_of_array = {}
        if self.extended_attributes:
            for _key in self.extended_attributes:
                if self.extended_attributes[_key]:
                    _field_dict_of_array[_key] = [
                        _item.to_dict() for _item in self.extended_attributes[_key]
                    ]
            _dict['extendedAttributes'] = _field_dict_of_array
        # override the default output from pydantic by calling `to_dict()` of each value in attribute_results (dict)
        _field_dict = {}
        if self.attribute_results:
            for _key in self.attribute_results:
                if self.attribute_results[_key]:
                    _field_dict[_key] = self.attribute_results[_key].to_dict()
            _dict['attributeResults'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SearchResults:
        """Create an instance of SearchResults from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SearchResults.parse_obj(obj)

        _obj = SearchResults.parse_obj({
            "stats": SearchResultsStats.from_dict(obj.get("stats")) if obj.get("stats") is not None else None,
            "search_terms": [SearchTerms.from_dict(_item) for _item in obj.get("searchTerms")] if obj.get("searchTerms") is not None else None,
            "extended_attributes": obj.get("extendedAttributes"),
            "attribute_results": dict(
                (_k, AttributeSuggestion.from_dict(_v))
                for _k, _v in obj.get("attributeResults").items()
            )
            if obj.get("attributeResults") is not None
            else None,
            "site_filter": obj.get("siteFilter")
        })
        return _obj


