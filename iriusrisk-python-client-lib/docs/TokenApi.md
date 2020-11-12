# swagger_client.TokenApi

All URIs are relative to *https://demo.iriusrisk.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_username_token_post**](TokenApi.md#users_username_token_post) | **POST** /users/{username}/token | Generates a user API token


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
api_instance = swagger_client.TokenApi()
api_token = 'api_token_example' # str | Authentication token
username = 'username_example' # str | User's username

try:
    # Generates a user API token
    api_response = api_instance.users_username_token_post(api_token, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->users_username_token_post: %s\n" % e)
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

