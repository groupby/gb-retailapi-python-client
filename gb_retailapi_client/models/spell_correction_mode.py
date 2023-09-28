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





class SpellCorrectionMode(str, Enum):
    """
    SpellCorrectionMode
    """

    """
    allowed enum values
    """
    AUTO = 'AUTO'
    SUGGESTION_ONLY = 'SUGGESTION_ONLY'

    @classmethod
    def from_json(cls, json_str: str) -> SpellCorrectionMode:
        """Create an instance of SpellCorrectionMode from a JSON string"""
        return SpellCorrectionMode(json.loads(json_str))


