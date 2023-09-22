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
from pydantic import BaseModel, Field, conlist
from gb_retailapi_client.models.custom_parameter_trigger import CustomParameterTrigger
from gb_retailapi_client.models.query_pattern_trigger import QueryPatternTrigger
from gb_retailapi_client.models.selected_refinement_trigger import SelectedRefinementTrigger

class TriggerSet(BaseModel):
    """
    TriggerSet
    """
    query_pattern_triggers: conlist(QueryPatternTrigger) = Field(..., alias="queryPatternTriggers", description="Query pattern triggers.")
    selected_refinement_triggers: conlist(SelectedRefinementTrigger) = Field(..., alias="selectedRefinementTriggers", description="Selected refinement triggers.")
    custom_parameter_triggers: conlist(CustomParameterTrigger) = Field(..., alias="customParameterTriggers", description="Custom parameter triggers.")
    __properties = ["queryPatternTriggers", "selectedRefinementTriggers", "customParameterTriggers"]

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
    def from_json(cls, json_str: str) -> TriggerSet:
        """Create an instance of TriggerSet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in query_pattern_triggers (list)
        _items = []
        if self.query_pattern_triggers:
            for _item in self.query_pattern_triggers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['queryPatternTriggers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in selected_refinement_triggers (list)
        _items = []
        if self.selected_refinement_triggers:
            for _item in self.selected_refinement_triggers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['selectedRefinementTriggers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in custom_parameter_triggers (list)
        _items = []
        if self.custom_parameter_triggers:
            for _item in self.custom_parameter_triggers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customParameterTriggers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TriggerSet:
        """Create an instance of TriggerSet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TriggerSet.parse_obj(obj)

        _obj = TriggerSet.parse_obj({
            "query_pattern_triggers": [QueryPatternTrigger.from_dict(_item) for _item in obj.get("queryPatternTriggers")] if obj.get("queryPatternTriggers") is not None else None,
            "selected_refinement_triggers": [SelectedRefinementTrigger.from_dict(_item) for _item in obj.get("selectedRefinementTriggers")] if obj.get("selectedRefinementTriggers") is not None else None,
            "custom_parameter_triggers": [CustomParameterTrigger.from_dict(_item) for _item in obj.get("customParameterTriggers")] if obj.get("customParameterTriggers") is not None else None
        })
        return _obj


