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



from pydantic import BaseModel, Field, StrictInt, StrictStr
from gb_retailapi_client.models.zone_type import ZoneType

class RuleTemplateSection(BaseModel):
    """
    RuleTemplateSection
    """
    zone_id: StrictInt = Field(..., alias="zoneId")
    name: StrictStr = Field(...)
    zone_content: StrictStr = Field(..., alias="zoneContent")
    zone_type: ZoneType = Field(..., alias="zoneType")
    __properties = ["zoneId", "name", "zoneContent", "zoneType"]

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
    def from_json(cls, json_str: str) -> RuleTemplateSection:
        """Create an instance of RuleTemplateSection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RuleTemplateSection:
        """Create an instance of RuleTemplateSection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RuleTemplateSection.parse_obj(obj)

        _obj = RuleTemplateSection.parse_obj({
            "zone_id": obj.get("zoneId"),
            "name": obj.get("name"),
            "zone_content": obj.get("zoneContent"),
            "zone_type": obj.get("zoneType")
        })
        return _obj

