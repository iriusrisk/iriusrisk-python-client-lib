# swagger_client.UsersApi

All URIs are relative to *https://demo.iriusrisk.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_group_users_delete**](UsersApi.md#groups_group_users_delete) | **DELETE** /groups/{group}/users | Unassign a list of users from a group
[**groups_group_users_get**](UsersApi.md#groups_group_users_get) | **GET** /groups/{group}/users | List users from a group
[**groups_group_users_put**](UsersApi.md#groups_group_users_put) | **PUT** /groups/{group}/users | Assigns users to a group
[**groups_group_users_user_delete**](UsersApi.md#groups_group_users_user_delete) | **DELETE** /groups/{group}/users/{user} | Removes a user from a group
[**products_ref_users_delete**](UsersApi.md#products_ref_users_delete) | **DELETE** /products/{ref}/users | Unassigns a list of users from a product.
[**products_ref_users_get**](UsersApi.md#products_ref_users_get) | **GET** /products/{ref}/users | List all users assigned to a product
[**products_ref_users_put**](UsersApi.md#products_ref_users_put) | **PUT** /products/{ref}/users | Assigns users to a product.
[**products_ref_users_user_delete**](UsersApi.md#products_ref_users_user_delete) | **DELETE** /products/{ref}/users/{user} | Unassigns a user from a product
[**users_get**](UsersApi.md#users_get) | **GET** /users | List of all Users.
[**users_post**](UsersApi.md#users_post) | **POST** /users | Creates a new user
[**users_username_delete**](UsersApi.md#users_username_delete) | **DELETE** /users/{username} | Deletes a user
[**users_username_get**](UsersApi.md#users_username_get) | **GET** /users/{username} | Get all the information of a user
[**users_username_token_post**](UsersApi.md#users_username_token_post) | **POST** /users/{username}/token | Generates a user API token


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
api_instance = swagger_client.UsersApi()
api_token = 'api_token_example' # str | Authentication token
group = 'group_example' # str | name of the group
unassing_users_group_request_body = swagger_client.UnassingUsersGroupRequestBody() # UnassingUsersGroupRequestBody | JSON object that contains information to unassign users from group

try:
    # Unassign a list of users from a group
    api_instance.groups_group_users_delete(api_token, group, unassing_users_group_request_body)
except ApiException as e:
    print("Exception when calling UsersApi->groups_group_users_delete: %s\n" % e)
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
api_instance = swagger_client.UsersApi()
api_token = 'api_token_example' # str | Authentication token
group = 'group_example' # str | name of the group

try:
    # List users from a group
    api_response = api_instance.groups_group_users_get(api_token, group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->groups_group_users_get: %s\n" % e)
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
api_instance = swagger_client.UsersApi()
api_token = 'api_token_example' # str | Authentication token
group = 'group_example' # str | name of the group
assign_user_group_request_body = swagger_client.AssignUserGroupRequestBody() # AssignUserGroupRequestBody | JSON object that contains information to assign users to group

try:
    # Assigns users to a group
    api_response = api_instance.groups_group_users_put(api_token, group, assign_user_group_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->groups_group_users_put: %s\n" % e)
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
api_instance = swagger_client.UsersApi()
api_token = 'api_token_example' # str | Authentication token
group = 'group_example' # str | name of the group
user = 'user_example' # str | user to be removed from group

try:
    # Removes a user from a group
    api_instance.groups_group_users_user_delete(api_token, group, user)
except ApiException as e:
    print("Exception when calling UsersApi->groups_group_users_user_delete: %s\n" % e)
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

# **products_ref_users_delete**
> products_ref_users_delete(api_token, ref, unassign_users_product_request_body)

Unassigns a list of users from a product.

Unassign a list of users from a product. Conditions to be able to perform the action:   - To have the permission **PRODUCT_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | Reference for product
unassign_users_product_request_body = swagger_client.UnassignUsersProductRequestBody() # UnassignUsersProductRequestBody | JSON object that contains information to unassign users from product

try:
    # Unassigns a list of users from a product.
    api_instance.products_ref_users_delete(api_token, ref, unassign_users_product_request_body)
except ApiException as e:
    print("Exception when calling UsersApi->products_ref_users_delete: %s\n" % e)
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
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | Reference to product

try:
    # List all users assigned to a product
    api_response = api_instance.products_ref_users_get(api_token, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->products_ref_users_get: %s\n" % e)
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
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | Reference for product
assign_users_product_request_body = swagger_client.AssignUsersProductRequestBody() # AssignUsersProductRequestBody | JSON data that contains the information to assign users to product

try:
    # Assigns users to a product.
    api_response = api_instance.products_ref_users_put(api_token, ref, assign_users_product_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->products_ref_users_put: %s\n" % e)
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
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | Reference for product
user = 'user_example' # str | Username of the user who will be unassigned from the product

try:
    # Unassigns a user from a product
    api_instance.products_ref_users_user_delete(api_token, ref, user)
except ApiException as e:
    print("Exception when calling UsersApi->products_ref_users_user_delete: %s\n" % e)
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

# **users_get**
> list[User] users_get(api_token)

List of all Users.

Returns a list of all the users of the system. Conditions to be able to perform the action:   - To have the permission **ALL_USERS_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
api_token = 'api_token_example' # str | Authentication token

try:
    # List of all Users.
    api_response = api_instance.users_get(api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post**
> users_post(api_token, create_user_request_body)

Creates a new user

Creates a new user. Conditions to be able to perform the action:   - To have the permission **ALL_USERS_UPDATE** granted. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
api_token = 'api_token_example' # str | Authentication token
create_user_request_body = swagger_client.CreateUserRequestBody() # CreateUserRequestBody | JSON data that contains information to creates new user

try:
    # Creates a new user
    api_instance.users_post(api_token, create_user_request_body)
except ApiException as e:
    print("Exception when calling UsersApi->users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **create_user_request_body** | [**CreateUserRequestBody**](CreateUserRequestBody.md)| JSON data that contains information to creates new user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_delete**
> users_username_delete(api_token, username)

Deletes a user

Deletes a user. Conditions to be able to perform the action:   - To have the permission **ALL_USERS_UPDATE** granted, or   - To have the permission **MANAGE_USERS_BU** granted. Having this permission you can delete users who belongs to some of your user groups. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
api_token = 'api_token_example' # str | Authentication token
username = 'username_example' # str | User's username

try:
    # Deletes a user
    api_instance.users_username_delete(api_token, username)
except ApiException as e:
    print("Exception when calling UsersApi->users_username_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **username** | **str**| User&#39;s username | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_get**
> UserDetailed users_username_get(api_token, username)

Get all the information of a user

Get all the relevant information of a user 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
api_token = 'api_token_example' # str | Authentication token
username = 'username_example' # str | User's username

try:
    # Get all the information of a user
    api_response = api_instance.users_username_get(api_token, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_username_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **username** | **str**| User&#39;s username | 

### Return type

[**UserDetailed**](UserDetailed.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_token_post**
> str users_username_token_post(api_token, username)

Generates a user API token

Generates a new user API token. If the user already has a generated API token, generates a new one. Conditions to be able to perform the action:   - To have the permission **ALL_USERS_UPDATE** granted, or   - To have the permission **MANAGE_USERS_BU** granted. Having this permission you can generate a user API token to users who belongs to some of your user groups. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
api_token = 'api_token_example' # str | Authentication token
username = 'username_example' # str | User's username

try:
    # Generates a user API token
    api_response = api_instance.users_username_token_post(api_token, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_username_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| Authentication token | 
 **username** | **str**| User&#39;s username | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

