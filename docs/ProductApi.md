# gb_retailapi_client.ProductApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_by_product_ids**](ProductApi.md#get_by_product_ids) | **GET** /api/search/product | Provided product search functionality


# **get_by_product_ids**
> ProductDto get_by_product_ids(collection, product_id, x_groupby_customer_id, variant_ids=variant_ids)

Provided product search functionality

Perform a product search against the GroupBy Retail Search API.

### Example

* Basic Authentication (GroupByIncEmployee):
* Api Key Authentication (ClientKey):
```python
import time
import os
import gb_retailapi_client
from gb_retailapi_client.models.product_dto import ProductDto
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
    api_instance = gb_retailapi_client.ProductApi(api_client)
    collection = 'collection_example' # str | Collection name
    product_id = 'product_id_example' # str | Product ID which need to be search
    x_groupby_customer_id = 'x_groupby_customer_id_example' # str | Required. This parameter will extract from header X-Groupby-Customer-Id. May contain tenant name. Used to define a                           client by its name.
    variant_ids = ['variant_ids_example'] # List[str] | Not required. If the product has variant list and the request specifies the variantIds, requested variants will be the                           first in the response. (optional)

    try:
        # Provided product search functionality
        api_response = api_instance.get_by_product_ids(collection, product_id, x_groupby_customer_id, variant_ids=variant_ids)
        print("The response of ProductApi->get_by_product_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->get_by_product_ids: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Collection name | 
 **product_id** | **str**| Product ID which need to be search | 
 **x_groupby_customer_id** | **str**| Required. This parameter will extract from header X-Groupby-Customer-Id. May contain tenant name. Used to define a                           client by its name. | 
 **variant_ids** | [**List[str]**](str.md)| Not required. If the product has variant list and the request specifies the variantIds, requested variants will be the                           first in the response. | [optional] 

### Return type

[**ProductDto**](ProductDto.md)

### Authorization

[GroupByIncEmployee](../README.md#GroupByIncEmployee), [ClientKey](../README.md#ClientKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product is found. |  * Content-Type - In responses, a Content-Type header provides the client with the actual content type of the returned content. <br>  * Date - The Date general HTTP header contains the date and time at which the message was originated. <br>  * Content-Length - The Content-Length header indicates the size of the message body, in bytes, sent to the recipient. <br>  * Connection - The Connection general header controls whether the network connection stays open after the current transaction finishes. If the value sent is keep-alive, the connection is persistent and not closed, allowing for subsequent requests to the same server to be done. <br>  |
**400** | Client has made a bad request, usually a validation constraint has been violated. See the message for further information. |  -  |
**403** | Client is not authorized to perform the requested operation. |  -  |
**500** | There was an internal error processing the search request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

