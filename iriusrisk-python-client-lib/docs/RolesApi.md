# iriusrisk_python_client_lib.RolesApi

All URIs are relative to *https://demo.iriusrisk.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**roles_post**](RolesApi.md#roles_post) | **POST** /roles | Creates a new Role
[**roles_role_name_delete**](RolesApi.md#roles_role_name_delete) | **DELETE** /roles/{role_name} | Deletes an existing role


# **roles_post**
> roles_post(api_token, create_role_request_body)

Creates a new Role

Creates a new role. Conditions to be able to perform the action:  - To have the permission **ROLES_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.RolesApi()
api_token = 'api_token_example' # str | Authentication token
create_role_request_body = iriusrisk_python_client_lib.CreateRoleRequestBody() # CreateRoleRequestBody | JSON data that contains information of the fields

try:
    # Creates a new Role
    api_instance.roles_post(api_token, create_role_request_body)
except ApiException as e:
    print("Exception when calling RolesApi->roles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **create_role_request_body** | [**CreateRoleRequestBody**](CreateRoleRequestBody.md)| JSON data that contains information of the fields | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_role_name_delete**
> roles_role_name_delete(api_token, role_name)

Deletes an existing role

Deletes an existing role. Conditions to be able to perform the action: - To have the permission **ROLES_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iriusrisk_python_client_lib.RolesApi()
api_token = 'api_token_example' # str | Authentication token
role_name = 'role_name_example' # str | Role name to delete

try:
    # Deletes an existing role
    api_instance.roles_role_name_delete(api_token, role_name)
except ApiException as e:
    print("Exception when calling RolesApi->roles_role_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **role_name** | **str**| Role name to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

