# PredictResults

Prediction result including list of recommendations based on provided inputs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warnings** | **List[object]** | Warnings collected with validation and Recommendations AI API issues. | [optional] 
**products** | **List[Dict[str, object]]** | Recommendations built by Recommendations AI model. | [optional] 
**records** | **List[Dict[str, object]]** | Recommendations built by Recommendations AI model. | [optional] 
**model_id** | **str** | Model Id used for predictions | [optional] 
**model_name** | **str** | Model Name used for predictions | [optional] 
**model_type** | **str** |   Currently supported values:   &#x60;recommended-for-you&#x60;   &#x60;others-you-may-like&#x60;,   &#x60;frequently-bought-together&#x60;   &#x60;page-optimization&#x60;   &#x60;similar-items&#x60;,   &#x60;buy-it-again&#x60;   &#x60;on-sale-items&#x60;   &#x60;recently-viewed&#x60;    This field together with optimization_objective describe model metadata to use to control model training and   serving. See https://cloud.google.com/retail/docs/models for more details.  | [optional] 
**optimization_objective** | **str** |   Currently supported values: &#x60;ctr&#x60;, &#x60;cvr&#x60;, &#x60;revenue-per-order&#x60;.     If not specified, we choose default based on model type. Default depends on type of recommendation:   &#x60;recommended-for-you&#x60; &#x3D;&gt; &#x60;ctr&#x60;   &#x60;others-you-may-like&#x60; &#x3D;&gt; &#x60;ctr&#x60;   &#x60;frequently-bought-together&#x60; &#x3D;&gt; &#x60;revenue_per_order&#x60;    This field together with modelType describe model metadata to use to control model training and serving.   See https://cloud.google.com/retail/docs/models for more details on what the model metadata control and which   combination of parameters are valid.  | [optional] 
**filter_set** | **str** | Filter set applied to the recommendation | [optional] 
**raw_filter** | **str** | RawFilter applied to the recommendation | [optional] 
**filters** | [**List[FilterParameter]**](FilterParameter.md) | Filters applied to the recommendation | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from gb_retailapi_client.models.predict_results import PredictResults

# TODO update the JSON string below
json = "{}"
# create an instance of PredictResults from a JSON string
predict_results_instance = PredictResults.from_json(json)
# print the JSON string representation of the object
print PredictResults.to_json()

# convert the object into a dict
predict_results_dict = predict_results_instance.to_dict()
# create an instance of PredictResults from a dict
predict_results_form_dict = predict_results.from_dict(predict_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


