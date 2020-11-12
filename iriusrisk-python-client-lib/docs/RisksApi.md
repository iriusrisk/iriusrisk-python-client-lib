# swagger_client.RisksApi

All URIs are relative to *https://demo.iriusrisk.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_ref_risks_get**](RisksApi.md#products_ref_risks_get) | **GET** /products/{ref}/risks | Gets the risks summary of a product


# **products_ref_risks_get**
> RiskSummary products_ref_risks_get(api_token, ref)

Gets the risks summary of a product

This endpoint returns a summary of the risks of a product. Conditions to be able to perform the action:   - No permissions are required to perform this action. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RisksApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product

try:
    # Gets the risks summary of a product
    api_response = api_instance.products_ref_risks_get(api_token, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->products_ref_risks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| ID for product | 

### Return type

[**RiskSummary**](RiskSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

