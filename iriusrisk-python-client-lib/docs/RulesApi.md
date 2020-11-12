# swagger_client.RulesApi

All URIs are relative to *https://demo.iriusrisk.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rules_product_ref_put**](RulesApi.md#rules_product_ref_put) | **PUT** /rules/product/{ref} | Executes rules by a product


# **rules_product_ref_put**
> rules_product_ref_put(api_token, ref, delete_countermeasures=delete_countermeasures)

Executes rules by a product

Execute the rules engine for a product and for all components within the product.  If the deleteCountermeasures parameter is true, then threats and countermeasure that no longer apply to the model will automatically be removed.  If it is false, then those threats and countermeasures will remain in the model.   - To have the permission **ARCHITECTURE_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RulesApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for Product
delete_countermeasures = 'delete_countermeasures_example' # str | This flag indicates if the rules execution will delete the threat and countermeasures which don't apply to the new product threat model. If true, the threats and countermeasures will be automatically removed from the model. If false, the threats and countermeasures won't be removed from the model. (optional)

try:
    # Executes rules by a product
    api_instance.rules_product_ref_put(api_token, ref, delete_countermeasures=delete_countermeasures)
except ApiException as e:
    print("Exception when calling RulesApi->rules_product_ref_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| ID for Product | 
 **delete_countermeasures** | **str**| This flag indicates if the rules execution will delete the threat and countermeasures which don&#39;t apply to the new product threat model. If true, the threats and countermeasures will be automatically removed from the model. If false, the threats and countermeasures won&#39;t be removed from the model. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

