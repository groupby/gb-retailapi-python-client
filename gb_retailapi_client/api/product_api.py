# coding: utf-8

"""
    GroupBy Retail

    GroupBy Retail API

    The version of the OpenAPI document: 0.0
    Contact: ops@groupbyinc.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictStr, conlist

from typing import Optional

from gb_retailapi_client.models.product_dto import ProductDto

from gb_retailapi_client.api_client import ApiClient
from gb_retailapi_client.api_response import ApiResponse
from gb_retailapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ProductApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_by_product_ids(self, collection : Annotated[StrictStr, Field(..., description="Collection name")], product_id : Annotated[StrictStr, Field(..., description="Product ID which need to be search")], x_groupby_customer_id : Annotated[StrictStr, Field(..., description="Required. This parameter will extract from header X-Groupby-Customer-Id. May contain tenant name. Used to define a                           client by its name.")], variant_ids : Annotated[Optional[conlist(StrictStr)], Field(description="Not required. If the product has variant list and the request specifies the variantIds, requested variants will be the                           first in the response.")] = None, **kwargs) -> ProductDto:  # noqa: E501
        """Provided product search functionality  # noqa: E501

        Perform a product search against the GroupBy Retail Search API.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_by_product_ids(collection, product_id, x_groupby_customer_id, variant_ids, async_req=True)
        >>> result = thread.get()

        :param collection: Collection name (required)
        :type collection: str
        :param product_id: Product ID which need to be search (required)
        :type product_id: str
        :param x_groupby_customer_id: Required. This parameter will extract from header X-Groupby-Customer-Id. May contain tenant name. Used to define a                           client by its name. (required)
        :type x_groupby_customer_id: str
        :param variant_ids: Not required. If the product has variant list and the request specifies the variantIds, requested variants will be the                           first in the response.
        :type variant_ids: List[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ProductDto
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_by_product_ids_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_by_product_ids_with_http_info(collection, product_id, x_groupby_customer_id, variant_ids, **kwargs)  # noqa: E501

    @validate_arguments
    def get_by_product_ids_with_http_info(self, collection : Annotated[StrictStr, Field(..., description="Collection name")], product_id : Annotated[StrictStr, Field(..., description="Product ID which need to be search")], x_groupby_customer_id : Annotated[StrictStr, Field(..., description="Required. This parameter will extract from header X-Groupby-Customer-Id. May contain tenant name. Used to define a                           client by its name.")], variant_ids : Annotated[Optional[conlist(StrictStr)], Field(description="Not required. If the product has variant list and the request specifies the variantIds, requested variants will be the                           first in the response.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Provided product search functionality  # noqa: E501

        Perform a product search against the GroupBy Retail Search API.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_by_product_ids_with_http_info(collection, product_id, x_groupby_customer_id, variant_ids, async_req=True)
        >>> result = thread.get()

        :param collection: Collection name (required)
        :type collection: str
        :param product_id: Product ID which need to be search (required)
        :type product_id: str
        :param x_groupby_customer_id: Required. This parameter will extract from header X-Groupby-Customer-Id. May contain tenant name. Used to define a                           client by its name. (required)
        :type x_groupby_customer_id: str
        :param variant_ids: Not required. If the product has variant list and the request specifies the variantIds, requested variants will be the                           first in the response.
        :type variant_ids: List[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ProductDto, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://search.{environment}.groupbycloud.com'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'collection',
            'product_id',
            'x_groupby_customer_id',
            'variant_ids'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_by_product_ids" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('collection') is not None:  # noqa: E501
            _query_params.append(('collection', _params['collection']))

        if _params.get('product_id') is not None:  # noqa: E501
            _query_params.append(('productId', _params['product_id']))

        if _params.get('variant_ids') is not None:  # noqa: E501
            _query_params.append(('variantIds', _params['variant_ids']))
            _collection_formats['variantIds'] = 'multi'

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['x_groupby_customer_id']:
            _header_params['X-Groupby-Customer-Id'] = _params['x_groupby_customer_id']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['GroupByIncEmployee', 'ClientKey']  # noqa: E501

        _response_types_map = {
            '200': "ProductDto",
            '400': "ErrorDto",
            '403': "ErrorDto",
            '500': "ErrorDto",
        }

        return self.api_client.call_api(
            '/api/search/product', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
