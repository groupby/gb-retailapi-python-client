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

from gb_retailapi_client.models.rule_template import RuleTemplate  # noqa: E501

class TestRuleTemplate(unittest.TestCase):
    """RuleTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RuleTemplate:
        """Test RuleTemplate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RuleTemplate`
        """
        model = RuleTemplate()  # noqa: E501
        if include_optional:
            return RuleTemplate(
                name = '',
                enable_exact_matching = True,
                sections = [
                    gb_retailapi_client.models.rule_template_section.RuleTemplateSection(
                        zone_id = 56, 
                        name = '', 
                        zone_content = '', 
                        zone_type = 'QUERY', )
                    ]
            )
        else:
            return RuleTemplate(
                name = '',
                enable_exact_matching = True,
                sections = [
                    gb_retailapi_client.models.rule_template_section.RuleTemplateSection(
                        zone_id = 56, 
                        name = '', 
                        zone_content = '', 
                        zone_type = 'QUERY', )
                    ],
        )
        """

    def testRuleTemplate(self):
        """Test RuleTemplate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()