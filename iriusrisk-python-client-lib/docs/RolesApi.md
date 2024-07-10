# iriusrisk_python_client_lib.RolesApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_role1**](RolesApi.md#add_user_role1) | **POST** /api/v2/roles/{role-id}/users/{username} | Adds a role to a user.
[**assign_global_permissions_to_role**](RolesApi.md#assign_global_permissions_to_role) | **POST** /api/v2/roles/{role-id}/global-permissions/bulk | Assigns a list of global permissions to a role.
[**assign_project_permissions_to_role**](RolesApi.md#assign_project_permissions_to_role) | **POST** /api/v2/roles/{role-id}/project-permissions/bulk | Assigns a list of project permissions to a role.
[**create_role**](RolesApi.md#create_role) | **POST** /api/v2/roles | Creates a new role.
[**delete_role**](RolesApi.md#delete_role) | **DELETE** /api/v2/roles/{role-id} | Deletes a role.
[**delete_role_user**](RolesApi.md#delete_role_user) | **DELETE** /api/v2/roles/{role-id}/users/{username} | Deletes a role from a user.
[**duplicate_role**](RolesApi.md#duplicate_role) | **POST** /api/v2/roles/{role-id}/duplicate | Duplicates a role.
[**get_all_custom_field_permissions_for_role**](RolesApi.md#get_all_custom_field_permissions_for_role) | **GET** /api/v2/roles/{role-id}/custom-field-permissions | Gets the list of custom field permissions for a role.
[**get_all_roles**](RolesApi.md#get_all_roles) | **GET** /api/v2/roles | Gets a list of all roles.
[**get_global_permissions**](RolesApi.md#get_global_permissions) | **GET** /api/v2/roles/global-permissions | Gets a list of all global permissions.
[**get_global_permissions_by_role_id**](RolesApi.md#get_global_permissions_by_role_id) | **GET** /api/v2/roles/{role-id}/global-permissions | Gets the global permissions of a role.
[**get_project_permissions**](RolesApi.md#get_project_permissions) | **GET** /api/v2/roles/project-permissions | Gets a list of all project permissions.
[**get_project_permissions_by_role_id**](RolesApi.md#get_project_permissions_by_role_id) | **GET** /api/v2/roles/{role-id}/project-permissions | Gets the project permissions of a role.
[**get_role**](RolesApi.md#get_role) | **GET** /api/v2/roles/{role-id} | Gets a role.
[**unassign_global_permissions_to_role**](RolesApi.md#unassign_global_permissions_to_role) | **DELETE** /api/v2/roles/{role-id}/global-permissions/bulk | Denies a list of global permissions from a role.
[**unassign_project_permissions_to_role**](RolesApi.md#unassign_project_permissions_to_role) | **DELETE** /api/v2/roles/{role-id}/project-permissions/bulk | Denies a list of project permissions from a role.
[**update_custom_field_permissions**](RolesApi.md#update_custom_field_permissions) | **PUT** /api/v2/roles/{role-id}/custom-field-permissions/bulk | Updates a custom field permission.
[**update_role**](RolesApi.md#update_role) | **PUT** /api/v2/roles/{role-id} | Updates an existing role.

# **add_user_role1**
> add_user_role1(username, role_id)

Adds a role to a user.

Adds a role to a user.  Conditions to be able to perform the action:  - To have the permission **ALL_USERS_UPDATE** granted, or, - To have the permission **MANAGE_USERS_BU** granted. With this permission you will be able to add roles to users **that belong to the same Business Units than you**.

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
api_instance = iriusrisk_python_client_lib.RolesApi(iriusrisk_python_client_lib.ApiClient(configuration))
username = 'username_example' # str | The username of the user requested.
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the role.

try:
    # Adds a role to a user.
    api_instance.add_user_role1(username, role_id)
except ApiException as e:
    print("Exception when calling RolesApi->add_user_role1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user requested. | 
 **role_id** | [**str**](.md)| ID of the role. | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_global_permissions_to_role**
> assign_global_permissions_to_role(role_id, body=body)

Assigns a list of global permissions to a role.

Assigns a list of global permissions to a role.  Conditions to be able to perform the action:  - To have the permission **ROLES_UPDATE** granted

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
api_instance = iriusrisk_python_client_lib.RolesApi(iriusrisk_python_client_lib.ApiClient(configuration))
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the role.
body = iriusrisk_python_client_lib.AssignPermissionToRoleRequest() # AssignPermissionToRoleRequest |  (optional)

try:
    # Assigns a list of global permissions to a role.
    api_instance.assign_global_permissions_to_role(role_id, body=body)
except ApiException as e:
    print("Exception when calling RolesApi->assign_global_permissions_to_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | [**str**](.md)| ID of the role. | 
 **body** | [**AssignPermissionToRoleRequest**](AssignPermissionToRoleRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_project_permissions_to_role**
> assign_project_permissions_to_role(role_id, body=body)

Assigns a list of project permissions to a role.

Assigns a list of project permissions to a role.  Conditions to be able to perform the action:  - To have the permission **ROLES_UPDATE** granted

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
api_instance = iriusrisk_python_client_lib.RolesApi(iriusrisk_python_client_lib.ApiClient(configuration))
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the role.
body = iriusrisk_python_client_lib.AssignPermissionToRoleRequest() # AssignPermissionToRoleRequest |  (optional)

try:
    # Assigns a list of project permissions to a role.
    api_instance.assign_project_permissions_to_role(role_id, body=body)
except ApiException as e:
    print("Exception when calling RolesApi->assign_project_permissions_to_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | [**str**](.md)| ID of the role. | 
 **body** | [**AssignPermissionToRoleRequest**](AssignPermissionToRoleRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role**
> RoleResponse create_role(body=body)

Creates a new role.

Creates a new role. Conditions to be able to perform the action: - To have the permission **ROLES_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.RolesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.RoleRequest() # RoleRequest |  (optional)

try:
    # Creates a new role.
    api_response = api_instance.create_role(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->create_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleRequest**](RoleRequest.md)|  | [optional] 

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> delete_role(role_id)

Deletes a role.

Deletes a role.  Conditions to be able to perform the action:  - To have the permission **ROLES_UPDATE** granted

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
api_instance = iriusrisk_python_client_lib.RolesApi(iriusrisk_python_client_lib.ApiClient(configuration))
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the role.

try:
    # Deletes a role.
    api_instance.delete_role(role_id)
except ApiException as e:
    print("Exception when calling RolesApi->delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | [**str**](.md)| ID of the role. | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_user**
> delete_role_user(username, role_id)

Deletes a role from a user.

Deletes a role from a user.  Conditions to be able to perform the action:  - To have the permission **ALL_USERS_UPDATE** granted, or, - To have the permission **MANAGE_USERS_BU** granted. With this permission you will be able to delete roles from users **that belong to the same Business Units than you**.

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
api_instance = iriusrisk_python_client_lib.RolesApi(iriusrisk_python_client_lib.ApiClient(configuration))
username = 'username_example' # str | The username of the user requested.
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the role.

try:
    # Deletes a role from a user.
    api_instance.delete_role_user(username, role_id)
except ApiException as e:
    print("Exception when calling RolesApi->delete_role_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user requested. | 
 **role_id** | [**str**](.md)| ID of the role. | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_role**
> RoleResponse duplicate_role(body, role_id)

Duplicates a role.

Duplicates a role.  Conditions to be able to perform the action:  - To have the permission **ROLES_UPDATE** granted

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
api_instance = iriusrisk_python_client_lib.RolesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.DuplicateRoleRequest() # DuplicateRoleRequest | 
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the role.

try:
    # Duplicates a role.
    api_response = api_instance.duplicate_role(body, role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->duplicate_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DuplicateRoleRequest**](DuplicateRoleRequest.md)|  | 
 **role_id** | [**str**](.md)| ID of the role. | 

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_custom_field_permissions_for_role**
> PagedModelCustomFieldPermissionResponse get_all_custom_field_permissions_for_role(role_id, filter=filter, page=page, size=size, sort=sort)

Gets the list of custom field permissions for a role.

Gets the list of custom field permissions for a role.  Conditions to be able to perform the action:  - To have the permission **ROLES_UPDATE** granted, or, - To have the permission **WORKFLOW_VIEW** granted, or, - To have the permission **WORKFLOW_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.RolesApi(iriusrisk_python_client_lib.ApiClient(configuration))
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the role.
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the list of custom field permissions for a role.
    api_response = api_instance.get_all_custom_field_permissions_for_role(role_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_all_custom_field_permissions_for_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | [**str**](.md)| ID of the role. | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelCustomFieldPermissionResponse**](PagedModelCustomFieldPermissionResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_roles**
> PagedModelRoleResponse get_all_roles(filter=filter, page=page, size=size, sort=sort)

Gets a list of all roles.

Gets a list of all roles.  Conditions to be able to perform the action:  - To have the permission **ALL_USERS_UPDATE** granted, or, - To have the permission **MANAGE_USERS_BU** granted, or, - To have the permission **ROLES_UPDATE** granted, or,  - To have the permission **WORKFLOW_VIEW** granted, or, - To have the permission **WORKFLOW_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.RolesApi(iriusrisk_python_client_lib.ApiClient(configuration))
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets a list of all roles.
    api_response = api_instance.get_all_roles(filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_all_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelRoleResponse**](PagedModelRoleResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_global_permissions**
> PagedModelPermissionResponse get_global_permissions(filter=filter, page=page, size=size, sort=sort)

Gets a list of all global permissions.

Gets a list of all global permissions.  Conditions to be able to perform the action:  - To have the permission **ROLES_UPDATE** granted - To have the permission **SYSTEM_SETTINGS_VIEW** granted - To have the permission **SYSTEM_SETTINGS_UPDATE** granted

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
api_instance = iriusrisk_python_client_lib.RolesApi(iriusrisk_python_client_lib.ApiClient(configuration))
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets a list of all global permissions.
    api_response = api_instance.get_global_permissions(filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_global_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelPermissionResponse**](PagedModelPermissionResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_global_permissions_by_role_id**
> PagedModelPermissionResponse get_global_permissions_by_role_id(role_id, filter=filter, page=page, size=size, sort=sort)

Gets the global permissions of a role.

Gets the global permissions of a role. Conditions to be able to perform the action: - To have the permission **ROLES_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.RolesApi(iriusrisk_python_client_lib.ApiClient(configuration))
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the role.
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the global permissions of a role.
    api_response = api_instance.get_global_permissions_by_role_id(role_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_global_permissions_by_role_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | [**str**](.md)| ID of the role. | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelPermissionResponse**](PagedModelPermissionResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_permissions**
> PagedModelPermissionResponse get_project_permissions(filter=filter, page=page, size=size, sort=sort)

Gets a list of all project permissions.

Gets a list of all project permissions.  Conditions to be able to perform the action:  - To have the permission **ROLES_UPDATE** granted or, - To have the permission **WORKFLOW_VIEW** granted, or, - To have the permission **WORKFLOW_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.RolesApi(iriusrisk_python_client_lib.ApiClient(configuration))
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets a list of all project permissions.
    api_response = api_instance.get_project_permissions(filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_project_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelPermissionResponse**](PagedModelPermissionResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_permissions_by_role_id**
> PagedModelPermissionResponse get_project_permissions_by_role_id(role_id, filter=filter, page=page, size=size, sort=sort)

Gets the project permissions of a role.

Gets the project permissions of a role.  Conditions to be able to perform the action:  - To have the permission **ROLES_UPDATE** granted or, - To have the permission **WORKFLOW_VIEW** granted, or, - To have the permission **WORKFLOW_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.RolesApi(iriusrisk_python_client_lib.ApiClient(configuration))
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the role.
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the project permissions of a role.
    api_response = api_instance.get_project_permissions_by_role_id(role_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_project_permissions_by_role_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | [**str**](.md)| ID of the role. | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelPermissionResponse**](PagedModelPermissionResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> RoleResponse get_role(role_id)

Gets a role.

Gets a role.  Conditions to be able to perform the action:  - To have the permission **ROLES_UPDATE** granted

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
api_instance = iriusrisk_python_client_lib.RolesApi(iriusrisk_python_client_lib.ApiClient(configuration))
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the role.

try:
    # Gets a role.
    api_response = api_instance.get_role(role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | [**str**](.md)| ID of the role. | 

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_global_permissions_to_role**
> unassign_global_permissions_to_role(role_id, permission)

Denies a list of global permissions from a role.

Denies a list of global permissions from a role.  Conditions to be able to perform the action:  - To have the permission **ROLES_UPDATE** granted

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
api_instance = iriusrisk_python_client_lib.RolesApi(iriusrisk_python_client_lib.ApiClient(configuration))
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the role.
permission = ['permission_example'] # list[str] | ID of the permission

try:
    # Denies a list of global permissions from a role.
    api_instance.unassign_global_permissions_to_role(role_id, permission)
except ApiException as e:
    print("Exception when calling RolesApi->unassign_global_permissions_to_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | [**str**](.md)| ID of the role. | 
 **permission** | [**list[str]**](str.md)| ID of the permission | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_project_permissions_to_role**
> unassign_project_permissions_to_role(role_id, permission)

Denies a list of project permissions from a role.

Denies a list of project permissions from a role.  Conditions to be able to perform the action:  - To have the permission **ROLES_UPDATE** granted

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
api_instance = iriusrisk_python_client_lib.RolesApi(iriusrisk_python_client_lib.ApiClient(configuration))
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the role.
permission = ['permission_example'] # list[str] | ID of the permission

try:
    # Denies a list of project permissions from a role.
    api_instance.unassign_project_permissions_to_role(role_id, permission)
except ApiException as e:
    print("Exception when calling RolesApi->unassign_project_permissions_to_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | [**str**](.md)| ID of the role. | 
 **permission** | [**list[str]**](str.md)| ID of the permission | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_field_permissions**
> AsyncOperationIdResponse update_custom_field_permissions(body, x_irius_async, role_id)

Updates a custom field permission.

Updates a custom field permission.  Conditions to be able to perform the action:  - To have the permission **ROLES_UPDATE** granted

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
api_instance = iriusrisk_python_client_lib.RolesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = [iriusrisk_python_client_lib.UpdateCustomFieldPermissionRequest()] # list[UpdateCustomFieldPermissionRequest] | 
x_irius_async = true # bool | Sets whether the endpoint works asynchronously or not passed as parameter.
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the role.

try:
    # Updates a custom field permission.
    api_response = api_instance.update_custom_field_permissions(body, x_irius_async, role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->update_custom_field_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[UpdateCustomFieldPermissionRequest]**](UpdateCustomFieldPermissionRequest.md)|  | 
 **x_irius_async** | **bool**| Sets whether the endpoint works asynchronously or not passed as parameter. | 
 **role_id** | [**str**](.md)| ID of the role. | 

### Return type

[**AsyncOperationIdResponse**](AsyncOperationIdResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> RoleResponse update_role(role_id, body=body)

Updates an existing role.

Updates an existing role.  Conditions to be able to perform the action: - To have the permission **ROLES_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.RolesApi(iriusrisk_python_client_lib.ApiClient(configuration))
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the role.
body = iriusrisk_python_client_lib.RoleRequest() # RoleRequest |  (optional)

try:
    # Updates an existing role.
    api_response = api_instance.update_role(role_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | [**str**](.md)| ID of the role. | 
 **body** | [**RoleRequest**](RoleRequest.md)|  | [optional] 

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

