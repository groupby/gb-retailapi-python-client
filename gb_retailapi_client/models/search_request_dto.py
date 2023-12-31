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


from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conint, conlist
from gb_retailapi_client.models.biasing_profile_dto import BiasingProfileDto
from gb_retailapi_client.models.custom_parameter_dto import CustomParameterDto
from gb_retailapi_client.models.search_request_dto_overwrites import SearchRequestDtoOverwrites
from gb_retailapi_client.models.selected_refinement_dto import SelectedRefinementDto
from gb_retailapi_client.models.sort_dto import SortDto

class SearchRequestDto(BaseModel):
    """
    Request that should be populated to configure a search API call, made by the client on behalf of a shopper.  # noqa: E501
    """
    query: Optional[StrictStr] = Field(None, description="Base textual search query.")
    area: Optional[StrictStr] = Field('Production', description="Area name the search is being performed in.")
    collection: Optional[StrictStr] = Field('default', description="Name of collection in project configuration setting which is mapped to the google retail backend.")
    visitor_id: Optional[StrictStr] = Field(None, alias="visitorId", description="Unique identifier identifying the shopper. Will be autogenerated if not provided.")
    refinements: conlist(SelectedRefinementDto) = Field(...)
    page_size: Optional[conint(strict=True, ge=0)] = Field(10, alias="pageSize", description="The number of products to be returned on each page.")
    skip: Optional[conint(strict=True, ge=0)] = Field(0, description="Where in the list of products to begin the page.")
    biasing_profile: Optional[StrictStr] = Field(None, alias="biasingProfile", description="Name of a biasing profile which should be applied to the search. Takes priority over area default.")
    biasing: Optional[BiasingProfileDto] = Field(...)
    custom_url_params: conlist(CustomParameterDto) = Field(..., alias="customUrlParams")
    sorts: conlist(SortDto) = Field(...)
    included_navigations: Optional[conlist(StrictStr)] = Field(None, alias="includedNavigations", description="Set of navigation fields to include in the search result. Cannot be set if 'excludedNavigations' is set.")
    excluded_navigations: Optional[conlist(StrictStr)] = Field(None, alias="excludedNavigations", description="Set of navigation fields to exclude in the search result. Cannot be set if 'includedNavigations' is set.")
    dynamic_facet: Optional[StrictBool] = Field(None, alias="dynamicFacet", description="Set the specifications of dynamically generated facets.")
    variant_rollup_keys: Optional[conlist(StrictStr)] = Field(None, alias="variantRollupKeys", description="Set the variant rollup keys.")
    pre_filter: Optional[StrictStr] = Field(None, alias="preFilter", description="Set of the prefilter specifications value.")
    site: Optional[StrictStr] = Field(None, description="Name of site filter. If not specified, the specified area's default site will be applied if configured in Command Center. To not use default specify empty value i.e.\"\".  If the site doesn't exist then the search will execute without the site filter and a warning will be provided.")
    response_mask: Optional[conlist(StrictStr)] = Field(None, alias="responseMask", description="List with fields which should be included in metadata object associated with each record in response.")
    page_categories: Optional[conlist(StrictStr)] = Field(None, alias="pageCategories", description="The categories associated with a category page. Required for category navigation queries to achieve good search quality. To represent full path of category, use '>' sign to separate different hierarchies. If '>' is part of the category name, please replace it with other character(s).Max item length = 1.")
    spell_correction_mode: Optional[Any] = Field(None, alias="spellCorrectionMode")
    include_expanded_results: Optional[StrictBool] = Field(None, alias="includeExpandedResults", description="When a shopper uses an ambiguous or a multi-word search phrase, they can get an empty response. After turning on include expanded results, Retail Search analyzes the request and returns the expanded list of products based on the parsed search query. For example, if you search \"Google Pixel 5\" without query expansion, you might only get \"google_pixel_5\" in the result. With query expansion, you might get \"google_pixel_4a_with_5g\", \"google_pixel_4a\" and \"google_pixel_5_case\" as well.The default value is configured in the tenant settings or true if there is no such setting")
    pin_unexpanded_results: Optional[StrictBool] = Field(None, alias="pinUnexpandedResults", description="This configuration depends on include expanded results settings. If this field is set to true,unexpanded products are always at the top of the search results, followed  by the expanded results. Default value: true")
    debug: Optional[StrictBool] = Field(None, description="Enable additional debug info in response.  Note: attaching debug info significantly affects performance. Is not supposed to be used for large requests.  ")
    facet_limit: Optional[StrictInt] = Field(None, alias="facetLimit", description="Maximum of facet values that should be returned for this facet. If not specified, defaults to 20. The maximum allowed value is 300. Values above 300 will be coerced to 300.  If this field is negative, an INVALID_ARGUMENT is returned.  This limit (300) is configured on Google side, but Google have an ability to change it for specific project. ")
    login_id: Optional[StrictStr] = Field(None, alias="loginId", description="Highly recommended for logged-in users. Unique identifier for logged-in user, such as a user name. Don't set for anonymous users.  Don't set the field to the same fixed ID for different users. This mixes the event history of those users together, which results in degraded model quality.  The field must be a UTF-8 encoded string with a length limit of 128 characters. ")
    overwrites: Optional[SearchRequestDtoOverwrites] = None
    __properties = ["query", "area", "collection", "visitorId", "refinements", "pageSize", "skip", "biasingProfile", "biasing", "customUrlParams", "sorts", "includedNavigations", "excludedNavigations", "dynamicFacet", "variantRollupKeys", "preFilter", "site", "responseMask", "pageCategories", "spellCorrectionMode", "includeExpandedResults", "pinUnexpandedResults", "debug", "facetLimit", "loginId", "overwrites"]

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
    def from_json(cls, json_str: str) -> SearchRequestDto:
        """Create an instance of SearchRequestDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in refinements (list)
        _items = []
        if self.refinements:
            for _item in self.refinements:
                if _item:
                    _items.append(_item.to_dict())
            _dict['refinements'] = _items
        # override the default output from pydantic by calling `to_dict()` of biasing
        if self.biasing:
            _dict['biasing'] = self.biasing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in custom_url_params (list)
        _items = []
        if self.custom_url_params:
            for _item in self.custom_url_params:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customUrlParams'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sorts (list)
        _items = []
        if self.sorts:
            for _item in self.sorts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sorts'] = _items
        # override the default output from pydantic by calling `to_dict()` of spell_correction_mode
        if self.spell_correction_mode:
            _dict['spellCorrectionMode'] = self.spell_correction_mode.to_dict()
        # override the default output from pydantic by calling `to_dict()` of overwrites
        if self.overwrites:
            _dict['overwrites'] = self.overwrites.to_dict()
        # set to None if query (nullable) is None
        # and __fields_set__ contains the field
        if self.query is None and "query" in self.__fields_set__:
            _dict['query'] = None

        # set to None if area (nullable) is None
        # and __fields_set__ contains the field
        if self.area is None and "area" in self.__fields_set__:
            _dict['area'] = None

        # set to None if collection (nullable) is None
        # and __fields_set__ contains the field
        if self.collection is None and "collection" in self.__fields_set__:
            _dict['collection'] = None

        # set to None if visitor_id (nullable) is None
        # and __fields_set__ contains the field
        if self.visitor_id is None and "visitor_id" in self.__fields_set__:
            _dict['visitorId'] = None

        # set to None if page_size (nullable) is None
        # and __fields_set__ contains the field
        if self.page_size is None and "page_size" in self.__fields_set__:
            _dict['pageSize'] = None

        # set to None if skip (nullable) is None
        # and __fields_set__ contains the field
        if self.skip is None and "skip" in self.__fields_set__:
            _dict['skip'] = None

        # set to None if biasing_profile (nullable) is None
        # and __fields_set__ contains the field
        if self.biasing_profile is None and "biasing_profile" in self.__fields_set__:
            _dict['biasingProfile'] = None

        # set to None if biasing (nullable) is None
        # and __fields_set__ contains the field
        if self.biasing is None and "biasing" in self.__fields_set__:
            _dict['biasing'] = None

        # set to None if included_navigations (nullable) is None
        # and __fields_set__ contains the field
        if self.included_navigations is None and "included_navigations" in self.__fields_set__:
            _dict['includedNavigations'] = None

        # set to None if excluded_navigations (nullable) is None
        # and __fields_set__ contains the field
        if self.excluded_navigations is None and "excluded_navigations" in self.__fields_set__:
            _dict['excludedNavigations'] = None

        # set to None if dynamic_facet (nullable) is None
        # and __fields_set__ contains the field
        if self.dynamic_facet is None and "dynamic_facet" in self.__fields_set__:
            _dict['dynamicFacet'] = None

        # set to None if variant_rollup_keys (nullable) is None
        # and __fields_set__ contains the field
        if self.variant_rollup_keys is None and "variant_rollup_keys" in self.__fields_set__:
            _dict['variantRollupKeys'] = None

        # set to None if pre_filter (nullable) is None
        # and __fields_set__ contains the field
        if self.pre_filter is None and "pre_filter" in self.__fields_set__:
            _dict['preFilter'] = None

        # set to None if site (nullable) is None
        # and __fields_set__ contains the field
        if self.site is None and "site" in self.__fields_set__:
            _dict['site'] = None

        # set to None if response_mask (nullable) is None
        # and __fields_set__ contains the field
        if self.response_mask is None and "response_mask" in self.__fields_set__:
            _dict['responseMask'] = None

        # set to None if page_categories (nullable) is None
        # and __fields_set__ contains the field
        if self.page_categories is None and "page_categories" in self.__fields_set__:
            _dict['pageCategories'] = None

        # set to None if spell_correction_mode (nullable) is None
        # and __fields_set__ contains the field
        if self.spell_correction_mode is None and "spell_correction_mode" in self.__fields_set__:
            _dict['spellCorrectionMode'] = None

        # set to None if include_expanded_results (nullable) is None
        # and __fields_set__ contains the field
        if self.include_expanded_results is None and "include_expanded_results" in self.__fields_set__:
            _dict['includeExpandedResults'] = None

        # set to None if pin_unexpanded_results (nullable) is None
        # and __fields_set__ contains the field
        if self.pin_unexpanded_results is None and "pin_unexpanded_results" in self.__fields_set__:
            _dict['pinUnexpandedResults'] = None

        # set to None if debug (nullable) is None
        # and __fields_set__ contains the field
        if self.debug is None and "debug" in self.__fields_set__:
            _dict['debug'] = None

        # set to None if facet_limit (nullable) is None
        # and __fields_set__ contains the field
        if self.facet_limit is None and "facet_limit" in self.__fields_set__:
            _dict['facetLimit'] = None

        # set to None if login_id (nullable) is None
        # and __fields_set__ contains the field
        if self.login_id is None and "login_id" in self.__fields_set__:
            _dict['loginId'] = None

        # set to None if overwrites (nullable) is None
        # and __fields_set__ contains the field
        if self.overwrites is None and "overwrites" in self.__fields_set__:
            _dict['overwrites'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SearchRequestDto:
        """Create an instance of SearchRequestDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SearchRequestDto.parse_obj(obj)

        _obj = SearchRequestDto.parse_obj({
            "query": obj.get("query"),
            "area": obj.get("area") if obj.get("area") is not None else 'Production',
            "collection": obj.get("collection") if obj.get("collection") is not None else 'default',
            "visitor_id": obj.get("visitorId"),
            "refinements": [SelectedRefinementDto.from_dict(_item) for _item in obj.get("refinements")] if obj.get("refinements") is not None else None,
            "page_size": obj.get("pageSize") if obj.get("pageSize") is not None else 10,
            "skip": obj.get("skip") if obj.get("skip") is not None else 0,
            "biasing_profile": obj.get("biasingProfile"),
            "biasing": BiasingProfileDto.from_dict(obj.get("biasing")) if obj.get("biasing") is not None else None,
            "custom_url_params": [CustomParameterDto.from_dict(_item) for _item in obj.get("customUrlParams")] if obj.get("customUrlParams") is not None else None,
            "sorts": [SortDto.from_dict(_item) for _item in obj.get("sorts")] if obj.get("sorts") is not None else None,
            "included_navigations": obj.get("includedNavigations"),
            "excluded_navigations": obj.get("excludedNavigations"),
            "dynamic_facet": obj.get("dynamicFacet"),
            "variant_rollup_keys": obj.get("variantRollupKeys"),
            "pre_filter": obj.get("preFilter"),
            "site": obj.get("site"),
            "response_mask": obj.get("responseMask"),
            "page_categories": obj.get("pageCategories"),
            "spell_correction_mode": SpellCorrectionMode.from_dict(obj.get("spellCorrectionMode")) if obj.get("spellCorrectionMode") is not None else None,
            "include_expanded_results": obj.get("includeExpandedResults"),
            "pin_unexpanded_results": obj.get("pinUnexpandedResults"),
            "debug": obj.get("debug"),
            "facet_limit": obj.get("facetLimit"),
            "login_id": obj.get("loginId"),
            "overwrites": SearchRequestDtoOverwrites.from_dict(obj.get("overwrites")) if obj.get("overwrites") is not None else None
        })
        return _obj


