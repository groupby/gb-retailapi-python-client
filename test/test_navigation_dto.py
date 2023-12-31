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

from gb_retailapi_client.models.navigation_dto import NavigationDto  # noqa: E501

class TestNavigationDto(unittest.TestCase):
    """NavigationDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NavigationDto:
        """Test NavigationDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NavigationDto`
        """
        model = NavigationDto()  # noqa: E501
        if include_optional:
            return NavigationDto(
                name = 'brands',
                display_name = 'Brand',
                type = 'Value',
                refinements = [
                    gb_retailapi_client.models.refinement.Refinement(
                        type = 'Value', 
                        count = 189, 
                        value = 'Surf's Up', 
                        low = 50, 
                        high = 100, )
                    ],
                var_or = True,
                source = '',
                metadata = [
                    gb_retailapi_client.models.metadata.Metadata(
                        key = '', 
                        value = '', )
                    ],
                place_id = ''
            )
        else:
            return NavigationDto(
                type = 'Value',
                refinements = [
                    gb_retailapi_client.models.refinement.Refinement(
                        type = 'Value', 
                        count = 189, 
                        value = 'Surf's Up', 
                        low = 50, 
                        high = 100, )
                    ],
                source = '',
                metadata = [
                    gb_retailapi_client.models.metadata.Metadata(
                        key = '', 
                        value = '', )
                    ],
                place_id = '',
        )
        """

    def testNavigationDto(self):
        """Test NavigationDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
