# swagger_client.TestsApi

All URIs are relative to *https://demo.iriusrisk.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_ref_components_component_ref_tests_cwe_put**](TestsApi.md#products_ref_components_component_ref_tests_cwe_put) | **PUT** /products/{ref}/components/{componentRef}/tests/{cwe} | Updates a single test to a component.
[**products_ref_components_component_ref_tests_test_type_upload_post**](TestsApi.md#products_ref_components_component_ref_tests_test_type_upload_post) | **POST** /products/{ref}/components/{componentRef}/tests/{testType}/upload | Imports test results from different sources to a component
[**products_ref_tests_test_type_upload_post**](TestsApi.md#products_ref_tests_test_type_upload_post) | **POST** /products/{ref}/tests/{testType}/upload | Imports test results from different sources to a product.


# **products_ref_components_component_ref_tests_cwe_put**
> list[InlineResponse2001] products_ref_components_component_ref_tests_cwe_put(api_token, ref, component_ref, cwe, update_status_test_request_body)

Updates a single test to a component.

Updates a single test to a component. Conditions to be able to perform the action:   - To have the permission **TEST_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TestsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product
component_ref = 'component_ref_example' # str | ID for component
cwe = 'cwe_example' # str | countermeasure or weakness CWE
update_status_test_request_body = swagger_client.UpdateStatusTestRequestBody() # UpdateStatusTestRequestBody | JSON data that contains the information to update test

try:
    # Updates a single test to a component.
    api_response = api_instance.products_ref_components_component_ref_tests_cwe_put(api_token, ref, component_ref, cwe, update_status_test_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestsApi->products_ref_components_component_ref_tests_cwe_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| ID for product | 
 **component_ref** | **str**| ID for component | 
 **cwe** | **str**| countermeasure or weakness CWE | 
 **update_status_test_request_body** | [**UpdateStatusTestRequestBody**](UpdateStatusTestRequestBody.md)| JSON data that contains the information to update test | 

### Return type

[**list[InlineResponse2001]**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_ref_components_component_ref_tests_test_type_upload_post**
> InlineResponse2011 products_ref_components_component_ref_tests_test_type_upload_post(api_token, ref, component_ref, test_type, file_name=file_name)

Imports test results from different sources to a component

Imports test results from different sources (OWASP ZAP, Cucumber, Micro Focus Fortify) into the specified component. More than one file can be attached to the call. Conditions to be able to perform the action:   - To have the permission **TEST_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TestsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product
component_ref = 'component_ref_example' # str | ID for component
test_type = 'test_type_example' # str | Type of test to be imported (zap|cucumber|junit|hp-fortify)
file_name = '/path/to/file.txt' # file | File to upload (optional)

try:
    # Imports test results from different sources to a component
    api_response = api_instance.products_ref_components_component_ref_tests_test_type_upload_post(api_token, ref, component_ref, test_type, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestsApi->products_ref_components_component_ref_tests_test_type_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| ID for product | 
 **component_ref** | **str**| ID for component | 
 **test_type** | **str**| Type of test to be imported (zap|cucumber|junit|hp-fortify) | 
 **file_name** | **file**| File to upload | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_ref_tests_test_type_upload_post**
> InlineResponse2011 products_ref_tests_test_type_upload_post(api_token, ref, test_type, file_name=file_name)

Imports test results from different sources to a product.

Imports test results from different sources (OWASP ZAP, Cucumber, Micro Focus Fortify) uploading files. More than one file can be attached to the call. Conditions to be able to perform the action:   - To have the permission **TEST_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TestsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product
test_type = 'test_type_example' # str | Type of test to be imported (zap|cucumber|junit|hp-fortify)
file_name = '/path/to/file.txt' # file | File to upload (optional)

try:
    # Imports test results from different sources to a product.
    api_response = api_instance.products_ref_tests_test_type_upload_post(api_token, ref, test_type, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestsApi->products_ref_tests_test_type_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| ID for product | 
 **test_type** | **str**| Type of test to be imported (zap|cucumber|junit|hp-fortify) | 
 **file_name** | **file**| File to upload | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

