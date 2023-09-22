# coding: utf-8

"""
    GroupBy Retail

    GroupBy Retail API

    The version of the OpenAPI document: 0.0
    Contact: ops@groupbyinc.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ZoneDtoType(str, Enum):
    """
    Define type of content which is can be stored in zone.
    """

    """
    allowed enum values
    """
    CONTENT = 'Content'
    RICH_CONTENT = 'Rich_Content'
    PRODUCTS = 'Products'
    GENERATED_CONTENT = 'Generated_Content'

    @classmethod
    def from_json(cls, json_str: str) -> ZoneDtoType:
        """Create an instance of ZoneDtoType from a JSON string"""
        return ZoneDtoType(json.loads(json_str))


