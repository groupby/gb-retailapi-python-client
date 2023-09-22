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

from gb_retailapi_client.models.price_info_price_range_original_price import PriceInfoPriceRangeOriginalPrice  # noqa: E501

class TestPriceInfoPriceRangeOriginalPrice(unittest.TestCase):
    """PriceInfoPriceRangeOriginalPrice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PriceInfoPriceRangeOriginalPrice:
        """Test PriceInfoPriceRangeOriginalPrice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PriceInfoPriceRangeOriginalPrice`
        """
        model = PriceInfoPriceRangeOriginalPrice()  # noqa: E501
        if include_optional:
            return PriceInfoPriceRangeOriginalPrice(
                minimum = 1,
                exclusive_minimum = 1,
                maximum = 1,
                exclusive_maximum = 1
            )
        else:
            return PriceInfoPriceRangeOriginalPrice(
        )
        """

    def testPriceInfoPriceRangeOriginalPrice(self):
        """Test PriceInfoPriceRangeOriginalPrice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()