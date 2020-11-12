# swagger_client.GroupsApi

All URIs are relative to *https://demo.iriusrisk.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_get**](GroupsApi.md#groups_get) | **GET** /groups | Gets a list of all Groups
[**groups_group_ref_delete**](GroupsApi.md#groups_group_ref_delete) | **DELETE** /groups/{groupRef} | Deletes a users group
[**groups_group_ref_get**](GroupsApi.md#groups_group_ref_get) | **GET** /groups/{groupRef} | Gets the group details.
[**groups_group_ref_put**](GroupsApi.md#groups_group_ref_put) | **PUT** /groups/{groupRef} | Update a users group
[**groups_group_users_delete**](GroupsApi.md#groups_group_users_delete) | **DELETE** /groups/{group}/users | Unassign a list of users from a group
[**groups_group_users_get**](GroupsApi.md#groups_group_users_get) | **GET** /groups/{group}/users | List users from a group
[**groups_group_users_put**](GroupsApi.md#groups_group_users_put) | **PUT** /groups/{group}/users | Assigns users to a group
[**groups_group_users_user_delete**](GroupsApi.md#groups_group_users_user_delete) | **DELETE** /groups/{group}/users/{user} | Removes a user from a group
[**groups_post**](GroupsApi.md#groups_post) | **POST** /groups | Creates a new user group
[**products_ref_groups_delete**](GroupsApi.md#products_ref_groups_delete) | **DELETE** /products/{ref}/groups | Unassigns a list of user groups from a product.
[**products_ref_groups_get**](GroupsApi.md#products_ref_groups_get) | **GET** /products/{ref}/groups | List all groups assigned to a product
[**products_ref_groups_put**](GroupsApi.md#products_ref_groups_put) | **PUT** /products/{ref}/groups | Assigns groups of users to a product.


# **groups_get**
> list[Group] groups_get(api_token)

Gets a list of all Groups

Gets a list of all user's groups. Conditions to be able to perform the action:    - To have the permission **ALL_USERS_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupsApi()
api_token = 'api_token_example' # str | Authentication token

try:
    # Gets a list of all Groups
    api_response = api_instance.groups_get(api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 

### Return type

[**list[Group]**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_ref_delete**
> groups_group_ref_delete(api_token, group_ref)

Deletes a users group

Deletes a users group. Conditions to be able to perform the action:    - To have the permission **ALL_USERS_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupsApi()
api_token = 'api_token_example' # str | Authentication token
group_ref = 'group_ref_example' # str | unique name of the group

try:
    # Deletes a users group
    api_instance.groups_group_ref_delete(api_token, group_ref)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_group_ref_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **group_ref** | **str**| unique name of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_ref_get**
> list[Group] groups_group_ref_get(api_token, group_ref)

Gets the group details.

Returns the group details for the requested group. Conditions to be able to perform the action:    - If the caller has the PRODUCTS_LIST_ALL permission then all groups can be queried without restriction.    - Without the PRODUCTS_LIST_ALL permission, the call will only return the group if the caller belongs to that group. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupsApi()
api_token = 'api_token_example' # str | Authentication token
group_ref = 'group_ref_example' # str | unique name of the group

try:
    # Gets the group details.
    api_response = api_instance.groups_group_ref_get(api_token, group_ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_group_ref_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **group_ref** | **str**| unique name of the group | 

### Return type

[**list[Group]**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_ref_put**
> Group groups_group_ref_put(api_token, group_ref, update_group_request_body)

Update a users group

Updates a users group. Conditions to be able to perform the action:    - To have the permission **ALL_USERS_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupsApi()
api_token = 'api_token_example' # str | Authentication token
group_ref = 'group_ref_example' # str | unique ref of the group
update_group_request_body = swagger_client.UpdateGroupRequestBody() # UpdateGroupRequestBody | JSON data that contains information of the fields

try:
    # Update a users group
    api_response = api_instance.groups_group_ref_put(api_token, group_ref, update_group_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_group_ref_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **group_ref** | **str**| unique ref of the group | 
 **update_group_request_body** | [**UpdateGroupRequestBody**](UpdateGroupRequestBody.md)| JSON data that contains information of the fields | 

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_users_delete**
> groups_group_users_delete(api_token, group, unassing_users_group_request_body)

Unassign a list of users from a group

Unassign a list of users from a group. Conditions to be able to perform the action:  - To have the permission **ALL_USERS_UPDATE** granted, or  - To have the permission **MANAGE_USERS_BU** granted. With this permission you will be able to unassign users from a group, **if you belong to this group**. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupsApi()
api_token = 'api_token_example' # str | Authentication token
group = 'group_example' # str | name of the group
unassing_users_group_request_body = swagger_client.UnassingUsersGroupRequestBody() # UnassingUsersGroupRequestBody | JSON object that contains information to unassign users from group

try:
    # Unassign a list of users from a group
    api_instance.groups_group_users_delete(api_token, group, unassing_users_group_request_body)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_group_users_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **group** | **str**| name of the group | 
 **unassing_users_group_request_body** | [**UnassingUsersGroupRequestBody**](UnassingUsersGroupRequestBody.md)| JSON object that contains information to unassign users from group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_users_get**
> list[User] groups_group_users_get(api_token, group)

List users from a group

List users who belongs to a group. Conditions to be able to perform the action:  - To have the permission **ALL_USERS_UPDATE** granted, or  - To have the permission **MANAGE_USERS_BU** granted. With this permission you will be able to list users of a group, **if you belong to this group**. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupsApi()
api_token = 'api_token_example' # str | Authentication token
group = 'group_example' # str | name of the group

try:
    # List users from a group
    api_response = api_instance.groups_group_users_get(api_token, group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_group_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **group** | **str**| name of the group | 

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_users_put**
> InlineResponse201 groups_group_users_put(api_token, group, assign_user_group_request_body)

Assigns users to a group

Assigns users to a group. Conditions to be able to perform the action:  - To have the permission **ALL_USERS_UPDATE** granted, or  - To have the permission **MANAGE_USERS_BU** granted. With this permission you will be able to assign users to a group, **if you belong to this group**. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupsApi()
api_token = 'api_token_example' # str | Authentication token
group = 'group_example' # str | name of the group
assign_user_group_request_body = swagger_client.AssignUserGroupRequestBody() # AssignUserGroupRequestBody | JSON object that contains information to assign users to group

try:
    # Assigns users to a group
    api_response = api_instance.groups_group_users_put(api_token, group, assign_user_group_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_group_users_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **group** | **str**| name of the group | 
 **assign_user_group_request_body** | [**AssignUserGroupRequestBody**](AssignUserGroupRequestBody.md)| JSON object that contains information to assign users to group | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_users_user_delete**
> groups_group_users_user_delete(api_token, group, user)

Removes a user from a group

Unassign a user from a group. Conditions to be able to perform the action:  - To have the permission **ALL_USERS_UPDATE** granted, or  - To have the permission **MANAGE_USERS_BU** granted. With this permission you will be able to unassign user from a group, **if you belong to this group**. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupsApi()
api_token = 'api_token_example' # str | Authentication token
group = 'group_example' # str | name of the group
user = 'user_example' # str | user to be removed from group

try:
    # Removes a user from a group
    api_instance.groups_group_users_user_delete(api_token, group, user)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_group_users_user_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **group** | **str**| name of the group | 
 **user** | **str**| user to be removed from group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_post**
> Group groups_post(api_token, create_group_request_body)

Creates a new user group

Creates a new user group. Conditions to be able to perform the action:    - To have the permission **ALL_USERS_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupsApi()
api_token = 'api_token_example' # str | Authentication token
create_group_request_body = swagger_client.CreateGroupRequestBody() # CreateGroupRequestBody | JSON data that contains information of the fields

try:
    # Creates a new user group
    api_response = api_instance.groups_post(api_token, create_group_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **create_group_request_body** | [**CreateGroupRequestBody**](CreateGroupRequestBody.md)| JSON data that contains information of the fields | 

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | Reference for product
unassign_groups_product_request_body = swagger_client.UnassignGroupsProductRequestBody() # UnassignGroupsProductRequestBody | JSON object that contains information to unassign groups from a product

try:
    # Unassigns a list of user groups from a product.
    api_response = api_instance.products_ref_groups_delete(api_token, ref, unassign_groups_product_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->products_ref_groups_delete: %s\n" % e)
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
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | Reference to product

try:
    # List all groups assigned to a product
    api_response = api_instance.products_ref_groups_get(api_token, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->products_ref_groups_get: %s\n" % e)
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
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupsApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | Reference for product
assign_groups_product_request_body = swagger_client.AssignGroupsProductRequestBody() # AssignGroupsProductRequestBody | JSON object that contains information to assign groups to product

try:
    # Assigns groups of users to a product.
    api_response = api_instance.products_ref_groups_put(api_token, ref, assign_groups_product_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->products_ref_groups_put: %s\n" % e)
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

