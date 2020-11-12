# iriusrisk_python_client_lib.LibrariesApi

All URIs are relative to *https://demo.iriusrisk.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**libraries_library_ref_delete**](LibrariesApi.md#libraries_library_ref_delete) | **DELETE** /libraries/{libraryRef} | Deletes a Library
[**libraries_library_ref_get**](LibrariesApi.md#libraries_library_ref_get) | **GET** /libraries/{libraryRef} | Gets library details
[**libraries_library_ref_riskpatterns_post**](LibrariesApi.md#libraries_library_ref_riskpatterns_post) | **POST** /libraries/{libraryRef}/riskpatterns | Creates new Risk Pattern
[**libraries_library_ref_riskpatterns_risk_pattern_ref_countermeasures_post**](LibrariesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_countermeasures_post) | **POST** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/countermeasures | Creates new countermeasure in a risk pattern
[**libraries_library_ref_riskpatterns_risk_pattern_ref_delete**](LibrariesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_delete) | **DELETE** /libraries/{libraryRef}/riskpatterns/{riskPatternRef} | Deletes a Risk Pattern
[**libraries_library_ref_riskpatterns_risk_pattern_ref_get**](LibrariesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_get) | **GET** /libraries/{libraryRef}/riskpatterns/{riskPatternRef} | Gets Risk Pattern details
[**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_post**](LibrariesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_post) | **POST** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases | Creates new use case in a library.
[**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_post**](LibrariesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_post) | **POST** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats | Creates a new threat in a library.
[**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_countermeasures_put**](LibrariesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_countermeasures_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/countermeasures | Associates a countermeasure to a threat in a risk pattern.
[**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put**](LibrariesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/weaknesses | Associates weakness to a threat in a risk pattern.
[**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put**](LibrariesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/weaknesses/{weaknessRef}/countermeasures | Associates a countermeasure to a weakness in a risk pattern.
[**libraries_library_ref_riskpatterns_risk_pattern_ref_weaknesses_post**](LibrariesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_weaknesses_post) | **POST** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/weaknesses | Creates a new weakness in a risk pattern
[**libraries_post**](LibrariesApi.md#libraries_post) | **POST** /libraries | Creates a Library
[**products_upload_post**](LibrariesApi.md#products_upload_post) | **POST** /products/upload | Creates a new product, library or template from a XML file upload.


# **libraries_library_ref_delete**
> libraries_library_ref_delete(api_token, library_ref)

Deletes a Library

Deletes a library. Conditions to be able to perform the action:   - To have the permission **LIBRARY_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi()
api_token = 'api_token_example' # str | Authentication token
library_ref = 'library_ref_example' # str | Reference for library

try:
    # Deletes a Library
    api_instance.libraries_library_ref_delete(api_token, library_ref)
except ApiException as e:
    print("Exception when calling LibrariesApi->libraries_library_ref_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **library_ref** | **str**| Reference for library | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **libraries_library_ref_get**
> Library libraries_library_ref_get(api_token, library_ref)

Gets library details

Gets the library details. Conditions to be able to perform the action:   - To have the permission **LIBRARY_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi()
api_token = 'api_token_example' # str | Authentication token
library_ref = 'library_ref_example' # str | Reference for library

try:
    # Gets library details
    api_response = api_instance.libraries_library_ref_get(api_token, library_ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->libraries_library_ref_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **library_ref** | **str**| Reference for library | 

### Return type

[**Library**](Library.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **libraries_library_ref_riskpatterns_post**
> RiskPattern libraries_library_ref_riskpatterns_post(api_token, library_ref, create_risk_pattern_request_body)

Creates new Risk Pattern

Creates new Risk Pattern. Conditions to be able to perform the action:   - To have the permission **LIBRARY_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi()
api_token = 'api_token_example' # str | Authentication token
library_ref = 'library_ref_example' # str | Reference for library
create_risk_pattern_request_body = iriusrisk_python_client_lib.CreateRiskPatternRequestBody() # CreateRiskPatternRequestBody | JSON data that contains information of the fields

try:
    # Creates new Risk Pattern
    api_response = api_instance.libraries_library_ref_riskpatterns_post(api_token, library_ref, create_risk_pattern_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->libraries_library_ref_riskpatterns_post: %s\n" % e)
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
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi()
api_token = 'api_token_example' # str | Authentication token
library_ref = 'library_ref_example' # str | Reference for library
risk_pattern_ref = 'risk_pattern_ref_example' # str | Reference for Risk Pattern
create_countermeasure_library_request_body = iriusrisk_python_client_lib.ControlCommand() # ControlCommand | JSON data that contains information of the fields

try:
    # Creates new countermeasure in a risk pattern
    api_response = api_instance.libraries_library_ref_riskpatterns_risk_pattern_ref_countermeasures_post(api_token, library_ref, risk_pattern_ref, create_countermeasure_library_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->libraries_library_ref_riskpatterns_risk_pattern_ref_countermeasures_post: %s\n" % e)
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
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi()
api_token = 'api_token_example' # str | Authentication token
library_ref = 'library_ref_example' # str | Reference for library
risk_pattern_ref = 'risk_pattern_ref_example' # str | Reference for Risk Pattern

try:
    # Deletes a Risk Pattern
    api_instance.libraries_library_ref_riskpatterns_risk_pattern_ref_delete(api_token, library_ref, risk_pattern_ref)
except ApiException as e:
    print("Exception when calling LibrariesApi->libraries_library_ref_riskpatterns_risk_pattern_ref_delete: %s\n" % e)
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
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi()
api_token = 'api_token_example' # str | Authentication token
library_ref = 'library_ref_example' # str | Reference for library
risk_pattern_ref = 'risk_pattern_ref_example' # str | Reference for Risk Pattern

try:
    # Gets Risk Pattern details
    api_response = api_instance.libraries_library_ref_riskpatterns_risk_pattern_ref_get(api_token, library_ref, risk_pattern_ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->libraries_library_ref_riskpatterns_risk_pattern_ref_get: %s\n" % e)
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

# **libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_post**
> LibraryUseCase libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_post(api_token, library_ref, risk_pattern_ref, create_use_case_library_request_body)

Creates new use case in a library.

Creates new use case in a library. Conditions to be able to perform the action:   - To have the permission **LIBRARY_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi()
api_token = 'api_token_example' # str | Authentication token
library_ref = 'library_ref_example' # str | Reference for library
risk_pattern_ref = 'risk_pattern_ref_example' # str | Reference for Risk Pattern
create_use_case_library_request_body = iriusrisk_python_client_lib.CreateUseCaseLibraryRequestBody() # CreateUseCaseLibraryRequestBody | JSON data that contains information of the fields

try:
    # Creates new use case in a library.
    api_response = api_instance.libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_post(api_token, library_ref, risk_pattern_ref, create_use_case_library_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **library_ref** | **str**| Reference for library | 
 **risk_pattern_ref** | **str**| Reference for Risk Pattern | 
 **create_use_case_library_request_body** | [**CreateUseCaseLibraryRequestBody**](CreateUseCaseLibraryRequestBody.md)| JSON data that contains information of the fields | 

### Return type

[**LibraryUseCase**](LibraryUseCase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_post**
> LibraryThreat libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_post(api_token, library_ref, risk_pattern_ref, use_case_ref, create_threat_library_request_body)

Creates a new threat in a library.

Creates a new threat in a library. Conditions to be able to perform the action:   - To have the permission **LIBRARY_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi()
api_token = 'api_token_example' # str | Authentication token
library_ref = 'library_ref_example' # str | Reference for library
risk_pattern_ref = 'risk_pattern_ref_example' # str | Reference for Risk Pattern
use_case_ref = 'use_case_ref_example' # str | Reference for Use Case
create_threat_library_request_body = iriusrisk_python_client_lib.CreateThreatLibraryRequestBody() # CreateThreatLibraryRequestBody | JSON data that contains information of the fields

try:
    # Creates a new threat in a library.
    api_response = api_instance.libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_post(api_token, library_ref, risk_pattern_ref, use_case_ref, create_threat_library_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **library_ref** | **str**| Reference for library | 
 **risk_pattern_ref** | **str**| Reference for Risk Pattern | 
 **use_case_ref** | **str**| Reference for Use Case | 
 **create_threat_library_request_body** | [**CreateThreatLibraryRequestBody**](CreateThreatLibraryRequestBody.md)| JSON data that contains information of the fields | 

### Return type

[**LibraryThreat**](LibraryThreat.md)

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
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi()
api_token = 'api_token_example' # str | Authentication token
library_ref = 'library_ref_example' # str | Reference for library
risk_pattern_ref = 'risk_pattern_ref_example' # str | Reference for Risk Pattern
use_case_ref = 'use_case_ref_example' # str | Reference for Use Case
threat_ref = 'threat_ref_example' # str | Reference for Threat
associate_countermeasure_threat_library_request_body = iriusrisk_python_client_lib.AssociateCountermeasureThreatLibraryRequestBody() # AssociateCountermeasureThreatLibraryRequestBody | JSON data that contains information of the fields

try:
    # Associates a countermeasure to a threat in a risk pattern.
    api_response = api_instance.libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_countermeasures_put(api_token, library_ref, risk_pattern_ref, use_case_ref, threat_ref, associate_countermeasure_threat_library_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_countermeasures_put: %s\n" % e)
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

# **libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put**
> LibraryWeakness libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put(api_token, library_ref, risk_pattern_ref, use_case_ref, threat_ref, associate_weakness_threat_library_request_body)

Associates weakness to a threat in a risk pattern.

Associates weakness to a threat in a risk pattern. Conditions to be able to perform the action:   - To have the permission **LIBRARY_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi()
api_token = 'api_token_example' # str | Authentication token
library_ref = 'library_ref_example' # str | Reference for library
risk_pattern_ref = 'risk_pattern_ref_example' # str | Reference for Risk Pattern
use_case_ref = 'use_case_ref_example' # str | Reference for Use Case
threat_ref = 'threat_ref_example' # str | Reference for Threat
associate_weakness_threat_library_request_body = iriusrisk_python_client_lib.AssociateWeaknessThreatLibraryRequestBody() # AssociateWeaknessThreatLibraryRequestBody | JSON data that contains information of the fields

try:
    # Associates weakness to a threat in a risk pattern.
    api_response = api_instance.libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put(api_token, library_ref, risk_pattern_ref, use_case_ref, threat_ref, associate_weakness_threat_library_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put: %s\n" % e)
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
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi()
api_token = 'api_token_example' # str | Authentication token
library_ref = 'library_ref_example' # str | Reference for library
risk_pattern_ref = 'risk_pattern_ref_example' # str | Reference for Risk Pattern
use_case_ref = 'use_case_ref_example' # str | Reference for Use Case
threat_ref = 'threat_ref_example' # str | Reference for Threat
weakness_ref = 'weakness_ref_example' # str | Reference for Weakness
associate_countermeasure_weakness_library_request_body = iriusrisk_python_client_lib.AssociateCountermeasureWeaknessLibraryRequestBody() # AssociateCountermeasureWeaknessLibraryRequestBody | JSON data that contains information of the fields

try:
    # Associates a countermeasure to a weakness in a risk pattern.
    api_response = api_instance.libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put(api_token, library_ref, risk_pattern_ref, use_case_ref, threat_ref, weakness_ref, associate_countermeasure_weakness_library_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put: %s\n" % e)
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
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi()
api_token = 'api_token_example' # str | Authentication token
library_ref = 'library_ref_example' # str | Reference for library
risk_pattern_ref = 'risk_pattern_ref_example' # str | Reference for Risk Pattern
create_weakness_library_request_body = iriusrisk_python_client_lib.CreateWeaknessLibraryRequestBody() # CreateWeaknessLibraryRequestBody | JSON data that contains information of the fields

try:
    # Creates a new weakness in a risk pattern
    api_response = api_instance.libraries_library_ref_riskpatterns_risk_pattern_ref_weaknesses_post(api_token, library_ref, risk_pattern_ref, create_weakness_library_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->libraries_library_ref_riskpatterns_risk_pattern_ref_weaknesses_post: %s\n" % e)
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

# **libraries_post**
> Library libraries_post(api_token, create_library_request_body)

Creates a Library

Creates a new empty Library. Conditions to be able to perform the action:   - To have the permission **LIBRARY_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi()
api_token = 'api_token_example' # str | Authentication token
create_library_request_body = iriusrisk_python_client_lib.CreateLibraryRequestBody() # CreateLibraryRequestBody | JSON data that contains information of the fields

try:
    # Creates a Library
    api_response = api_instance.libraries_post(api_token, create_library_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->libraries_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **create_library_request_body** | [**CreateLibraryRequestBody**](CreateLibraryRequestBody.md)| JSON data that contains information of the fields | 

### Return type

[**Library**](Library.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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
api_instance = iriusrisk_python_client_lib.LibrariesApi()
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
    print("Exception when calling LibrariesApi->products_upload_post: %s\n" % e)
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

