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

from gb_retailapi_client.models.search_terms import SearchTerms  # noqa: E501

class TestSearchTerms(unittest.TestCase):
    """SearchTerms unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchTerms:
        """Test SearchTerms
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchTerms`
        """
        model = SearchTerms()  # noqa: E501
        if include_optional:
            return SearchTerms(
                value = '',
                additional_info = gb_retailapi_client.models.additional_info.AdditionalInfo(
                    brands = [
                        ''
                        ], 
                    categories = [
                        ''
                        ], )
            )
        else:
            return SearchTerms(
                additional_info = gb_retailapi_client.models.additional_info.AdditionalInfo(
                    brands = [
                        ''
                        ], 
                    categories = [
                        ''
                        ], ),
        )
        """

    def testSearchTerms(self):
        """Test SearchTerms"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()