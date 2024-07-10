# iriusrisk_python_client_lib.LibrariesApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_library_changes**](LibrariesApi.md#apply_library_changes) | **POST** /api/v2/libraries/{library-id}/projects/apply-changes | Applies library changes to projects.
[**copy_library_countermeasure**](LibrariesApi.md#copy_library_countermeasure) | **POST** /api/v2/libraries/countermeasures/copy | Add an existing countermeasure to the selected threat or weakness.
[**copy_library_weakness**](LibrariesApi.md#copy_library_weakness) | **POST** /api/v2/libraries/weaknesses/copy | Adds an existing weakness to the selected threat.
[**copy_threat**](LibrariesApi.md#copy_threat) | **POST** /api/v2/libraries/threats/copy | An existing threat will be copied to the selected use case.
[**create_countermeasure_comment**](LibrariesApi.md#create_countermeasure_comment) | **POST** /api/v2/libraries/countermeasures/comments | Creates a comment in a library countermeasure.
[**create_countermeasure_test_reference**](LibrariesApi.md#create_countermeasure_test_reference) | **POST** /api/v2/libraries/countermeasures/tests/references | Creates a reference in a countermeasure test in a library context.
[**create_library**](LibrariesApi.md#create_library) | **POST** /api/v2/libraries | Creates a risk pattern library.
[**create_library_countermeasure**](LibrariesApi.md#create_library_countermeasure) | **POST** /api/v2/libraries/countermeasures | Creates a new countermeasure within a risk pattern.
[**create_library_countermeasure_implementation**](LibrariesApi.md#create_library_countermeasure_implementation) | **POST** /api/v2/libraries/countermeasures/implementations | Creates a new countermeasure implementation.
[**create_library_countermeasure_reference**](LibrariesApi.md#create_library_countermeasure_reference) | **POST** /api/v2/libraries/countermeasures/references | Adds a reference to a library countermeasure.
[**create_library_countermeasure_standard_reference**](LibrariesApi.md#create_library_countermeasure_standard_reference) | **POST** /api/v2/libraries/countermeasures/standard-references | Adds a standard reference to a countermeasure in a library context.
[**create_library_threat_reference**](LibrariesApi.md#create_library_threat_reference) | **POST** /api/v2/libraries/threats/references | Creates a new threat reference for a library.
[**create_library_weakness**](LibrariesApi.md#create_library_weakness) | **POST** /api/v2/libraries/weaknesses | Creates a new weakness within a risk pattern.
[**create_risk_pattern**](LibrariesApi.md#create_risk_pattern) | **POST** /api/v2/libraries/risk-patterns | Creates a risk pattern in a library.
[**create_threat**](LibrariesApi.md#create_threat) | **POST** /api/v2/libraries/threats | Creates a new threat within a use case.
[**create_threat_comment**](LibrariesApi.md#create_threat_comment) | **POST** /api/v2/libraries/threats/comments | Creates a comment in a library threat.
[**create_use_case**](LibrariesApi.md#create_use_case) | **POST** /api/v2/libraries/use-cases | Creates a new use case within a risk pattern.
[**create_weakness_test_reference**](LibrariesApi.md#create_weakness_test_reference) | **POST** /api/v2/libraries/weaknesses/tests/references | Associates a new reference to a weakness test.
[**delete_library_by_uuid**](LibrariesApi.md#delete_library_by_uuid) | **DELETE** /api/v2/libraries/{library-id} | Deletes a risk pattern library by id
[**delete_library_countermeasure**](LibrariesApi.md#delete_library_countermeasure) | **DELETE** /api/v2/libraries/countermeasures/{countermeasure-id} | Deletes a countermeasure in a library context.
[**delete_library_countermeasure1**](LibrariesApi.md#delete_library_countermeasure1) | **DELETE** /api/v2/libraries/countermeasures/tests/references/{reference-id} | Deletes a reference in a countermeasure test in a library context.
[**delete_library_countermeasure_implementation**](LibrariesApi.md#delete_library_countermeasure_implementation) | **DELETE** /api/v2/libraries/countermeasures/implementations/{implementation-id} | Deletes an implementation from a countermeasure in a library context.
[**delete_library_countermeasure_reference**](LibrariesApi.md#delete_library_countermeasure_reference) | **DELETE** /api/v2/libraries/countermeasures/references/{reference-id} | Deletes a reference in a countermeasure in a library context.
[**delete_library_countermeasure_standard_reference**](LibrariesApi.md#delete_library_countermeasure_standard_reference) | **DELETE** /api/v2/libraries/countermeasures/standard-references/{standard-reference-id} | Deletes a countermeasure standard reference.
[**delete_library_threat_reference**](LibrariesApi.md#delete_library_threat_reference) | **DELETE** /api/v2/libraries/threats/references/{reference-id} | Deletes a threat reference from a library.
[**delete_risk_pattern_by_id**](LibrariesApi.md#delete_risk_pattern_by_id) | **DELETE** /api/v2/libraries/risk-patterns/{risk-pattern-id} | Deletes a risk pattern in a library context.
[**delete_threat_by_uuid**](LibrariesApi.md#delete_threat_by_uuid) | **DELETE** /api/v2/libraries/threats/{threat-id} | Deletes a threat.
[**delete_use_case**](LibrariesApi.md#delete_use_case) | **DELETE** /api/v2/libraries/use-cases/{use-case-id} | Deletes a use case in a library context.
[**delete_weakness**](LibrariesApi.md#delete_weakness) | **DELETE** /api/v2/libraries/weaknesses/{weakness-id} | Deletes a weakness in a library context.
[**delete_weakness_test_reference**](LibrariesApi.md#delete_weakness_test_reference) | **DELETE** /api/v2/libraries/weaknesses/tests/references/{reference-id} | Deletes the reference of a weakness test.
[**detach_countermeasure_from_library_threat**](LibrariesApi.md#detach_countermeasure_from_library_threat) | **DELETE** /api/v2/libraries/threats/{threat-id}/countermeasures/{countermeasure-id} | Unassigns a countermeasure from a library threat.
[**detach_countermeasure_from_library_weakness**](LibrariesApi.md#detach_countermeasure_from_library_weakness) | **DELETE** /api/v2/libraries/weaknesses/{weakness-id}/countermeasures/{countermeasure-id} | Unassigns a countermeasure from a library weakness.
[**detach_weakness_from_library_threat**](LibrariesApi.md#detach_weakness_from_library_threat) | **DELETE** /api/v2/libraries/threats/{threat-id}/weaknesses/{weakness-id} | Unassigns a weakness from a library threat.
[**disable_library**](LibrariesApi.md#disable_library) | **POST** /api/v2/libraries/{library-id}/disable | Disables a risk pattern library by id.
[**enable_library**](LibrariesApi.md#enable_library) | **POST** /api/v2/libraries/{library-id}/enable | Enables a risk pattern library by id.
[**export_library_by_uuid**](LibrariesApi.md#export_library_by_uuid) | **GET** /api/v2/libraries/{library-id}/export | Gets a risk pattern library as XML file by id.
[**get_all_countermeasure_comments**](LibrariesApi.md#get_all_countermeasure_comments) | **GET** /api/v2/libraries/countermeasures/{countermeasure-id}/comments | Gets all the comments of a countermeasure in a library context.
[**get_all_libraries**](LibrariesApi.md#get_all_libraries) | **GET** /api/v2/libraries | Gets all libraries.
[**get_all_libraries_countermeasure_summary**](LibrariesApi.md#get_all_libraries_countermeasure_summary) | **GET** /api/v2/libraries/countermeasures/summary | Gets the  list of countermeasure summaries in a library.
[**get_all_libraries_summary**](LibrariesApi.md#get_all_libraries_summary) | **GET** /api/v2/libraries/summary | Gets all the libraries registered in the system.
[**get_all_library_countermeasure_implementations_by_uuid**](LibrariesApi.md#get_all_library_countermeasure_implementations_by_uuid) | **GET** /api/v2/libraries/countermeasures/{countermeasure-id}/implementations | Gets all the implementations of a countermeasure in a library context.
[**get_all_library_countermeasure_test_references**](LibrariesApi.md#get_all_library_countermeasure_test_references) | **GET** /api/v2/libraries/countermeasures/tests/{test-id}/references | Gets all the references of a countermeasure test in a library context.
[**get_all_library_countermeasures**](LibrariesApi.md#get_all_library_countermeasures) | **GET** /api/v2/libraries/countermeasures | Gets all the library countermeasures.
[**get_all_library_countermeasures_by_threat_uuid**](LibrariesApi.md#get_all_library_countermeasures_by_threat_uuid) | **GET** /api/v2/libraries/threats/{threat-id}/countermeasures | Gets all the library countermeasures in a threat.
[**get_all_library_countermeasures_summary**](LibrariesApi.md#get_all_library_countermeasures_summary) | **GET** /api/v2/libraries/{library-id}/countermeasures/summary | Gets the  list of countermeasure summaries in a library.
[**get_all_library_countermeasures_summary_by_threat_uuid**](LibrariesApi.md#get_all_library_countermeasures_summary_by_threat_uuid) | **GET** /api/v2/libraries/threats/{threat-id}/countermeasures/summary | Gets a summary of all the library countermeasures in a threat.
[**get_all_library_threat_references**](LibrariesApi.md#get_all_library_threat_references) | **GET** /api/v2/libraries/threats/{threat-id}/references | Obtains the library threat references through the threat id.
[**get_all_library_threats_summary**](LibrariesApi.md#get_all_library_threats_summary) | **GET** /api/v2/libraries/threats/summary | Gets the summary threat list in a library context.
[**get_all_library_weaknesses**](LibrariesApi.md#get_all_library_weaknesses) | **GET** /api/v2/libraries/weaknesses | Gets all the library weaknesses.
[**get_all_library_weaknesses_by_threat**](LibrariesApi.md#get_all_library_weaknesses_by_threat) | **GET** /api/v2/libraries/threats/{threat-id}/weaknesses | Gets all the library weaknesses in a threat.
[**get_all_projects_for_library**](LibrariesApi.md#get_all_projects_for_library) | **GET** /api/v2/libraries/{library-id}/projects | Gets all the projects related with the given library.
[**get_all_references_by_countermeasure_uuid**](LibrariesApi.md#get_all_references_by_countermeasure_uuid) | **GET** /api/v2/libraries/countermeasures/{countermeasure-id}/references | Gets all the references of a countermeasure in a library context.
[**get_all_risk_patterns_for_library**](LibrariesApi.md#get_all_risk_patterns_for_library) | **GET** /api/v2/libraries/{library-id}/risk-patterns | Gets all the risk patterns in a library.
[**get_all_risk_patterns_summary_for_library**](LibrariesApi.md#get_all_risk_patterns_summary_for_library) | **GET** /api/v2/libraries/{library-id}/risk-patterns/summary | Gets the summary list of risk patterns in a library.
[**get_all_standard_references_by_countermeasure_uuid**](LibrariesApi.md#get_all_standard_references_by_countermeasure_uuid) | **GET** /api/v2/libraries/countermeasures/{countermeasure-id}/standard-references | Gets all the standard references associated with a given countermeasure in a library context.
[**get_all_summary_threats_by_library_use_case**](LibrariesApi.md#get_all_summary_threats_by_library_use_case) | **GET** /api/v2/libraries/use-cases/{use-case-id}/threats/summary | Given a use case, returns the summary list of its threats.
[**get_all_threat_comments**](LibrariesApi.md#get_all_threat_comments) | **GET** /api/v2/libraries/threats/{threat-id}/comments | Gets all the comments of a threat in a library context.
[**get_all_threats**](LibrariesApi.md#get_all_threats) | **GET** /api/v2/libraries/threats | Gets all threats.
[**get_all_threats_summaries**](LibrariesApi.md#get_all_threats_summaries) | **GET** /api/v2/libraries/{library-id}/threats/summary | Gets the summary threat list from a library.
[**get_all_use_cases_for_risk_pattern**](LibrariesApi.md#get_all_use_cases_for_risk_pattern) | **GET** /api/v2/libraries/risk-patterns/{risk-pattern-id}/use-cases | Gets all the use cases of a risk pattern in a library context.
[**get_all_use_cases_summary_for_risk_pattern**](LibrariesApi.md#get_all_use_cases_summary_for_risk_pattern) | **GET** /api/v2/libraries/risk-patterns/{risk-pattern-id}/use-cases/summary | Gets the summary list of use cases of a risk pattern in a library context.
[**get_all_weakness_test_reference**](LibrariesApi.md#get_all_weakness_test_reference) | **GET** /api/v2/libraries/weaknesses/tests/{weakness-test-id}/references | Gets all the references of a weakness test.
[**get_all_weaknesses_summary**](LibrariesApi.md#get_all_weaknesses_summary) | **GET** /api/v2/libraries/weaknesses/summary | Gets the list of weakness summaries in the system.
[**get_library_by_uuid**](LibrariesApi.md#get_library_by_uuid) | **GET** /api/v2/libraries/{library-id} | Gets a risk pattern library by id.
[**get_library_countermeasure_by_uuid**](LibrariesApi.md#get_library_countermeasure_by_uuid) | **GET** /api/v2/libraries/countermeasures/{countermeasure-id} | Gets a countermeasure in a library context
[**get_library_countermeasure_history**](LibrariesApi.md#get_library_countermeasure_history) | **GET** /api/v2/libraries/countermeasures/{countermeasure-id}/history | Gets the history records for a countermeasure.
[**get_library_countermeasure_implementation_by_uuid**](LibrariesApi.md#get_library_countermeasure_implementation_by_uuid) | **GET** /api/v2/libraries/countermeasures/implementations/{implementation-id} | Gets the countermeasure implementation details.
[**get_library_countermeasure_reference**](LibrariesApi.md#get_library_countermeasure_reference) | **GET** /api/v2/libraries/countermeasures/references/{reference-id} | Gets a specific countermeasure reference of the library.
[**get_library_countermeasure_standard_reference**](LibrariesApi.md#get_library_countermeasure_standard_reference) | **GET** /api/v2/libraries/countermeasures/standard-references/{standard-reference-id} | Gets a specific countermeasure standard reference of the library.
[**get_library_countermeasure_test_by_uuid**](LibrariesApi.md#get_library_countermeasure_test_by_uuid) | **GET** /api/v2/libraries/countermeasures/tests/{test-id} | Gets the test related to a countermeasure.
[**get_library_countermeasure_test_history**](LibrariesApi.md#get_library_countermeasure_test_history) | **GET** /api/v2/libraries/countermeasures/tests/{test-id}/history | Gets the history records for a countermeasure test.
[**get_library_countermeasure_test_reference**](LibrariesApi.md#get_library_countermeasure_test_reference) | **GET** /api/v2/libraries/countermeasures/tests/references/{reference-id} | Gets the reference details of a countermeasure test in a library context.
[**get_library_threat_reference**](LibrariesApi.md#get_library_threat_reference) | **GET** /api/v2/libraries/threats/references/{reference-id} | Gets a specific threat reference of the library.
[**get_library_weakness_by_uuid**](LibrariesApi.md#get_library_weakness_by_uuid) | **GET** /api/v2/libraries/weaknesses/{weakness-id} | Gets a weakness in a library context.
[**get_risk_pattern_by_uuid**](LibrariesApi.md#get_risk_pattern_by_uuid) | **GET** /api/v2/libraries/risk-patterns/{risk-pattern-id} | Gets a risk pattern in a library context.
[**get_threat_by_uuid**](LibrariesApi.md#get_threat_by_uuid) | **GET** /api/v2/libraries/threats/{threat-id} | Gets a threat by id.
[**get_threat_history**](LibrariesApi.md#get_threat_history) | **GET** /api/v2/libraries/threats/{threat-id}/history | Gets the history records for a threat.
[**get_use_case_by_id1**](LibrariesApi.md#get_use_case_by_id1) | **GET** /api/v2/libraries/use-cases/{use-case-id} | Gets a use case in a library context.
[**get_weakness_test**](LibrariesApi.md#get_weakness_test) | **GET** /api/v2/libraries/weaknesses/tests/{weakness-test-id} | Gets the test related to a weakness.
[**get_weakness_test_reference_by_uuid**](LibrariesApi.md#get_weakness_test_reference_by_uuid) | **GET** /api/v2/libraries/weaknesses/tests/references/{reference-id} | Gets the reference of a weakness test details.
[**import_library**](LibrariesApi.md#import_library) | **POST** /api/v2/libraries/import | Imports a risk pattern library from XML file.
[**update_library**](LibrariesApi.md#update_library) | **PUT** /api/v2/libraries/{library-id} | Modifies the library.
[**update_library_by_xml_file**](LibrariesApi.md#update_library_by_xml_file) | **POST** /api/v2/libraries/{library-id}/update-with-file | Modifies the library from an XML file.
[**update_library_countermeasure**](LibrariesApi.md#update_library_countermeasure) | **PUT** /api/v2/libraries/countermeasures/{countermeasure-id} | Updates a countermeasure in a library context.
[**update_library_countermeasure_implementation**](LibrariesApi.md#update_library_countermeasure_implementation) | **PUT** /api/v2/libraries/countermeasures/implementations/{implementation-id} | Updates an implementation from a countermeasure in a library context.
[**update_library_countermeasure_reference**](LibrariesApi.md#update_library_countermeasure_reference) | **PUT** /api/v2/libraries/countermeasures/references/{reference-id} | Updates a reference in a countermeasure in a library context.
[**update_library_countermeasure_standard_reference**](LibrariesApi.md#update_library_countermeasure_standard_reference) | **PUT** /api/v2/libraries/countermeasures/standard-references/{standard-reference-id} | Updates a standard reference in a countermeasure in a library context.
[**update_library_countermeasure_state**](LibrariesApi.md#update_library_countermeasure_state) | **PUT** /api/v2/libraries/countermeasures/{countermeasure-id}/state | Updates the status of a library countermeasure.
[**update_library_countermeasure_test**](LibrariesApi.md#update_library_countermeasure_test) | **PUT** /api/v2/libraries/countermeasures/tests/{test-id} | Updates the test related to a countermeasure.
[**update_library_countermeasure_test_reference**](LibrariesApi.md#update_library_countermeasure_test_reference) | **PUT** /api/v2/libraries/countermeasures/tests/references/{reference-id} | Updates a reference in a countermeasure test in a library context.
[**update_library_threat_countermeasure_mitigation**](LibrariesApi.md#update_library_threat_countermeasure_mitigation) | **PUT** /api/v2/libraries/threats/{threat-id}/countermeasures/{countermeasure-id} | Modifies the mitigation of a countermeasure in a threat.
[**update_library_threat_reference**](LibrariesApi.md#update_library_threat_reference) | **PUT** /api/v2/libraries/threats/references/{reference-id} | Updates a reference for a threat of a library.
[**update_risk_pattern**](LibrariesApi.md#update_risk_pattern) | **PUT** /api/v2/libraries/risk-patterns/{risk-pattern-id} | Modifies the risk pattern in a library context.
[**update_threat**](LibrariesApi.md#update_threat) | **PUT** /api/v2/libraries/threats/{threat-id} | Modifies the threat.
[**update_use_case**](LibrariesApi.md#update_use_case) | **PUT** /api/v2/libraries/use-cases/{use-case-id} | Updates a use case in a library context.
[**update_weakness**](LibrariesApi.md#update_weakness) | **PUT** /api/v2/libraries/weaknesses/{weakness-id} | Updates a weakness in a library context.
[**update_weakness_test**](LibrariesApi.md#update_weakness_test) | **PUT** /api/v2/libraries/weaknesses/tests/{weakness-test-id} | Updates the test related to a weakness.
[**update_weakness_test_reference**](LibrariesApi.md#update_weakness_test_reference) | **PUT** /api/v2/libraries/weaknesses/tests/references/{reference-id} | Updates the reference of a weakness test.

# **apply_library_changes**
> AsyncOperationIdResponse apply_library_changes(body, x_irius_async, library_id)

Applies library changes to projects.

The library information will be applied to the specified projects, updating their use cases, threats, countermeasures and weaknesses. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.ApplyLibraryChangesRequest() # ApplyLibraryChangesRequest | 
x_irius_async = true # bool | Sets whether the endpoint works asynchronously or not passed as parameter.
library_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the library

try:
    # Applies library changes to projects.
    api_response = api_instance.apply_library_changes(body, x_irius_async, library_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->apply_library_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplyLibraryChangesRequest**](ApplyLibraryChangesRequest.md)|  | 
 **x_irius_async** | **bool**| Sets whether the endpoint works asynchronously or not passed as parameter. | 
 **library_id** | [**str**](.md)| ID of the library | 

### Return type

[**AsyncOperationIdResponse**](AsyncOperationIdResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_library_countermeasure**
> LibraryCountermeasureResponse copy_library_countermeasure(body)

Add an existing countermeasure to the selected threat or weakness.

Add an existing countermeasure to the selected threat or weakness. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CopyLibraryCountermeasureRequest() # CopyLibraryCountermeasureRequest | 

try:
    # Add an existing countermeasure to the selected threat or weakness.
    api_response = api_instance.copy_library_countermeasure(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->copy_library_countermeasure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CopyLibraryCountermeasureRequest**](CopyLibraryCountermeasureRequest.md)|  | 

### Return type

[**LibraryCountermeasureResponse**](LibraryCountermeasureResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_library_weakness**
> LibraryWeaknessResponse copy_library_weakness(body)

Adds an existing weakness to the selected threat.

Adds an existing weakness to the selected threat. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CopyLibraryWeaknessRequest() # CopyLibraryWeaknessRequest | 

try:
    # Adds an existing weakness to the selected threat.
    api_response = api_instance.copy_library_weakness(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->copy_library_weakness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CopyLibraryWeaknessRequest**](CopyLibraryWeaknessRequest.md)|  | 

### Return type

[**LibraryWeaknessResponse**](LibraryWeaknessResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_threat**
> ThreatResponse copy_threat(body)

An existing threat will be copied to the selected use case.

An existing threat will be copied to the selected use case. Conditions to be able to perform the action: - To have the permission LIBRARY_UPDATE granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CopyThreatRequest() # CopyThreatRequest | 

try:
    # An existing threat will be copied to the selected use case.
    api_response = api_instance.copy_threat(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->copy_threat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CopyThreatRequest**](CopyThreatRequest.md)|  | 

### Return type

[**ThreatResponse**](ThreatResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_countermeasure_comment**
> LibraryCountermeasureCommentResponse create_countermeasure_comment(body=body)

Creates a comment in a library countermeasure.

Creates a new countermeasure comment. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.LibraryCountermeasureCommentRequest() # LibraryCountermeasureCommentRequest |  (optional)

try:
    # Creates a comment in a library countermeasure.
    api_response = api_instance.create_countermeasure_comment(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->create_countermeasure_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LibraryCountermeasureCommentRequest**](LibraryCountermeasureCommentRequest.md)|  | [optional] 

### Return type

[**LibraryCountermeasureCommentResponse**](LibraryCountermeasureCommentResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_countermeasure_test_reference**
> LibraryCountermeasureTestReferenceResponse create_countermeasure_test_reference(body)

Creates a reference in a countermeasure test in a library context.

Creates a reference in a countermeasure test in a library context. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateLibraryCountermeasureTestReferenceRequest() # CreateLibraryCountermeasureTestReferenceRequest | 

try:
    # Creates a reference in a countermeasure test in a library context.
    api_response = api_instance.create_countermeasure_test_reference(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->create_countermeasure_test_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLibraryCountermeasureTestReferenceRequest**](CreateLibraryCountermeasureTestReferenceRequest.md)|  | 

### Return type

[**LibraryCountermeasureTestReferenceResponse**](LibraryCountermeasureTestReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_library**
> LibraryResponse create_library(body)

Creates a risk pattern library.

Creates a new risk pattern library. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.LibraryRequest() # LibraryRequest | 

try:
    # Creates a risk pattern library.
    api_response = api_instance.create_library(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->create_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LibraryRequest**](LibraryRequest.md)|  | 

### Return type

[**LibraryResponse**](LibraryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_library_countermeasure**
> LibraryCountermeasureResponse create_library_countermeasure(body)

Creates a new countermeasure within a risk pattern.

Creates the countermeasure. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateLibraryCountermeasureRequest() # CreateLibraryCountermeasureRequest | 

try:
    # Creates a new countermeasure within a risk pattern.
    api_response = api_instance.create_library_countermeasure(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->create_library_countermeasure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLibraryCountermeasureRequest**](CreateLibraryCountermeasureRequest.md)|  | 

### Return type

[**LibraryCountermeasureResponse**](LibraryCountermeasureResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_library_countermeasure_implementation**
> LibraryCountermeasureImplementationResponse create_library_countermeasure_implementation(body)

Creates a new countermeasure implementation.

Creates an implementation from a countermeasure in a library context. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateLibraryCountermeasureImplementationRequest() # CreateLibraryCountermeasureImplementationRequest | 

try:
    # Creates a new countermeasure implementation.
    api_response = api_instance.create_library_countermeasure_implementation(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->create_library_countermeasure_implementation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLibraryCountermeasureImplementationRequest**](CreateLibraryCountermeasureImplementationRequest.md)|  | 

### Return type

[**LibraryCountermeasureImplementationResponse**](LibraryCountermeasureImplementationResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_library_countermeasure_reference**
> LibraryCountermeasureReferenceResponse create_library_countermeasure_reference(body)

Adds a reference to a library countermeasure.

Adds a reference to a library countermeasure. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateLibraryCountermeasureReferenceRequest() # CreateLibraryCountermeasureReferenceRequest | 

try:
    # Adds a reference to a library countermeasure.
    api_response = api_instance.create_library_countermeasure_reference(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->create_library_countermeasure_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLibraryCountermeasureReferenceRequest**](CreateLibraryCountermeasureReferenceRequest.md)|  | 

### Return type

[**LibraryCountermeasureReferenceResponse**](LibraryCountermeasureReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_library_countermeasure_standard_reference**
> LibraryCountermeasureStandardReferenceResponse create_library_countermeasure_standard_reference(body)

Adds a standard reference to a countermeasure in a library context.

Adds a standard reference to a countermeasure in a library context. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateLibraryCountermeasureStandardReferenceRequest() # CreateLibraryCountermeasureStandardReferenceRequest | 

try:
    # Adds a standard reference to a countermeasure in a library context.
    api_response = api_instance.create_library_countermeasure_standard_reference(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->create_library_countermeasure_standard_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLibraryCountermeasureStandardReferenceRequest**](CreateLibraryCountermeasureStandardReferenceRequest.md)|  | 

### Return type

[**LibraryCountermeasureStandardReferenceResponse**](LibraryCountermeasureStandardReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_library_threat_reference**
> ThreatReferenceResponse create_library_threat_reference(body)

Creates a new threat reference for a library.

Creates a new threat reference for a library. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateLibraryThreatReferenceRequest() # CreateLibraryThreatReferenceRequest | 

try:
    # Creates a new threat reference for a library.
    api_response = api_instance.create_library_threat_reference(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->create_library_threat_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLibraryThreatReferenceRequest**](CreateLibraryThreatReferenceRequest.md)|  | 

### Return type

[**ThreatReferenceResponse**](ThreatReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_library_weakness**
> LibraryWeaknessResponse create_library_weakness(body)

Creates a new weakness within a risk pattern.

Creates the weakness. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateLibraryWeaknessRequest() # CreateLibraryWeaknessRequest | 

try:
    # Creates a new weakness within a risk pattern.
    api_response = api_instance.create_library_weakness(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->create_library_weakness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLibraryWeaknessRequest**](CreateLibraryWeaknessRequest.md)|  | 

### Return type

[**LibraryWeaknessResponse**](LibraryWeaknessResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_risk_pattern**
> RiskPatternResponse create_risk_pattern(body)

Creates a risk pattern in a library.

Creates a new risk pattern. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateRiskPatternRequest() # CreateRiskPatternRequest | 

try:
    # Creates a risk pattern in a library.
    api_response = api_instance.create_risk_pattern(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->create_risk_pattern: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRiskPatternRequest**](CreateRiskPatternRequest.md)|  | 

### Return type

[**RiskPatternResponse**](RiskPatternResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_threat**
> ThreatResponse create_threat(body)

Creates a new threat within a use case.

Creates a new threat within a use case. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateThreatRequest() # CreateThreatRequest | 

try:
    # Creates a new threat within a use case.
    api_response = api_instance.create_threat(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->create_threat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateThreatRequest**](CreateThreatRequest.md)|  | 

### Return type

[**ThreatResponse**](ThreatResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_threat_comment**
> LibraryThreatCommentResponse create_threat_comment(body)

Creates a comment in a library threat.

Creates a new threat comment. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.LibraryThreatCommentRequest() # LibraryThreatCommentRequest | 

try:
    # Creates a comment in a library threat.
    api_response = api_instance.create_threat_comment(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->create_threat_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LibraryThreatCommentRequest**](LibraryThreatCommentRequest.md)|  | 

### Return type

[**LibraryThreatCommentResponse**](LibraryThreatCommentResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_use_case**
> UseCaseResponse create_use_case(body)

Creates a new use case within a risk pattern.

Creates a new use case. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateUseCaseRequest() # CreateUseCaseRequest | 

try:
    # Creates a new use case within a risk pattern.
    api_response = api_instance.create_use_case(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->create_use_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUseCaseRequest**](CreateUseCaseRequest.md)|  | 

### Return type

[**UseCaseResponse**](UseCaseResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_weakness_test_reference**
> WeaknessTestReferenceResponse create_weakness_test_reference(body)

Associates a new reference to a weakness test.

Associates a new reference to a weakness test. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateWeaknessTestReferenceRequest() # CreateWeaknessTestReferenceRequest | 

try:
    # Associates a new reference to a weakness test.
    api_response = api_instance.create_weakness_test_reference(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->create_weakness_test_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWeaknessTestReferenceRequest**](CreateWeaknessTestReferenceRequest.md)|  | 

### Return type

[**WeaknessTestReferenceResponse**](WeaknessTestReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_library_by_uuid**
> delete_library_by_uuid(library_id)

Deletes a risk pattern library by id

Deletes a risk pattern library by id. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
library_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the library

try:
    # Deletes a risk pattern library by id
    api_instance.delete_library_by_uuid(library_id)
except ApiException as e:
    print("Exception when calling LibrariesApi->delete_library_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | [**str**](.md)| ID of the library | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_library_countermeasure**
> delete_library_countermeasure(countermeasure_id)

Deletes a countermeasure in a library context.

Deletes a countermeasure in a library context. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the countermeasure

try:
    # Deletes a countermeasure in a library context.
    api_instance.delete_library_countermeasure(countermeasure_id)
except ApiException as e:
    print("Exception when calling LibrariesApi->delete_library_countermeasure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countermeasure_id** | [**str**](.md)| ID of the countermeasure | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_library_countermeasure1**
> delete_library_countermeasure1(reference_id)

Deletes a reference in a countermeasure test in a library context.

Deletes a reference in a countermeasure test in a library context. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of a reference.

try:
    # Deletes a reference in a countermeasure test in a library context.
    api_instance.delete_library_countermeasure1(reference_id)
except ApiException as e:
    print("Exception when calling LibrariesApi->delete_library_countermeasure1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_id** | [**str**](.md)| ID of a reference. | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_library_countermeasure_implementation**
> delete_library_countermeasure_implementation(implementation_id)

Deletes an implementation from a countermeasure in a library context.

Deletes an implementation from a countermeasure in a library context. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
implementation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure implementation.

try:
    # Deletes an implementation from a countermeasure in a library context.
    api_instance.delete_library_countermeasure_implementation(implementation_id)
except ApiException as e:
    print("Exception when calling LibrariesApi->delete_library_countermeasure_implementation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **implementation_id** | [**str**](.md)| The id of the countermeasure implementation. | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_library_countermeasure_reference**
> delete_library_countermeasure_reference(reference_id)

Deletes a reference in a countermeasure in a library context.

Deletes a reference in a countermeasure in a library context. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of a reference.

try:
    # Deletes a reference in a countermeasure in a library context.
    api_instance.delete_library_countermeasure_reference(reference_id)
except ApiException as e:
    print("Exception when calling LibrariesApi->delete_library_countermeasure_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_id** | [**str**](.md)| ID of a reference. | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_library_countermeasure_standard_reference**
> delete_library_countermeasure_standard_reference(standard_reference_id)

Deletes a countermeasure standard reference.

Deletes a countermeasure standard reference. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
standard_reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the countermeasure standard reference

try:
    # Deletes a countermeasure standard reference.
    api_instance.delete_library_countermeasure_standard_reference(standard_reference_id)
except ApiException as e:
    print("Exception when calling LibrariesApi->delete_library_countermeasure_standard_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standard_reference_id** | [**str**](.md)| ID of the countermeasure standard reference | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_library_threat_reference**
> delete_library_threat_reference(reference_id)

Deletes a threat reference from a library.

Deletes a threat reference from a library. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of a reference.

try:
    # Deletes a threat reference from a library.
    api_instance.delete_library_threat_reference(reference_id)
except ApiException as e:
    print("Exception when calling LibrariesApi->delete_library_threat_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_id** | [**str**](.md)| ID of a reference. | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_risk_pattern_by_id**
> delete_risk_pattern_by_id(risk_pattern_id)

Deletes a risk pattern in a library context.

Deletes a risk pattern in a library context. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
risk_pattern_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the risk pattern

try:
    # Deletes a risk pattern in a library context.
    api_instance.delete_risk_pattern_by_id(risk_pattern_id)
except ApiException as e:
    print("Exception when calling LibrariesApi->delete_risk_pattern_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_pattern_id** | [**str**](.md)| ID of the risk pattern | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_threat_by_uuid**
> delete_threat_by_uuid(threat_id)

Deletes a threat.

Deletes a threat. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the threat

try:
    # Deletes a threat.
    api_instance.delete_threat_by_uuid(threat_id)
except ApiException as e:
    print("Exception when calling LibrariesApi->delete_threat_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_id** | [**str**](.md)| ID of the threat | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_use_case**
> delete_use_case(use_case_id)

Deletes a use case in a library context.

Deletes the use case. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
use_case_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the use case

try:
    # Deletes a use case in a library context.
    api_instance.delete_use_case(use_case_id)
except ApiException as e:
    print("Exception when calling LibrariesApi->delete_use_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **use_case_id** | [**str**](.md)| ID of the use case | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_weakness**
> delete_weakness(weakness_id)

Deletes a weakness in a library context.

Deletes the weakness. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
weakness_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the weakness

try:
    # Deletes a weakness in a library context.
    api_instance.delete_weakness(weakness_id)
except ApiException as e:
    print("Exception when calling LibrariesApi->delete_weakness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **weakness_id** | [**str**](.md)| ID of the weakness | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_weakness_test_reference**
> delete_weakness_test_reference(reference_id)

Deletes the reference of a weakness test.

Deletes the reference of a weakness test. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of a reference.

try:
    # Deletes the reference of a weakness test.
    api_instance.delete_weakness_test_reference(reference_id)
except ApiException as e:
    print("Exception when calling LibrariesApi->delete_weakness_test_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_id** | [**str**](.md)| ID of a reference. | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_countermeasure_from_library_threat**
> detach_countermeasure_from_library_threat(threat_id, countermeasure_id)

Unassigns a countermeasure from a library threat.

Unassigns a countermeasure from a library threat. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the threat
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the countermeasure

try:
    # Unassigns a countermeasure from a library threat.
    api_instance.detach_countermeasure_from_library_threat(threat_id, countermeasure_id)
except ApiException as e:
    print("Exception when calling LibrariesApi->detach_countermeasure_from_library_threat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_id** | [**str**](.md)| ID of the threat | 
 **countermeasure_id** | [**str**](.md)| ID of the countermeasure | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_countermeasure_from_library_weakness**
> detach_countermeasure_from_library_weakness(weakness_id, countermeasure_id)

Unassigns a countermeasure from a library weakness.

Unassigns a countermeasure from a library weakness. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
weakness_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the weakness
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the countermeasure

try:
    # Unassigns a countermeasure from a library weakness.
    api_instance.detach_countermeasure_from_library_weakness(weakness_id, countermeasure_id)
except ApiException as e:
    print("Exception when calling LibrariesApi->detach_countermeasure_from_library_weakness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **weakness_id** | [**str**](.md)| ID of the weakness | 
 **countermeasure_id** | [**str**](.md)| ID of the countermeasure | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_weakness_from_library_threat**
> detach_weakness_from_library_threat(threat_id, weakness_id)

Unassigns a weakness from a library threat.

Unassigns a weakness from a library threat. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the threat
weakness_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the weakness

try:
    # Unassigns a weakness from a library threat.
    api_instance.detach_weakness_from_library_threat(threat_id, weakness_id)
except ApiException as e:
    print("Exception when calling LibrariesApi->detach_weakness_from_library_threat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_id** | [**str**](.md)| ID of the threat | 
 **weakness_id** | [**str**](.md)| ID of the weakness | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_library**
> disable_library(library_id)

Disables a risk pattern library by id.

Disables the library. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
library_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the library

try:
    # Disables a risk pattern library by id.
    api_instance.disable_library(library_id)
except ApiException as e:
    print("Exception when calling LibrariesApi->disable_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | [**str**](.md)| ID of the library | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_library**
> enable_library(library_id)

Enables a risk pattern library by id.

Enables the library. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
library_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the library

try:
    # Enables a risk pattern library by id.
    api_instance.enable_library(library_id)
except ApiException as e:
    print("Exception when calling LibrariesApi->enable_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | [**str**](.md)| ID of the library | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_library_by_uuid**
> export_library_by_uuid(library_id)

Gets a risk pattern library as XML file by id.

Gets the library. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
library_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the library

try:
    # Gets a risk pattern library as XML file by id.
    api_instance.export_library_by_uuid(library_id)
except ApiException as e:
    print("Exception when calling LibrariesApi->export_library_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | [**str**](.md)| ID of the library | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_countermeasure_comments**
> PagedModelLibraryCountermeasureCommentResponse get_all_countermeasure_comments(countermeasure_id, filter=filter, page=page, size=size, sort=sort)

Gets all the comments of a countermeasure in a library context.

Gets all the comments of a countermeasure in a library context registered in the system. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the countermeasure.
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the comments of a countermeasure in a library context.
    api_response = api_instance.get_all_countermeasure_comments(countermeasure_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_countermeasure_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countermeasure_id** | [**str**](.md)| Unique identifier of the countermeasure. | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelLibraryCountermeasureCommentResponse**](PagedModelLibraryCountermeasureCommentResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_libraries**
> PagedModelLibraryResponse get_all_libraries(filter=filter, page=page, size=size, sort=sort)

Gets all libraries.

Gets all the libraries registered in the system. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all libraries.
    api_response = api_instance.get_all_libraries(filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_libraries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelLibraryResponse**](PagedModelLibraryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_libraries_countermeasure_summary**
> PagedModelLibrariesCountermeasuresSummaryResponse get_all_libraries_countermeasure_summary(filter=filter, page=page, size=size, sort=sort)

Gets the  list of countermeasure summaries in a library.

Gets the list of countermeasure summaries registered in the system.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the  list of countermeasure summaries in a library.
    api_response = api_instance.get_all_libraries_countermeasure_summary(filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_libraries_countermeasure_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelLibrariesCountermeasuresSummaryResponse**](PagedModelLibrariesCountermeasuresSummaryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_libraries_summary**
> PagedModelLibrarySummaryResponse get_all_libraries_summary(filter=filter, page=page, size=size, sort=sort)

Gets all the libraries registered in the system.

Gets all the libraries registered in the system containing risk patterns assignable to a component. Conditions to be able to perform the action: - The user must be authenticated

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the libraries registered in the system.
    api_response = api_instance.get_all_libraries_summary(filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_libraries_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelLibrarySummaryResponse**](PagedModelLibrarySummaryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_library_countermeasure_implementations_by_uuid**
> PagedModelLibraryCountermeasureImplementationResponse get_all_library_countermeasure_implementations_by_uuid(countermeasure_id, filter=filter, page=page, size=size, sort=sort)

Gets all the implementations of a countermeasure in a library context.

Gets all the implementations of a countermeasure in a library context registered in the system. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the countermeasure
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the implementations of a countermeasure in a library context.
    api_response = api_instance.get_all_library_countermeasure_implementations_by_uuid(countermeasure_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_library_countermeasure_implementations_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countermeasure_id** | [**str**](.md)| ID of the countermeasure | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelLibraryCountermeasureImplementationResponse**](PagedModelLibraryCountermeasureImplementationResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_library_countermeasure_test_references**
> PagedModelGetAllLibraryCountermeasureTestReferenceResponse get_all_library_countermeasure_test_references(test_id, filter=filter, page=page, size=size, sort=sort)

Gets all the references of a countermeasure test in a library context.

Gets all the references of a countermeasure test in a library context registered in the system. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
test_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the test
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the references of a countermeasure test in a library context.
    api_response = api_instance.get_all_library_countermeasure_test_references(test_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_library_countermeasure_test_references: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | [**str**](.md)| ID of the test | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelGetAllLibraryCountermeasureTestReferenceResponse**](PagedModelGetAllLibraryCountermeasureTestReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_library_countermeasures**
> PagedModelGetAllLibraryCountermeasureResponse get_all_library_countermeasures(filter=filter, page=page, size=size, sort=sort)

Gets all the library countermeasures.

Gets all the library countermeasures registered in the system. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted, or, - To have the permission **COUNTERMEASURE_CREATE** granted, or, - To have the permission **COUNTERMEASURE_ADD_FROM_EXISTING** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the library countermeasures.
    api_response = api_instance.get_all_library_countermeasures(filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_library_countermeasures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelGetAllLibraryCountermeasureResponse**](PagedModelGetAllLibraryCountermeasureResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_library_countermeasures_by_threat_uuid**
> PagedModelLibraryThreatCountermeasureResponse get_all_library_countermeasures_by_threat_uuid(threat_id, filter=filter, page=page, size=size, sort=sort)

Gets all the library countermeasures in a threat.

Gets all the library countermeasures registered in the system associated with the threat identified by the given id. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the threat
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the library countermeasures in a threat.
    api_response = api_instance.get_all_library_countermeasures_by_threat_uuid(threat_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_library_countermeasures_by_threat_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_id** | [**str**](.md)| ID of the threat | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelLibraryThreatCountermeasureResponse**](PagedModelLibraryThreatCountermeasureResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_library_countermeasures_summary**
> PagedModelCountermeasureSummaryResponse get_all_library_countermeasures_summary(library_id, filter=filter, page=page, size=size, sort=sort)

Gets the  list of countermeasure summaries in a library.

Gets the list of countermeasure summaries registered in the system.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
library_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the library
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the  list of countermeasure summaries in a library.
    api_response = api_instance.get_all_library_countermeasures_summary(library_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_library_countermeasures_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | [**str**](.md)| ID of the library | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelCountermeasureSummaryResponse**](PagedModelCountermeasureSummaryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_library_countermeasures_summary_by_threat_uuid**
> PagedModelLibraryThreatCountermeasureSummaryResponse get_all_library_countermeasures_summary_by_threat_uuid(threat_id, filter=filter, page=page, size=size, sort=sort)

Gets a summary of all the library countermeasures in a threat.

Gets a summary of all the library countermeasures registered in the system associated with the threat identified by the given id.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the threat
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets a summary of all the library countermeasures in a threat.
    api_response = api_instance.get_all_library_countermeasures_summary_by_threat_uuid(threat_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_library_countermeasures_summary_by_threat_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_id** | [**str**](.md)| ID of the threat | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelLibraryThreatCountermeasureSummaryResponse**](PagedModelLibraryThreatCountermeasureSummaryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_library_threat_references**
> PagedModelThreatReferenceResponse get_all_library_threat_references(threat_id, page=page, size=size, sort=sort)

Obtains the library threat references through the threat id.

Gets the library threat references details. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted or - To have the permission **LIBRARY_UPDATE** granted

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the threat.
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Obtains the library threat references through the threat id.
    api_response = api_instance.get_all_library_threat_references(threat_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_library_threat_references: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_id** | [**str**](.md)| Unique identifier of the threat. | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelThreatReferenceResponse**](PagedModelThreatReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_library_threats_summary**
> PagedModelLibraryThreatSummaryResponse get_all_library_threats_summary(filter=filter, page=page, size=size, sort=sort)

Gets the summary threat list in a library context.

Gets the summary threat list. Conditions to be able to perform the action: - The user must be authenticated

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the summary threat list in a library context.
    api_response = api_instance.get_all_library_threats_summary(filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_library_threats_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelLibraryThreatSummaryResponse**](PagedModelLibraryThreatSummaryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_library_weaknesses**
> PagedModelLibraryWeaknessResponse get_all_library_weaknesses(filter=filter, page=page, size=size, sort=sort)

Gets all the library weaknesses.

Gets all the library weaknesses registered in the system. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted, or, - To have the permission **THREAT_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the library weaknesses.
    api_response = api_instance.get_all_library_weaknesses(filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_library_weaknesses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelLibraryWeaknessResponse**](PagedModelLibraryWeaknessResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_library_weaknesses_by_threat**
> PagedModelLibraryThreatWeaknessResponse get_all_library_weaknesses_by_threat(threat_id, filter=filter, page=page, size=size, sort=sort)

Gets all the library weaknesses in a threat.

Gets all the library weaknesses registered in the system associated with the threat identified by the given id. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the threat
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the library weaknesses in a threat.
    api_response = api_instance.get_all_library_weaknesses_by_threat(threat_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_library_weaknesses_by_threat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_id** | [**str**](.md)| ID of the threat | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelLibraryThreatWeaknessResponse**](PagedModelLibraryThreatWeaknessResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_projects_for_library**
> PagedModelLibraryProjectResponse get_all_projects_for_library(library_id, filter=filter, page=page, size=size, sort=sort)

Gets all the projects related with the given library.

Gets all the projects related with the given library. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
library_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the library
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the projects related with the given library.
    api_response = api_instance.get_all_projects_for_library(library_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_projects_for_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | [**str**](.md)| ID of the library | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelLibraryProjectResponse**](PagedModelLibraryProjectResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_references_by_countermeasure_uuid**
> PagedModelGetAllLibraryCountermeasureReferenceResponse get_all_references_by_countermeasure_uuid(countermeasure_id, page=page, size=size, sort=sort)

Gets all the references of a countermeasure in a library context.

Gets all the references of a countermeasure in a library context registered in the system. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the countermeasure
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the references of a countermeasure in a library context.
    api_response = api_instance.get_all_references_by_countermeasure_uuid(countermeasure_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_references_by_countermeasure_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countermeasure_id** | [**str**](.md)| ID of the countermeasure | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelGetAllLibraryCountermeasureReferenceResponse**](PagedModelGetAllLibraryCountermeasureReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_risk_patterns_for_library**
> PagedModelRiskPatternResponse get_all_risk_patterns_for_library(library_id, filter=filter, page=page, size=size, sort=sort)

Gets all the risk patterns in a library.

Gets all the risk patterns registered in the system associated with the library identified by the given id. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
library_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the library
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the risk patterns in a library.
    api_response = api_instance.get_all_risk_patterns_for_library(library_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_risk_patterns_for_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | [**str**](.md)| ID of the library | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelRiskPatternResponse**](PagedModelRiskPatternResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_risk_patterns_summary_for_library**
> PagedModelRiskPatternSummaryResponse get_all_risk_patterns_summary_for_library(library_id, filter=filter, page=page, size=size, sort=sort)

Gets the summary list of risk patterns in a library.

Gets the summary list of risk patterns registered in the system associated with the library identified by the given id. Conditions to be able to perform the action: - The user must be authenticated

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
library_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the library
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the summary list of risk patterns in a library.
    api_response = api_instance.get_all_risk_patterns_summary_for_library(library_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_risk_patterns_summary_for_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | [**str**](.md)| ID of the library | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelRiskPatternSummaryResponse**](PagedModelRiskPatternSummaryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_standard_references_by_countermeasure_uuid**
> PagedModelLibraryCountermeasureStandardReferenceResponse get_all_standard_references_by_countermeasure_uuid(countermeasure_id, filter=filter, page=page, size=size, sort=sort)

Gets all the standard references associated with a given countermeasure in a library context.

Gets all the standard references associated with a given countermeasure in a library context registered in the system. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the countermeasure
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the standard references associated with a given countermeasure in a library context.
    api_response = api_instance.get_all_standard_references_by_countermeasure_uuid(countermeasure_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_standard_references_by_countermeasure_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countermeasure_id** | [**str**](.md)| ID of the countermeasure | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelLibraryCountermeasureStandardReferenceResponse**](PagedModelLibraryCountermeasureStandardReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_summary_threats_by_library_use_case**
> PagedModelThreatSummaryResponse get_all_summary_threats_by_library_use_case(use_case_id, filter=filter, page=page, size=size, sort=sort)

Given a use case, returns the summary list of its threats.

Given a use case, returns the summary list of its threats. Conditions to be able to perform the action: - The user must be authenticated

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
use_case_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the use case
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Given a use case, returns the summary list of its threats.
    api_response = api_instance.get_all_summary_threats_by_library_use_case(use_case_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_summary_threats_by_library_use_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **use_case_id** | [**str**](.md)| ID of the use case | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelThreatSummaryResponse**](PagedModelThreatSummaryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_threat_comments**
> PagedModelLibraryThreatCommentResponse get_all_threat_comments(threat_id, filter=filter, page=page, size=size, sort=sort)

Gets all the comments of a threat in a library context.

Gets all the comments of a threat in a library context registered in the system. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the threat.
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the comments of a threat in a library context.
    api_response = api_instance.get_all_threat_comments(threat_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_threat_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_id** | [**str**](.md)| Unique identifier of the threat. | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelLibraryThreatCommentResponse**](PagedModelLibraryThreatCommentResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_threats**
> PagedModelGetAllLibraryThreatResponse get_all_threats(filter=filter, page=page, size=size, sort=sort)

Gets all threats.

Gets all threats. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted, or, - To have the permission **THREAT_CREATE** granted, or, - To have the permission **THREAT_ADD_FROM_EXISTING** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all threats.
    api_response = api_instance.get_all_threats(filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_threats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelGetAllLibraryThreatResponse**](PagedModelGetAllLibraryThreatResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_threats_summaries**
> PagedModelThreatSummaryResponse get_all_threats_summaries(library_id, filter=filter, page=page, size=size, sort=sort)

Gets the summary threat list from a library.

Gets the list of threats id, reference and name from a library.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
library_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the library
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the summary threat list from a library.
    api_response = api_instance.get_all_threats_summaries(library_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_threats_summaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | [**str**](.md)| ID of the library | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelThreatSummaryResponse**](PagedModelThreatSummaryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_use_cases_for_risk_pattern**
> PagedModelUseCaseResponse get_all_use_cases_for_risk_pattern(risk_pattern_id, filter=filter, page=page, size=size, sort=sort)

Gets all the use cases of a risk pattern in a library context.

Gets all the use cases of a risk pattern in a library context registered in the system. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
risk_pattern_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the risk pattern
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the use cases of a risk pattern in a library context.
    api_response = api_instance.get_all_use_cases_for_risk_pattern(risk_pattern_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_use_cases_for_risk_pattern: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_pattern_id** | [**str**](.md)| ID of the risk pattern | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelUseCaseResponse**](PagedModelUseCaseResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_use_cases_summary_for_risk_pattern**
> PagedModelUseCaseSummaryResponse get_all_use_cases_summary_for_risk_pattern(risk_pattern_id, filter=filter, page=page, size=size, sort=sort)

Gets the summary list of use cases of a risk pattern in a library context.

Gets the summary list of use cases of a risk pattern in a library context.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
risk_pattern_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the risk pattern
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the summary list of use cases of a risk pattern in a library context.
    api_response = api_instance.get_all_use_cases_summary_for_risk_pattern(risk_pattern_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_use_cases_summary_for_risk_pattern: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_pattern_id** | [**str**](.md)| ID of the risk pattern | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelUseCaseSummaryResponse**](PagedModelUseCaseSummaryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_weakness_test_reference**
> PagedModelWeaknessTestReferencesResponse get_all_weakness_test_reference(weakness_test_id, filter=filter, page=page, size=size, sort=sort)

Gets all the references of a weakness test.

Gets all the references of a weakness test. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
weakness_test_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the weakness test.
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the references of a weakness test.
    api_response = api_instance.get_all_weakness_test_reference(weakness_test_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_weakness_test_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **weakness_test_id** | [**str**](.md)| ID of the weakness test. | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelWeaknessTestReferencesResponse**](PagedModelWeaknessTestReferencesResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_weaknesses_summary**
> PagedModelLibraryWeaknessSummaryResponse get_all_weaknesses_summary(filter=filter, page=page, size=size, sort=sort)

Gets the list of weakness summaries in the system.

Gets the list of weakness summaries registered in the system.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the list of weakness summaries in the system.
    api_response = api_instance.get_all_weaknesses_summary(filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_all_weaknesses_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelLibraryWeaknessSummaryResponse**](PagedModelLibraryWeaknessSummaryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_by_uuid**
> LibraryResponse get_library_by_uuid(library_id)

Gets a risk pattern library by id.

Gets the library. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
library_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the library

try:
    # Gets a risk pattern library by id.
    api_response = api_instance.get_library_by_uuid(library_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_library_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | [**str**](.md)| ID of the library | 

### Return type

[**LibraryResponse**](LibraryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_countermeasure_by_uuid**
> LibraryCountermeasureResponse get_library_countermeasure_by_uuid(countermeasure_id)

Gets a countermeasure in a library context

Gets the countermeasure. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the countermeasure

try:
    # Gets a countermeasure in a library context
    api_response = api_instance.get_library_countermeasure_by_uuid(countermeasure_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_library_countermeasure_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countermeasure_id** | [**str**](.md)| ID of the countermeasure | 

### Return type

[**LibraryCountermeasureResponse**](LibraryCountermeasureResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_countermeasure_history**
> PagedModelHistoryResponse get_library_countermeasure_history(countermeasure_id, page=page, size=size, sort=sort)

Gets the history records for a countermeasure.

Gets the historical changes for a countermeasure, ordered by most recent by default. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the countermeasure
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the history records for a countermeasure.
    api_response = api_instance.get_library_countermeasure_history(countermeasure_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_library_countermeasure_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countermeasure_id** | [**str**](.md)| ID of the countermeasure | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelHistoryResponse**](PagedModelHistoryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_countermeasure_implementation_by_uuid**
> LibraryCountermeasureImplementationResponse get_library_countermeasure_implementation_by_uuid(implementation_id)

Gets the countermeasure implementation details.

Gets the countermeasure implementation details. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted or - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
implementation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure implementation.

try:
    # Gets the countermeasure implementation details.
    api_response = api_instance.get_library_countermeasure_implementation_by_uuid(implementation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_library_countermeasure_implementation_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **implementation_id** | [**str**](.md)| The id of the countermeasure implementation. | 

### Return type

[**LibraryCountermeasureImplementationResponse**](LibraryCountermeasureImplementationResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_countermeasure_reference**
> LibraryCountermeasureReferenceResponse get_library_countermeasure_reference(reference_id)

Gets a specific countermeasure reference of the library.

Gets a specific countermeasure reference of the library. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted or - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of a reference.

try:
    # Gets a specific countermeasure reference of the library.
    api_response = api_instance.get_library_countermeasure_reference(reference_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_library_countermeasure_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_id** | [**str**](.md)| ID of a reference. | 

### Return type

[**LibraryCountermeasureReferenceResponse**](LibraryCountermeasureReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_countermeasure_standard_reference**
> LibraryCountermeasureStandardReferenceResponse get_library_countermeasure_standard_reference(standard_reference_id)

Gets a specific countermeasure standard reference of the library.

Gets a specific countermeasure standard reference of the library. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted or - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
standard_reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the countermeasure standard reference

try:
    # Gets a specific countermeasure standard reference of the library.
    api_response = api_instance.get_library_countermeasure_standard_reference(standard_reference_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_library_countermeasure_standard_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standard_reference_id** | [**str**](.md)| ID of the countermeasure standard reference | 

### Return type

[**LibraryCountermeasureStandardReferenceResponse**](LibraryCountermeasureStandardReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_countermeasure_test_by_uuid**
> GetLibraryCountermeasureTestResponse get_library_countermeasure_test_by_uuid(test_id)

Gets the test related to a countermeasure.

Gets the test related to a countermeasure. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
test_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the test

try:
    # Gets the test related to a countermeasure.
    api_response = api_instance.get_library_countermeasure_test_by_uuid(test_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_library_countermeasure_test_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | [**str**](.md)| ID of the test | 

### Return type

[**GetLibraryCountermeasureTestResponse**](GetLibraryCountermeasureTestResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_countermeasure_test_history**
> PagedModelHistoryResponse get_library_countermeasure_test_history(test_id, page=page, size=size, sort=sort)

Gets the history records for a countermeasure test.

Gets the historical changes for a countermeasure test, ordered by most recent by default. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
test_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the test
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the history records for a countermeasure test.
    api_response = api_instance.get_library_countermeasure_test_history(test_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_library_countermeasure_test_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | [**str**](.md)| ID of the test | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelHistoryResponse**](PagedModelHistoryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_countermeasure_test_reference**
> LibraryCountermeasureTestReferenceResponse get_library_countermeasure_test_reference(reference_id)

Gets the reference details of a countermeasure test in a library context.

Gets the reference details of a countermeasure test in a library context registered in the system. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of a reference.

try:
    # Gets the reference details of a countermeasure test in a library context.
    api_response = api_instance.get_library_countermeasure_test_reference(reference_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_library_countermeasure_test_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_id** | [**str**](.md)| ID of a reference. | 

### Return type

[**LibraryCountermeasureTestReferenceResponse**](LibraryCountermeasureTestReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_threat_reference**
> ThreatReferenceResponse get_library_threat_reference(reference_id)

Gets a specific threat reference of the library.

Gets a specific threat reference of the library. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted or - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of a reference.

try:
    # Gets a specific threat reference of the library.
    api_response = api_instance.get_library_threat_reference(reference_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_library_threat_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_id** | [**str**](.md)| ID of a reference. | 

### Return type

[**ThreatReferenceResponse**](ThreatReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_weakness_by_uuid**
> LibraryWeaknessResponse get_library_weakness_by_uuid(weakness_id)

Gets a weakness in a library context.

Gets the weakness. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
weakness_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the weakness

try:
    # Gets a weakness in a library context.
    api_response = api_instance.get_library_weakness_by_uuid(weakness_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_library_weakness_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **weakness_id** | [**str**](.md)| ID of the weakness | 

### Return type

[**LibraryWeaknessResponse**](LibraryWeaknessResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_risk_pattern_by_uuid**
> RiskPatternResponse get_risk_pattern_by_uuid(risk_pattern_id)

Gets a risk pattern in a library context.

Gets the risk pattern. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
risk_pattern_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the risk pattern

try:
    # Gets a risk pattern in a library context.
    api_response = api_instance.get_risk_pattern_by_uuid(risk_pattern_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_risk_pattern_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_pattern_id** | [**str**](.md)| ID of the risk pattern | 

### Return type

[**RiskPatternResponse**](RiskPatternResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_by_uuid**
> ThreatResponse get_threat_by_uuid(threat_id)

Gets a threat by id.

Gets the threat. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the threat

try:
    # Gets a threat by id.
    api_response = api_instance.get_threat_by_uuid(threat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_threat_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_id** | [**str**](.md)| ID of the threat | 

### Return type

[**ThreatResponse**](ThreatResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_history**
> PagedModelHistoryResponse get_threat_history(threat_id, page=page, size=size, sort=sort)

Gets the history records for a threat.

Gets the historical changes for a threat, ordered by most recent by default.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the threat
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the history records for a threat.
    api_response = api_instance.get_threat_history(threat_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_threat_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_id** | [**str**](.md)| ID of the threat | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelHistoryResponse**](PagedModelHistoryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_use_case_by_id1**
> UseCaseResponse get_use_case_by_id1(use_case_id)

Gets a use case in a library context.

Gets the use case. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
use_case_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the use case

try:
    # Gets a use case in a library context.
    api_response = api_instance.get_use_case_by_id1(use_case_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_use_case_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **use_case_id** | [**str**](.md)| ID of the use case | 

### Return type

[**UseCaseResponse**](UseCaseResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_weakness_test**
> WeaknessTestResponse get_weakness_test(weakness_test_id)

Gets the test related to a weakness.

Gets the test related to a weakness. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
weakness_test_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the weakness test.

try:
    # Gets the test related to a weakness.
    api_response = api_instance.get_weakness_test(weakness_test_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_weakness_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **weakness_test_id** | [**str**](.md)| ID of the weakness test. | 

### Return type

[**WeaknessTestResponse**](WeaknessTestResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_weakness_test_reference_by_uuid**
> WeaknessTestReferenceResponse get_weakness_test_reference_by_uuid(reference_id)

Gets the reference of a weakness test details.

Gets the reference of a weakness test details. Conditions to be able to perform the action: - To have the permission **LIBRARY_VIEW** granted, or, - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of a reference.

try:
    # Gets the reference of a weakness test details.
    api_response = api_instance.get_weakness_test_reference_by_uuid(reference_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->get_weakness_test_reference_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_id** | [**str**](.md)| ID of a reference. | 

### Return type

[**WeaknessTestReferenceResponse**](WeaknessTestReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_library**
> LibraryResponse import_library(file, reference_id, name)

Imports a risk pattern library from XML file.

Imports risk pattern library from XML file. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
file = 'file_example' # str | 
reference_id = 'reference_id_example' # str | 
name = 'name_example' # str | 

try:
    # Imports a risk pattern library from XML file.
    api_response = api_instance.import_library(file, reference_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->import_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **reference_id** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**LibraryResponse**](LibraryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_library**
> LibraryResponse update_library(body, library_id)

Modifies the library.

Modifies the library. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.LibraryRequest() # LibraryRequest | 
library_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the library

try:
    # Modifies the library.
    api_response = api_instance.update_library(body, library_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->update_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LibraryRequest**](LibraryRequest.md)|  | 
 **library_id** | [**str**](.md)| ID of the library | 

### Return type

[**LibraryResponse**](LibraryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_library_by_xml_file**
> AsyncOperationIdResponse update_library_by_xml_file(x_irius_async, library_id, file=file)

Modifies the library from an XML file.

Modifies the library from an XML file upload. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
x_irius_async = true # bool | Sets whether the endpoint works asynchronously or not passed as parameter.
library_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the library
file = 'file_example' # str |  (optional)

try:
    # Modifies the library from an XML file.
    api_response = api_instance.update_library_by_xml_file(x_irius_async, library_id, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->update_library_by_xml_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_irius_async** | **bool**| Sets whether the endpoint works asynchronously or not passed as parameter. | 
 **library_id** | [**str**](.md)| ID of the library | 
 **file** | **str**|  | [optional] 

### Return type

[**AsyncOperationIdResponse**](AsyncOperationIdResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_library_countermeasure**
> LibraryCountermeasureResponse update_library_countermeasure(body, countermeasure_id)

Updates a countermeasure in a library context.

Updates the countermeasure. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateLibraryCountermeasureRequest() # UpdateLibraryCountermeasureRequest | 
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the countermeasure

try:
    # Updates a countermeasure in a library context.
    api_response = api_instance.update_library_countermeasure(body, countermeasure_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->update_library_countermeasure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateLibraryCountermeasureRequest**](UpdateLibraryCountermeasureRequest.md)|  | 
 **countermeasure_id** | [**str**](.md)| ID of the countermeasure | 

### Return type

[**LibraryCountermeasureResponse**](LibraryCountermeasureResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_library_countermeasure_implementation**
> LibraryCountermeasureImplementationResponse update_library_countermeasure_implementation(body, implementation_id)

Updates an implementation from a countermeasure in a library context.

Updates an implementation from a countermeasure in a library context. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateLibraryCountermeasureImplementationRequest() # UpdateLibraryCountermeasureImplementationRequest | 
implementation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure implementation.

try:
    # Updates an implementation from a countermeasure in a library context.
    api_response = api_instance.update_library_countermeasure_implementation(body, implementation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->update_library_countermeasure_implementation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateLibraryCountermeasureImplementationRequest**](UpdateLibraryCountermeasureImplementationRequest.md)|  | 
 **implementation_id** | [**str**](.md)| The id of the countermeasure implementation. | 

### Return type

[**LibraryCountermeasureImplementationResponse**](LibraryCountermeasureImplementationResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_library_countermeasure_reference**
> LibraryCountermeasureReferenceResponse update_library_countermeasure_reference(body, reference_id)

Updates a reference in a countermeasure in a library context.

Updates a reference in a countermeasure in a library context. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateLibraryCountermeasureReferenceRequest() # UpdateLibraryCountermeasureReferenceRequest | 
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of a reference.

try:
    # Updates a reference in a countermeasure in a library context.
    api_response = api_instance.update_library_countermeasure_reference(body, reference_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->update_library_countermeasure_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateLibraryCountermeasureReferenceRequest**](UpdateLibraryCountermeasureReferenceRequest.md)|  | 
 **reference_id** | [**str**](.md)| ID of a reference. | 

### Return type

[**LibraryCountermeasureReferenceResponse**](LibraryCountermeasureReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_library_countermeasure_standard_reference**
> LibraryCountermeasureStandardReferenceResponse update_library_countermeasure_standard_reference(body, standard_reference_id)

Updates a standard reference in a countermeasure in a library context.

Updates a standard reference in a countermeasure in a library context. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateLibraryCountermeasureStandardReferenceRequest() # UpdateLibraryCountermeasureStandardReferenceRequest | 
standard_reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the countermeasure standard reference

try:
    # Updates a standard reference in a countermeasure in a library context.
    api_response = api_instance.update_library_countermeasure_standard_reference(body, standard_reference_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->update_library_countermeasure_standard_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateLibraryCountermeasureStandardReferenceRequest**](UpdateLibraryCountermeasureStandardReferenceRequest.md)|  | 
 **standard_reference_id** | [**str**](.md)| ID of the countermeasure standard reference | 

### Return type

[**LibraryCountermeasureStandardReferenceResponse**](LibraryCountermeasureStandardReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_library_countermeasure_state**
> LibraryCountermeasureResponse update_library_countermeasure_state(body, countermeasure_id)

Updates the status of a library countermeasure.

Updates the status of a library countermeasure.  A reason must be given for these transitions: rejected or not-applicable.  Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CountermeasureidStateBody2() # CountermeasureidStateBody2 | 
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the countermeasure

try:
    # Updates the status of a library countermeasure.
    api_response = api_instance.update_library_countermeasure_state(body, countermeasure_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->update_library_countermeasure_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CountermeasureidStateBody2**](CountermeasureidStateBody2.md)|  | 
 **countermeasure_id** | [**str**](.md)| ID of the countermeasure | 

### Return type

[**LibraryCountermeasureResponse**](LibraryCountermeasureResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_library_countermeasure_test**
> GetLibraryCountermeasureTestResponse update_library_countermeasure_test(body, test_id)

Updates the test related to a countermeasure.

Updates the test related to a countermeasure. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateLibraryCountermeasureTestRequest() # UpdateLibraryCountermeasureTestRequest | 
test_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the test

try:
    # Updates the test related to a countermeasure.
    api_response = api_instance.update_library_countermeasure_test(body, test_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->update_library_countermeasure_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateLibraryCountermeasureTestRequest**](UpdateLibraryCountermeasureTestRequest.md)|  | 
 **test_id** | [**str**](.md)| ID of the test | 

### Return type

[**GetLibraryCountermeasureTestResponse**](GetLibraryCountermeasureTestResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_library_countermeasure_test_reference**
> LibraryCountermeasureTestReferenceResponse update_library_countermeasure_test_reference(body, reference_id)

Updates a reference in a countermeasure test in a library context.

Updates a reference in a countermeasure test in a library context. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateLibraryCountermeasureTestReferenceRequest() # UpdateLibraryCountermeasureTestReferenceRequest | 
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of a reference.

try:
    # Updates a reference in a countermeasure test in a library context.
    api_response = api_instance.update_library_countermeasure_test_reference(body, reference_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->update_library_countermeasure_test_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateLibraryCountermeasureTestReferenceRequest**](UpdateLibraryCountermeasureTestReferenceRequest.md)|  | 
 **reference_id** | [**str**](.md)| ID of a reference. | 

### Return type

[**LibraryCountermeasureTestReferenceResponse**](LibraryCountermeasureTestReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_library_threat_countermeasure_mitigation**
> LibraryThreatCountermeasureMitigationResponse update_library_threat_countermeasure_mitigation(body, threat_id, countermeasure_id)

Modifies the mitigation of a countermeasure in a threat.

Modifies the mitigation of the association of a countermeasure and a threat identified by their ids. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateMitigationRequest() # UpdateMitigationRequest | 
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the threat
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the countermeasure

try:
    # Modifies the mitigation of a countermeasure in a threat.
    api_response = api_instance.update_library_threat_countermeasure_mitigation(body, threat_id, countermeasure_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->update_library_threat_countermeasure_mitigation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateMitigationRequest**](UpdateMitigationRequest.md)|  | 
 **threat_id** | [**str**](.md)| ID of the threat | 
 **countermeasure_id** | [**str**](.md)| ID of the countermeasure | 

### Return type

[**LibraryThreatCountermeasureMitigationResponse**](LibraryThreatCountermeasureMitigationResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_library_threat_reference**
> ThreatReferenceResponse update_library_threat_reference(body, reference_id)

Updates a reference for a threat of a library.

Updates a reference for a threat of a library. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateLibraryThreatReferenceRequest() # UpdateLibraryThreatReferenceRequest | 
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of a reference.

try:
    # Updates a reference for a threat of a library.
    api_response = api_instance.update_library_threat_reference(body, reference_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->update_library_threat_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateLibraryThreatReferenceRequest**](UpdateLibraryThreatReferenceRequest.md)|  | 
 **reference_id** | [**str**](.md)| ID of a reference. | 

### Return type

[**ThreatReferenceResponse**](ThreatReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_risk_pattern**
> RiskPatternResponse update_risk_pattern(body, risk_pattern_id)

Modifies the risk pattern in a library context.

Modifies the risk pattern. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateRiskPatternRequest() # UpdateRiskPatternRequest | 
risk_pattern_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the risk pattern

try:
    # Modifies the risk pattern in a library context.
    api_response = api_instance.update_risk_pattern(body, risk_pattern_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->update_risk_pattern: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRiskPatternRequest**](UpdateRiskPatternRequest.md)|  | 
 **risk_pattern_id** | [**str**](.md)| ID of the risk pattern | 

### Return type

[**RiskPatternResponse**](RiskPatternResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_threat**
> ThreatResponse update_threat(body, threat_id)

Modifies the threat.

Modifies the threat. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateThreatRequest() # UpdateThreatRequest | 
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the threat

try:
    # Modifies the threat.
    api_response = api_instance.update_threat(body, threat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->update_threat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateThreatRequest**](UpdateThreatRequest.md)|  | 
 **threat_id** | [**str**](.md)| ID of the threat | 

### Return type

[**ThreatResponse**](ThreatResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_use_case**
> UseCaseResponse update_use_case(body, use_case_id)

Updates a use case in a library context.

Updates the use case. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateUseCaseRequest() # UpdateUseCaseRequest | 
use_case_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the use case

try:
    # Updates a use case in a library context.
    api_response = api_instance.update_use_case(body, use_case_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->update_use_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateUseCaseRequest**](UpdateUseCaseRequest.md)|  | 
 **use_case_id** | [**str**](.md)| ID of the use case | 

### Return type

[**UseCaseResponse**](UseCaseResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_weakness**
> LibraryWeaknessResponse update_weakness(body, weakness_id)

Updates a weakness in a library context.

Updates the weakness. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateLibraryWeaknessRequest() # UpdateLibraryWeaknessRequest | 
weakness_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the weakness

try:
    # Updates a weakness in a library context.
    api_response = api_instance.update_weakness(body, weakness_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->update_weakness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateLibraryWeaknessRequest**](UpdateLibraryWeaknessRequest.md)|  | 
 **weakness_id** | [**str**](.md)| ID of the weakness | 

### Return type

[**LibraryWeaknessResponse**](LibraryWeaknessResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_weakness_test**
> WeaknessTestResponse update_weakness_test(body, weakness_test_id)

Updates the test related to a weakness.

Updates the test related to a weakness. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateWeaknessTestRequest() # UpdateWeaknessTestRequest | 
weakness_test_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the weakness test.

try:
    # Updates the test related to a weakness.
    api_response = api_instance.update_weakness_test(body, weakness_test_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->update_weakness_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateWeaknessTestRequest**](UpdateWeaknessTestRequest.md)|  | 
 **weakness_test_id** | [**str**](.md)| ID of the weakness test. | 

### Return type

[**WeaknessTestResponse**](WeaknessTestResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_weakness_test_reference**
> WeaknessTestReferenceResponse update_weakness_test_reference(body, reference_id)

Updates the reference of a weakness test.

Updates the reference of a weakness test. Conditions to be able to perform the action: - To have the permission **LIBRARY_UPDATE** granted.

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-token
configuration = iriusrisk_python_client_lib.Configuration()
configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.LibrariesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateWeaknessTestReferenceRequest() # UpdateWeaknessTestReferenceRequest | 
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of a reference.

try:
    # Updates the reference of a weakness test.
    api_response = api_instance.update_weakness_test_reference(body, reference_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibrariesApi->update_weakness_test_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateWeaknessTestReferenceRequest**](UpdateWeaknessTestReferenceRequest.md)|  | 
 **reference_id** | [**str**](.md)| ID of a reference. | 

### Return type

[**WeaknessTestReferenceResponse**](WeaknessTestReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

