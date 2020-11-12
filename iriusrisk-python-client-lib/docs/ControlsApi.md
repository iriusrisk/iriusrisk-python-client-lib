# iriusrisk_python_client_lib.ControlsApi

All URIs are relative to *https://demo.iriusrisk.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_ref_components_component_ref_controls_control_ref_status_put**](ControlsApi.md#products_ref_components_component_ref_controls_control_ref_status_put) | **PUT** /products/{ref}/components/{componentRef}/controls/{controlRef}/status | Sets the desired status to a countermeasure
[**products_ref_controls_get**](ControlsApi.md#products_ref_controls_get) | **GET** /products/{ref}/controls | Gets a list of all product countermeasures
[**products_ref_controls_implemented_get**](ControlsApi.md#products_ref_controls_implemented_get) | **GET** /products/{ref}/controls/implemented | Gets a list of all implemented countermeasures of a product.
[**products_ref_controls_required_get**](ControlsApi.md#products_ref_controls_required_get) | **GET** /products/{ref}/controls/required | Gets a list of all required countermeasures of a product


# **products_ref_components_component_ref_controls_control_ref_status_put**
> products_ref_components_component_ref_controls_control_ref_status_put(api_token, ref, component_ref, control_ref, update_status_countermeasure_request_body)

Sets the desired status to a countermeasure

Sets the desired status to a countermeasure. Possible values are:             - implemented             - recommended             - rejected             - required Conditions to be able to perform the action:   - To have the permission **COUNTERMEASURE_UPDATE** granted to set any state.   - To have the permission **COUNTERMEASURE_SELECT_IMPLEMENTED** granted to set implemented state.   - To have the permission **COUNTERMEASURE_SELECT_RECOMMENDED** granted to set recommended state.   - To have the permission **COUNTERMEASURE_SELECT_REJECTED** granted to set reject state.   - To have the permission **COUNTERMEASURE_SELECT_REQUIRED** granted to set required state. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ControlsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product
component_ref = 'component_ref_example' # str | ID for component
control_ref = 'control_ref_example' # str | Control ref
update_status_countermeasure_request_body = iriusrisk_python_client_lib.UpdateStatusCountermeasureRequestBody() # UpdateStatusCountermeasureRequestBody | JSON data that contains the information to update countermeasure

try:
    # Sets the desired status to a countermeasure
    api_instance.products_ref_components_component_ref_controls_control_ref_status_put(api_token, ref, component_ref, control_ref, update_status_countermeasure_request_body)
except ApiException as e:
    print("Exception when calling ControlsApi->products_ref_components_component_ref_controls_control_ref_status_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| ID for product | 
 **component_ref** | **str**| ID for component | 
 **control_ref** | **str**| Control ref | 
 **update_status_countermeasure_request_body** | [**UpdateStatusCountermeasureRequestBody**](UpdateStatusCountermeasureRequestBody.md)| JSON data that contains the information to update countermeasure | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_ref_controls_get**
> list[ComponentControl] products_ref_controls_get(api_token, ref)

Gets a list of all product countermeasures

Returns a list of all the countermeasures of a product. Conditions to be able to perform the action:   - To have the permission **COUNTERMEASURE_VIEW** granted, or   - To have the permission **COUNTERMEASURE_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ControlsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product

try:
    # Gets a list of all product countermeasures
    api_response = api_instance.products_ref_controls_get(api_token, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ControlsApi->products_ref_controls_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| ID for product | 

### Return type

[**list[ComponentControl]**](ComponentControl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_ref_controls_implemented_get**
> list[ComponentControl] products_ref_controls_implemented_get(api_token, ref)

Gets a list of all implemented countermeasures of a product.

Returns a list of all the implemented countermeasures of a product. Conditions to be able to perform the action:   - To have the permission **COUNTERMEASURE_VIEW** granted, or   - To have the permission **COUNTERMEASURE_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ControlsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product

try:
    # Gets a list of all implemented countermeasures of a product.
    api_response = api_instance.products_ref_controls_implemented_get(api_token, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ControlsApi->products_ref_controls_implemented_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| ID for product | 

### Return type

[**list[ComponentControl]**](ComponentControl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_ref_controls_required_get**
> list[ComponentControl] products_ref_controls_required_get(api_token, ref)

Gets a list of all required countermeasures of a product

Returns a list of all the required countermeasures of a product. Conditions to be able to perform the action:   - To have the permission **COUNTERMEASURE_VIEW** granted, or   - To have the permission **COUNTERMEASURE_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ControlsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product

try:
    # Gets a list of all required countermeasures of a product
    api_response = api_instance.products_ref_controls_required_get(api_token, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ControlsApi->products_ref_controls_required_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| ID for product | 

### Return type

[**list[ComponentControl]**](ComponentControl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

