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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, conlist

class Rating(BaseModel):
    """
    The rating of this product.  # noqa: E501
    """
    rating_count: Optional[StrictInt] = Field(None, alias="ratingCount", description="The total number of ratings. This value is independent of the value of histogram.This value must be nonnegative.")
    average_rating: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="averageRating", description="The average rating of the product. The rating is scaled at 1-5.")
    rating_histogram: Optional[conlist(StrictInt)] = Field(None, alias="ratingHistogram", description="List of rating counts per rating value (index = rating - 1). The list is empty if there is no rating. If the list is non-empty, its size is always 5. For example, [41, 14, 13, 47, 303]. It means that the product got 41 ratings with 1 star, 14 ratings with 2 star, and so on.")
    __properties = ["ratingCount", "averageRating", "ratingHistogram"]

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
    def from_json(cls, json_str: str) -> Rating:
        """Create an instance of Rating from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Rating:
        """Create an instance of Rating from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Rating.parse_obj(obj)

        _obj = Rating.parse_obj({
            "rating_count": obj.get("ratingCount"),
            "average_rating": obj.get("averageRating"),
            "rating_histogram": obj.get("ratingHistogram")
        })
        return _obj

