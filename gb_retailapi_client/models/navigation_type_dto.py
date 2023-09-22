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





class NavigationTypeDto(str, Enum):
    """
    Type of navigation.
    """

    """
    allowed enum values
    """
    VALUE = 'Value'
    RANGE = 'Range'

    @classmethod
    def from_json(cls, json_str: str) -> NavigationTypeDto:
        """Create an instance of NavigationTypeDto from a JSON string"""
        return NavigationTypeDto(json.loads(json_str))


