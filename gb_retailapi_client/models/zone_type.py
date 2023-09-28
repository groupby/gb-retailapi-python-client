# coding: utf-8

"""
    GroupBy Retail

    GroupBy Retail API

    The version of the OpenAPI document: 0.0.0
    Contact: ops@groupbyinc.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ZoneType(str, Enum):
    """
    ZoneType
    """

    """
    allowed enum values
    """
    QUERY = 'QUERY'
    CONTENT = 'CONTENT'
    RICH_CONTENT = 'RICH_CONTENT'
    EXPECT_QUERY = 'EXPECT_QUERY'
    GENERATED_CONTENT = 'GENERATED_CONTENT'

    @classmethod
    def from_json(cls, json_str: str) -> ZoneType:
        """Create an instance of ZoneType from a JSON string"""
        return ZoneType(json.loads(json_str))


