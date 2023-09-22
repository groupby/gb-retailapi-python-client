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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from gb_retailapi_client.models.template_dto_trigger_set import TemplateDtoTriggerSet
from gb_retailapi_client.models.zone_dto import ZoneDto

class TemplateDto(BaseModel):
    """
    Template to assist the front end application in rendering the UI. Currently only the triggered rule name will be included, or the 'default' template name to indicate no rule was triggered. This is to mainly compatibility with the Searchandiser API and the addition of templates in the future. Template is search agnostic and do not affect search request or result. Templated selected only by triggered rule.  # noqa: E501
    """
    name: Optional[StrictStr] = Field(None, description="Name of the template.")
    rule_name: Optional[StrictStr] = Field(None, alias="ruleName", description="Name of the rule which may have triggered.")
    trigger_set: Optional[TemplateDtoTriggerSet] = Field(None, alias="triggerSet")
    zones: Optional[conlist(ZoneDto)] = Field(None, description="Zones for linked template.")
    __properties = ["name", "ruleName", "triggerSet", "zones"]

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
    def from_json(cls, json_str: str) -> TemplateDto:
        """Create an instance of TemplateDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of trigger_set
        if self.trigger_set:
            _dict['triggerSet'] = self.trigger_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in zones (list)
        _items = []
        if self.zones:
            for _item in self.zones:
                if _item:
                    _items.append(_item.to_dict())
            _dict['zones'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TemplateDto:
        """Create an instance of TemplateDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TemplateDto.parse_obj(obj)

        _obj = TemplateDto.parse_obj({
            "name": obj.get("name"),
            "rule_name": obj.get("ruleName"),
            "trigger_set": TemplateDtoTriggerSet.from_dict(obj.get("triggerSet")) if obj.get("triggerSet") is not None else None,
            "zones": [ZoneDto.from_dict(_item) for _item in obj.get("zones")] if obj.get("zones") is not None else None
        })
        return _obj

