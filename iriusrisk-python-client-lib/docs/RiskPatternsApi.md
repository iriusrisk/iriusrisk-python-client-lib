# swagger_client.RiskPatternsApi

All URIs are relative to *https://demo.iriusrisk.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**libraries_library_ref_riskpatterns_post**](RiskPatternsApi.md#libraries_library_ref_riskpatterns_post) | **POST** /libraries/{libraryRef}/riskpatterns | Creates new Risk Pattern
[**libraries_library_ref_riskpatterns_risk_pattern_ref_countermeasures_post**](RiskPatternsApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_countermeasures_post) | **POST** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/countermeasures | Creates new countermeasure in a risk pattern
[**libraries_library_ref_riskpatterns_risk_pattern_ref_delete**](RiskPatternsApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_delete) | **DELETE** /libraries/{libraryRef}/riskpatterns/{riskPatternRef} | Deletes a Risk Pattern
[**libraries_library_ref_riskpatterns_risk_pattern_ref_get**](RiskPatternsApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_get) | **GET** /libraries/{libraryRef}/riskpatterns/{riskPatternRef} | Gets Risk Pattern details
[**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put**](RiskPatternsApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/weaknesses | Associates weakness to a threat in a risk pattern.
[**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put**](RiskPatternsApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/weaknesses/{weaknessRef}/countermeasures | Associates a countermeasure to a weakness in a risk pattern.
[**libraries_library_ref_riskpatterns_risk_pattern_ref_weaknesses_post**](RiskPatternsApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_weaknesses_post) | **POST** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/weaknesses | Creates a new weakness in a risk pattern


# **libraries_library_ref_riskpatterns_post**
> RiskPattern libraries_library_ref_riskpatterns_post(api_token, library_ref, create_risk_pattern_request_body)

Creates new Risk Pattern

Creates new Risk Pattern. Conditions to be able to perform the action:   - To have the permission **LIBRARY_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RiskPatternsApi()
api_token = 'api_token_example' # str | Authentication token
library_ref = 'library_ref_example' # str | Reference for library
create_risk_pattern_request_body = swagger_client.CreateRiskPatternRequestBody() # CreateRiskPatternRequestBody | JSON data that contains information of the fields

try:
    # Creates new Risk Pattern
    api_response = api_instance.libraries_library_ref_riskpatterns_post(api_token, library_ref, create_risk_pattern_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskPatternsApi->libraries_library_ref_riskpatterns_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **library_ref** | **str**| Reference for library | 
 **create_risk_pattern_request_body** | [**CreateRiskPatternRequestBody**](CreateRiskPatternRequestBody.md)| JSON data that contains information of the fields | 

### Return type

[**RiskPattern**](RiskPattern.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **libraries_library_ref_riskpatterns_risk_pattern_ref_countermeasures_post**
> LibraryControl libraries_library_ref_riskpatterns_risk_pattern_ref_countermeasures_post(api_token, library_ref, risk_pattern_ref, create_countermeasure_library_request_body)

Creates new countermeasure in a risk pattern

Creates new countermeasure in a risk pattern. Conditions to be able to perform the action:   - To have the permission **LIBRARY_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RiskPatternsApi()
api_token = 'api_token_example' # str | Authentication token
library_ref = 'library_ref_example' # str | Reference for library
risk_pattern_ref = 'risk_pattern_ref_example' # str | Reference for Risk Pattern
create_countermeasure_library_request_body = swagger_client.ControlCommand() # ControlCommand | JSON data that contains information of the fields

try:
    # Creates new countermeasure in a risk pattern
    api_response = api_instance.libraries_library_ref_riskpatterns_risk_pattern_ref_countermeasures_post(api_token, library_ref, risk_pattern_ref, create_countermeasure_library_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskPatternsApi->libraries_library_ref_riskpatterns_risk_pattern_ref_countermeasures_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **library_ref** | **str**| Reference for library | 
 **risk_pattern_ref** | **str**| Reference for Risk Pattern | 
 **create_countermeasure_library_request_body** | [**ControlCommand**](ControlCommand.md)| JSON data that contains information of the fields | 

### Return type

[**LibraryControl**](LibraryControl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **libraries_library_ref_riskpatterns_risk_pattern_ref_delete**
> libraries_library_ref_riskpatterns_risk_pattern_ref_delete(api_token, library_ref, risk_pattern_ref)

Deletes a Risk Pattern

Deletes a Risk Pattern. Conditions to be able to perform the action:   - To have the permission **LIBRARY_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RiskPatternsApi()
api_token = 'api_token_example' # str | Authentication token
library_ref = 'library_ref_example' # str | Reference for library
risk_pattern_ref = 'risk_pattern_ref_example' # str | Reference for Risk Pattern

try:
    # Deletes a Risk Pattern
    api_instance.libraries_library_ref_riskpatterns_risk_pattern_ref_delete(api_token, library_ref, risk_pattern_ref)
except ApiException as e:
    print("Exception when calling RiskPatternsApi->libraries_library_ref_riskpatterns_risk_pattern_ref_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **library_ref** | **str**| Reference for library | 
 **risk_pattern_ref** | **str**| Reference for Risk Pattern | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **libraries_library_ref_riskpatterns_risk_pattern_ref_get**
> RiskPattern libraries_library_ref_riskpatterns_risk_pattern_ref_get(api_token, library_ref, risk_pattern_ref)

Gets Risk Pattern details

Gets Risk Pattern details. Conditions to be able to perform the action:   - To have the permission **LIBRARY_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RiskPatternsApi()
api_token = 'api_token_example' # str | Authentication token
library_ref = 'library_ref_example' # str | Reference for library
risk_pattern_ref = 'risk_pattern_ref_example' # str | Reference for Risk Pattern

try:
    # Gets Risk Pattern details
    api_response = api_instance.libraries_library_ref_riskpatterns_risk_pattern_ref_get(api_token, library_ref, risk_pattern_ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskPatternsApi->libraries_library_ref_riskpatterns_risk_pattern_ref_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **library_ref** | **str**| Reference for library | 
 **risk_pattern_ref** | **str**| Reference for Risk Pattern | 

### Return type

[**RiskPattern**](RiskPattern.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = swagger_client.RiskPatternsApi()
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
    print("Exception when calling RiskPatternsApi->libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put: %s\n" % e)
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
api_instance = swagger_client.RiskPatternsApi()
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
    print("Exception when calling RiskPatternsApi->libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put: %s\n" % e)
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
api_instance = swagger_client.RiskPatternsApi()
api_token = 'api_token_example' # str | Authentication token
library_ref = 'library_ref_example' # str | Reference for library
risk_pattern_ref = 'risk_pattern_ref_example' # str | Reference for Risk Pattern
create_weakness_library_request_body = swagger_client.CreateWeaknessLibraryRequestBody() # CreateWeaknessLibraryRequestBody | JSON data that contains information of the fields

try:
    # Creates a new weakness in a risk pattern
    api_response = api_instance.libraries_library_ref_riskpatterns_risk_pattern_ref_weaknesses_post(api_token, library_ref, risk_pattern_ref, create_weakness_library_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskPatternsApi->libraries_library_ref_riskpatterns_risk_pattern_ref_weaknesses_post: %s\n" % e)
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

