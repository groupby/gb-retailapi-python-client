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





class Order(str, Enum):
    """
    Order
    """

    """
    allowed enum values
    """
    ASCENDING = 'ASCENDING'
    DESCENDING = 'DESCENDING'

    @classmethod
    def from_json(cls, json_str: str) -> Order:
        """Create an instance of Order from a JSON string"""
        return Order(json.loads(json_str))


