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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from gb_retailapi_client.models.filter_parameter import FilterParameter

class PredictResults(BaseModel):
    """
    Prediction result including list of recommendations based on provided inputs.  # noqa: E501
    """
    warnings: Optional[conlist(Dict[str, Any])] = Field(None, description="Warnings collected with validation and Recommendations AI API issues.")
    products: Optional[conlist(Dict[str, Any])] = Field(None, description="Recommendations built by Recommendations AI model.")
    records: Optional[conlist(Dict[str, Any])] = Field(None, description="Recommendations built by Recommendations AI model.")
    model_id: Optional[StrictStr] = Field(None, alias="modelId", description="Model Id used for predictions")
    model_name: Optional[StrictStr] = Field(None, alias="modelName", description="Model Name used for predictions")
    model_type: Optional[StrictStr] = Field(None, alias="modelType", description="  Currently supported values:   `recommended-for-you`   `others-you-may-like`,   `frequently-bought-together`   `page-optimization`   `similar-items`,   `buy-it-again`   `on-sale-items`   `recently-viewed`    This field together with optimization_objective describe model metadata to use to control model training and   serving. See https://cloud.google.com/retail/docs/models for more details. ")
    optimization_objective: Optional[StrictStr] = Field(None, alias="optimizationObjective", description="  Currently supported values: `ctr`, `cvr`, `revenue-per-order`.     If not specified, we choose default based on model type. Default depends on type of recommendation:   `recommended-for-you` => `ctr`   `others-you-may-like` => `ctr`   `frequently-bought-together` => `revenue_per_order`    This field together with modelType describe model metadata to use to control model training and serving.   See https://cloud.google.com/retail/docs/models for more details on what the model metadata control and which   combination of parameters are valid. ")
    filter_set: Optional[StrictStr] = Field(None, alias="filterSet", description="Filter set applied to the recommendation")
    raw_filter: Optional[StrictStr] = Field(None, alias="rawFilter", description="RawFilter applied to the recommendation")
    filters: Optional[conlist(FilterParameter)] = Field(None, description="Filters applied to the recommendation")
    metadata: Optional[Any] = None
    __properties = ["warnings", "products", "records", "modelId", "modelName", "modelType", "optimizationObjective", "filterSet", "rawFilter", "filters", "metadata"]

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
    def from_json(cls, json_str: str) -> PredictResults:
        """Create an instance of PredictResults from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in filters (list)
        _items = []
        if self.filters:
            for _item in self.filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['filters'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PredictResults:
        """Create an instance of PredictResults from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PredictResults.parse_obj(obj)

        _obj = PredictResults.parse_obj({
            "warnings": obj.get("warnings"),
            "products": obj.get("products"),
            "records": obj.get("records"),
            "model_id": obj.get("modelId"),
            "model_name": obj.get("modelName"),
            "model_type": obj.get("modelType"),
            "optimization_objective": obj.get("optimizationObjective"),
            "filter_set": obj.get("filterSet"),
            "raw_filter": obj.get("rawFilter"),
            "filters": [FilterParameter.from_dict(_item) for _item in obj.get("filters")] if obj.get("filters") is not None else None,
            "metadata": obj.get("metadata")
        })
        return _obj


