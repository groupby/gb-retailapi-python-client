# coding: utf-8

"""
    GroupBy Retail

    GroupBy Retail API

    The version of the OpenAPI document: 0.0
    Contact: ops@groupbyinc.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from gb_retailapi_client.models.recommendations_error_response import RecommendationsErrorResponse  # noqa: E501

class TestRecommendationsErrorResponse(unittest.TestCase):
    """RecommendationsErrorResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecommendationsErrorResponse:
        """Test RecommendationsErrorResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecommendationsErrorResponse`
        """
        model = RecommendationsErrorResponse()  # noqa: E501
        if include_optional:
            return RecommendationsErrorResponse(
                tracking_id = 'bb25d616-2cd7-44a1-8d11-27159f2aa03c',
                method = 'POST',
                path = '',
                message = 'Search request page size must be greater than or equal to 0.'
            )
        else:
            return RecommendationsErrorResponse(
        )
        """

    def testRecommendationsErrorResponse(self):
        """Test RecommendationsErrorResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
