# iriusrisk_python_client_lib.RulesApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_rule**](RulesApi.md#copy_rule) | **POST** /api/v2/rules/{rule-id}/copy | Copies an existing rule.
[**create_rule**](RulesApi.md#create_rule) | **POST** /api/v2/rules | Creates a new rule.
[**delete_rule**](RulesApi.md#delete_rule) | **DELETE** /api/v2/rules/{rule-id} | Deletes a rule.
[**execute_rules**](RulesApi.md#execute_rules) | **POST** /api/v2/rules/execute | Executes the rules over all visible projects.
[**get_all_actions**](RulesApi.md#get_all_actions) | **GET** /api/v2/rules/actions | Gets all the actions.
[**get_all_answers**](RulesApi.md#get_all_answers) | **GET** /api/v2/rules/{rule-context-id}/answers | Gets all the answers applicable to the context.
[**get_all_conclusions**](RulesApi.md#get_all_conclusions) | **GET** /api/v2/rules/{rule-context-id}/conclusions | Gets all the conclusions applicable to the context.
[**get_all_conditions**](RulesApi.md#get_all_conditions) | **GET** /api/v2/rules/conditions | Gets all the conditions.
[**get_all_questions**](RulesApi.md#get_all_questions) | **GET** /api/v2/rules/{rule-context-id}/questions | Gets all the questions applicable to the context.
[**get_all_rules**](RulesApi.md#get_all_rules) | **GET** /api/v2/rules | Gets all rules.
[**get_rule**](RulesApi.md#get_rule) | **GET** /api/v2/rules/{rule-id} | Gets the details of a rule.
[**get_rule_source_code**](RulesApi.md#get_rule_source_code) | **GET** /api/v2/rules/{rule-id}/source-code | Gets the source code of a rule.
[**reload_rule**](RulesApi.md#reload_rule) | **POST** /api/v2/rules/reload | Reloads all enabled rules into the containers.
[**update_rule**](RulesApi.md#update_rule) | **PUT** /api/v2/rules/{rule-id} | Updates an existing rule.
[**update_rule_source_code**](RulesApi.md#update_rule_source_code) | **PUT** /api/v2/rules/{rule-id}/source-code | Updates the source code of a rule.

# **copy_rule**
> RuleDetailResponse copy_rule(body, rule_id)

Copies an existing rule.

Copies an existing rule.  Conditions to be able to perform the action:<ul><li>To have the permission **EDIT_RULES** granted.</li><li>The target library must not be an IriusRisk provided library.</li></ul>

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
api_instance = iriusrisk_python_client_lib.RulesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CopyRuleRequest() # CopyRuleRequest | 
rule_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique id of the rule.

try:
    # Copies an existing rule.
    api_response = api_instance.copy_rule(body, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->copy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CopyRuleRequest**](CopyRuleRequest.md)|  | 
 **rule_id** | [**str**](.md)| The unique id of the rule. | 

### Return type

[**RuleDetailResponse**](RuleDetailResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rule**
> RuleDetailResponse create_rule(body)

Creates a new rule.

Creates a new rule.  Conditions to be able to perform the action:<ul><li>To have the permission **EDIT_RULES** granted.</li><li>The rule must not be placed in an IriusRisk provided library.</li></ul>

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
api_instance = iriusrisk_python_client_lib.RulesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.RuleRequest() # RuleRequest | 

try:
    # Creates a new rule.
    api_response = api_instance.create_rule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->create_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RuleRequest**](RuleRequest.md)|  | 

### Return type

[**RuleDetailResponse**](RuleDetailResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rule**
> delete_rule(rule_id)

Deletes a rule.

Deletes a rule.  Conditions to be able to perform the action:<ul><li>To have the permission **EDIT_RULES** granted.</li><li>The rule must not reside in an IriusRisk provided library.</li></ul>

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
api_instance = iriusrisk_python_client_lib.RulesApi(iriusrisk_python_client_lib.ApiClient(configuration))
rule_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique id of the rule.

try:
    # Deletes a rule.
    api_instance.delete_rule(rule_id)
except ApiException as e:
    print("Exception when calling RulesApi->delete_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | [**str**](.md)| The unique id of the rule. | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_rules**
> AsyncOperationIdResponse execute_rules(body, x_irius_async)

Executes the rules over all visible projects.

Executes the rules over all visible projects.  Conditions to be able to perform the action:<ul><li>To have the permission **EDIT_RULES** granted.</li><li>Only projects visible to the user will be affected.</li><li>Projects that are currently undergoing synchronization already will not be affected.</li><li>Projects that are locked mode will not be affected.</li><li>Projects that are in read-only mode will not be affected.</li></ul>

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
api_instance = iriusrisk_python_client_lib.RulesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.ExecuteRulesRequest() # ExecuteRulesRequest | 
x_irius_async = true # bool | Sets whether the endpoint works asynchronously or not passed as parameter.

try:
    # Executes the rules over all visible projects.
    api_response = api_instance.execute_rules(body, x_irius_async)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->execute_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExecuteRulesRequest**](ExecuteRulesRequest.md)|  | 
 **x_irius_async** | **bool**| Sets whether the endpoint works asynchronously or not passed as parameter. | 

### Return type

[**AsyncOperationIdResponse**](AsyncOperationIdResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_actions**
> PagedModelActionListResponse get_all_actions(filter=filter, page=page, size=size, sort=sort)

Gets all the actions.

Gets all the actions. Conditions to be able to perform the action:<ul><li>To have the permission **EDIT_RULES** granted.</li></ul>

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
api_instance = iriusrisk_python_client_lib.RulesApi(iriusrisk_python_client_lib.ApiClient(configuration))
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the actions.
    api_response = api_instance.get_all_actions(filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->get_all_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelActionListResponse**](PagedModelActionListResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_answers**
> PagedModelAnswerListResponse get_all_answers(rule_context_id, filter=filter, page=page, size=size, sort=sort)

Gets all the answers applicable to the context.

Gets all the answers applicable to the context. Conditions to be able to perform the action:<ul><li>To have the permission **EDIT_RULES** granted.</li></ul>

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
api_instance = iriusrisk_python_client_lib.RulesApi(iriusrisk_python_client_lib.ApiClient(configuration))
rule_context_id = 'rule_context_id_example' # str | The unique id of the rules context.
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the answers applicable to the context.
    api_response = api_instance.get_all_answers(rule_context_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->get_all_answers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_context_id** | **str**| The unique id of the rules context. | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelAnswerListResponse**](PagedModelAnswerListResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_conclusions**
> PagedModelConclusionListResponse get_all_conclusions(rule_context_id, filter=filter, page=page, size=size, sort=sort)

Gets all the conclusions applicable to the context.

Gets all the conclusions applicable to the context. Conditions to be able to perform the action:<ul><li>To have the permission **EDIT_RULES** granted.</li></ul>

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
api_instance = iriusrisk_python_client_lib.RulesApi(iriusrisk_python_client_lib.ApiClient(configuration))
rule_context_id = 'rule_context_id_example' # str | The unique id of the rules context.
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the conclusions applicable to the context.
    api_response = api_instance.get_all_conclusions(rule_context_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->get_all_conclusions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_context_id** | **str**| The unique id of the rules context. | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelConclusionListResponse**](PagedModelConclusionListResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_conditions**
> PagedModelConditionListResponse get_all_conditions(filter=filter, page=page, size=size, sort=sort)

Gets all the conditions.

Gets all the conditions. Conditions to be able to perform the action:<ul><li>To have the permission **EDIT_RULES** granted.</li></ul>

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
api_instance = iriusrisk_python_client_lib.RulesApi(iriusrisk_python_client_lib.ApiClient(configuration))
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the conditions.
    api_response = api_instance.get_all_conditions(filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->get_all_conditions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelConditionListResponse**](PagedModelConditionListResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_questions**
> PagedModelQuestionListResponse get_all_questions(rule_context_id, filter=filter, page=page, size=size, sort=sort)

Gets all the questions applicable to the context.

Gets all the questions applicable to the context. Conditions to be able to perform the action:<ul><li>To have the permission **EDIT_RULES** granted.</li></ul>

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
api_instance = iriusrisk_python_client_lib.RulesApi(iriusrisk_python_client_lib.ApiClient(configuration))
rule_context_id = 'rule_context_id_example' # str | The unique id of the rules context.
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the questions applicable to the context.
    api_response = api_instance.get_all_questions(rule_context_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->get_all_questions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_context_id** | **str**| The unique id of the rules context. | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelQuestionListResponse**](PagedModelQuestionListResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_rules**
> PagedModelRuleResponse get_all_rules(page=page, size=size, sort=sort, filter=filter)

Gets all rules.

Gets all rules.  Conditions to be able to perform the action:<ul><li>To have the permission **EDIT_RULES** granted.</li></ul>

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
api_instance = iriusrisk_python_client_lib.RulesApi(iriusrisk_python_client_lib.ApiClient(configuration))
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)

try:
    # Gets all rules.
    api_response = api_instance.get_all_rules(page=page, size=size, sort=sort, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->get_all_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 

### Return type

[**PagedModelRuleResponse**](PagedModelRuleResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule**
> RuleDetailResponse get_rule(rule_id)

Gets the details of a rule.

Gets the details of a rule.  Conditions to be able to perform the action:<ul><li>To have the permission **EDIT_RULES** granted.</li></ul>

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
api_instance = iriusrisk_python_client_lib.RulesApi(iriusrisk_python_client_lib.ApiClient(configuration))
rule_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique id of the rule.

try:
    # Gets the details of a rule.
    api_response = api_instance.get_rule(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->get_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | [**str**](.md)| The unique id of the rule. | 

### Return type

[**RuleDetailResponse**](RuleDetailResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_source_code**
> RuleSourceCodeResponse get_rule_source_code(rule_id)

Gets the source code of a rule.

Gets the source code of a rule.  Conditions to be able to perform the action:<ul><li>To have both permissions **EDIT_RULES** and **DROOLS_CREATION_RULE** granted.</li></ul>

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
api_instance = iriusrisk_python_client_lib.RulesApi(iriusrisk_python_client_lib.ApiClient(configuration))
rule_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique id of the rule.

try:
    # Gets the source code of a rule.
    api_response = api_instance.get_rule_source_code(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->get_rule_source_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | [**str**](.md)| The unique id of the rule. | 

### Return type

[**RuleSourceCodeResponse**](RuleSourceCodeResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reload_rule**
> reload_rule()

Reloads all enabled rules into the containers.

Reloads all enabled rules into the containers restoring their state. Conditions to be able to perform the action:<ul><li>To have the permission **EDIT_RULES** granted.</li><li>To have the permission **DROOLS_CREATION_RULE** granted.</li></ul>

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
api_instance = iriusrisk_python_client_lib.RulesApi(iriusrisk_python_client_lib.ApiClient(configuration))

try:
    # Reloads all enabled rules into the containers.
    api_instance.reload_rule()
except ApiException as e:
    print("Exception when calling RulesApi->reload_rule: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rule**
> RuleDetailResponse update_rule(body, rule_id)

Updates an existing rule.

Updates an existing rule.  Conditions to be able to perform the action:<ul><li>To have the permission **EDIT_RULES** granted.</li><li>The rule must not reside in an IriusRisk provided library.</li></ul>

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
api_instance = iriusrisk_python_client_lib.RulesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.RuleRequest() # RuleRequest | 
rule_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique id of the rule.

try:
    # Updates an existing rule.
    api_response = api_instance.update_rule(body, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->update_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RuleRequest**](RuleRequest.md)|  | 
 **rule_id** | [**str**](.md)| The unique id of the rule. | 

### Return type

[**RuleDetailResponse**](RuleDetailResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rule_source_code**
> RuleSourceCodeResponse update_rule_source_code(body, rule_id)

Updates the source code of a rule.

Updates the source code of a rule.  Conditions to be able to perform the action:<ul><li>To have both permissions **EDIT_RULES** and **DROOLS_CREATION_RULE** granted.</li><li>The rule must not reside in an IriusRisk provided library.</li></ul>If this endpoint is used, the **conditions** and **actions** inserted through PUT:/api/v2/rules/{rule-id} will be removed, and only the provided source code will be used.

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
api_instance = iriusrisk_python_client_lib.RulesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateRuleSourceCodeRequest() # UpdateRuleSourceCodeRequest | 
rule_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique id of the rule.

try:
    # Updates the source code of a rule.
    api_response = api_instance.update_rule_source_code(body, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->update_rule_source_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRuleSourceCodeRequest**](UpdateRuleSourceCodeRequest.md)|  | 
 **rule_id** | [**str**](.md)| The unique id of the rule. | 

### Return type

[**RuleSourceCodeResponse**](RuleSourceCodeResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

