# gb_retailapi_client.RecommendationsAPIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**predict**](RecommendationsAPIApi.md#predict) | **POST** /api/predict | Provide Recommendations AI functionality.
[**predict_v2**](RecommendationsAPIApi.md#predict_v2) | **POST** /api/recommendation | Provide Recommendations AI functionality.


# **predict**
> PredictResults predict(x_groupby_customer_id, recommendations_request)

Provide Recommendations AI functionality.

Perform a recommendation request against the GroupBy Retail Recommendations API.

### Example

* Basic Authentication (GroupByIncEmployee):
* Api Key Authentication (ClientKey):
```python
import time
import os
import gb_retailapi_client
from gb_retailapi_client.models.predict_results import PredictResults
from gb_retailapi_client.models.recommendations_request import RecommendationsRequest
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
    api_instance = gb_retailapi_client.RecommendationsAPIApi(api_client)
    x_groupby_customer_id = 'x_groupby_customer_id_example' # str | Custom HTTP header which may contain tenant name. Used to define a client by its name.
    recommendations_request = gb_retailapi_client.RecommendationsRequest() # RecommendationsRequest | Request that should be populated to configure a recommendations API call made by the client.

    try:
        # Provide Recommendations AI functionality.
        api_response = api_instance.predict(x_groupby_customer_id, recommendations_request)
        print("The response of RecommendationsAPIApi->predict:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationsAPIApi->predict: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_groupby_customer_id** | **str**| Custom HTTP header which may contain tenant name. Used to define a client by its name. | 
 **recommendations_request** | [**RecommendationsRequest**](RecommendationsRequest.md)| Request that should be populated to configure a recommendations API call made by the client. | 

### Return type

[**PredictResults**](PredictResults.md)

### Authorization

[GroupByIncEmployee](../README.md#GroupByIncEmployee), [ClientKey](../README.md#ClientKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * Content-Type - In responses, a Content-Type header provides the client with the actual content type of the returned content. <br>  * Date - The Date general HTTP header contains the date and time at which the message was originated. <br>  * Content-Length - The Content-Length header indicates the size of the message body, in bytes, sent to the recipient. <br>  * Connection - The Connection general header controls whether the network connection stays open after the current transaction finishes. If the value sent is keep-alive, the connection is persistent and not closed, allowing for subsequent requests to the same server to be done. <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **predict_v2**
> PredictResults predict_v2(x_groupby_customer_id, recommendations_request)

Provide Recommendations AI functionality.

Perform a recommendation request against the GroupBy Retail Recommendations API.

### Example

* Basic Authentication (GroupByIncEmployee):
* Api Key Authentication (ClientKey):
```python
import time
import os
import gb_retailapi_client
from gb_retailapi_client.models.predict_results import PredictResults
from gb_retailapi_client.models.recommendations_request import RecommendationsRequest
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
    api_instance = gb_retailapi_client.RecommendationsAPIApi(api_client)
    x_groupby_customer_id = 'x_groupby_customer_id_example' # str | Custom HTTP header which may contain tenant name. Used to define a client by its name.
    recommendations_request = gb_retailapi_client.RecommendationsRequest() # RecommendationsRequest | Request that should be populated to configure a recommendations API call made by the client.

    try:
        # Provide Recommendations AI functionality.
        api_response = api_instance.predict_v2(x_groupby_customer_id, recommendations_request)
        print("The response of RecommendationsAPIApi->predict_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationsAPIApi->predict_v2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_groupby_customer_id** | **str**| Custom HTTP header which may contain tenant name. Used to define a client by its name. | 
 **recommendations_request** | [**RecommendationsRequest**](RecommendationsRequest.md)| Request that should be populated to configure a recommendations API call made by the client. | 

### Return type

[**PredictResults**](PredictResults.md)

### Authorization

[GroupByIncEmployee](../README.md#GroupByIncEmployee), [ClientKey](../README.md#ClientKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * Content-Type - In responses, a Content-Type header provides the client with the actual content type of the returned content. <br>  * Date - The Date general HTTP header contains the date and time at which the message was originated. <br>  * Content-Length - The Content-Length header indicates the size of the message body, in bytes, sent to the recipient. <br>  * Connection - The Connection general header controls whether the network connection stays open after the current transaction finishes. If the value sent is keep-alive, the connection is persistent and not closed, allowing for subsequent requests to the same server to be done. <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

