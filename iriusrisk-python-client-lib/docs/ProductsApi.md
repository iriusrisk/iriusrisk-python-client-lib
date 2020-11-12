# iriusrisk_python_client_lib.ProductsApi

All URIs are relative to *https://demo.iriusrisk.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_get**](ProductsApi.md#products_get) | **GET** /products | Gets a list of all products.
[**products_post**](ProductsApi.md#products_post) | **POST** /products | Creates a new product
[**products_ref_components_component_ref_controls_control_ref_status_put**](ProductsApi.md#products_ref_components_component_ref_controls_control_ref_status_put) | **PUT** /products/{ref}/components/{componentRef}/controls/{controlRef}/status | Sets the desired status to a countermeasure
[**products_ref_components_component_ref_tests_cwe_put**](ProductsApi.md#products_ref_components_component_ref_tests_cwe_put) | **PUT** /products/{ref}/components/{componentRef}/tests/{cwe} | Updates a single test to a component.
[**products_ref_components_component_ref_tests_test_type_upload_post**](ProductsApi.md#products_ref_components_component_ref_tests_test_type_upload_post) | **POST** /products/{ref}/components/{componentRef}/tests/{testType}/upload | Imports test results from different sources to a component
[**products_ref_controls_get**](ProductsApi.md#products_ref_controls_get) | **GET** /products/{ref}/controls | Gets a list of all product countermeasures
[**products_ref_controls_implemented_get**](ProductsApi.md#products_ref_controls_implemented_get) | **GET** /products/{ref}/controls/implemented | Gets a list of all implemented countermeasures of a product.
[**products_ref_controls_required_get**](ProductsApi.md#products_ref_controls_required_get) | **GET** /products/{ref}/controls/required | Gets a list of all required countermeasures of a product
[**products_ref_delete**](ProductsApi.md#products_ref_delete) | **DELETE** /products/{ref} | Deletes a product
[**products_ref_diagram_image_get**](ProductsApi.md#products_ref_diagram_image_get) | **GET** /products/{ref}/diagram/image | Gets diagram image for product.
[**products_ref_get**](ProductsApi.md#products_ref_get) | **GET** /products/{ref} | Gets product details
[**products_ref_groups_delete**](ProductsApi.md#products_ref_groups_delete) | **DELETE** /products/{ref}/groups | Unassigns a list of user groups from a product.
[**products_ref_groups_get**](ProductsApi.md#products_ref_groups_get) | **GET** /products/{ref}/groups | List all groups assigned to a product
[**products_ref_groups_put**](ProductsApi.md#products_ref_groups_put) | **PUT** /products/{ref}/groups | Assigns groups of users to a product.
[**products_ref_put**](ProductsApi.md#products_ref_put) | **PUT** /products/{ref} | Updates a product
[**products_ref_risks_get**](ProductsApi.md#products_ref_risks_get) | **GET** /products/{ref}/risks | Gets the risks summary of a product
[**products_ref_tests_test_type_upload_post**](ProductsApi.md#products_ref_tests_test_type_upload_post) | **POST** /products/{ref}/tests/{testType}/upload | Imports test results from different sources to a product.
[**products_ref_threats_get**](ProductsApi.md#products_ref_threats_get) | **GET** /products/{ref}/threats | Gets a list of all threats of a product
[**products_ref_users_delete**](ProductsApi.md#products_ref_users_delete) | **DELETE** /products/{ref}/users | Unassigns a list of users from a product.
[**products_ref_users_get**](ProductsApi.md#products_ref_users_get) | **GET** /products/{ref}/users | List all users assigned to a product
[**products_ref_users_put**](ProductsApi.md#products_ref_users_put) | **PUT** /products/{ref}/users | Assigns users to a product.
[**products_ref_users_user_delete**](ProductsApi.md#products_ref_users_user_delete) | **DELETE** /products/{ref}/users/{user} | Unassigns a user from a product
[**products_ref_weaknesses_get**](ProductsApi.md#products_ref_weaknesses_get) | **GET** /products/{ref}/weaknesses | Gets a list of all weaknesses of a product
[**products_ref_weaknesses_test_state_get**](ProductsApi.md#products_ref_weaknesses_test_state_get) | **GET** /products/{ref}/weaknesses/{test_state} | Gets a list of all weaknesses of a product filtered by test state
[**products_upload_post**](ProductsApi.md#products_upload_post) | **POST** /products/upload | Creates a new product, library or template from a XML file upload.
[**products_upload_ref_post**](ProductsApi.md#products_upload_ref_post) | **POST** /products/upload/{ref} | Updates an existing product from a XML file upload.
[**rules_product_ref_put**](ProductsApi.md#rules_product_ref_put) | **PUT** /rules/product/{ref} | Executes rules by a product


# **products_get**
> list[ProductShort] products_get(api_token, max=max, index=index, workflow_state=workflow_state)

Gets a list of all products.

Gets a list of all products visible by the user who perform the call. Conditions to be able to perform the action:   - No permissions are required to perform this action. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
max = 1 # int | maximun number of items returned (optional) (default to 1)
index = 1 # int | index of the first element to return (optional) (default to 1)
workflow_state = 'workflow_state_example' # str | filter for products by workflow state ref (optional)

try:
    # Gets a list of all products.
    api_response = api_instance.products_get(api_token, max=max, index=index, workflow_state=workflow_state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **max** | **int**| maximun number of items returned | [optional] [default to 1]
 **index** | **int**| index of the first element to return | [optional] [default to 1]
 **workflow_state** | **str**| filter for products by workflow state ref | [optional] 

### Return type

[**list[ProductShort]**](ProductShort.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_post**
> ProductShort products_post(api_token, create_product_request_body)

Creates a new product

Createa a new product. Conditions to be able to perform the action:   - To have the permission **PRODUCT_CREATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
create_product_request_body = iriusrisk_python_client_lib.CreateProduct() # CreateProduct | JSON data that contains information to create new product

try:
    # Creates a new product
    api_response = api_instance.products_post(api_token, create_product_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **create_product_request_body** | [**CreateProduct**](CreateProduct.md)| JSON data that contains information to create new product | 

### Return type

[**ProductShort**](ProductShort.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product
component_ref = 'component_ref_example' # str | ID for component
control_ref = 'control_ref_example' # str | Control ref
update_status_countermeasure_request_body = iriusrisk_python_client_lib.UpdateStatusCountermeasureRequestBody() # UpdateStatusCountermeasureRequestBody | JSON data that contains the information to update countermeasure

try:
    # Sets the desired status to a countermeasure
    api_instance.products_ref_components_component_ref_controls_control_ref_status_put(api_token, ref, component_ref, control_ref, update_status_countermeasure_request_body)
except ApiException as e:
    print("Exception when calling ProductsApi->products_ref_components_component_ref_controls_control_ref_status_put: %s\n" % e)
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

# **products_ref_components_component_ref_tests_cwe_put**
> list[InlineResponse2001] products_ref_components_component_ref_tests_cwe_put(api_token, ref, component_ref, cwe, update_status_test_request_body)

Updates a single test to a component.

Updates a single test to a component. Conditions to be able to perform the action:   - To have the permission **TEST_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product
component_ref = 'component_ref_example' # str | ID for component
cwe = 'cwe_example' # str | countermeasure or weakness CWE
update_status_test_request_body = iriusrisk_python_client_lib.UpdateStatusTestRequestBody() # UpdateStatusTestRequestBody | JSON data that contains the information to update test

try:
    # Updates a single test to a component.
    api_response = api_instance.products_ref_components_component_ref_tests_cwe_put(api_token, ref, component_ref, cwe, update_status_test_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_ref_components_component_ref_tests_cwe_put: %s\n" % e)
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
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
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
    print("Exception when calling ProductsApi->products_ref_components_component_ref_tests_test_type_upload_post: %s\n" % e)
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
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product

try:
    # Gets a list of all product countermeasures
    api_response = api_instance.products_ref_controls_get(api_token, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_ref_controls_get: %s\n" % e)
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
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product

try:
    # Gets a list of all implemented countermeasures of a product.
    api_response = api_instance.products_ref_controls_implemented_get(api_token, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_ref_controls_implemented_get: %s\n" % e)
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
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product

try:
    # Gets a list of all required countermeasures of a product
    api_response = api_instance.products_ref_controls_required_get(api_token, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_ref_controls_required_get: %s\n" % e)
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

# **products_ref_delete**
> products_ref_delete(api_token, ref)

Deletes a product

Deletes a product. Conditions to be able to perform the action:   - To have the permission **PRODUCT_DELETE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product

try:
    # Deletes a product
    api_instance.products_ref_delete(api_token, ref)
except ApiException as e:
    print("Exception when calling ProductsApi->products_ref_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| ID for product | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_ref_diagram_image_get**
> str products_ref_diagram_image_get(api_token, ref)

Gets diagram image for product.

Gets a an image in png format of the product diagram. Conditions to be able to perform the action:   - No special permissions are required to perform this action.   - This API call can be used only if the user who performs the call has visibility over the product. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product

try:
    # Gets diagram image for product.
    api_response = api_instance.products_ref_diagram_image_get(api_token, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_ref_diagram_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| ID for product | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_ref_get**
> Product products_ref_get(api_token, ref)

Gets product details

Gets the details of a product. Conditions to be able to perform the action:   - No permissions are required to perform this action. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product

try:
    # Gets product details
    api_response = api_instance.products_ref_get(api_token, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_ref_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| ID for product | 

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_ref_groups_delete**
> InlineResponse200 products_ref_groups_delete(api_token, ref, unassign_groups_product_request_body)

Unassigns a list of user groups from a product.

Unassigns a list of user groups from a product. Conditions to be able to perform the action:   - To have the permission **PRODUCT_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | Reference for product
unassign_groups_product_request_body = iriusrisk_python_client_lib.UnassignGroupsProductRequestBody() # UnassignGroupsProductRequestBody | JSON object that contains information to unassign groups from a product

try:
    # Unassigns a list of user groups from a product.
    api_response = api_instance.products_ref_groups_delete(api_token, ref, unassign_groups_product_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_ref_groups_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| Reference for product | 
 **unassign_groups_product_request_body** | [**UnassignGroupsProductRequestBody**](UnassignGroupsProductRequestBody.md)| JSON object that contains information to unassign groups from a product | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_ref_groups_get**
> list[str] products_ref_groups_get(api_token, ref)

List all groups assigned to a product

List all groups assigned to a product.     Conditions to be able to perform the action:         - If the caller has the PRODUCTS_LIST_ALL permission then all products can be queried without restriction.         - Without the PRODUCTS_LIST_ALL permission, the call will only return the groups if the caller belongs to that product. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | Reference to product

try:
    # List all groups assigned to a product
    api_response = api_instance.products_ref_groups_get(api_token, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_ref_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| Reference to product | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_ref_groups_put**
> ProductShortGroups products_ref_groups_put(api_token, ref, assign_groups_product_request_body)

Assigns groups of users to a product.

Assigns groups of users to a product. Conditions to be able to perform the action:   - To have the permission **PRODUCT_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | Reference for product
assign_groups_product_request_body = iriusrisk_python_client_lib.AssignGroupsProductRequestBody() # AssignGroupsProductRequestBody | JSON object that contains information to assign groups to product

try:
    # Assigns groups of users to a product.
    api_response = api_instance.products_ref_groups_put(api_token, ref, assign_groups_product_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_ref_groups_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| Reference for product | 
 **assign_groups_product_request_body** | [**AssignGroupsProductRequestBody**](AssignGroupsProductRequestBody.md)| JSON object that contains information to assign groups to product | 

### Return type

[**ProductShortGroups**](ProductShortGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_ref_put**
> products_ref_put(api_token, ref, update_product_request_body)

Updates a product

Updates the details of a product. Conditions to be able to perform the action:   - To have the permission **PRODUCT_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product
update_product_request_body = iriusrisk_python_client_lib.UpdateProduct() # UpdateProduct | JSON data that contains product details to update

try:
    # Updates a product
    api_instance.products_ref_put(api_token, ref, update_product_request_body)
except ApiException as e:
    print("Exception when calling ProductsApi->products_ref_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| ID for product | 
 **update_product_request_body** | [**UpdateProduct**](UpdateProduct.md)| JSON data that contains product details to update | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_ref_risks_get**
> RiskSummary products_ref_risks_get(api_token, ref)

Gets the risks summary of a product

This endpoint returns a summary of the risks of a product. Conditions to be able to perform the action:   - No permissions are required to perform this action. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product

try:
    # Gets the risks summary of a product
    api_response = api_instance.products_ref_risks_get(api_token, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_ref_risks_get: %s\n" % e)
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

# **products_ref_tests_test_type_upload_post**
> InlineResponse2011 products_ref_tests_test_type_upload_post(api_token, ref, test_type, file_name=file_name)

Imports test results from different sources to a product.

Imports test results from different sources (OWASP ZAP, Cucumber, Micro Focus Fortify) uploading files. More than one file can be attached to the call. Conditions to be able to perform the action:   - To have the permission **TEST_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product
test_type = 'test_type_example' # str | Type of test to be imported (zap|cucumber|junit|hp-fortify)
file_name = '/path/to/file.txt' # file | File to upload (optional)

try:
    # Imports test results from different sources to a product.
    api_response = api_instance.products_ref_tests_test_type_upload_post(api_token, ref, test_type, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_ref_tests_test_type_upload_post: %s\n" % e)
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

# **products_ref_threats_get**
> list[ComponentUseCaseThreatShort] products_ref_threats_get(api_token, ref)

Gets a list of all threats of a product

Returns a list of all the threats of a product. Conditions to be able to perform the action:   - To have the permission **THREAT_VIEW** granted, or   - To have the permission **THREAT_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product

try:
    # Gets a list of all threats of a product
    api_response = api_instance.products_ref_threats_get(api_token, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_ref_threats_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| ID for product | 

### Return type

[**list[ComponentUseCaseThreatShort]**](ComponentUseCaseThreatShort.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_ref_users_delete**
> products_ref_users_delete(api_token, ref, unassign_users_product_request_body)

Unassigns a list of users from a product.

Unassign a list of users from a product. Conditions to be able to perform the action:   - To have the permission **PRODUCT_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | Reference for product
unassign_users_product_request_body = iriusrisk_python_client_lib.UnassignUsersProductRequestBody() # UnassignUsersProductRequestBody | JSON object that contains information to unassign users from product

try:
    # Unassigns a list of users from a product.
    api_instance.products_ref_users_delete(api_token, ref, unassign_users_product_request_body)
except ApiException as e:
    print("Exception when calling ProductsApi->products_ref_users_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| Reference for product | 
 **unassign_users_product_request_body** | [**UnassignUsersProductRequestBody**](UnassignUsersProductRequestBody.md)| JSON object that contains information to unassign users from product | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_ref_users_get**
> list[str] products_ref_users_get(api_token, ref)

List all users assigned to a product

List all users assigned to a product.     Conditions to be able to perform the action:         - No permissions are required to perform this action. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | Reference to product

try:
    # List all users assigned to a product
    api_response = api_instance.products_ref_users_get(api_token, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_ref_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| Reference to product | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_ref_users_put**
> ProductShortUsers products_ref_users_put(api_token, ref, assign_users_product_request_body)

Assigns users to a product.

Assigns users to a product. Conditions to be able to perform the action:   - To have the permission **PRODUCT_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | Reference for product
assign_users_product_request_body = iriusrisk_python_client_lib.AssignUsersProductRequestBody() # AssignUsersProductRequestBody | JSON data that contains the information to assign users to product

try:
    # Assigns users to a product.
    api_response = api_instance.products_ref_users_put(api_token, ref, assign_users_product_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_ref_users_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| Reference for product | 
 **assign_users_product_request_body** | [**AssignUsersProductRequestBody**](AssignUsersProductRequestBody.md)| JSON data that contains the information to assign users to product | 

### Return type

[**ProductShortUsers**](ProductShortUsers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_ref_users_user_delete**
> products_ref_users_user_delete(api_token, ref, user)

Unassigns a user from a product

Unassigns a user from a product. Conditions to be able to perform the action:   - To have the permission **PRODUCT_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | Reference for product
user = 'user_example' # str | Username of the user who will be unassigned from the product

try:
    # Unassigns a user from a product
    api_instance.products_ref_users_user_delete(api_token, ref, user)
except ApiException as e:
    print("Exception when calling ProductsApi->products_ref_users_user_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| Reference for product | 
 **user** | **str**| Username of the user who will be unassigned from the product | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_ref_weaknesses_get**
> list[ComponentWeakness] products_ref_weaknesses_get(api_token, ref)

Gets a list of all weaknesses of a product

Returns a list of all the weaknesses of a product. Conditions to be able to perform the action:   - To have the permission **THREAT_VIEW** granted, or   - To have the permission **THREAT_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product

try:
    # Gets a list of all weaknesses of a product
    api_response = api_instance.products_ref_weaknesses_get(api_token, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_ref_weaknesses_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| ID for product | 

### Return type

[**list[ComponentWeakness]**](ComponentWeakness.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_ref_weaknesses_test_state_get**
> list[ComponentWeakness] products_ref_weaknesses_test_state_get(api_token, ref, test_state)

Gets a list of all weaknesses of a product filtered by test state

Returns a list of all the weaknesses of a product. With the optional parameter `test_state` can filter the weakness by test state. Conditions to be able to perform the action:   - To have the permission **THREAT_VIEW** granted, or   - To have the permission **THREAT_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product
test_state = 'test_state_example' # str | Code for a test state

try:
    # Gets a list of all weaknesses of a product filtered by test state
    api_response = api_instance.products_ref_weaknesses_test_state_get(api_token, ref, test_state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_ref_weaknesses_test_state_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| ID for product | 
 **test_state** | **str**| Code for a test state | 

### Return type

[**list[ComponentWeakness]**](ComponentWeakness.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_upload_post**
> ProductShort products_upload_post(api_token, ref, name, file_name, type=type)

Creates a new product, library or template from a XML file upload.

Creates a new product, library or template from a XML file upload. Conditions to be able to perform the action: - To have the permission **PRODUCT_CREATE** granted allows to create a product. - To have the permission **LIBRARY_UPDATE** granted allows to create a library. - To have the permission **TEMPLATE_UPDATE** granted allows to create a template. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | Product ref
name = 'name_example' # str | Product name
file_name = '/path/to/file.txt' # file | File to upload in XML format
type = 'type_example' # str | Product type - STANDARD (By default), TEMPLATE or LIBRARY (optional)

try:
    # Creates a new product, library or template from a XML file upload.
    api_response = api_instance.products_upload_post(api_token, ref, name, file_name, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| Product ref | 
 **name** | **str**| Product name | 
 **file_name** | **file**| File to upload in XML format | 
 **type** | **str**| Product type - STANDARD (By default), TEMPLATE or LIBRARY | [optional] 

### Return type

[**ProductShort**](ProductShort.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_upload_ref_post**
> ProductShort products_upload_ref_post(api_token, ref, file_name, delete_countermeasures=delete_countermeasures)

Updates an existing product from a XML file upload.

Updates a product from a XML file upload. Conditions to be able to perform the action: - To have the permission **PRODUCT_UPDATE** granted allows to update a product. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product
file_name = '/path/to/file.txt' # file | File to upload in XML format
delete_countermeasures = 'delete_countermeasures_example' # str | This flag indicates if the rules execution will delete the threat and countermeasures which don't apply to the new product threat model. If true, the threats and countermeasures will be automatically removed from the model. If false, the threats and countermeasures won't be removed from the model. (optional)

try:
    # Updates an existing product from a XML file upload.
    api_response = api_instance.products_upload_ref_post(api_token, ref, file_name, delete_countermeasures=delete_countermeasures)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_upload_ref_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **ref** | **str**| ID for product | 
 **file_name** | **file**| File to upload in XML format | 
 **delete_countermeasures** | **str**| This flag indicates if the rules execution will delete the threat and countermeasures which don&#39;t apply to the new product threat model. If true, the threats and countermeasures will be automatically removed from the model. If false, the threats and countermeasures won&#39;t be removed from the model. | [optional] 

### Return type

[**ProductShort**](ProductShort.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rules_product_ref_put**
> rules_product_ref_put(api_token, ref, delete_countermeasures=delete_countermeasures)

Executes rules by a product

Execute the rules engine for a product and for all components within the product.  If the deleteCountermeasures parameter is true, then threats and countermeasure that no longer apply to the model will automatically be removed.  If it is false, then those threats and countermeasures will remain in the model.   - To have the permission **ARCHITECTURE_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.ProductsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for Product
delete_countermeasures = 'delete_countermeasures_example' # str | This flag indicates if the rules execution will delete the threat and countermeasures which don't apply to the new product threat model. If true, the threats and countermeasures will be automatically removed from the model. If false, the threats and countermeasures won't be removed from the model. (optional)

try:
    # Executes rules by a product
    api_instance.rules_product_ref_put(api_token, ref, delete_countermeasures=delete_countermeasures)
except ApiException as e:
    print("Exception when calling ProductsApi->rules_product_ref_put: %s\n" % e)
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

