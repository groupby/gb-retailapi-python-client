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

from gb_retailapi_client.models.merchandiser import Merchandiser  # noqa: E501

class TestMerchandiser(unittest.TestCase):
    """Merchandiser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Merchandiser:
        """Test Merchandiser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Merchandiser`
        """
        model = Merchandiser()  # noqa: E501
        if include_optional:
            return Merchandiser(
                merchandiser_id = ''
            )
        else:
            return Merchandiser(
                merchandiser_id = '',
        )
        """

    def testMerchandiser(self):
        """Test Merchandiser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
