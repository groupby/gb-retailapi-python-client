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

from gb_retailapi_client.models.product_dto_publish_time import ProductDtoPublishTime  # noqa: E501

class TestProductDtoPublishTime(unittest.TestCase):
    """ProductDtoPublishTime unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductDtoPublishTime:
        """Test ProductDtoPublishTime
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductDtoPublishTime`
        """
        model = ProductDtoPublishTime()  # noqa: E501
        if include_optional:
            return ProductDtoPublishTime(
                seconds = 100,
                nanos = 100
            )
        else:
            return ProductDtoPublishTime(
        )
        """

    def testProductDtoPublishTime(self):
        """Test ProductDtoPublishTime"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
