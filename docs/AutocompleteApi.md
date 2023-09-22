# gb_retailapi_client.AutocompleteApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocompletesearch**](AutocompleteApi.md#autocompletesearch) | **GET** /api/request | 


# **autocompletesearch**
> SearchResults autocompletesearch(x_groupby_customer_id, identity, merchandiser, request=request)



A simple request used to get completes the specified prefix with keyword suggestions.

### Example

* Basic Authentication (GroupByIncEmployee):
* Api Key Authentication (ClientKey):
```python
import time
import os
import gb_retailapi_client
from gb_retailapi_client.models.identity import Identity
from gb_retailapi_client.models.merchandiser import Merchandiser
from gb_retailapi_client.models.request import Request
from gb_retailapi_client.models.search_results import SearchResults
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
    api_instance = gb_retailapi_client.AutocompleteApi(api_client)
    x_groupby_customer_id = 'x_groupby_customer_id_example' # str | Header on incoming HTTP requests that is populated by the API gateway and indicates the customer ID.
    identity = gb_retailapi_client.Identity() # Identity | 
    merchandiser = gb_retailapi_client.Merchandiser() # Merchandiser | 
    request = gb_retailapi_client.Request() # Request | Object which is represent autocomplete request and encapsulate all passed parameters.  (optional)

    try:
        api_response = api_instance.autocompletesearch(x_groupby_customer_id, identity, merchandiser, request=request)
        print("The response of AutocompleteApi->autocompletesearch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutocompleteApi->autocompletesearch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_groupby_customer_id** | **str**| Header on incoming HTTP requests that is populated by the API gateway and indicates the customer ID. | 
 **identity** | [**Identity**](.md)|  | 
 **merchandiser** | [**Merchandiser**](.md)|  | 
 **request** | [**Request**](.md)| Object which is represent autocomplete request and encapsulate all passed parameters.  | [optional] 

### Return type

[**SearchResults**](SearchResults.md)

### Authorization

[GroupByIncEmployee](../README.md#GroupByIncEmployee), [ClientKey](../README.md#ClientKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response, returns result of operation. It is can be either empty body, object model or list of models. |  * Content-Type - In responses, a Content-Type header provides the client with the actual content type of the returned content. <br>  * Date - The Date general HTTP header contains the date and time at which the message was originated. <br>  * Content-Length - The Content-Length header indicates the size of the message body, in bytes, sent to the recipient. <br>  * Connection - The Connection general header controls whether the network connection stays open after the current transaction finishes. If the value sent is keep-alive, the connection is persistent and not closed, allowing for subsequent requests to the same server to be done. <br>  * Content-Encoding - The Content-Encoding representation header lists any encodings that have been applied to the representation (message payload), and in what order. This lets the recipient know how to decode the representation in order to obtain the original payload format. Content encoding is mainly used to compress the message data without losing information about the origin media type. <br>  |
**400** | Client has made a bad request, usually a validation constraint has been violated. See the message for further information. |  * Content-Type - In responses, a Content-Type header provides the client with the actual content type of the returned content. <br>  * Date - The Date general HTTP header contains the date and time at which the message was originated. <br>  * Content-Length - The Content-Length header indicates the size of the message body, in bytes, sent to the recipient. <br>  * Connection - The Connection general header controls whether the network connection stays open after the current transaction finishes. If the value sent is keep-alive, the connection is persistent and not closed, allowing for subsequent requests to the same server to be done. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

