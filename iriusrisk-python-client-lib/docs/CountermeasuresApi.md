# swagger_client.CountermeasuresApi

All URIs are relative to *https://demo.iriusrisk.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**libraries_library_ref_riskpatterns_risk_pattern_ref_countermeasures_post**](CountermeasuresApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_countermeasures_post) | **POST** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/countermeasures | Creates new countermeasure in a risk pattern
[**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_countermeasures_put**](CountermeasuresApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_countermeasures_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/countermeasures | Associates a countermeasure to a threat in a risk pattern.
[**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put**](CountermeasuresApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/weaknesses/{weaknessRef}/countermeasures | Associates a countermeasure to a weakness in a risk pattern.


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
api_instance = swagger_client.CountermeasuresApi()
api_token = 'api_token_example' # str | Authentication token
library_ref = 'library_ref_example' # str | Reference for library
risk_pattern_ref = 'risk_pattern_ref_example' # str | Reference for Risk Pattern
create_countermeasure_library_request_body = swagger_client.ControlCommand() # ControlCommand | JSON data that contains information of the fields

try:
    # Creates new countermeasure in a risk pattern
    api_response = api_instance.libraries_library_ref_riskpatterns_risk_pattern_ref_countermeasures_post(api_token, library_ref, risk_pattern_ref, create_countermeasure_library_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountermeasuresApi->libraries_library_ref_riskpatterns_risk_pattern_ref_countermeasures_post: %s\n" % e)
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

# **libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_countermeasures_put**
> LibraryControl libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_countermeasures_put(api_token, library_ref, risk_pattern_ref, use_case_ref, threat_ref, associate_countermeasure_threat_library_request_body)

Associates a countermeasure to a threat in a risk pattern.

Associates a countermeasure to a threat in a risk pattern. Conditions to be able to perform the action:   - To have the permission **LIBRARY_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CountermeasuresApi()
api_token = 'api_token_example' # str | Authentication token
library_ref = 'library_ref_example' # str | Reference for library
risk_pattern_ref = 'risk_pattern_ref_example' # str | Reference for Risk Pattern
use_case_ref = 'use_case_ref_example' # str | Reference for Use Case
threat_ref = 'threat_ref_example' # str | Reference for Threat
associate_countermeasure_threat_library_request_body = swagger_client.AssociateCountermeasureThreatLibraryRequestBody() # AssociateCountermeasureThreatLibraryRequestBody | JSON data that contains information of the fields

try:
    # Associates a countermeasure to a threat in a risk pattern.
    api_response = api_instance.libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_countermeasures_put(api_token, library_ref, risk_pattern_ref, use_case_ref, threat_ref, associate_countermeasure_threat_library_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountermeasuresApi->libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_countermeasures_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **library_ref** | **str**| Reference for library | 
 **risk_pattern_ref** | **str**| Reference for Risk Pattern | 
 **use_case_ref** | **str**| Reference for Use Case | 
 **threat_ref** | **str**| Reference for Threat | 
 **associate_countermeasure_threat_library_request_body** | [**AssociateCountermeasureThreatLibraryRequestBody**](AssociateCountermeasureThreatLibraryRequestBody.md)| JSON data that contains information of the fields | 

### Return type

[**LibraryControl**](LibraryControl.md)

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
api_instance = swagger_client.CountermeasuresApi()
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
    print("Exception when calling CountermeasuresApi->libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put: %s\n" % e)
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

