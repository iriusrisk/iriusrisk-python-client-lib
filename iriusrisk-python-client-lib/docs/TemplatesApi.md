# iriusrisk_python_client_lib.TemplatesApi

All URIs are relative to *https://demo.iriusrisk.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_upload_post**](TemplatesApi.md#products_upload_post) | **POST** /products/upload | Creates a new product, library or template from a XML file upload.


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
api_instance = iriusrisk_python_client_lib.TemplatesApi()
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
    print("Exception when calling TemplatesApi->products_upload_post: %s\n" % e)
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

