# swagger_client.WeaknessesApi

All URIs are relative to *https://demo.iriusrisk.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put**](WeaknessesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/weaknesses | Associates weakness to a threat in a risk pattern.
[**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put**](WeaknessesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/weaknesses/{weaknessRef}/countermeasures | Associates a countermeasure to a weakness in a risk pattern.
[**libraries_library_ref_riskpatterns_risk_pattern_ref_weaknesses_post**](WeaknessesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_weaknesses_post) | **POST** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/weaknesses | Creates a new weakness in a risk pattern
[**products_ref_weaknesses_get**](WeaknessesApi.md#products_ref_weaknesses_get) | **GET** /products/{ref}/weaknesses | Gets a list of all weaknesses of a product
[**products_ref_weaknesses_test_state_get**](WeaknessesApi.md#products_ref_weaknesses_test_state_get) | **GET** /products/{ref}/weaknesses/{test_state} | Gets a list of all weaknesses of a product filtered by test state


# **libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put**
> LibraryWeakness libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put(api_token, library_ref, risk_pattern_ref, use_case_ref, threat_ref, associate_weakness_threat_library_request_body)

Associates weakness to a threat in a risk pattern.

Associates weakness to a threat in a risk pattern. Conditions to be able to perform the action:   - To have the permission **LIBRARY_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeaknessesApi()
api_token = 'api_token_example' # str | Authentication token
library_ref = 'library_ref_example' # str | Reference for library
risk_pattern_ref = 'risk_pattern_ref_example' # str | Reference for Risk Pattern
use_case_ref = 'use_case_ref_example' # str | Reference for Use Case
threat_ref = 'threat_ref_example' # str | Reference for Threat
associate_weakness_threat_library_request_body = swagger_client.AssociateWeaknessThreatLibraryRequestBody() # AssociateWeaknessThreatLibraryRequestBody | JSON data that contains information of the fields

try:
    # Associates weakness to a threat in a risk pattern.
    api_response = api_instance.libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put(api_token, library_ref, risk_pattern_ref, use_case_ref, threat_ref, associate_weakness_threat_library_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeaknessesApi->libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **library_ref** | **str**| Reference for library | 
 **risk_pattern_ref** | **str**| Reference for Risk Pattern | 
 **use_case_ref** | **str**| Reference for Use Case | 
 **threat_ref** | **str**| Reference for Threat | 
 **associate_weakness_threat_library_request_body** | [**AssociateWeaknessThreatLibraryRequestBody**](AssociateWeaknessThreatLibraryRequestBody.md)| JSON data that contains information of the fields | 

### Return type

[**LibraryWeakness**](LibraryWeakness.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put**
> LibraryControl libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put(api_token, library_ref, risk_pattern_ref, use_case_ref, threat_ref, weakness_ref, associate_countermeasure_weakness_library_request_body)

Associates a countermeasure to a weakness in a risk pattern.

Associates a countermeasure to a weakness in a risk pattern. Conditions to be able to perform the action:   - To have the permission **LIBRARY_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeaknessesApi()
api_token = 'api_token_example' # str | Authentication token
library_ref = 'library_ref_example' # str | Reference for library
risk_pattern_ref = 'risk_pattern_ref_example' # str | Reference for Risk Pattern
use_case_ref = 'use_case_ref_example' # str | Reference for Use Case
threat_ref = 'threat_ref_example' # str | Reference for Threat
weakness_ref = 'weakness_ref_example' # str | Reference for Weakness
associate_countermeasure_weakness_library_request_body = swagger_client.AssociateCountermeasureWeaknessLibraryRequestBody() # AssociateCountermeasureWeaknessLibraryRequestBody | JSON data that contains information of the fields

try:
    # Associates a countermeasure to a weakness in a risk pattern.
    api_response = api_instance.libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put(api_token, library_ref, risk_pattern_ref, use_case_ref, threat_ref, weakness_ref, associate_countermeasure_weakness_library_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeaknessesApi->libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **library_ref** | **str**| Reference for library | 
 **risk_pattern_ref** | **str**| Reference for Risk Pattern | 
 **use_case_ref** | **str**| Reference for Use Case | 
 **threat_ref** | **str**| Reference for Threat | 
 **weakness_ref** | **str**| Reference for Weakness | 
 **associate_countermeasure_weakness_library_request_body** | [**AssociateCountermeasureWeaknessLibraryRequestBody**](AssociateCountermeasureWeaknessLibraryRequestBody.md)| JSON data that contains information of the fields | 

### Return type

[**LibraryControl**](LibraryControl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **libraries_library_ref_riskpatterns_risk_pattern_ref_weaknesses_post**
> LibraryWeakness libraries_library_ref_riskpatterns_risk_pattern_ref_weaknesses_post(api_token, library_ref, risk_pattern_ref, create_weakness_library_request_body)

Creates a new weakness in a risk pattern

Creates a new Weakness in a risk pattern. Conditions to be able to perform the action:   - To have the permission **LIBRARY_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeaknessesApi()
api_token = 'api_token_example' # str | Authentication token
library_ref = 'library_ref_example' # str | Reference for library
risk_pattern_ref = 'risk_pattern_ref_example' # str | Reference for Risk Pattern
create_weakness_library_request_body = swagger_client.CreateWeaknessLibraryRequestBody() # CreateWeaknessLibraryRequestBody | JSON data that contains information of the fields

try:
    # Creates a new weakness in a risk pattern
    api_response = api_instance.libraries_library_ref_riskpatterns_risk_pattern_ref_weaknesses_post(api_token, library_ref, risk_pattern_ref, create_weakness_library_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeaknessesApi->libraries_library_ref_riskpatterns_risk_pattern_ref_weaknesses_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **library_ref** | **str**| Reference for library | 
 **risk_pattern_ref** | **str**| Reference for Risk Pattern | 
 **create_weakness_library_request_body** | [**CreateWeaknessLibraryRequestBody**](CreateWeaknessLibraryRequestBody.md)| JSON data that contains information of the fields | 

### Return type

[**LibraryWeakness**](LibraryWeakness.md)

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
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeaknessesApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product

try:
    # Gets a list of all weaknesses of a product
    api_response = api_instance.products_ref_weaknesses_get(api_token, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeaknessesApi->products_ref_weaknesses_get: %s\n" % e)
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
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeaknessesApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product
test_state = 'test_state_example' # str | Code for a test state

try:
    # Gets a list of all weaknesses of a product filtered by test state
    api_response = api_instance.products_ref_weaknesses_test_state_get(api_token, ref, test_state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeaknessesApi->products_ref_weaknesses_test_state_get: %s\n" % e)
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

