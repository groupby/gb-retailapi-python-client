# gb-retailapi-client
GroupBy Retail API

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/groupby/gb-retailapi-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/groupby/gb-retailapi-python-client.git`)

Then import the package:
```python
import gb_retailapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import gb_retailapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import gb_retailapi_client
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
    except ApiException as e:
        print("Exception when calling AutocompleteApi->autocompletesearch: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AutocompleteApi* | [**autocompletesearch**](docs/AutocompleteApi.md#autocompletesearch) | **GET** /api/request | 
*ProductApi* | [**get_by_product_ids**](docs/ProductApi.md#get_by_product_ids) | **GET** /api/search/product | Provided product search functionality
*RecommendationsAPIApi* | [**predict**](docs/RecommendationsAPIApi.md#predict) | **POST** /api/predict | Provide Recommendations AI functionality.
*RecommendationsAPIApi* | [**predict_v2**](docs/RecommendationsAPIApi.md#predict_v2) | **POST** /api/recommendation | Provide Recommendations AI functionality.
*SearchApi* | [**facet_search**](docs/SearchApi.md#facet_search) | **POST** /api/search/facet | Provided search functionality
*SearchApi* | [**search**](docs/SearchApi.md#search) | **POST** /api/search | Provided search functionality


## Documentation For Models

 - [AdditionalInfo](docs/AdditionalInfo.md)
 - [AttributeSuggestion](docs/AttributeSuggestion.md)
 - [Audience](docs/Audience.md)
 - [BiasDto](docs/BiasDto.md)
 - [BiasDtoStrengthDto](docs/BiasDtoStrengthDto.md)
 - [BiasingProfileDto](docs/BiasingProfileDto.md)
 - [BoostedProductBucket](docs/BoostedProductBucket.md)
 - [ColorInfo](docs/ColorInfo.md)
 - [CustomParameterDto](docs/CustomParameterDto.md)
 - [CustomParameterTrigger](docs/CustomParameterTrigger.md)
 - [DebugDto](docs/DebugDto.md)
 - [ErrorDto](docs/ErrorDto.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [Experiment](docs/Experiment.md)
 - [ExperimentVariant](docs/ExperimentVariant.md)
 - [Facet](docs/Facet.md)
 - [FacetSearchRequestDto](docs/FacetSearchRequestDto.md)
 - [FacetSearchResponseDto](docs/FacetSearchResponseDto.md)
 - [FieldMask](docs/FieldMask.md)
 - [Filter](docs/Filter.md)
 - [FilterParameter](docs/FilterParameter.md)
 - [FulfillmentInfo](docs/FulfillmentInfo.md)
 - [Identity](docs/Identity.md)
 - [Image](docs/Image.md)
 - [Interval](docs/Interval.md)
 - [Merchandiser](docs/Merchandiser.md)
 - [MessageType](docs/MessageType.md)
 - [Metadata](docs/Metadata.md)
 - [NavigationDto](docs/NavigationDto.md)
 - [NavigationType](docs/NavigationType.md)
 - [NavigationTypeDto](docs/NavigationTypeDto.md)
 - [Order](docs/Order.md)
 - [Overwrites](docs/Overwrites.md)
 - [PageInfoDto](docs/PageInfoDto.md)
 - [PinnedRefinement](docs/PinnedRefinement.md)
 - [PredictResults](docs/PredictResults.md)
 - [PriceInfo](docs/PriceInfo.md)
 - [PriceInfoPriceEffectiveTime](docs/PriceInfoPriceEffectiveTime.md)
 - [PriceInfoPriceExpireTime](docs/PriceInfoPriceExpireTime.md)
 - [PriceInfoPriceRange](docs/PriceInfoPriceRange.md)
 - [PriceInfoPriceRangeOriginalPrice](docs/PriceInfoPriceRangeOriginalPrice.md)
 - [PriceInfoPriceRangePrice](docs/PriceInfoPriceRangePrice.md)
 - [ProductCustomAttribute](docs/ProductCustomAttribute.md)
 - [ProductDto](docs/ProductDto.md)
 - [ProductDtoAudience](docs/ProductDtoAudience.md)
 - [ProductDtoAvailableTime](docs/ProductDtoAvailableTime.md)
 - [ProductDtoColorInfo](docs/ProductDtoColorInfo.md)
 - [ProductDtoPriceInfo](docs/ProductDtoPriceInfo.md)
 - [ProductDtoPublishTime](docs/ProductDtoPublishTime.md)
 - [ProductDtoRating](docs/ProductDtoRating.md)
 - [ProductDtoRetrievableFields](docs/ProductDtoRetrievableFields.md)
 - [Promotion](docs/Promotion.md)
 - [QueryPatternTrigger](docs/QueryPatternTrigger.md)
 - [QueryPatternTriggerType](docs/QueryPatternTriggerType.md)
 - [Range](docs/Range.md)
 - [RangeFilter](docs/RangeFilter.md)
 - [Rating](docs/Rating.md)
 - [RecommendationsErrorResponse](docs/RecommendationsErrorResponse.md)
 - [RecommendationsRequest](docs/RecommendationsRequest.md)
 - [RecordDto](docs/RecordDto.md)
 - [Refinement](docs/Refinement.md)
 - [RefinementDto](docs/RefinementDto.md)
 - [Request](docs/Request.md)
 - [Role](docs/Role.md)
 - [RuleConfiguration](docs/RuleConfiguration.md)
 - [RuleTemplate](docs/RuleTemplate.md)
 - [RuleTemplateSection](docs/RuleTemplateSection.md)
 - [RuleType](docs/RuleType.md)
 - [RuleVariant](docs/RuleVariant.md)
 - [SearchFilter](docs/SearchFilter.md)
 - [SearchMetadataDto](docs/SearchMetadataDto.md)
 - [SearchRequestDto](docs/SearchRequestDto.md)
 - [SearchRequestDtoOverwrites](docs/SearchRequestDtoOverwrites.md)
 - [SearchResponseDto](docs/SearchResponseDto.md)
 - [SearchResults](docs/SearchResults.md)
 - [SearchResultsStats](docs/SearchResultsStats.md)
 - [SearchTerms](docs/SearchTerms.md)
 - [SelectedRefinementDto](docs/SelectedRefinementDto.md)
 - [SelectedRefinementTrigger](docs/SelectedRefinementTrigger.md)
 - [SelectedRefinementTriggerType](docs/SelectedRefinementTriggerType.md)
 - [Sort](docs/Sort.md)
 - [SortDto](docs/SortDto.md)
 - [SortDtoOrderDto](docs/SortDtoOrderDto.md)
 - [SpellCorrectionMode](docs/SpellCorrectionMode.md)
 - [Stats](docs/Stats.md)
 - [TemplateDto](docs/TemplateDto.md)
 - [TemplateDtoTriggerSet](docs/TemplateDtoTriggerSet.md)
 - [Timestamp](docs/Timestamp.md)
 - [TriggerSet](docs/TriggerSet.md)
 - [ValueFilter](docs/ValueFilter.md)
 - [ValueFilterValueFilterType](docs/ValueFilterValueFilterType.md)
 - [ZoneDto](docs/ZoneDto.md)
 - [ZoneDtoType](docs/ZoneDtoType.md)
 - [ZoneType](docs/ZoneType.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ClientKey"></a>
### ClientKey

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

<a id="GroupByIncEmployee"></a>
### GroupByIncEmployee

- **Type**: HTTP basic authentication


## Author

ops@groupbyinc.com


