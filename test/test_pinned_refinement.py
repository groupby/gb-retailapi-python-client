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

from gb_retailapi_client.models.pinned_refinement import PinnedRefinement  # noqa: E501

class TestPinnedRefinement(unittest.TestCase):
    """PinnedRefinement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PinnedRefinement:
        """Test PinnedRefinement
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PinnedRefinement`
        """
        model = PinnedRefinement()  # noqa: E501
        if include_optional:
            return PinnedRefinement(
                navigation = '',
                refinements = [
                    gb_retailapi_client.models.refinement.Refinement(
                        value = '', 
                        priority = 56, )
                    ]
            )
        else:
            return PinnedRefinement(
                navigation = '',
                refinements = [
                    gb_retailapi_client.models.refinement.Refinement(
                        value = '', 
                        priority = 56, )
                    ],
        )
        """

    def testPinnedRefinement(self):
        """Test PinnedRefinement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
