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

from gb_retailapi_client.models.error_response import ErrorResponse  # noqa: E501

class TestErrorResponse(unittest.TestCase):
    """ErrorResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorResponse:
        """Test ErrorResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorResponse`
        """
        model = ErrorResponse()  # noqa: E501
        if include_optional:
            return ErrorResponse(
                tracking_id = '2c9ea473-730e-346a-a24e-23aae0623583',
                method = 'GET',
                path = '/ccapi/example/path',
                message = 'Something went wrong, please do....'
            )
        else:
            return ErrorResponse(
                tracking_id = '2c9ea473-730e-346a-a24e-23aae0623583',
                method = 'GET',
                path = '/ccapi/example/path',
                message = 'Something went wrong, please do....',
        )
        """

    def testErrorResponse(self):
        """Test ErrorResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
