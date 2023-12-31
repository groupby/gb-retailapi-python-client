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

from gb_retailapi_client.models.facet_search_response_dto import FacetSearchResponseDto  # noqa: E501

class TestFacetSearchResponseDto(unittest.TestCase):
    """FacetSearchResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FacetSearchResponseDto:
        """Test FacetSearchResponseDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FacetSearchResponseDto`
        """
        model = FacetSearchResponseDto()  # noqa: E501
        if include_optional:
            return FacetSearchResponseDto(
                original_request = gb_retailapi_client.models.search_request.Search Request(
                    query = 'blue sweater', 
                    area = 'Production', 
                    collection = 'default', 
                    visitor_id = '38400000-8cf0-11bd-b23e-10b96e40000d', 
                    refinements = [
                        gb_retailapi_client.models.selected_refinement.Selected Refinement(
                            navigation_name = 'brands', 
                            type = null, 
                            value = '', 
                            low = 50, 
                            high = 100, 
                            source = 'Dynamic', 
                            or = False, )
                        ], 
                    page_size = 25, 
                    skip = 50, 
                    biasing_profile = '', 
                    biasing = gb_retailapi_client.models.biasing_profile.Biasing Profile(
                        biases = [
                            gb_retailapi_client.models.bias.Bias(
                                field = 'colorFamilies', 
                                content = 'Red', 
                                strength = 'ABSOLUTE_INCREASE', )
                            ], ), 
                    custom_url_params = [
                        gb_retailapi_client.models.custom_parameter.Custom Parameter(
                            key = 'landing-page', 
                            value = 'easter-2021', )
                        ], 
                    sorts = [
                        gb_retailapi_client.models.sort.Sort(
                            field = 'rating', 
                            order = 'Ascending', )
                        ], 
                    included_navigations = [
                        ''
                        ], 
                    excluded_navigations = [
                        ''
                        ], 
                    dynamic_facet = True, 
                    variant_rollup_keys = [
                        ''
                        ], 
                    pre_filter = '(categories:ANY("Men")) AND (ageGroups:ANY("adult")) AND (price: IN(150, 200))', 
                    site = '', 
                    response_mask = ["key.innerKey.value", "key2", "key.innerKey2.value2"], 
                    page_categories = ["Sales > 2017 Black Friday Deals"], 
                    spell_correction_mode = null, 
                    include_expanded_results = True, 
                    pin_unexpanded_results = True, 
                    debug = True, 
                    facet_limit = 56, 
                    login_id = '', 
                    overwrites = null, ),
                available_navigation = gb_retailapi_client.models.navigation.Navigation(
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
                    or = True, 
                    source = '', 
                    metadata = [
                        gb_retailapi_client.models.metadata.Metadata(
                            key = '', 
                            value = '', )
                        ], 
                    place_id = '', )
            )
        else:
            return FacetSearchResponseDto(
                original_request = gb_retailapi_client.models.search_request.Search Request(
                    query = 'blue sweater', 
                    area = 'Production', 
                    collection = 'default', 
                    visitor_id = '38400000-8cf0-11bd-b23e-10b96e40000d', 
                    refinements = [
                        gb_retailapi_client.models.selected_refinement.Selected Refinement(
                            navigation_name = 'brands', 
                            type = null, 
                            value = '', 
                            low = 50, 
                            high = 100, 
                            source = 'Dynamic', 
                            or = False, )
                        ], 
                    page_size = 25, 
                    skip = 50, 
                    biasing_profile = '', 
                    biasing = gb_retailapi_client.models.biasing_profile.Biasing Profile(
                        biases = [
                            gb_retailapi_client.models.bias.Bias(
                                field = 'colorFamilies', 
                                content = 'Red', 
                                strength = 'ABSOLUTE_INCREASE', )
                            ], ), 
                    custom_url_params = [
                        gb_retailapi_client.models.custom_parameter.Custom Parameter(
                            key = 'landing-page', 
                            value = 'easter-2021', )
                        ], 
                    sorts = [
                        gb_retailapi_client.models.sort.Sort(
                            field = 'rating', 
                            order = 'Ascending', )
                        ], 
                    included_navigations = [
                        ''
                        ], 
                    excluded_navigations = [
                        ''
                        ], 
                    dynamic_facet = True, 
                    variant_rollup_keys = [
                        ''
                        ], 
                    pre_filter = '(categories:ANY("Men")) AND (ageGroups:ANY("adult")) AND (price: IN(150, 200))', 
                    site = '', 
                    response_mask = ["key.innerKey.value", "key2", "key.innerKey2.value2"], 
                    page_categories = ["Sales > 2017 Black Friday Deals"], 
                    spell_correction_mode = null, 
                    include_expanded_results = True, 
                    pin_unexpanded_results = True, 
                    debug = True, 
                    facet_limit = 56, 
                    login_id = '', 
                    overwrites = null, ),
                available_navigation = gb_retailapi_client.models.navigation.Navigation(
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
                    or = True, 
                    source = '', 
                    metadata = [
                        gb_retailapi_client.models.metadata.Metadata(
                            key = '', 
                            value = '', )
                        ], 
                    place_id = '', ),
        )
        """

    def testFacetSearchResponseDto(self):
        """Test FacetSearchResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
