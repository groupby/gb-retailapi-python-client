# gb_retailapi_client.SearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**facet_search**](SearchApi.md#facet_search) | **POST** /api/search/facet | Provided search functionality
[**search**](SearchApi.md#search) | **POST** /api/search | Provided search functionality


# **facet_search**
> FacetSearchResponseDto facet_search(x_groupby_customer_id, facet_search_request_dto)

Provided search functionality

Perform a facet search against the GroupBy Retail Search API.

### Example

* Basic Authentication (GroupByIncEmployee):
* Api Key Authentication (ClientKey):
```python
import time
import os
import gb_retailapi_client
from gb_retailapi_client.models.facet_search_request_dto import FacetSearchRequestDto
from gb_retailapi_client.models.facet_search_response_dto import FacetSearchResponseDto
from gb_retailapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gb_retailapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: GroupByIncEmployee
configuration = gb_retailapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: ClientKey
configuration.api_key['ClientKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ClientKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gb_retailapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gb_retailapi_client.SearchApi(api_client)
    x_groupby_customer_id = 'x_groupby_customer_id_example' # str | Custom HTTP header which may contain tenant name. Used to define a client by its name.
    facet_search_request_dto = gb_retailapi_client.FacetSearchRequestDto() # FacetSearchRequestDto | Request that should be populated to configure a search API call, made by the client on behalf of a shopper. Contains original request and information about facet for which extra keys requested.

    try:
        # Provided search functionality
        api_response = api_instance.facet_search(x_groupby_customer_id, facet_search_request_dto)
        print("The response of SearchApi->facet_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->facet_search: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_groupby_customer_id** | **str**| Custom HTTP header which may contain tenant name. Used to define a client by its name. | 
 **facet_search_request_dto** | [**FacetSearchRequestDto**](FacetSearchRequestDto.md)| Request that should be populated to configure a search API call, made by the client on behalf of a shopper. Contains original request and information about facet for which extra keys requested. | 

### Return type

[**FacetSearchResponseDto**](FacetSearchResponseDto.md)

### Authorization

[GroupByIncEmployee](../README.md#GroupByIncEmployee), [ClientKey](../README.md#ClientKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful facet search response. Contains original request and navigation with relevant facet keys. |  * Content-Type - In responses, a Content-Type header provides the client with the actual content type of the returned content. <br>  * Date - The Date general HTTP header contains the date and time at which the message was originated. <br>  * Content-Length - The Content-Length header indicates the size of the message body, in bytes, sent to the recipient. <br>  * Connection - The Connection general header controls whether the network connection stays open after the current transaction finishes. If the value sent is keep-alive, the connection is persistent and not closed, allowing for subsequent requests to the same server to be done. <br>  |
**400** | Client has made a bad request, usually a validation constraint has been violated. See the message for further information. |  -  |
**403** | Client is not authorized to perform the requested operation. |  -  |
**500** | There was an internal error processing the search request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> SearchResponseDto search(x_groupby_customer_id, search_request_dto)

Provided search functionality

Perform a search against the GroupBy Retail Search API.

### Example

* Basic Authentication (GroupByIncEmployee):
* Api Key Authentication (ClientKey):
```python
import time
import os
import gb_retailapi_client
from gb_retailapi_client.models.search_request_dto import SearchRequestDto
from gb_retailapi_client.models.search_response_dto import SearchResponseDto
from gb_retailapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gb_retailapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: GroupByIncEmployee
configuration = gb_retailapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: ClientKey
configuration.api_key['ClientKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ClientKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gb_retailapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gb_retailapi_client.SearchApi(api_client)
    x_groupby_customer_id = 'x_groupby_customer_id_example' # str | Custom HTTP header which may contain tenant name. Used to define a client by its name.
    search_request_dto = gb_retailapi_client.SearchRequestDto() # SearchRequestDto | Request that should be populated to configure a search API call, made by the client on behalf of a shopper.

    try:
        # Provided search functionality
        api_response = api_instance.search(x_groupby_customer_id, search_request_dto)
        print("The response of SearchApi->search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_groupby_customer_id** | **str**| Custom HTTP header which may contain tenant name. Used to define a client by its name. | 
 **search_request_dto** | [**SearchRequestDto**](SearchRequestDto.md)| Request that should be populated to configure a search API call, made by the client on behalf of a shopper. | 

### Return type

[**SearchResponseDto**](SearchResponseDto.md)

### Authorization

[GroupByIncEmployee](../README.md#GroupByIncEmployee), [ClientKey](../README.md#ClientKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search was accepted and a normal response could be generated. |  * Content-Type - In responses, a Content-Type header provides the client with the actual content type of the returned content. <br>  * Date - The Date general HTTP header contains the date and time at which the message was originated. <br>  * Content-Length - The Content-Length header indicates the size of the message body, in bytes, sent to the recipient. <br>  * Connection - The Connection general header controls whether the network connection stays open after the current transaction finishes. If the value sent is keep-alive, the connection is persistent and not closed, allowing for subsequent requests to the same server to be done. <br>  |
**400** | Client has made a bad request, usually a validation constraint has been violated. See the message for further information. |  -  |
**403** | Client is not authorized to perform the requested operation. |  -  |
**500** | There was an internal error processing the search request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

