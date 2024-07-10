# iriusrisk_python_client_lib.TestsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_general_test_settings**](TestsApi.md#get_general_test_settings) | **GET** /api/v2/test-trackers/settings | Get the general settings of Test Trackers.
[**update_general_test_settings**](TestsApi.md#update_general_test_settings) | **PUT** /api/v2/test-trackers/settings | Update general settings of Test Trackers.

# **get_general_test_settings**
> TestSettingsResponse get_general_test_settings()

Get the general settings of Test Trackers.

Get the general settings of Test Trackers.

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
api_instance = iriusrisk_python_client_lib.TestsApi(iriusrisk_python_client_lib.ApiClient(configuration))

try:
    # Get the general settings of Test Trackers.
    api_response = api_instance.get_general_test_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestsApi->get_general_test_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TestSettingsResponse**](TestSettingsResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_general_test_settings**
> TestSettingsResponse update_general_test_settings(body)

Update general settings of Test Trackers.

Update general settings of Test Trackers.

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
api_instance = iriusrisk_python_client_lib.TestsApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.TestSettingsRequest() # TestSettingsRequest | 

try:
    # Update general settings of Test Trackers.
    api_response = api_instance.update_general_test_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestsApi->update_general_test_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TestSettingsRequest**](TestSettingsRequest.md)|  | 

### Return type

[**TestSettingsResponse**](TestSettingsResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

