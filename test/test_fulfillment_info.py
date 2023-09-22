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

from gb_retailapi_client.models.fulfillment_info import FulfillmentInfo  # noqa: E501

class TestFulfillmentInfo(unittest.TestCase):
    """FulfillmentInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FulfillmentInfo:
        """Test FulfillmentInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FulfillmentInfo`
        """
        model = FulfillmentInfo()  # noqa: E501
        if include_optional:
            return FulfillmentInfo(
                type = 'pickup-in-store',
                place_ids = 6, 4, 8
            )
        else:
            return FulfillmentInfo(
        )
        """

    def testFulfillmentInfo(self):
        """Test FulfillmentInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
