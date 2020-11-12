# swagger-client
Products API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentsApi(swagger_client.ApiClient(configuration))
api_token = 'api_token_example' # str | Authentication token
ref = 'ref_example' # str | ID for product
component_ref = 'component_ref_example' # str | ID for component
cwe = 'cwe_example' # str | countermeasure or weakness CWE
update_status_test_request_body = swagger_client.UpdateStatusTestRequestBody() # UpdateStatusTestRequestBody | JSON data that contains the information to update test

try:
    # Updates a single test to a component.
    api_response = api_instance.products_ref_components_component_ref_tests_cwe_put(api_token, ref, component_ref, cwe, update_status_test_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->products_ref_components_component_ref_tests_cwe_put: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://demo.iriusrisk.com/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ComponentsApi* | [**products_ref_components_component_ref_tests_cwe_put**](docs/ComponentsApi.md#products_ref_components_component_ref_tests_cwe_put) | **PUT** /products/{ref}/components/{componentRef}/tests/{cwe} | Updates a single test to a component.
*ComponentsApi* | [**products_ref_components_component_ref_tests_test_type_upload_post**](docs/ComponentsApi.md#products_ref_components_component_ref_tests_test_type_upload_post) | **POST** /products/{ref}/components/{componentRef}/tests/{testType}/upload | Imports test results from different sources to a component
*ControlsApi* | [**products_ref_components_component_ref_controls_control_ref_status_put**](docs/ControlsApi.md#products_ref_components_component_ref_controls_control_ref_status_put) | **PUT** /products/{ref}/components/{componentRef}/controls/{controlRef}/status | Sets the desired status to a countermeasure
*ControlsApi* | [**products_ref_controls_get**](docs/ControlsApi.md#products_ref_controls_get) | **GET** /products/{ref}/controls | Gets a list of all product countermeasures
*ControlsApi* | [**products_ref_controls_implemented_get**](docs/ControlsApi.md#products_ref_controls_implemented_get) | **GET** /products/{ref}/controls/implemented | Gets a list of all implemented countermeasures of a product.
*ControlsApi* | [**products_ref_controls_required_get**](docs/ControlsApi.md#products_ref_controls_required_get) | **GET** /products/{ref}/controls/required | Gets a list of all required countermeasures of a product
*CountermeasuresApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_countermeasures_post**](docs/CountermeasuresApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_countermeasures_post) | **POST** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/countermeasures | Creates new countermeasure in a risk pattern
*CountermeasuresApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_countermeasures_put**](docs/CountermeasuresApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_countermeasures_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/countermeasures | Associates a countermeasure to a threat in a risk pattern.
*CountermeasuresApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put**](docs/CountermeasuresApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/weaknesses/{weaknessRef}/countermeasures | Associates a countermeasure to a weakness in a risk pattern.
*GroupsApi* | [**groups_get**](docs/GroupsApi.md#groups_get) | **GET** /groups | Gets a list of all Groups
*GroupsApi* | [**groups_group_ref_delete**](docs/GroupsApi.md#groups_group_ref_delete) | **DELETE** /groups/{groupRef} | Deletes a users group
*GroupsApi* | [**groups_group_ref_get**](docs/GroupsApi.md#groups_group_ref_get) | **GET** /groups/{groupRef} | Gets the group details.
*GroupsApi* | [**groups_group_ref_put**](docs/GroupsApi.md#groups_group_ref_put) | **PUT** /groups/{groupRef} | Update a users group
*GroupsApi* | [**groups_group_users_delete**](docs/GroupsApi.md#groups_group_users_delete) | **DELETE** /groups/{group}/users | Unassign a list of users from a group
*GroupsApi* | [**groups_group_users_get**](docs/GroupsApi.md#groups_group_users_get) | **GET** /groups/{group}/users | List users from a group
*GroupsApi* | [**groups_group_users_put**](docs/GroupsApi.md#groups_group_users_put) | **PUT** /groups/{group}/users | Assigns users to a group
*GroupsApi* | [**groups_group_users_user_delete**](docs/GroupsApi.md#groups_group_users_user_delete) | **DELETE** /groups/{group}/users/{user} | Removes a user from a group
*GroupsApi* | [**groups_post**](docs/GroupsApi.md#groups_post) | **POST** /groups | Creates a new user group
*GroupsApi* | [**products_ref_groups_delete**](docs/GroupsApi.md#products_ref_groups_delete) | **DELETE** /products/{ref}/groups | Unassigns a list of user groups from a product.
*GroupsApi* | [**products_ref_groups_get**](docs/GroupsApi.md#products_ref_groups_get) | **GET** /products/{ref}/groups | List all groups assigned to a product
*GroupsApi* | [**products_ref_groups_put**](docs/GroupsApi.md#products_ref_groups_put) | **PUT** /products/{ref}/groups | Assigns groups of users to a product.
*LibrariesApi* | [**libraries_library_ref_delete**](docs/LibrariesApi.md#libraries_library_ref_delete) | **DELETE** /libraries/{libraryRef} | Deletes a Library
*LibrariesApi* | [**libraries_library_ref_get**](docs/LibrariesApi.md#libraries_library_ref_get) | **GET** /libraries/{libraryRef} | Gets library details
*LibrariesApi* | [**libraries_library_ref_riskpatterns_post**](docs/LibrariesApi.md#libraries_library_ref_riskpatterns_post) | **POST** /libraries/{libraryRef}/riskpatterns | Creates new Risk Pattern
*LibrariesApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_countermeasures_post**](docs/LibrariesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_countermeasures_post) | **POST** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/countermeasures | Creates new countermeasure in a risk pattern
*LibrariesApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_delete**](docs/LibrariesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_delete) | **DELETE** /libraries/{libraryRef}/riskpatterns/{riskPatternRef} | Deletes a Risk Pattern
*LibrariesApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_get**](docs/LibrariesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_get) | **GET** /libraries/{libraryRef}/riskpatterns/{riskPatternRef} | Gets Risk Pattern details
*LibrariesApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_post**](docs/LibrariesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_post) | **POST** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases | Creates new use case in a library.
*LibrariesApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_post**](docs/LibrariesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_post) | **POST** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats | Creates a new threat in a library.
*LibrariesApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_countermeasures_put**](docs/LibrariesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_countermeasures_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/countermeasures | Associates a countermeasure to a threat in a risk pattern.
*LibrariesApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put**](docs/LibrariesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/weaknesses | Associates weakness to a threat in a risk pattern.
*LibrariesApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put**](docs/LibrariesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/weaknesses/{weaknessRef}/countermeasures | Associates a countermeasure to a weakness in a risk pattern.
*LibrariesApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_weaknesses_post**](docs/LibrariesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_weaknesses_post) | **POST** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/weaknesses | Creates a new weakness in a risk pattern
*LibrariesApi* | [**libraries_post**](docs/LibrariesApi.md#libraries_post) | **POST** /libraries | Creates a Library
*LibrariesApi* | [**products_upload_post**](docs/LibrariesApi.md#products_upload_post) | **POST** /products/upload | Creates a new product, library or template from a XML file upload.
*ProductsApi* | [**products_get**](docs/ProductsApi.md#products_get) | **GET** /products | Gets a list of all products.
*ProductsApi* | [**products_post**](docs/ProductsApi.md#products_post) | **POST** /products | Creates a new product
*ProductsApi* | [**products_ref_components_component_ref_controls_control_ref_status_put**](docs/ProductsApi.md#products_ref_components_component_ref_controls_control_ref_status_put) | **PUT** /products/{ref}/components/{componentRef}/controls/{controlRef}/status | Sets the desired status to a countermeasure
*ProductsApi* | [**products_ref_components_component_ref_tests_cwe_put**](docs/ProductsApi.md#products_ref_components_component_ref_tests_cwe_put) | **PUT** /products/{ref}/components/{componentRef}/tests/{cwe} | Updates a single test to a component.
*ProductsApi* | [**products_ref_components_component_ref_tests_test_type_upload_post**](docs/ProductsApi.md#products_ref_components_component_ref_tests_test_type_upload_post) | **POST** /products/{ref}/components/{componentRef}/tests/{testType}/upload | Imports test results from different sources to a component
*ProductsApi* | [**products_ref_controls_get**](docs/ProductsApi.md#products_ref_controls_get) | **GET** /products/{ref}/controls | Gets a list of all product countermeasures
*ProductsApi* | [**products_ref_controls_implemented_get**](docs/ProductsApi.md#products_ref_controls_implemented_get) | **GET** /products/{ref}/controls/implemented | Gets a list of all implemented countermeasures of a product.
*ProductsApi* | [**products_ref_controls_required_get**](docs/ProductsApi.md#products_ref_controls_required_get) | **GET** /products/{ref}/controls/required | Gets a list of all required countermeasures of a product
*ProductsApi* | [**products_ref_delete**](docs/ProductsApi.md#products_ref_delete) | **DELETE** /products/{ref} | Deletes a product
*ProductsApi* | [**products_ref_diagram_image_get**](docs/ProductsApi.md#products_ref_diagram_image_get) | **GET** /products/{ref}/diagram/image | Gets diagram image for product.
*ProductsApi* | [**products_ref_get**](docs/ProductsApi.md#products_ref_get) | **GET** /products/{ref} | Gets product details
*ProductsApi* | [**products_ref_groups_delete**](docs/ProductsApi.md#products_ref_groups_delete) | **DELETE** /products/{ref}/groups | Unassigns a list of user groups from a product.
*ProductsApi* | [**products_ref_groups_get**](docs/ProductsApi.md#products_ref_groups_get) | **GET** /products/{ref}/groups | List all groups assigned to a product
*ProductsApi* | [**products_ref_groups_put**](docs/ProductsApi.md#products_ref_groups_put) | **PUT** /products/{ref}/groups | Assigns groups of users to a product.
*ProductsApi* | [**products_ref_put**](docs/ProductsApi.md#products_ref_put) | **PUT** /products/{ref} | Updates a product
*ProductsApi* | [**products_ref_risks_get**](docs/ProductsApi.md#products_ref_risks_get) | **GET** /products/{ref}/risks | Gets the risks summary of a product
*ProductsApi* | [**products_ref_tests_test_type_upload_post**](docs/ProductsApi.md#products_ref_tests_test_type_upload_post) | **POST** /products/{ref}/tests/{testType}/upload | Imports test results from different sources to a product.
*ProductsApi* | [**products_ref_threats_get**](docs/ProductsApi.md#products_ref_threats_get) | **GET** /products/{ref}/threats | Gets a list of all threats of a product
*ProductsApi* | [**products_ref_users_delete**](docs/ProductsApi.md#products_ref_users_delete) | **DELETE** /products/{ref}/users | Unassigns a list of users from a product.
*ProductsApi* | [**products_ref_users_get**](docs/ProductsApi.md#products_ref_users_get) | **GET** /products/{ref}/users | List all users assigned to a product
*ProductsApi* | [**products_ref_users_put**](docs/ProductsApi.md#products_ref_users_put) | **PUT** /products/{ref}/users | Assigns users to a product.
*ProductsApi* | [**products_ref_users_user_delete**](docs/ProductsApi.md#products_ref_users_user_delete) | **DELETE** /products/{ref}/users/{user} | Unassigns a user from a product
*ProductsApi* | [**products_ref_weaknesses_get**](docs/ProductsApi.md#products_ref_weaknesses_get) | **GET** /products/{ref}/weaknesses | Gets a list of all weaknesses of a product
*ProductsApi* | [**products_ref_weaknesses_test_state_get**](docs/ProductsApi.md#products_ref_weaknesses_test_state_get) | **GET** /products/{ref}/weaknesses/{test_state} | Gets a list of all weaknesses of a product filtered by test state
*ProductsApi* | [**products_upload_post**](docs/ProductsApi.md#products_upload_post) | **POST** /products/upload | Creates a new product, library or template from a XML file upload.
*ProductsApi* | [**products_upload_ref_post**](docs/ProductsApi.md#products_upload_ref_post) | **POST** /products/upload/{ref} | Updates an existing product from a XML file upload.
*ProductsApi* | [**rules_product_ref_put**](docs/ProductsApi.md#rules_product_ref_put) | **PUT** /rules/product/{ref} | Executes rules by a product
*RiskPatternsApi* | [**libraries_library_ref_riskpatterns_post**](docs/RiskPatternsApi.md#libraries_library_ref_riskpatterns_post) | **POST** /libraries/{libraryRef}/riskpatterns | Creates new Risk Pattern
*RiskPatternsApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_countermeasures_post**](docs/RiskPatternsApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_countermeasures_post) | **POST** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/countermeasures | Creates new countermeasure in a risk pattern
*RiskPatternsApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_delete**](docs/RiskPatternsApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_delete) | **DELETE** /libraries/{libraryRef}/riskpatterns/{riskPatternRef} | Deletes a Risk Pattern
*RiskPatternsApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_get**](docs/RiskPatternsApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_get) | **GET** /libraries/{libraryRef}/riskpatterns/{riskPatternRef} | Gets Risk Pattern details
*RiskPatternsApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put**](docs/RiskPatternsApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/weaknesses | Associates weakness to a threat in a risk pattern.
*RiskPatternsApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put**](docs/RiskPatternsApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/weaknesses/{weaknessRef}/countermeasures | Associates a countermeasure to a weakness in a risk pattern.
*RiskPatternsApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_weaknesses_post**](docs/RiskPatternsApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_weaknesses_post) | **POST** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/weaknesses | Creates a new weakness in a risk pattern
*RisksApi* | [**products_ref_risks_get**](docs/RisksApi.md#products_ref_risks_get) | **GET** /products/{ref}/risks | Gets the risks summary of a product
*RolesApi* | [**roles_post**](docs/RolesApi.md#roles_post) | **POST** /roles | Creates a new Role
*RolesApi* | [**roles_role_name_delete**](docs/RolesApi.md#roles_role_name_delete) | **DELETE** /roles/{role_name} | Deletes an existing role
*RulesApi* | [**rules_product_ref_put**](docs/RulesApi.md#rules_product_ref_put) | **PUT** /rules/product/{ref} | Executes rules by a product
*TemplatesApi* | [**products_upload_post**](docs/TemplatesApi.md#products_upload_post) | **POST** /products/upload | Creates a new product, library or template from a XML file upload.
*TestsApi* | [**products_ref_components_component_ref_tests_cwe_put**](docs/TestsApi.md#products_ref_components_component_ref_tests_cwe_put) | **PUT** /products/{ref}/components/{componentRef}/tests/{cwe} | Updates a single test to a component.
*TestsApi* | [**products_ref_components_component_ref_tests_test_type_upload_post**](docs/TestsApi.md#products_ref_components_component_ref_tests_test_type_upload_post) | **POST** /products/{ref}/components/{componentRef}/tests/{testType}/upload | Imports test results from different sources to a component
*TestsApi* | [**products_ref_tests_test_type_upload_post**](docs/TestsApi.md#products_ref_tests_test_type_upload_post) | **POST** /products/{ref}/tests/{testType}/upload | Imports test results from different sources to a product.
*ThreatsApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_post**](docs/ThreatsApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_post) | **POST** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats | Creates a new threat in a library.
*ThreatsApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_countermeasures_put**](docs/ThreatsApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_countermeasures_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/countermeasures | Associates a countermeasure to a threat in a risk pattern.
*ThreatsApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put**](docs/ThreatsApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/weaknesses | Associates weakness to a threat in a risk pattern.
*ThreatsApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put**](docs/ThreatsApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/weaknesses/{weaknessRef}/countermeasures | Associates a countermeasure to a weakness in a risk pattern.
*ThreatsApi* | [**products_ref_threats_get**](docs/ThreatsApi.md#products_ref_threats_get) | **GET** /products/{ref}/threats | Gets a list of all threats of a product
*TokenApi* | [**users_username_token_post**](docs/TokenApi.md#users_username_token_post) | **POST** /users/{username}/token | Generates a user API token
*UseCasesApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_post**](docs/UseCasesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_post) | **POST** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases | Creates new use case in a library.
*UseCasesApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_countermeasures_put**](docs/UseCasesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_countermeasures_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/countermeasures | Associates a countermeasure to a threat in a risk pattern.
*UseCasesApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put**](docs/UseCasesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/weaknesses | Associates weakness to a threat in a risk pattern.
*UseCasesApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put**](docs/UseCasesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/weaknesses/{weaknessRef}/countermeasures | Associates a countermeasure to a weakness in a risk pattern.
*UsersApi* | [**groups_group_users_delete**](docs/UsersApi.md#groups_group_users_delete) | **DELETE** /groups/{group}/users | Unassign a list of users from a group
*UsersApi* | [**groups_group_users_get**](docs/UsersApi.md#groups_group_users_get) | **GET** /groups/{group}/users | List users from a group
*UsersApi* | [**groups_group_users_put**](docs/UsersApi.md#groups_group_users_put) | **PUT** /groups/{group}/users | Assigns users to a group
*UsersApi* | [**groups_group_users_user_delete**](docs/UsersApi.md#groups_group_users_user_delete) | **DELETE** /groups/{group}/users/{user} | Removes a user from a group
*UsersApi* | [**products_ref_users_delete**](docs/UsersApi.md#products_ref_users_delete) | **DELETE** /products/{ref}/users | Unassigns a list of users from a product.
*UsersApi* | [**products_ref_users_get**](docs/UsersApi.md#products_ref_users_get) | **GET** /products/{ref}/users | List all users assigned to a product
*UsersApi* | [**products_ref_users_put**](docs/UsersApi.md#products_ref_users_put) | **PUT** /products/{ref}/users | Assigns users to a product.
*UsersApi* | [**products_ref_users_user_delete**](docs/UsersApi.md#products_ref_users_user_delete) | **DELETE** /products/{ref}/users/{user} | Unassigns a user from a product
*UsersApi* | [**users_get**](docs/UsersApi.md#users_get) | **GET** /users | List of all Users.
*UsersApi* | [**users_post**](docs/UsersApi.md#users_post) | **POST** /users | Creates a new user
*UsersApi* | [**users_username_delete**](docs/UsersApi.md#users_username_delete) | **DELETE** /users/{username} | Deletes a user
*UsersApi* | [**users_username_get**](docs/UsersApi.md#users_username_get) | **GET** /users/{username} | Get all the information of a user
*UsersApi* | [**users_username_token_post**](docs/UsersApi.md#users_username_token_post) | **POST** /users/{username}/token | Generates a user API token
*WeaknessesApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put**](docs/WeaknessesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/weaknesses | Associates weakness to a threat in a risk pattern.
*WeaknessesApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put**](docs/WeaknessesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put) | **PUT** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/usecases/{useCaseRef}/threats/{threatRef}/weaknesses/{weaknessRef}/countermeasures | Associates a countermeasure to a weakness in a risk pattern.
*WeaknessesApi* | [**libraries_library_ref_riskpatterns_risk_pattern_ref_weaknesses_post**](docs/WeaknessesApi.md#libraries_library_ref_riskpatterns_risk_pattern_ref_weaknesses_post) | **POST** /libraries/{libraryRef}/riskpatterns/{riskPatternRef}/weaknesses | Creates a new weakness in a risk pattern
*WeaknessesApi* | [**products_ref_weaknesses_get**](docs/WeaknessesApi.md#products_ref_weaknesses_get) | **GET** /products/{ref}/weaknesses | Gets a list of all weaknesses of a product
*WeaknessesApi* | [**products_ref_weaknesses_test_state_get**](docs/WeaknessesApi.md#products_ref_weaknesses_test_state_get) | **GET** /products/{ref}/weaknesses/{test_state} | Gets a list of all weaknesses of a product filtered by test state


## Documentation For Models

 - [ArchitectureDiagram](docs/ArchitectureDiagram.md)
 - [AssignGroupsProductRequestBody](docs/AssignGroupsProductRequestBody.md)
 - [AssignUserGroupRequestBody](docs/AssignUserGroupRequestBody.md)
 - [AssignUsersProductRequestBody](docs/AssignUsersProductRequestBody.md)
 - [AssociateCountermeasureThreatLibraryRequestBody](docs/AssociateCountermeasureThreatLibraryRequestBody.md)
 - [AssociateCountermeasureWeaknessLibraryRequestBody](docs/AssociateCountermeasureWeaknessLibraryRequestBody.md)
 - [AssociateWeaknessThreatLibraryRequestBody](docs/AssociateWeaknessThreatLibraryRequestBody.md)
 - [CategoryComponent](docs/CategoryComponent.md)
 - [Component](docs/Component.md)
 - [ComponentAsset](docs/ComponentAsset.md)
 - [ComponentControl](docs/ComponentControl.md)
 - [ComponentDefinition](docs/ComponentDefinition.md)
 - [ComponentDefinitionRiskPatterns](docs/ComponentDefinitionRiskPatterns.md)
 - [ComponentTrustZone](docs/ComponentTrustZone.md)
 - [ComponentUseCase](docs/ComponentUseCase.md)
 - [ComponentUseCaseShort](docs/ComponentUseCaseShort.md)
 - [ComponentUseCaseThreatShort](docs/ComponentUseCaseThreatShort.md)
 - [ComponentWeakness](docs/ComponentWeakness.md)
 - [ControlCommand](docs/ControlCommand.md)
 - [ControlCommandStandards](docs/ControlCommandStandards.md)
 - [CreateGroupRequestBody](docs/CreateGroupRequestBody.md)
 - [CreateLibraryRequestBody](docs/CreateLibraryRequestBody.md)
 - [CreateProduct](docs/CreateProduct.md)
 - [CreateRiskPatternRequestBody](docs/CreateRiskPatternRequestBody.md)
 - [CreateRoleRequestBody](docs/CreateRoleRequestBody.md)
 - [CreateThreatLibraryRequestBody](docs/CreateThreatLibraryRequestBody.md)
 - [CreateUseCaseLibraryRequestBody](docs/CreateUseCaseLibraryRequestBody.md)
 - [CreateUserRequestBody](docs/CreateUserRequestBody.md)
 - [CreateWeaknessLibraryRequestBody](docs/CreateWeaknessLibraryRequestBody.md)
 - [DataFlow](docs/DataFlow.md)
 - [DataFlowAssets](docs/DataFlowAssets.md)
 - [Error](docs/Error.md)
 - [Group](docs/Group.md)
 - [Implementation](docs/Implementation.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [InlineResponse2011](docs/InlineResponse2011.md)
 - [LibrarieslibraryRefriskpatternsriskPatternRefusecasesuseCaseRefthreatsRiskRating](docs/LibrarieslibraryRefriskpatternsriskPatternRefusecasesuseCaseRefthreatsRiskRating.md)
 - [Library](docs/Library.md)
 - [LibraryControl](docs/LibraryControl.md)
 - [LibraryThreat](docs/LibraryThreat.md)
 - [LibraryUseCase](docs/LibraryUseCase.md)
 - [LibraryWeakness](docs/LibraryWeakness.md)
 - [Message](docs/Message.md)
 - [Product](docs/Product.md)
 - [ProductAccessType](docs/ProductAccessType.md)
 - [ProductAsset](docs/ProductAsset.md)
 - [ProductAssetClassification](docs/ProductAssetClassification.md)
 - [ProductSetting](docs/ProductSetting.md)
 - [ProductShort](docs/ProductShort.md)
 - [ProductShortGroups](docs/ProductShortGroups.md)
 - [ProductShortUsers](docs/ProductShortUsers.md)
 - [ProductTrustZone](docs/ProductTrustZone.md)
 - [ProductsrefcomponentscomponentReftestscweControl](docs/ProductsrefcomponentscomponentReftestscweControl.md)
 - [ProductsrefcomponentscomponentReftestscweSource](docs/ProductsrefcomponentscomponentReftestscweSource.md)
 - [Question](docs/Question.md)
 - [Reference](docs/Reference.md)
 - [RiskCount](docs/RiskCount.md)
 - [RiskPattern](docs/RiskPattern.md)
 - [RiskRating](docs/RiskRating.md)
 - [RiskSummary](docs/RiskSummary.md)
 - [Standard](docs/Standard.md)
 - [SupportedStandard](docs/SupportedStandard.md)
 - [Test](docs/Test.md)
 - [TestCommand](docs/TestCommand.md)
 - [TestSource](docs/TestSource.md)
 - [Threat](docs/Threat.md)
 - [ThreatControl](docs/ThreatControl.md)
 - [ThreatNameAndRef](docs/ThreatNameAndRef.md)
 - [ThreatShort](docs/ThreatShort.md)
 - [ThreatWeakness](docs/ThreatWeakness.md)
 - [Udt](docs/Udt.md)
 - [UnassignGroupsProductRequestBody](docs/UnassignGroupsProductRequestBody.md)
 - [UnassignUsersProductRequestBody](docs/UnassignUsersProductRequestBody.md)
 - [UnassingUsersGroupRequestBody](docs/UnassingUsersGroupRequestBody.md)
 - [UpdateGroupRequestBody](docs/UpdateGroupRequestBody.md)
 - [UpdateProduct](docs/UpdateProduct.md)
 - [UpdateStatusCountermeasureRequestBody](docs/UpdateStatusCountermeasureRequestBody.md)
 - [UpdateStatusTestRequestBody](docs/UpdateStatusTestRequestBody.md)
 - [User](docs/User.md)
 - [UserDetailed](docs/UserDetailed.md)
 - [WeaknessNameAndRef](docs/WeaknessNameAndRef.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author


