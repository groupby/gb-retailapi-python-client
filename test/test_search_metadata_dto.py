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

from gb_retailapi_client.models.search_metadata_dto import SearchMetadataDto  # noqa: E501

class TestSearchMetadataDto(unittest.TestCase):
    """SearchMetadataDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchMetadataDto:
        """Test SearchMetadataDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchMetadataDto`
        """
        model = SearchMetadataDto()  # noqa: E501
        if include_optional:
            return SearchMetadataDto(
                search_attribution_token = 'NtQKDAjYrrGEBhCWs_v3AhABGiQ2MDlhNjA5Yy0wMDAwLTI2ZDctODQ0OS1mNGY1ZTgwODc1YjQ',
                cached = False,
                total_time = 153
            )
        else:
            return SearchMetadataDto(
        )
        """

    def testSearchMetadataDto(self):
        """Test SearchMetadataDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
