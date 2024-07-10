# iriusrisk_python_client_lib.ComponentsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_category_component**](ComponentsApi.md#create_category_component) | **POST** /api/v2/components/categories | Creates a new component category
[**create_component**](ComponentsApi.md#create_component) | **POST** /api/v2/components | Creates a new component
[**create_component_definition_risk_pattern**](ComponentsApi.md#create_component_definition_risk_pattern) | **POST** /api/v2/components/{component-id}/risk-patterns | Associates a component to a risk pattern
[**delete_component_by_uuid**](ComponentsApi.md#delete_component_by_uuid) | **DELETE** /api/v2/components/{component-id} | Removes the component permanently
[**delete_component_custom_icon**](ComponentsApi.md#delete_component_custom_icon) | **DELETE** /api/v2/components/{component-id}/custom-icon | Removes the associated custom icon from a component
[**delete_risk_pattern_from_component**](ComponentsApi.md#delete_risk_pattern_from_component) | **DELETE** /api/v2/components/{component-id}/risk-patterns/{risk-pattern-id} | Removes the association between a component to a risk pattern
[**get_all_business_units_for_project_component**](ComponentsApi.md#get_all_business_units_for_project_component) | **GET** /api/v2/components/{component-id}/visibility/business-units | Gets the list of business units with whom a project component is shared.
[**get_all_component_risk_patterns**](ComponentsApi.md#get_all_component_risk_patterns) | **GET** /api/v2/components/{component-id}/risk-patterns | Gets all the risk patterns associated with a component
[**get_all_component_risk_patterns_summary_for_component**](ComponentsApi.md#get_all_component_risk_patterns_summary_for_component) | **GET** /api/v2/components/{component-id}/risk-patterns/summary | Given a component, returns the summary list of its risk patterns.
[**get_all_components_summary**](ComponentsApi.md#get_all_components_summary) | **GET** /api/v2/components/summary | Gets the summary list of components
[**get_all_library_risk_patterns_for_components**](ComponentsApi.md#get_all_library_risk_patterns_for_components) | **GET** /api/v2/components/risk-patterns | Gets all the risk patterns associated with a library
[**get_all_projects_by_component**](ComponentsApi.md#get_all_projects_by_component) | **GET** /api/v2/components/{component-id}/projects | Gets all the projects registered in the system associated with a component
[**get_all_users_for_project_component**](ComponentsApi.md#get_all_users_for_project_component) | **GET** /api/v2/components/{component-id}/visibility/users | Gets the list of users with whom a project component is shared.
[**get_category_components_summary**](ComponentsApi.md#get_category_components_summary) | **GET** /api/v2/components/categories/summary | Gets all the component categories
[**get_component_by_uuid**](ComponentsApi.md#get_component_by_uuid) | **GET** /api/v2/components/{component-id} | Gets the component
[**get_filtered_components**](ComponentsApi.md#get_filtered_components) | **GET** /api/v2/components | Gets all the components registered in the system
[**share_project_component_with_business_unit**](ComponentsApi.md#share_project_component_with_business_unit) | **POST** /api/v2/components/{component-id}/visibility/business-units | Shares a project component with a new business unit.
[**share_project_component_with_user**](ComponentsApi.md#share_project_component_with_user) | **POST** /api/v2/components/{component-id}/visibility/users | Shares a project component with a new user.
[**un_share_project_component_with_business_unit**](ComponentsApi.md#un_share_project_component_with_business_unit) | **DELETE** /api/v2/components/{component-id}/visibility/business-units/{business-unit-id} | Stops sharing a project component with a specific business unit.
[**un_share_project_component_with_user**](ComponentsApi.md#un_share_project_component_with_user) | **DELETE** /api/v2/components/{component-id}/visibility/users/{username} | Stops sharing a project component with a specific user.
[**update_component**](ComponentsApi.md#update_component) | **PUT** /api/v2/components/{component-id} | Modifies the component
[**update_component_custom_icon**](ComponentsApi.md#update_component_custom_icon) | **PUT** /api/v2/components/{component-id}/custom-icon | Updates the custom icon associated to a component

# **create_category_component**
> CategoryComponentResponse create_category_component(body)

Creates a new component category

Creates a new component category. Conditions to be able to perform the action: - To have the permission **COMPONENT_DEFINITIONS_UPDATE** granted

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
api_instance = iriusrisk_python_client_lib.ComponentsApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateCategoryComponentRequest() # CreateCategoryComponentRequest | 

try:
    # Creates a new component category
    api_response = api_instance.create_category_component(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->create_category_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCategoryComponentRequest**](CreateCategoryComponentRequest.md)|  | 

### Return type

[**CategoryComponentResponse**](CategoryComponentResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_component**
> ComponentBaseResponse create_component(body)

Creates a new component

Creates a new component. Conditions to be able to perform the action: - To have the permission **COMPONENT_DEFINITIONS_UPDATE** granted

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
api_instance = iriusrisk_python_client_lib.ComponentsApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.ComponentRequest() # ComponentRequest | 

try:
    # Creates a new component
    api_response = api_instance.create_component(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->create_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComponentRequest**](ComponentRequest.md)|  | 

### Return type

[**ComponentBaseResponse**](ComponentBaseResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_component_definition_risk_pattern**
> create_component_definition_risk_pattern(body, component_id)

Associates a component to a risk pattern

Associates the given component to the given risk pattern. Conditions to be able to perform the action: - To have the permission **COMPONENT_DEFINITIONS_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.ComponentsApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateComponentDefinitionRiskPatternRequest() # CreateComponentDefinitionRiskPatternRequest | 
component_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Associates a component to a risk pattern
    api_instance.create_component_definition_risk_pattern(body, component_id)
except ApiException as e:
    print("Exception when calling ComponentsApi->create_component_definition_risk_pattern: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateComponentDefinitionRiskPatternRequest**](CreateComponentDefinitionRiskPatternRequest.md)|  | 
 **component_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_component_by_uuid**
> delete_component_by_uuid(component_id)

Removes the component permanently

Removes the component permanently. Conditions to be able to perform the action: - To have the permission **COMPONENT_DEFINITIONS_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.ComponentsApi(iriusrisk_python_client_lib.ApiClient(configuration))
component_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the component

try:
    # Removes the component permanently
    api_instance.delete_component_by_uuid(component_id)
except ApiException as e:
    print("Exception when calling ComponentsApi->delete_component_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | [**str**](.md)| ID of the component | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_component_custom_icon**
> delete_component_custom_icon(component_id)

Removes the associated custom icon from a component

Removes the associated custom icon from a component. Conditions to be able to perform the action: - To have the permission **COMPONENT_DEFINITIONS_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.ComponentsApi(iriusrisk_python_client_lib.ApiClient(configuration))
component_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the component

try:
    # Removes the associated custom icon from a component
    api_instance.delete_component_custom_icon(component_id)
except ApiException as e:
    print("Exception when calling ComponentsApi->delete_component_custom_icon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | [**str**](.md)| ID of the component | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_risk_pattern_from_component**
> delete_risk_pattern_from_component(component_id, risk_pattern_id)

Removes the association between a component to a risk pattern

Removes the association between the given component to the given risk pattern. Conditions to be able to perform the action. - To have the permission **COMPONENT_DEFINITIONS_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.ComponentsApi(iriusrisk_python_client_lib.ApiClient(configuration))
component_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the component
risk_pattern_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the risk pattern

try:
    # Removes the association between a component to a risk pattern
    api_instance.delete_risk_pattern_from_component(component_id, risk_pattern_id)
except ApiException as e:
    print("Exception when calling ComponentsApi->delete_risk_pattern_from_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | [**str**](.md)| ID of the component | 
 **risk_pattern_id** | [**str**](.md)| ID of the risk pattern | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_business_units_for_project_component**
> PagedModelGetAllProjectComponentBusinessUnitResponse get_all_business_units_for_project_component(component_id, filter=filter, page=page, size=size, sort=sort)

Gets the list of business units with whom a project component is shared.

Gets the list of business units with whom a project component is shared. Conditions to be able to perform the action: - To have the permission **COMPONENT_DEFINITIONS_VIEW** granted, or, - To have the permission **COMPONENT_DEFINITIONS_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.ComponentsApi(iriusrisk_python_client_lib.ApiClient(configuration))
component_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the component
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the list of business units with whom a project component is shared.
    api_response = api_instance.get_all_business_units_for_project_component(component_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_all_business_units_for_project_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | [**str**](.md)| ID of the component | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelGetAllProjectComponentBusinessUnitResponse**](PagedModelGetAllProjectComponentBusinessUnitResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_component_risk_patterns**
> PagedModelComponentRiskPatternResponse get_all_component_risk_patterns(component_id, filter=filter, page=page, size=size, sort=sort)

Gets all the risk patterns associated with a component

Gets all the risk patterns registered in the system associated with the component identified by the given id. Conditions to be able to perform the action: - To have the permission **COMPONENT_DEFINITIONS_VIEW** granted, or, - To have the permission **COMPONENT_DEFINITIONS_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.ComponentsApi(iriusrisk_python_client_lib.ApiClient(configuration))
component_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the component
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the risk patterns associated with a component
    api_response = api_instance.get_all_component_risk_patterns(component_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_all_component_risk_patterns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | [**str**](.md)| ID of the component | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelComponentRiskPatternResponse**](PagedModelComponentRiskPatternResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_component_risk_patterns_summary_for_component**
> PagedModelComponentRiskPatternSummaryResponse get_all_component_risk_patterns_summary_for_component(component_id, filter=filter, page=page, size=size, sort=sort)

Given a component, returns the summary list of its risk patterns.

Get the summary list of risk patterns registered in the system associated with the component identified by the given id. Conditions to be able to perform the action: - The user must be authenticated

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
api_instance = iriusrisk_python_client_lib.ComponentsApi(iriusrisk_python_client_lib.ApiClient(configuration))
component_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the component
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Given a component, returns the summary list of its risk patterns.
    api_response = api_instance.get_all_component_risk_patterns_summary_for_component(component_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_all_component_risk_patterns_summary_for_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | [**str**](.md)| ID of the component | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelComponentRiskPatternSummaryResponse**](PagedModelComponentRiskPatternSummaryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_components_summary**
> PagedModelComponentDefinitionSummaryResponse get_all_components_summary(filter=filter, page=page, size=size, sort=sort)

Gets the summary list of components

Gets the summary list of components registered in the system. Conditions to be able to perform the action: - The user must be authenticated

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
api_instance = iriusrisk_python_client_lib.ComponentsApi(iriusrisk_python_client_lib.ApiClient(configuration))
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the summary list of components
    api_response = api_instance.get_all_components_summary(filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_all_components_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelComponentDefinitionSummaryResponse**](PagedModelComponentDefinitionSummaryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_library_risk_patterns_for_components**
> PagedModelComponentLibraryRiskPatternResponse get_all_library_risk_patterns_for_components(filter=filter, page=page, size=size, sort=sort)

Gets all the risk patterns associated with a library

Gets all the risk patterns registered in the system associated with the library identified by the given id. Conditions to be able to perform the action: - To have the permission **COMPONENT_DEFINITIONS_VIEW** granted or, - To have the permission **COMPONENT_DEFINITIONS_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.ComponentsApi(iriusrisk_python_client_lib.ApiClient(configuration))
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the risk patterns associated with a library
    api_response = api_instance.get_all_library_risk_patterns_for_components(filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_all_library_risk_patterns_for_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelComponentLibraryRiskPatternResponse**](PagedModelComponentLibraryRiskPatternResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_projects_by_component**
> PagedModelProjectsByComponentResponse get_all_projects_by_component(component_id, filter=filter, page=page, size=size, sort=sort)

Gets all the projects registered in the system associated with a component

Gets all the projects registered in the system associated with the component identified by the given id. Conditions to be able to perform the action: - To have the permission **COMPONENT_DEFINITIONS_VIEW** granted, or, - To have the permission **COMPONENT_DEFINITIONS_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.ComponentsApi(iriusrisk_python_client_lib.ApiClient(configuration))
component_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the component
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the projects registered in the system associated with a component
    api_response = api_instance.get_all_projects_by_component(component_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_all_projects_by_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | [**str**](.md)| ID of the component | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelProjectsByComponentResponse**](PagedModelProjectsByComponentResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_users_for_project_component**
> PagedModelGetAllProjectComponentUserResponse get_all_users_for_project_component(component_id, filter=filter, page=page, size=size, sort=sort)

Gets the list of users with whom a project component is shared.

Gets the list of users with whom a project component is shared. Conditions to be able to perform the action: - To have the permission **COMPONENT_DEFINITIONS_VIEW** granted, or, - To have the permission **COMPONENT_DEFINITIONS_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.ComponentsApi(iriusrisk_python_client_lib.ApiClient(configuration))
component_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the component
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the list of users with whom a project component is shared.
    api_response = api_instance.get_all_users_for_project_component(component_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_all_users_for_project_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | [**str**](.md)| ID of the component | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelGetAllProjectComponentUserResponse**](PagedModelGetAllProjectComponentUserResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_components_summary**
> PagedModelCategoryComponentResponse get_category_components_summary(filter=filter, page=page, size=size, sort=sort)

Gets all the component categories

Gets all the component categories registered in the system. - The user must be authenticated

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
api_instance = iriusrisk_python_client_lib.ComponentsApi(iriusrisk_python_client_lib.ApiClient(configuration))
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the component categories
    api_response = api_instance.get_category_components_summary(filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_category_components_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelCategoryComponentResponse**](PagedModelCategoryComponentResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_component_by_uuid**
> ComponentResponseBody get_component_by_uuid(component_id)

Gets the component

Gets the component. Conditions to be able to perform the action: - To have the permission **COMPONENT_DEFINITIONS_VIEW** granted, or, - To have the permission **COMPONENT_DEFINITIONS_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.ComponentsApi(iriusrisk_python_client_lib.ApiClient(configuration))
component_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the component

try:
    # Gets the component
    api_response = api_instance.get_component_by_uuid(component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_component_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | [**str**](.md)| ID of the component | 

### Return type

[**ComponentResponseBody**](ComponentResponseBody.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filtered_components**
> PagedModelComponentBaseResponse get_filtered_components(filter=filter, page=page, size=size, sort=sort)

Gets all the components registered in the system

Gets all the components registered in the system. Conditions to be able to perform the action: - To have the permission **COMPONENT_DEFINITIONS_VIEW** granted, or, - To have the permission **COMPONENT_DEFINITIONS_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.ComponentsApi(iriusrisk_python_client_lib.ApiClient(configuration))
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the components registered in the system
    api_response = api_instance.get_filtered_components(filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_filtered_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelComponentBaseResponse**](PagedModelComponentBaseResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_project_component_with_business_unit**
> share_project_component_with_business_unit(body, component_id)

Shares a project component with a new business unit.

Shares a project component with a new business unit. Conditions to be able to perform the action: - To have the permission **COMPONENT_DEFINITIONS_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.ComponentsApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.ComponentBusinessUnitRequest() # ComponentBusinessUnitRequest | 
component_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the component

try:
    # Shares a project component with a new business unit.
    api_instance.share_project_component_with_business_unit(body, component_id)
except ApiException as e:
    print("Exception when calling ComponentsApi->share_project_component_with_business_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComponentBusinessUnitRequest**](ComponentBusinessUnitRequest.md)|  | 
 **component_id** | [**str**](.md)| ID of the component | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_project_component_with_user**
> share_project_component_with_user(body, component_id)

Shares a project component with a new user.

Shares a project component with a new user. Conditions to be able to perform the action: - To have the permission **COMPONENT_DEFINITIONS_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.ComponentsApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UserProjectComponentRequest() # UserProjectComponentRequest | 
component_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the component

try:
    # Shares a project component with a new user.
    api_instance.share_project_component_with_user(body, component_id)
except ApiException as e:
    print("Exception when calling ComponentsApi->share_project_component_with_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserProjectComponentRequest**](UserProjectComponentRequest.md)|  | 
 **component_id** | [**str**](.md)| ID of the component | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **un_share_project_component_with_business_unit**
> un_share_project_component_with_business_unit(component_id, business_unit_id)

Stops sharing a project component with a specific business unit.

Stops sharing a project component with a specific business unit. Conditions to be able to perform the action: - To have the permission **COMPONENT_DEFINITIONS_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.ComponentsApi(iriusrisk_python_client_lib.ApiClient(configuration))
component_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the component
business_unit_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the business unit.

try:
    # Stops sharing a project component with a specific business unit.
    api_instance.un_share_project_component_with_business_unit(component_id, business_unit_id)
except ApiException as e:
    print("Exception when calling ComponentsApi->un_share_project_component_with_business_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | [**str**](.md)| ID of the component | 
 **business_unit_id** | [**str**](.md)| Unique identifier of the business unit. | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **un_share_project_component_with_user**
> un_share_project_component_with_user(component_id, username)

Stops sharing a project component with a specific user.

Stops sharing a project component with a specific user. Conditions to be able to perform the action: - To have the permission **COMPONENT_DEFINITIONS_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.ComponentsApi(iriusrisk_python_client_lib.ApiClient(configuration))
component_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the component
username = 'username_example' # str | The username of the user requested.

try:
    # Stops sharing a project component with a specific user.
    api_instance.un_share_project_component_with_user(component_id, username)
except ApiException as e:
    print("Exception when calling ComponentsApi->un_share_project_component_with_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | [**str**](.md)| ID of the component | 
 **username** | **str**| The username of the user requested. | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_component**
> ComponentResponseBody update_component(body, component_id)

Modifies the component

Modifies the component. Conditions to be able to perform the action: - To have the permission **COMPONENT_DEFINITIONS_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.ComponentsApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateComponentRequestBody() # UpdateComponentRequestBody | 
component_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the component

try:
    # Modifies the component
    api_response = api_instance.update_component(body, component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->update_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateComponentRequestBody**](UpdateComponentRequestBody.md)|  | 
 **component_id** | [**str**](.md)| ID of the component | 

### Return type

[**ComponentResponseBody**](ComponentResponseBody.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_component_custom_icon**
> ComponentCustomIconResponse update_component_custom_icon(body, component_id)

Updates the custom icon associated to a component

Updates the custom icon associated to a component. Conditions to be able to perform the action: - To have the permission **COMPONENT_DEFINITIONS_UPDATE** granted. - The component identified by component-id must exist

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
api_instance = iriusrisk_python_client_lib.ComponentsApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.ComponentCustomIconRequest() # ComponentCustomIconRequest | 
component_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the component

try:
    # Updates the custom icon associated to a component
    api_response = api_instance.update_component_custom_icon(body, component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->update_component_custom_icon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComponentCustomIconRequest**](ComponentCustomIconRequest.md)|  | 
 **component_id** | [**str**](.md)| ID of the component | 

### Return type

[**ComponentCustomIconResponse**](ComponentCustomIconResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

