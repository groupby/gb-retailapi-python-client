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

from gb_retailapi_client.models.price_info_price_effective_time import PriceInfoPriceEffectiveTime  # noqa: E501

class TestPriceInfoPriceEffectiveTime(unittest.TestCase):
    """PriceInfoPriceEffectiveTime unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PriceInfoPriceEffectiveTime:
        """Test PriceInfoPriceEffectiveTime
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PriceInfoPriceEffectiveTime`
        """
        model = PriceInfoPriceEffectiveTime()  # noqa: E501
        if include_optional:
            return PriceInfoPriceEffectiveTime(
                seconds = 100,
                nanos = 100
            )
        else:
            return PriceInfoPriceEffectiveTime(
        )
        """

    def testPriceInfoPriceEffectiveTime(self):
        """Test PriceInfoPriceEffectiveTime"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
