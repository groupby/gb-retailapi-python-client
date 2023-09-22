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

from gb_retailapi_client.models.refinement_dto import RefinementDto  # noqa: E501

class TestRefinementDto(unittest.TestCase):
    """RefinementDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RefinementDto:
        """Test RefinementDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RefinementDto`
        """
        model = RefinementDto()  # noqa: E501
        if include_optional:
            return RefinementDto(
                type = 'Value',
                count = 189,
                value = 'Surf's Up',
                low = 50,
                high = 100
            )
        else:
            return RefinementDto(
                type = 'Value',
        )
        """

    def testRefinementDto(self):
        """Test RefinementDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
