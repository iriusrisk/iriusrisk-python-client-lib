# iriusrisk_python_client_lib.TemplatesApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_standard_to_template**](TemplatesApi.md#apply_standard_to_template) | **POST** /api/v2/templates/{template-id}/apply-standard | Apply a standard to the recommended countermeasures of the template.
[**bulk_delete_template_countermeasure**](TemplatesApi.md#bulk_delete_template_countermeasure) | **DELETE** /api/v2/templates/countermeasures/bulk | Deletes a list of countermeasures.
[**bulk_delete_template_threat**](TemplatesApi.md#bulk_delete_template_threat) | **DELETE** /api/v2/templates/threats/bulk | Delete multiple threats by their ids.
[**bulk_update_template_countermeasure_priority**](TemplatesApi.md#bulk_update_template_countermeasure_priority) | **PUT** /api/v2/templates/countermeasures/priority/bulk | Updates the priority of a list of countermeasures.
[**bulk_update_template_countermeasure_state**](TemplatesApi.md#bulk_update_template_countermeasure_state) | **PUT** /api/v2/templates/countermeasures/state/bulk | Updates the status of a list of countermeasures.
[**bulk_update_template_threat_state**](TemplatesApi.md#bulk_update_template_threat_state) | **PUT** /api/v2/templates/threats/state/bulk | Update multiple threats by their ids.
[**change_template_threat_state_by_id**](TemplatesApi.md#change_template_threat_state_by_id) | **PUT** /api/v2/templates/threats/{threat-id}/state | Updates the status of a template threat.
[**copy_countermeasure_in_template_threat**](TemplatesApi.md#copy_countermeasure_in_template_threat) | **POST** /api/v2/templates/countermeasures/copy | Copy Countermeasure into template Threat.
[**copy_threat_in_template_use_case**](TemplatesApi.md#copy_threat_in_template_use_case) | **POST** /api/v2/templates/threats/copy | Copy Threat into template Use Case.
[**copy_weakness_in_template_threat**](TemplatesApi.md#copy_weakness_in_template_threat) | **POST** /api/v2/templates/weaknesses/copy | Copy Weakness into template Threat.
[**create_template**](TemplatesApi.md#create_template) | **POST** /api/v2/templates | Create a new template.
[**create_template_countermeasure**](TemplatesApi.md#create_template_countermeasure) | **POST** /api/v2/templates/countermeasures | Create a Template Countermeasure.
[**create_template_countermeasure_comment**](TemplatesApi.md#create_template_countermeasure_comment) | **POST** /api/v2/templates/countermeasures/comments | Creates a new comment for a countermeasure.
[**create_template_countermeasure_implementation**](TemplatesApi.md#create_template_countermeasure_implementation) | **POST** /api/v2/templates/countermeasures/implementations | Creates a new countermeasure implementation.
[**create_template_countermeasure_reference**](TemplatesApi.md#create_template_countermeasure_reference) | **POST** /api/v2/templates/countermeasures/references | Creates a reference for a countermeasure.
[**create_template_countermeasure_standard_reference**](TemplatesApi.md#create_template_countermeasure_standard_reference) | **POST** /api/v2/templates/countermeasures/standard-references | Creates a template countermeasure standard reference.
[**create_template_countermeasure_test_reference**](TemplatesApi.md#create_template_countermeasure_test_reference) | **POST** /api/v2/templates/countermeasures/tests/references | Creates a new reference related to a countermeasure test.
[**create_template_from_project**](TemplatesApi.md#create_template_from_project) | **POST** /api/v2/templates/create-from-project/{project-id} | Create a new template based on a project.
[**create_template_threat**](TemplatesApi.md#create_template_threat) | **POST** /api/v2/templates/threats | Create a new Threat.
[**create_template_threat_comment**](TemplatesApi.md#create_template_threat_comment) | **POST** /api/v2/templates/threats/comments | Create a new comment for a threat.
[**create_template_threat_reference**](TemplatesApi.md#create_template_threat_reference) | **POST** /api/v2/templates/threats/references | Creates a new threat reference.
[**create_template_use_case**](TemplatesApi.md#create_template_use_case) | **POST** /api/v2/templates/use-cases | Create a use case.
[**create_template_weakness_test_reference**](TemplatesApi.md#create_template_weakness_test_reference) | **POST** /api/v2/templates/weaknesses/tests/references | Creates a new reference related to a weakness test.
[**crete_template_weakness**](TemplatesApi.md#crete_template_weakness) | **POST** /api/v2/templates/weaknesses | Creates the weakness.
[**delete_template_by_id**](TemplatesApi.md#delete_template_by_id) | **DELETE** /api/v2/templates/{template-id} | Delete the template.
[**delete_template_countermeasure**](TemplatesApi.md#delete_template_countermeasure) | **DELETE** /api/v2/templates/countermeasures/{countermeasure-id} | Delete a Template Countermeasure.
[**delete_template_countermeasure_by_threat**](TemplatesApi.md#delete_template_countermeasure_by_threat) | **DELETE** /api/v2/templates/threats/{threat-id}/countermeasures/{countermeasure-id} | Delete a countermeasure belongs to a threat.
[**delete_template_countermeasure_by_weakness**](TemplatesApi.md#delete_template_countermeasure_by_weakness) | **DELETE** /api/v2/templates/weaknesses/{weakness-id}/countermeasures/{countermeasure-id} | Delete a countermeasure belongs to a weakness.
[**delete_template_countermeasure_implementation**](TemplatesApi.md#delete_template_countermeasure_implementation) | **DELETE** /api/v2/templates/countermeasures/implementations/{implementation-id} | Deletes a countermeasure implementation.
[**delete_template_countermeasure_reference**](TemplatesApi.md#delete_template_countermeasure_reference) | **DELETE** /api/v2/templates/countermeasures/references/{reference-id} | Deletes a reference for a countermeasure.
[**delete_template_countermeasure_standard_reference**](TemplatesApi.md#delete_template_countermeasure_standard_reference) | **DELETE** /api/v2/templates/countermeasures/standard-references/{standard-reference-id} | Deletes a template countermeasure standard reference.
[**delete_template_countermeasure_test_reference**](TemplatesApi.md#delete_template_countermeasure_test_reference) | **DELETE** /api/v2/templates/countermeasures/tests/references/{reference-id} | Deletes a reference for a countermeasure test.
[**delete_template_threat_by_id**](TemplatesApi.md#delete_template_threat_by_id) | **DELETE** /api/v2/templates/threats/{threat-id} | Delete a Threat by its ID
[**delete_template_threat_reference**](TemplatesApi.md#delete_template_threat_reference) | **DELETE** /api/v2/templates/threats/references/{reference-id} | Deletes a threat reference.
[**delete_template_use_case**](TemplatesApi.md#delete_template_use_case) | **DELETE** /api/v2/templates/use-cases/{use-case-id} | Delete a use case.
[**delete_template_weakness**](TemplatesApi.md#delete_template_weakness) | **DELETE** /api/v2/templates/threats/{threat-id}/weaknesses/{weakness-id} | Deletes the weakness.
[**delete_template_weakness_test_reference**](TemplatesApi.md#delete_template_weakness_test_reference) | **DELETE** /api/v2/templates/weaknesses/tests/references/{reference-id} | Deletes a reference for a weakness test.
[**export_template**](TemplatesApi.md#export_template) | **GET** /api/v2/templates/{template-id}/export | Export the information of a template in XML format.
[**export_template_countermeasures**](TemplatesApi.md#export_template_countermeasures) | **POST** /api/v2/templates/{template-id}/countermeasures/export | Export the countermeasures of a template, based on filters.
[**export_template_threats**](TemplatesApi.md#export_template_threats) | **POST** /api/v2/templates/{template-id}/threats/export | Exports the threats of a template, based on filters.
[**get_all_countermeasures_by_template**](TemplatesApi.md#get_all_countermeasures_by_template) | **GET** /api/v2/templates/{template-id}/countermeasures | Gets all countermeasures for a template.
[**get_all_standard_references_by_template_countermeasure_uuid**](TemplatesApi.md#get_all_standard_references_by_template_countermeasure_uuid) | **GET** /api/v2/templates/countermeasures/{countermeasure-id}/standard-references | Gets all the standard references associated with a given countermeasure in a template context.
[**get_all_standards_by_template_id**](TemplatesApi.md#get_all_standards_by_template_id) | **GET** /api/v2/templates/{template-id}/standards | Returns all available security standards for the template.
[**get_all_template_artifacts**](TemplatesApi.md#get_all_template_artifacts) | **GET** /api/v2/templates/{template-id}/artifacts | Get the available artifacts for a template.
[**get_all_template_countermeasure_comments**](TemplatesApi.md#get_all_template_countermeasure_comments) | **GET** /api/v2/templates/countermeasures/{countermeasure-id}/comments | Gets the comments of a countermeasure.
[**get_all_template_countermeasure_implementations**](TemplatesApi.md#get_all_template_countermeasure_implementations) | **GET** /api/v2/templates/countermeasures/{countermeasure-id}/implementations | Gets all the countermeasure implementations.
[**get_all_template_countermeasure_references**](TemplatesApi.md#get_all_template_countermeasure_references) | **GET** /api/v2/templates/countermeasures/{countermeasure-id}/references | Gets all the countermeasure references.
[**get_all_template_countermeasure_test_references**](TemplatesApi.md#get_all_template_countermeasure_test_references) | **GET** /api/v2/templates/countermeasures/tests/{test-id}/references | Gets the list of references related to a countermeasure test.
[**get_all_template_countermeasures**](TemplatesApi.md#get_all_template_countermeasures) | **GET** /api/v2/templates/countermeasures | Get all countermeasures for visible templates.
[**get_all_template_countermeasures_by_threat**](TemplatesApi.md#get_all_template_countermeasures_by_threat) | **GET** /api/v2/templates/threats/{threat-id}/countermeasures | Retrieves all the countermeasures for a template threat.
[**get_all_template_countermeasures_by_weakness**](TemplatesApi.md#get_all_template_countermeasures_by_weakness) | **GET** /api/v2/templates/weaknesses/{weakness-id}/countermeasures | Retrieves all the countermeasures for a template weakness.
[**get_all_template_diagram_categories**](TemplatesApi.md#get_all_template_diagram_categories) | **GET** /api/v2/templates/{template-id}/diagram/metadata/categories | Provides the categories from a template&#x27;s diagram metadata.
[**get_all_template_diagram_components1**](TemplatesApi.md#get_all_template_diagram_components1) | **GET** /api/v2/templates/{template-id}/diagram/metadata/components | Provides the components from a template&#x27;s diagram metadata.
[**get_all_template_diagram_risk_patterns**](TemplatesApi.md#get_all_template_diagram_risk_patterns) | **GET** /api/v2/templates/{template-id}/diagram/metadata/components/{component-id}/risk-patterns | Provides the risk patterns of a component from the metadata of a template diagram.
[**get_all_template_diagram_trustzones**](TemplatesApi.md#get_all_template_diagram_trustzones) | **GET** /api/v2/templates/{template-id}/diagram/metadata/trust-zones | Provides the trustzones from a template&#x27;s diagram metadata.
[**get_all_template_threat_comments**](TemplatesApi.md#get_all_template_threat_comments) | **GET** /api/v2/templates/threats/{threat-id}/comments | Gets the comments of a threat.
[**get_all_template_threat_references**](TemplatesApi.md#get_all_template_threat_references) | **GET** /api/v2/templates/threats/{threat-id}/references | Gets the threat references through the threat id.
[**get_all_template_weakness_test_references**](TemplatesApi.md#get_all_template_weakness_test_references) | **GET** /api/v2/templates/weaknesses/tests/{test-id}/references | Gets the list of references related to a weakness test.
[**get_all_template_weaknesses**](TemplatesApi.md#get_all_template_weaknesses) | **GET** /api/v2/templates/weaknesses | Get all weaknesses for visible templates.
[**get_all_templates_threats**](TemplatesApi.md#get_all_templates_threats) | **GET** /api/v2/templates/threats | Get all the threats for visible templates
[**get_all_weakness_by_template**](TemplatesApi.md#get_all_weakness_by_template) | **GET** /api/v2/templates/{template-id}/weaknesses | Get the weaknesses that belong to the given template.
[**get_all_weakness_by_template_threat**](TemplatesApi.md#get_all_weakness_by_template_threat) | **GET** /api/v2/templates/threats/{threat-id}/weaknesses | Get the weaknesses that belong to the given threat.
[**get_component_for_template_by_id**](TemplatesApi.md#get_component_for_template_by_id) | **GET** /api/v2/templates/components/{component-id} | Gets the template component.
[**get_components_by_template**](TemplatesApi.md#get_components_by_template) | **GET** /api/v2/templates/{template-id}/components | Get all the components by template.
[**get_project_risk_average**](TemplatesApi.md#get_project_risk_average) | **GET** /api/v2/templates/{template-id}/analytics/risk/average | Gets the risk average of a template.
[**get_project_weakness_test_distribution**](TemplatesApi.md#get_project_weakness_test_distribution) | **GET** /api/v2/templates/{template-id}/weaknesses/tests/analytics/results/distribution | Gets the weakness test distribution of a template.
[**get_template_alerts**](TemplatesApi.md#get_template_alerts) | **GET** /api/v2/templates/{template-id}/alerts | Get all alerts for a template.
[**get_template_architecture_questionnaire**](TemplatesApi.md#get_template_architecture_questionnaire) | **GET** /api/v2/templates/{template-id}/questionnaire | Retrieves the current status of the architecture questionnaire for the template.
[**get_template_artifact_by_id**](TemplatesApi.md#get_template_artifact_by_id) | **GET** /api/v2/templates/artifacts/{artifact-id} | Return the details for an artifact id
[**get_template_by_id**](TemplatesApi.md#get_template_by_id) | **GET** /api/v2/templates/{template-id} | Retrieves the template that matches the id.
[**get_template_component_questionnaire**](TemplatesApi.md#get_template_component_questionnaire) | **GET** /api/v2/templates/components/{component-id}/questionnaire | Retrieves the current status of the template component questionnaire.
[**get_template_countermeasure_by_id**](TemplatesApi.md#get_template_countermeasure_by_id) | **GET** /api/v2/templates/countermeasures/{countermeasure-id} | Gets the details for a template countermeasure.
[**get_template_countermeasure_history**](TemplatesApi.md#get_template_countermeasure_history) | **GET** /api/v2/templates/countermeasures/{countermeasure-id}/history | Gets the history records for a countermeasure.
[**get_template_countermeasure_implementation_by_id**](TemplatesApi.md#get_template_countermeasure_implementation_by_id) | **GET** /api/v2/templates/countermeasures/implementations/{implementation-id} | Gets the countermeasure implementation details.
[**get_template_countermeasure_reference_by_id**](TemplatesApi.md#get_template_countermeasure_reference_by_id) | **GET** /api/v2/templates/countermeasures/tests/references/{reference-id} | Gets a reference related to a countermeasure test.
[**get_template_countermeasure_reference_by_id1**](TemplatesApi.md#get_template_countermeasure_reference_by_id1) | **GET** /api/v2/templates/countermeasures/references/{reference-id} | Gets the countermeasure reference details.
[**get_template_countermeasure_standard_reference**](TemplatesApi.md#get_template_countermeasure_standard_reference) | **GET** /api/v2/templates/countermeasures/standard-references/{standard-reference-id} | Gets a specific countermeasure standard reference of the template.
[**get_template_countermeasure_state_distribution**](TemplatesApi.md#get_template_countermeasure_state_distribution) | **GET** /api/v2/templates/{template-id}/countermeasures/analytics/states/distribution | Gets the number of countermeasures in each state for a template.
[**get_template_countermeasure_test**](TemplatesApi.md#get_template_countermeasure_test) | **GET** /api/v2/templates/countermeasures/tests/{test-id} | Gets the test related to a countermeasure.
[**get_template_countermeasure_test_history**](TemplatesApi.md#get_template_countermeasure_test_history) | **GET** /api/v2/templates/countermeasures/tests/{test-id}/history | Gets the history records for a countermeasure test.
[**get_template_current_artifact**](TemplatesApi.md#get_template_current_artifact) | **GET** /api/v2/templates/{template-id}/artifacts/current | Get the details of the current artifact of a template by template id.
[**get_template_diagram_by_id**](TemplatesApi.md#get_template_diagram_by_id) | **GET** /api/v2/templates/{template-id}/diagram | Get the diagram of a template.
[**get_template_diagram_content_by_id**](TemplatesApi.md#get_template_diagram_content_by_id) | **GET** /api/v2/templates/{template-id}/diagram/content | Get the raw diagram of a template.
[**get_template_diagram_metadata**](TemplatesApi.md#get_template_diagram_metadata) | **GET** /api/v2/templates/{template-id}/diagram/metadata | Provides a template&#x27;s diagram metadata.
[**get_template_risk_distribution**](TemplatesApi.md#get_template_risk_distribution) | **GET** /api/v2/templates/{template-id}/analytics/risk/distribution | Obtains the template risk distribution.
[**get_template_settings_by_id**](TemplatesApi.md#get_template_settings_by_id) | **GET** /api/v2/templates/{template-id}/settings | Get settings for a template.
[**get_template_summary**](TemplatesApi.md#get_template_summary) | **GET** /api/v2/templates/summary | Retrieves a list of templates.
[**get_template_threat_by_id**](TemplatesApi.md#get_template_threat_by_id) | **GET** /api/v2/templates/threats/{threat-id} | Get the threat details.
[**get_template_threat_history**](TemplatesApi.md#get_template_threat_history) | **GET** /api/v2/templates/threats/{threat-id}/history | Gets the history records for a threat.
[**get_template_threat_reference**](TemplatesApi.md#get_template_threat_reference) | **GET** /api/v2/templates/threats/references/{reference-id} | Gets the threat reference through the id.
[**get_template_use_case_by_id**](TemplatesApi.md#get_template_use_case_by_id) | **GET** /api/v2/templates/use-cases/{use-case-id} | Get the use case by ID.
[**get_template_weakness_test**](TemplatesApi.md#get_template_weakness_test) | **GET** /api/v2/templates/weaknesses/tests/{test-id} | Gets the test related to a weakness.
[**get_template_weakness_test_reference**](TemplatesApi.md#get_template_weakness_test_reference) | **GET** /api/v2/templates/weaknesses/tests/references/{reference-id} | Gets the reference related to a weakness test.
[**get_templates**](TemplatesApi.md#get_templates) | **GET** /api/v2/templates | Get the list of templates.
[**get_threats_by_template**](TemplatesApi.md#get_threats_by_template) | **GET** /api/v2/templates/{template-id}/threats | Get all the threats of the template.
[**get_threats_by_template_use_case**](TemplatesApi.md#get_threats_by_template_use_case) | **GET** /api/v2/templates/use-cases/{use-case-id}/threats | Get all the threats by use case.
[**get_use_cases_by_template**](TemplatesApi.md#get_use_cases_by_template) | **GET** /api/v2/templates/{template-id}/use-cases | Get all the use cases by template.
[**get_use_cases_by_template_component**](TemplatesApi.md#get_use_cases_by_template_component) | **GET** /api/v2/templates/components/{component-id}/use-cases | Get all the template use cases by component.
[**get_weakness_by_id**](TemplatesApi.md#get_weakness_by_id) | **GET** /api/v2/templates/weaknesses/{weakness-id} | Get the weakness that matches the id.
[**import_template**](TemplatesApi.md#import_template) | **POST** /api/v2/templates/import | Create a new template based on the uploaded XML file.
[**import_template_into_template**](TemplatesApi.md#import_template_into_template) | **POST** /api/v2/templates/{template-id}/import-template | Import the selected templates into a template.
[**query_template_components_by_threat_filters**](TemplatesApi.md#query_template_components_by_threat_filters) | **POST** /api/v2/templates/{template-id}/components/query | Get all the components by template and threat filters.
[**query_template_countermeasures**](TemplatesApi.md#query_template_countermeasures) | **POST** /api/v2/templates/{template-id}/countermeasures/query | Gets the countermeasures for a template, based on filters
[**query_template_threats_by_template**](TemplatesApi.md#query_template_threats_by_template) | **POST** /api/v2/templates/{template-id}/threats/query | Search the threats for a template, based on filters.
[**query_template_weaknesses**](TemplatesApi.md#query_template_weaknesses) | **POST** /api/v2/templates/{template-id}/weaknesses/query | Searches the weaknesses for a template, based on filters
[**reset_template_diagram_by_id**](TemplatesApi.md#reset_template_diagram_by_id) | **POST** /api/v2/templates/{template-id}/diagram/reset | Restore an edited diagram where the threat model has not been updated
[**simulate_template_architecture_questionnaire**](TemplatesApi.md#simulate_template_architecture_questionnaire) | **POST** /api/v2/templates/{template-id}/questionnaire/simulate | Executes a simulation of the outcome of running the architecture questionnaire.
[**simulate_template_component_questionnaire**](TemplatesApi.md#simulate_template_component_questionnaire) | **POST** /api/v2/templates/components/{component-id}/questionnaire/simulate | Executes a simulation of the outcome of running this template component questionnaire.
[**sync_template**](TemplatesApi.md#sync_template) | **POST** /api/v2/templates/{template-id}/sync | Creates a new async operation to synchronize the template.
[**update_project_use_case**](TemplatesApi.md#update_project_use_case) | **PUT** /api/v2/templates/use-cases/{use-case-id} | Update a use case.
[**update_template**](TemplatesApi.md#update_template) | **PUT** /api/v2/templates/{template-id} | Update the template that matches the id.
[**update_template_architecture_questionnaire**](TemplatesApi.md#update_template_architecture_questionnaire) | **POST** /api/v2/templates/{template-id}/questionnaire | Executes an update of the architecture questionnaire for the template.
[**update_template_component_questionnaire**](TemplatesApi.md#update_template_component_questionnaire) | **POST** /api/v2/templates/components/{component-id}/questionnaire | Executes an update of the template component questionnaire.
[**update_template_countermeasure**](TemplatesApi.md#update_template_countermeasure) | **PUT** /api/v2/templates/countermeasures/{countermeasure-id} | Update a Template Countermeasure.
[**update_template_countermeasure_implementation**](TemplatesApi.md#update_template_countermeasure_implementation) | **PUT** /api/v2/templates/countermeasures/implementations/{implementation-id} | Updates a countermeasure implementation.
[**update_template_countermeasure_reference**](TemplatesApi.md#update_template_countermeasure_reference) | **PUT** /api/v2/templates/countermeasures/references/{reference-id} | Updates a reference for a countermeasure.
[**update_template_countermeasure_standard_reference**](TemplatesApi.md#update_template_countermeasure_standard_reference) | **PUT** /api/v2/templates/countermeasures/standard-references/{standard-reference-id} | Updates a template countermeasure standard reference.
[**update_template_countermeasure_state**](TemplatesApi.md#update_template_countermeasure_state) | **PUT** /api/v2/templates/countermeasures/{countermeasure-id}/state | Updates the status of a template countermeasure.
[**update_template_countermeasure_test**](TemplatesApi.md#update_template_countermeasure_test) | **PUT** /api/v2/templates/countermeasures/tests/{test-id} | Updates the test related to a countermeasure.
[**update_template_countermeasure_test_reference**](TemplatesApi.md#update_template_countermeasure_test_reference) | **PUT** /api/v2/templates/countermeasures/tests/references/{reference-id} | Updates a reference for a countermeasure test.
[**update_template_diagram_by_id**](TemplatesApi.md#update_template_diagram_by_id) | **PUT** /api/v2/templates/{template-id}/diagram/content | Update the diagram of a template.
[**update_template_settings_by_id**](TemplatesApi.md#update_template_settings_by_id) | **PUT** /api/v2/templates/{template-id}/settings | Update the settings of a template.
[**update_template_threat_by_id**](TemplatesApi.md#update_template_threat_by_id) | **PUT** /api/v2/templates/threats/{threat-id} | Modify the threat details.
[**update_template_threat_countermeasure_mitigation**](TemplatesApi.md#update_template_threat_countermeasure_mitigation) | **PUT** /api/v2/templates/threats/{threat-id}/countermeasures/{countermeasure-id} | Update the mitigation value of a countermeasure of a threat.
[**update_template_threat_reference**](TemplatesApi.md#update_template_threat_reference) | **PUT** /api/v2/templates/threats/references/{reference-id} | Updates a reference for a threat.
[**update_template_weakness**](TemplatesApi.md#update_template_weakness) | **PUT** /api/v2/templates/weaknesses/{weakness-id} | Updates the weakness.
[**update_template_weakness_test**](TemplatesApi.md#update_template_weakness_test) | **PUT** /api/v2/templates/weaknesses/tests/{test-id} | Updates the test related to a weakness.
[**update_template_weakness_test_reference**](TemplatesApi.md#update_template_weakness_test_reference) | **PUT** /api/v2/templates/weaknesses/tests/references/{reference-id} | Updates a reference related to a weakness test.
[**update_with_file_template**](TemplatesApi.md#update_with_file_template) | **POST** /api/v2/templates/{template-id}/update-with-file | Updates an existing template from an XML file

# **apply_standard_to_template**
> apply_standard_to_template(body, template_id)

Apply a standard to the recommended countermeasures of the template.

Apply a standard to the recommended countermeasures of the template. Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.ApplyStandardToTemplateRequest() # ApplyStandardToTemplateRequest | 
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Apply a standard to the recommended countermeasures of the template.
    api_instance.apply_standard_to_template(body, template_id)
except ApiException as e:
    print("Exception when calling TemplatesApi->apply_standard_to_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplyStandardToTemplateRequest**](ApplyStandardToTemplateRequest.md)|  | 
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_template_countermeasure**
> AsyncOperationIdResponse bulk_delete_template_countermeasure(x_irius_async, id)

Deletes a list of countermeasures.

Deletes a list of countermeasures. This operation must be executed with the header X-Irius-Async set to true. Conditions to be able to perform the action: - To have update permissions granted for the templates (**TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** with visibility over the template)

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
x_irius_async = true # bool | Sets whether the endpoint works asynchronously or not passed as parameter.
id = ['id_example'] # list[str] | Unique identifier of the countermeasure.

try:
    # Deletes a list of countermeasures.
    api_response = api_instance.bulk_delete_template_countermeasure(x_irius_async, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->bulk_delete_template_countermeasure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_irius_async** | **bool**| Sets whether the endpoint works asynchronously or not passed as parameter. | 
 **id** | [**list[str]**](str.md)| Unique identifier of the countermeasure. | 

### Return type

[**AsyncOperationIdResponse**](AsyncOperationIdResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_template_threat**
> AsyncOperationIdResponse bulk_delete_template_threat(x_irius_async, id)

Delete multiple threats by their ids.

Deletes a set of threats. This operation must be executed with the header X-Irius-Async set to true.  Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE_ALL** granted or **TEMPLATE_UPDATE** and visibility over the template.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
x_irius_async = true # bool | Sets whether the endpoint works asynchronously or not passed as parameter.
id = ['id_example'] # list[str] | Unique identifier of the threat.

try:
    # Delete multiple threats by their ids.
    api_response = api_instance.bulk_delete_template_threat(x_irius_async, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->bulk_delete_template_threat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_irius_async** | **bool**| Sets whether the endpoint works asynchronously or not passed as parameter. | 
 **id** | [**list[str]**](str.md)| Unique identifier of the threat. | 

### Return type

[**AsyncOperationIdResponse**](AsyncOperationIdResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_template_countermeasure_priority**
> AsyncOperationIdResponse bulk_update_template_countermeasure_priority(body, x_irius_async)

Updates the priority of a list of countermeasures.

Updates the priority of a list of countermeasures. Conditions to be able to perform the action: - To have update permissions granted for the templates (**TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** with visibility over the template)

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = [iriusrisk_python_client_lib.UpdateTemplateCountermeasurePriorityRequest()] # list[UpdateTemplateCountermeasurePriorityRequest] | 
x_irius_async = true # bool | Sets whether the endpoint works asynchronously or not passed as parameter.

try:
    # Updates the priority of a list of countermeasures.
    api_response = api_instance.bulk_update_template_countermeasure_priority(body, x_irius_async)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->bulk_update_template_countermeasure_priority: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[UpdateTemplateCountermeasurePriorityRequest]**](UpdateTemplateCountermeasurePriorityRequest.md)|  | 
 **x_irius_async** | **bool**| Sets whether the endpoint works asynchronously or not passed as parameter. | 

### Return type

[**AsyncOperationIdResponse**](AsyncOperationIdResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_template_countermeasure_state**
> AsyncOperationIdResponse bulk_update_template_countermeasure_state(body, x_irius_async)

Updates the status of a list of countermeasures.

Updates the status of a list of countermeasures. Conditions to be able to perform the action: - To have update permissions granted for the templates (**TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** with visibility over the template)

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = NULL # list[object] | 
x_irius_async = true # bool | Sets whether the endpoint works asynchronously or not passed as parameter.

try:
    # Updates the status of a list of countermeasures.
    api_response = api_instance.bulk_update_template_countermeasure_state(body, x_irius_async)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->bulk_update_template_countermeasure_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[object]**](object.md)|  | 
 **x_irius_async** | **bool**| Sets whether the endpoint works asynchronously or not passed as parameter. | 

### Return type

[**AsyncOperationIdResponse**](AsyncOperationIdResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_template_threat_state**
> AsyncOperationIdResponse bulk_update_template_threat_state(body, x_irius_async)

Update multiple threats by their ids.

Updates the status of a set of threats. Allows to execute a state transition for each one of them. This operation must be executed with the header X-Irius-Async set to true. A reason must be given for these transitions: expose, accept or not-applicable.  Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = NULL # list[object] | 
x_irius_async = true # bool | Sets whether the endpoint works asynchronously or not passed as parameter.

try:
    # Update multiple threats by their ids.
    api_response = api_instance.bulk_update_template_threat_state(body, x_irius_async)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->bulk_update_template_threat_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[object]**](object.md)|  | 
 **x_irius_async** | **bool**| Sets whether the endpoint works asynchronously or not passed as parameter. | 

### Return type

[**AsyncOperationIdResponse**](AsyncOperationIdResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_template_threat_state_by_id**
> TemplateThreatWithCustomFieldsResponse change_template_threat_state_by_id(body, threat_id)

Updates the status of a template threat.

Updates the status of a template threat. A reason must be given for these transitions: expose, accept or not-applicable.  Conditions to be able to perform the action are verified in the background, for every threat that must be updated: - To have the permission **TEMPLATE_UPDATE** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, - The transition undo-not-applicable can only be applied to threats currently in the state not-applicable - The template must not be locked - The template must be visible for the user - The template must not be locked or in a read-only state

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.ThreatidStateBody() # ThreatidStateBody | 
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the threat.

try:
    # Updates the status of a template threat.
    api_response = api_instance.change_template_threat_state_by_id(body, threat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->change_template_threat_state_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ThreatidStateBody**](ThreatidStateBody.md)|  | 
 **threat_id** | [**str**](.md)| Unique identifier of the threat. | 

### Return type

[**TemplateThreatWithCustomFieldsResponse**](TemplateThreatWithCustomFieldsResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_countermeasure_in_template_threat**
> TemplateCountermeasureDetailResponse copy_countermeasure_in_template_threat(body)

Copy Countermeasure into template Threat.

Copy an existing Countermeasure into a specified Threat by referencing both entities. By default the State of the Countermeasure will be **RECOMMENDED**. Conditions to be able to perform the action: - Countermeasure must be visible for the User. Extra permissions may be needed depending on the source  The target template must also be editable: - It must not be read-only. - It must be visible for the User - User must have **TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** permissions.  If the process involves a Weakness, it would be necessary to have the permission to view the Weakness.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CopyCountermeasureInTemplateThreatRequest() # CopyCountermeasureInTemplateThreatRequest | 

try:
    # Copy Countermeasure into template Threat.
    api_response = api_instance.copy_countermeasure_in_template_threat(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->copy_countermeasure_in_template_threat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CopyCountermeasureInTemplateThreatRequest**](CopyCountermeasureInTemplateThreatRequest.md)|  | 

### Return type

[**TemplateCountermeasureDetailResponse**](TemplateCountermeasureDetailResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_threat_in_template_use_case**
> TemplateThreatWithCustomFieldsResponse copy_threat_in_template_use_case(body)

Copy Threat into template Use Case.

Copy an existing Threat into a specified template Use Case. Conditions to be able to perform the action: - Threat must be visible for the User. Extra permissions may be needed depending on the source  The target template must also be editable: - It must not be read-only. - It must be visible for the User - User must have **TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** permissions.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CopyThreatInTemplateUseCaseRequest() # CopyThreatInTemplateUseCaseRequest | 

try:
    # Copy Threat into template Use Case.
    api_response = api_instance.copy_threat_in_template_use_case(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->copy_threat_in_template_use_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CopyThreatInTemplateUseCaseRequest**](CopyThreatInTemplateUseCaseRequest.md)|  | 

### Return type

[**TemplateThreatWithCustomFieldsResponse**](TemplateThreatWithCustomFieldsResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_weakness_in_template_threat**
> TemplateWeaknessResponse copy_weakness_in_template_threat(body)

Copy Weakness into template Threat.

Copy an existing weakness into a specified template threat. Conditions to be able to perform the action: - Weakness must be visible for the User. Extra permissions may be needed depending on the source  The target template must also be editable: - It must not be read-only. - It must be visible for the User - User must have **TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** permissions.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CopyWeaknessInTemplateThreatRequest() # CopyWeaknessInTemplateThreatRequest | 

try:
    # Copy Weakness into template Threat.
    api_response = api_instance.copy_weakness_in_template_threat(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->copy_weakness_in_template_threat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CopyWeaknessInTemplateThreatRequest**](CopyWeaknessInTemplateThreatRequest.md)|  | 

### Return type

[**TemplateWeaknessResponse**](TemplateWeaknessResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template**
> TemplateResponse create_template(body)

Create a new template.

Create a new template.  Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateTemplateRequest() # CreateTemplateRequest | Payload to create a template.

try:
    # Create a new template.
    api_response = api_instance.create_template(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->create_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTemplateRequest**](CreateTemplateRequest.md)| Payload to create a template. | 

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_countermeasure**
> TemplateCountermeasureDetailResponse create_template_countermeasure(body)

Create a Template Countermeasure.

Creates a new countermeasure within a template, specifying its details. To perform the action the template must be editable: - It must not be read-only. - It must be visible for the User - User must have **TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** permissions.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateTemplateCountermeasureRequest() # CreateTemplateCountermeasureRequest | 

try:
    # Create a Template Countermeasure.
    api_response = api_instance.create_template_countermeasure(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->create_template_countermeasure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTemplateCountermeasureRequest**](CreateTemplateCountermeasureRequest.md)|  | 

### Return type

[**TemplateCountermeasureDetailResponse**](TemplateCountermeasureDetailResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_countermeasure_comment**
> TemplateCountermeasureCommentResponse create_template_countermeasure_comment(body)

Creates a new comment for a countermeasure.

Creates a new comment for a countermeasure. Conditions to be able to perform the action: - To have update permissions granted for the templates (**TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** with visibility over the template) 

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateTemplateCountermeasureCommentRequest() # CreateTemplateCountermeasureCommentRequest | 

try:
    # Creates a new comment for a countermeasure.
    api_response = api_instance.create_template_countermeasure_comment(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->create_template_countermeasure_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTemplateCountermeasureCommentRequest**](CreateTemplateCountermeasureCommentRequest.md)|  | 

### Return type

[**TemplateCountermeasureCommentResponse**](TemplateCountermeasureCommentResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_countermeasure_implementation**
> TemplateCountermeasureImplementationResponse create_template_countermeasure_implementation(body)

Creates a new countermeasure implementation.

Creates a new countermeasure implementation. Conditions to be able to perform the action: - To have update permissions granted for the templates (**TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** with visibility over the template)

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateTemplateCountermeasureImplementationRequest() # CreateTemplateCountermeasureImplementationRequest | 

try:
    # Creates a new countermeasure implementation.
    api_response = api_instance.create_template_countermeasure_implementation(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->create_template_countermeasure_implementation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTemplateCountermeasureImplementationRequest**](CreateTemplateCountermeasureImplementationRequest.md)|  | 

### Return type

[**TemplateCountermeasureImplementationResponse**](TemplateCountermeasureImplementationResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_countermeasure_reference**
> TemplateCountermeasureReferenceResponse create_template_countermeasure_reference(body)

Creates a reference for a countermeasure.

Creates a reference for a countermeasure. Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE** granted or - To have the permission **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateTemplateCountermeasureReferenceRequest() # CreateTemplateCountermeasureReferenceRequest | 

try:
    # Creates a reference for a countermeasure.
    api_response = api_instance.create_template_countermeasure_reference(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->create_template_countermeasure_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTemplateCountermeasureReferenceRequest**](CreateTemplateCountermeasureReferenceRequest.md)|  | 

### Return type

[**TemplateCountermeasureReferenceResponse**](TemplateCountermeasureReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_countermeasure_standard_reference**
> TemplateCountermeasureStandardReferenceResponse create_template_countermeasure_standard_reference(body)

Creates a template countermeasure standard reference.

Creates a template countermeasure standard reference. Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE_ALL** granted, or</li> - To have the permission **TEMPLATE_UPDATE** granted.</li>

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateTemplateCountermeasureStandardReferenceRequest() # CreateTemplateCountermeasureStandardReferenceRequest | 

try:
    # Creates a template countermeasure standard reference.
    api_response = api_instance.create_template_countermeasure_standard_reference(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->create_template_countermeasure_standard_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTemplateCountermeasureStandardReferenceRequest**](CreateTemplateCountermeasureStandardReferenceRequest.md)|  | 

### Return type

[**TemplateCountermeasureStandardReferenceResponse**](TemplateCountermeasureStandardReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_countermeasure_test_reference**
> GetTemplateCountermeasureTestReferenceResponse create_template_countermeasure_test_reference(body)

Creates a new reference related to a countermeasure test.

Creates a new reference related to a countermeasure test. Conditions to be able to perform the action:<ul><li>To have the permission **TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** granted</li></ul>

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateTemplateCountermeasureTestReferenceRequest() # CreateTemplateCountermeasureTestReferenceRequest | 

try:
    # Creates a new reference related to a countermeasure test.
    api_response = api_instance.create_template_countermeasure_test_reference(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->create_template_countermeasure_test_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTemplateCountermeasureTestReferenceRequest**](CreateTemplateCountermeasureTestReferenceRequest.md)|  | 

### Return type

[**GetTemplateCountermeasureTestReferenceResponse**](GetTemplateCountermeasureTestReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_from_project**
> TemplateResponse create_template_from_project(body, project_id)

Create a new template based on a project.

Create a new template based on a project. Conditions to be able to perform the action: - To have the permission **PRODUCT_UPDATE** granted. - To have the permission **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateTemplateFromProjectRequest() # CreateTemplateFromProjectRequest | Payload to create a template from a project.
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the project

try:
    # Create a new template based on a project.
    api_response = api_instance.create_template_from_project(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->create_template_from_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTemplateFromProjectRequest**](CreateTemplateFromProjectRequest.md)| Payload to create a template from a project. | 
 **project_id** | [**str**](.md)| ID of the project | 

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_threat**
> TemplateThreatWithCustomFieldsResponse create_template_threat(body)

Create a new Threat.

Create a new Threat. To perform the action the template must be editable: - It must not be read-only. - It must be visible for the User - User must have **TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** permissions.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.TemplateThreatRequest() # TemplateThreatRequest | 

try:
    # Create a new Threat.
    api_response = api_instance.create_template_threat(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->create_template_threat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemplateThreatRequest**](TemplateThreatRequest.md)|  | 

### Return type

[**TemplateThreatWithCustomFieldsResponse**](TemplateThreatWithCustomFieldsResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_threat_comment**
> TemplateThreatCommentResponse create_template_threat_comment(body)

Create a new comment for a threat.

Creates a new comment for a threat. Conditions to be able to perform the action: - To have update permissions granted for the templates (**TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** with visibility over the template)

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateTemplateThreatCommentRequest() # CreateTemplateThreatCommentRequest | 

try:
    # Create a new comment for a threat.
    api_response = api_instance.create_template_threat_comment(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->create_template_threat_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTemplateThreatCommentRequest**](CreateTemplateThreatCommentRequest.md)|  | 

### Return type

[**TemplateThreatCommentResponse**](TemplateThreatCommentResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_threat_reference**
> TemplateThreatReferenceResponse create_template_threat_reference(body)

Creates a new threat reference.

Creates a new threat reference. Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE** granted or - To have the permission **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateTemplateThreatReferenceRequest() # CreateTemplateThreatReferenceRequest | 

try:
    # Creates a new threat reference.
    api_response = api_instance.create_template_threat_reference(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->create_template_threat_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTemplateThreatReferenceRequest**](CreateTemplateThreatReferenceRequest.md)|  | 

### Return type

[**TemplateThreatReferenceResponse**](TemplateThreatReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_use_case**
> TemplateUseCaseResponse create_template_use_case(body)

Create a use case.

Create a use case. Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateTemplateUseCaseRequest() # CreateTemplateUseCaseRequest | 

try:
    # Create a use case.
    api_response = api_instance.create_template_use_case(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->create_template_use_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTemplateUseCaseRequest**](CreateTemplateUseCaseRequest.md)|  | 

### Return type

[**TemplateUseCaseResponse**](TemplateUseCaseResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_weakness_test_reference**
> GetTemplateWeaknessTestReferenceResponse create_template_weakness_test_reference(body)

Creates a new reference related to a weakness test.

Creates a new reference related to a weakness test. Conditions to be able to perform the action:<ul><li>To have the permission **TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** granted</li></ul>

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateTemplateWeaknessTestReferenceRequest() # CreateTemplateWeaknessTestReferenceRequest | 

try:
    # Creates a new reference related to a weakness test.
    api_response = api_instance.create_template_weakness_test_reference(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->create_template_weakness_test_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTemplateWeaknessTestReferenceRequest**](CreateTemplateWeaknessTestReferenceRequest.md)|  | 

### Return type

[**GetTemplateWeaknessTestReferenceResponse**](GetTemplateWeaknessTestReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crete_template_weakness**
> TemplateWeaknessResponse crete_template_weakness(body)

Creates the weakness.

Creates the weakness. Conditions to be able to perform the action:<ul><li>To have the permission **TEMPLATE_UPDATE** granted, or</li><li> To have the permission **TEMPLATE_UPDATE_ALL** granted.</li></ul>

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CreateTemplateWeaknessRequest() # CreateTemplateWeaknessRequest | 

try:
    # Creates the weakness.
    api_response = api_instance.crete_template_weakness(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->crete_template_weakness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTemplateWeaknessRequest**](CreateTemplateWeaknessRequest.md)|  | 

### Return type

[**TemplateWeaknessResponse**](TemplateWeaknessResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_by_id**
> delete_template_by_id(template_id)

Delete the template.

Delete the template that matches the id.  Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE** granted to delete own templates. - To have the permission **TEMPLATE_UPDATE_ALL** granted to delete any templates.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Delete the template.
    api_instance.delete_template_by_id(template_id)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_countermeasure**
> delete_template_countermeasure(countermeasure_id)

Delete a Template Countermeasure.

Deletes an existing template countermeasure using its ID. To perform the action the template must be editable: - It must not be read-only. - It must be visible for the User - User must have **TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** permissions.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure.

try:
    # Delete a Template Countermeasure.
    api_instance.delete_template_countermeasure(countermeasure_id)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_template_countermeasure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countermeasure_id** | [**str**](.md)| The id of the countermeasure. | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_countermeasure_by_threat**
> delete_template_countermeasure_by_threat(threat_id, countermeasure_id)

Delete a countermeasure belongs to a threat.

Delete a countermeasure belongs to a threat. Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE_ALL** granted or - To have the permission **TEMPLATE_UPDATE** granted

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the threat.
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure.

try:
    # Delete a countermeasure belongs to a threat.
    api_instance.delete_template_countermeasure_by_threat(threat_id, countermeasure_id)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_template_countermeasure_by_threat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_id** | [**str**](.md)| Unique identifier of the threat. | 
 **countermeasure_id** | [**str**](.md)| The id of the countermeasure. | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_countermeasure_by_weakness**
> delete_template_countermeasure_by_weakness(weakness_id, countermeasure_id)

Delete a countermeasure belongs to a weakness.

Delete a countermeasure belongs to a weakness. Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE_ALL** granted or - To have the permission **TEMPLATE_UPDATE** granted

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
weakness_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the weakness
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure.

try:
    # Delete a countermeasure belongs to a weakness.
    api_instance.delete_template_countermeasure_by_weakness(weakness_id, countermeasure_id)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_template_countermeasure_by_weakness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **weakness_id** | [**str**](.md)| ID of the weakness | 
 **countermeasure_id** | [**str**](.md)| The id of the countermeasure. | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_countermeasure_implementation**
> delete_template_countermeasure_implementation(implementation_id)

Deletes a countermeasure implementation.

Deletes a countermeasure implementation. Conditions to be able to perform the action: - To have update permissions granted for the templates (**TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** with visibility over the template)

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
implementation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure implementation.

try:
    # Deletes a countermeasure implementation.
    api_instance.delete_template_countermeasure_implementation(implementation_id)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_template_countermeasure_implementation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **implementation_id** | [**str**](.md)| The id of the countermeasure implementation. | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_countermeasure_reference**
> delete_template_countermeasure_reference(reference_id)

Deletes a reference for a countermeasure.

Deletes a reference for a countermeasure. Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE** granted or - To have the permission **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure reference.

try:
    # Deletes a reference for a countermeasure.
    api_instance.delete_template_countermeasure_reference(reference_id)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_template_countermeasure_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_id** | [**str**](.md)| The id of the countermeasure reference. | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_countermeasure_standard_reference**
> delete_template_countermeasure_standard_reference(standard_reference_id)

Deletes a template countermeasure standard reference.

Deletes a template countermeasure standard reference. Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE_ALL** granted, or</li> - To have the permission **TEMPLATE_UPDATE** granted.</li>

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
standard_reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template countermeasure standard reference

try:
    # Deletes a template countermeasure standard reference.
    api_instance.delete_template_countermeasure_standard_reference(standard_reference_id)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_template_countermeasure_standard_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standard_reference_id** | [**str**](.md)| ID of the template countermeasure standard reference | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_countermeasure_test_reference**
> delete_template_countermeasure_test_reference(reference_id)

Deletes a reference for a countermeasure test.

Deletes a reference for a countermeasure test. Conditions to be able to perform the action:<ul><li>To have the permission **TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** granted</li></ul>

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure test reference.

try:
    # Deletes a reference for a countermeasure test.
    api_instance.delete_template_countermeasure_test_reference(reference_id)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_template_countermeasure_test_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_id** | [**str**](.md)| The id of the countermeasure test reference. | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_threat_by_id**
> delete_template_threat_by_id(threat_id)

Delete a Threat by its ID

This operation allows the deletion of a specific threat identified by its unique ID. To perform the action the template must be editable: - It must not be read-only. - It must be visible for the User - User must have **TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** permissions.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the threat.

try:
    # Delete a Threat by its ID
    api_instance.delete_template_threat_by_id(threat_id)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_template_threat_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_id** | [**str**](.md)| Unique identifier of the threat. | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_threat_reference**
> delete_template_threat_reference(reference_id)

Deletes a threat reference.

Deletes a threat reference. Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE** granted or - To have the permission **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of a reference.

try:
    # Deletes a threat reference.
    api_instance.delete_template_threat_reference(reference_id)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_template_threat_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_id** | [**str**](.md)| ID of a reference. | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_use_case**
> delete_template_use_case(use_case_id)

Delete a use case.

Delete a use case. Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
use_case_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the use case.

try:
    # Delete a use case.
    api_instance.delete_template_use_case(use_case_id)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_template_use_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **use_case_id** | [**str**](.md)| ID of the use case. | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_weakness**
> TemplateWeaknessResponse delete_template_weakness(threat_id, weakness_id)

Deletes the weakness.

Deletes the weakness. Conditions to be able to perform the action:<ul><li>To have the permission **TEMPLATE_UPDATE** granted, or</li><li> To have the permission **TEMPLATE_UPDATE_ALL** granted.</li></ul>

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the threat.
weakness_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the weakness

try:
    # Deletes the weakness.
    api_response = api_instance.delete_template_weakness(threat_id, weakness_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_template_weakness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_id** | [**str**](.md)| Unique identifier of the threat. | 
 **weakness_id** | [**str**](.md)| ID of the weakness | 

### Return type

[**TemplateWeaknessResponse**](TemplateWeaknessResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_weakness_test_reference**
> delete_template_weakness_test_reference(reference_id)

Deletes a reference for a weakness test.

Deletes a reference for a weakness test. Conditions to be able to perform the action:<ul><li>To have the permission **TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** granted</li></ul>

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the weakness test reference.

try:
    # Deletes a reference for a weakness test.
    api_instance.delete_template_weakness_test_reference(reference_id)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_template_weakness_test_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_id** | [**str**](.md)| ID of the weakness test reference. | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_template**
> export_template(template_id)

Export the information of a template in XML format.

Export the information of a template in XML format.  Conditions to be able to perform the action:  - To have the permission **TEMPLATE_UPDATE_ALL** granted or  - To have visibility over the template and the permission **TEMPLATE_UPDATE**

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Export the information of a template in XML format.
    api_instance.export_template(template_id)
except ApiException as e:
    print("Exception when calling TemplatesApi->export_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_template_countermeasures**
> export_template_countermeasures(body, template_id, accept=accept)

Export the countermeasures of a template, based on filters.

<p>Export the countermeasures of a template, based on filters.</p><p>The allowed formats for the data can be specified by using the Accept header in the request. Here are the formats you can choose from:</p><ul><li><strong>text/csv</strong> for CSV files.</li><li><strong>application/vnd.openxmlformats-officedocument.spreadsheetml.sheet</strong> for modern Excel files (.xlsx).</li><li><strong>application/vnd.ms-excel</strong> for older Excel files (.xls).</li></ul><p>When making your request, include the Accept header and specify one of these formats to determine how you'd like to receive the data.</p><p>Conditions to be able to perform the action:</p><ul><li>To have the permission <strong>TEMPLATE_UPDATE</strong> granted or</li><li>To have the permission <strong>TEMPLATE_UPDATE_ALL</strong> granted</li></ul>

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.ExportTemplateCountermeasureQueryRequest() # ExportTemplateCountermeasureQueryRequest | 
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template
accept = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' # str |  (optional) (default to application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)

try:
    # Export the countermeasures of a template, based on filters.
    api_instance.export_template_countermeasures(body, template_id, accept=accept)
except ApiException as e:
    print("Exception when calling TemplatesApi->export_template_countermeasures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExportTemplateCountermeasureQueryRequest**](ExportTemplateCountermeasureQueryRequest.md)|  | 
 **template_id** | [**str**](.md)| ID of the template | 
 **accept** | **str**|  | [optional] [default to application/vnd.openxmlformats-officedocument.spreadsheetml.sheet]

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_template_threats**
> export_template_threats(body, template_id, accept=accept)

Exports the threats of a template, based on filters.

<p>Exports the threats of a template, based on filters.</p><p>The allowed formats for the data can be specified by using the Accept header in the request. Here are the formats you can choose from:</p><ul><li><strong>text/csv</strong> for CSV files.</li><li><strong>application/vnd.openxmlformats-officedocument.spreadsheetml.sheet</strong> for modern Excel files (.xlsx).</li><li><strong>application/vnd.ms-excel</strong> for older Excel files (.xls).</li></ul><p>When making your request, include the Accept header and specify one of these formats to determine how you'd like to receive the data.</p><p>Conditions to be able to perform the action:</p><ul><li>To have the permission <strong>TEMPLATE_UPDATE</strong> granted or</li><li>To have the permission <strong>TEMPLATE_UPDATE_ALL</strong> granted</li></ul>

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.ExportTemplateThreatQueryRequest() # ExportTemplateThreatQueryRequest | <p>The <strong>RequestBody</strong> currently includes the <strong>filters</strong> property, which serves as a placeholder for future enhancements. As of now, the <strong>all</strong> property is supported, functioning as an AND condition where all specified filters must match.</p>

<p><strong>Current functionality:</strong></p>
<ul>
  <li><strong>all</strong>: When this property is used, all of the filters included must match for the request to be processed. This is equivalent to an AND condition in logical operations.</li>
</ul>

<p><strong>Example:</strong> If a request body specifies filters for <strong>states</strong> as <strong>["required", "implemented"]</strong> and <strong>tags</strong> as <strong>["tag1", "tag2"]</strong>, then only items that are both in the 'required' or 'implemented' states and tagged with 'tag1' or 'tag2' will match.</p>

<pre>
{
  "all": {
    "states": ["required", "implemented"],
    "tags": ["tag1", "tag2"]
  }
}
</pre>


template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template
accept = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' # str |  (optional) (default to application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)

try:
    # Exports the threats of a template, based on filters.
    api_instance.export_template_threats(body, template_id, accept=accept)
except ApiException as e:
    print("Exception when calling TemplatesApi->export_template_threats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExportTemplateThreatQueryRequest**](ExportTemplateThreatQueryRequest.md)| &lt;p&gt;The &lt;strong&gt;RequestBody&lt;/strong&gt; currently includes the &lt;strong&gt;filters&lt;/strong&gt; property, which serves as a placeholder for future enhancements. As of now, the &lt;strong&gt;all&lt;/strong&gt; property is supported, functioning as an AND condition where all specified filters must match.&lt;/p&gt;

&lt;p&gt;&lt;strong&gt;Current functionality:&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
  &lt;li&gt;&lt;strong&gt;all&lt;/strong&gt;: When this property is used, all of the filters included must match for the request to be processed. This is equivalent to an AND condition in logical operations.&lt;/li&gt;
&lt;/ul&gt;

&lt;p&gt;&lt;strong&gt;Example:&lt;/strong&gt; If a request body specifies filters for &lt;strong&gt;states&lt;/strong&gt; as &lt;strong&gt;[&quot;required&quot;, &quot;implemented&quot;]&lt;/strong&gt; and &lt;strong&gt;tags&lt;/strong&gt; as &lt;strong&gt;[&quot;tag1&quot;, &quot;tag2&quot;]&lt;/strong&gt;, then only items that are both in the &#x27;required&#x27; or &#x27;implemented&#x27; states and tagged with &#x27;tag1&#x27; or &#x27;tag2&#x27; will match.&lt;/p&gt;

&lt;pre&gt;
{
  &quot;all&quot;: {
    &quot;states&quot;: [&quot;required&quot;, &quot;implemented&quot;],
    &quot;tags&quot;: [&quot;tag1&quot;, &quot;tag2&quot;]
  }
}
&lt;/pre&gt;

 | 
 **template_id** | [**str**](.md)| ID of the template | 
 **accept** | **str**|  | [optional] [default to application/vnd.openxmlformats-officedocument.spreadsheetml.sheet]

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_countermeasures_by_template**
> PagedModelTemplateCountermeasureResponse get_all_countermeasures_by_template(template_id, filter=filter, page=page, size=size, sort=sort)

Gets all countermeasures for a template.

Gets all countermeasures for a template. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all countermeasures for a template.
    api_response = api_instance.get_all_countermeasures_by_template(template_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_countermeasures_by_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelTemplateCountermeasureResponse**](PagedModelTemplateCountermeasureResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_standard_references_by_template_countermeasure_uuid**
> PagedModelTemplateCountermeasureStandardReferenceResponse get_all_standard_references_by_template_countermeasure_uuid(countermeasure_id, filter=filter, page=page, size=size, sort=sort)

Gets all the standard references associated with a given countermeasure in a template context.

Gets all the standard references associated with a given countermeasure in a template context registered in the system. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the countermeasure
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the standard references associated with a given countermeasure in a template context.
    api_response = api_instance.get_all_standard_references_by_template_countermeasure_uuid(countermeasure_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_standard_references_by_template_countermeasure_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countermeasure_id** | [**str**](.md)| ID of the countermeasure | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelTemplateCountermeasureStandardReferenceResponse**](PagedModelTemplateCountermeasureStandardReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_standards_by_template_id**
> PagedModelTemplateStandardResponse get_all_standards_by_template_id(template_id, filter=filter, page=page, size=size, sort=sort)

Returns all available security standards for the template.

Returns all available security standards for the template. Conditions to be able to perform the action:  - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Returns all available security standards for the template.
    api_response = api_instance.get_all_standards_by_template_id(template_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_standards_by_template_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelTemplateStandardResponse**](PagedModelTemplateStandardResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_template_artifacts**
> PagedModelArtifactResponse get_all_template_artifacts(template_id, page=page, size=size, sort=sort)

Get the available artifacts for a template.

For a template id get the available artifacts.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Get the available artifacts for a template.
    api_response = api_instance.get_all_template_artifacts(template_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_template_artifacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelArtifactResponse**](PagedModelArtifactResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_template_countermeasure_comments**
> TemplateCountermeasureCommentResponse get_all_template_countermeasure_comments(countermeasure_id, page=page, size=size, sort=sort)

Gets the comments of a countermeasure.

Gets the comments of a countermeasure. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure.
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the comments of a countermeasure.
    api_response = api_instance.get_all_template_countermeasure_comments(countermeasure_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_template_countermeasure_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countermeasure_id** | [**str**](.md)| The id of the countermeasure. | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**TemplateCountermeasureCommentResponse**](TemplateCountermeasureCommentResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_template_countermeasure_implementations**
> PagedModelTemplateCountermeasureImplementationResponse get_all_template_countermeasure_implementations(countermeasure_id, filter=filter, page=page, size=size, sort=sort)

Gets all the countermeasure implementations.

Gets all the countermeasure implementations. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure.
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the countermeasure implementations.
    api_response = api_instance.get_all_template_countermeasure_implementations(countermeasure_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_template_countermeasure_implementations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countermeasure_id** | [**str**](.md)| The id of the countermeasure. | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelTemplateCountermeasureImplementationResponse**](PagedModelTemplateCountermeasureImplementationResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_template_countermeasure_references**
> PagedModelTemplateCountermeasureReferenceResponse get_all_template_countermeasure_references(countermeasure_id, page=page, size=size, sort=sort)

Gets all the countermeasure references.

Gets all the countermeasure references. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure.
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets all the countermeasure references.
    api_response = api_instance.get_all_template_countermeasure_references(countermeasure_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_template_countermeasure_references: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countermeasure_id** | [**str**](.md)| The id of the countermeasure. | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelTemplateCountermeasureReferenceResponse**](PagedModelTemplateCountermeasureReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_template_countermeasure_test_references**
> PagedModelGetTemplateCountermeasureTestReferenceResponse get_all_template_countermeasure_test_references(test_id, filter=filter, page=page, size=size, sort=sort)

Gets the list of references related to a countermeasure test.

Gets the list of references related to a countermeasure test.  Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
test_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure test.
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the list of references related to a countermeasure test.
    api_response = api_instance.get_all_template_countermeasure_test_references(test_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_template_countermeasure_test_references: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | [**str**](.md)| The id of the countermeasure test. | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelGetTemplateCountermeasureTestReferenceResponse**](PagedModelGetTemplateCountermeasureTestReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_template_countermeasures**
> PagedModelTemplateCountermeasureResponse get_all_template_countermeasures(filter=filter, page=page, size=size, sort=sort)

Get all countermeasures for visible templates.

Get all countermeasures for visible templates. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Get all countermeasures for visible templates.
    api_response = api_instance.get_all_template_countermeasures(filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_template_countermeasures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelTemplateCountermeasureResponse**](PagedModelTemplateCountermeasureResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_template_countermeasures_by_threat**
> PagedModelTemplateCountermeasureForThreatResponse get_all_template_countermeasures_by_threat(threat_id, filter=filter, page=page, size=size, sort=sort)

Retrieves all the countermeasures for a template threat.

Retrieves all the countermeasures for a template threat.  Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the threat.
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Retrieves all the countermeasures for a template threat.
    api_response = api_instance.get_all_template_countermeasures_by_threat(threat_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_template_countermeasures_by_threat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_id** | [**str**](.md)| Unique identifier of the threat. | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelTemplateCountermeasureForThreatResponse**](PagedModelTemplateCountermeasureForThreatResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_template_countermeasures_by_weakness**
> PagedModelTemplateCountermeasureForWeaknessResponse get_all_template_countermeasures_by_weakness(weakness_id, filter=filter, page=page, size=size, sort=sort)

Retrieves all the countermeasures for a template weakness.

Retrieves all the countermeasures for a template weakness. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
weakness_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the weakness
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Retrieves all the countermeasures for a template weakness.
    api_response = api_instance.get_all_template_countermeasures_by_weakness(weakness_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_template_countermeasures_by_weakness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **weakness_id** | [**str**](.md)| ID of the weakness | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelTemplateCountermeasureForWeaknessResponse**](PagedModelTemplateCountermeasureForWeaknessResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_template_diagram_categories**
> PagedModelDiagramCategoryResponse get_all_template_diagram_categories(template_id, page=page, size=size, sort=sort)

Provides the categories from a template's diagram metadata.

Provides the categories from a template's diagram metadata. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted or - To have the permission **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Provides the categories from a template's diagram metadata.
    api_response = api_instance.get_all_template_diagram_categories(template_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_template_diagram_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelDiagramCategoryResponse**](PagedModelDiagramCategoryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_template_diagram_components1**
> PagedModelDiagramComponentResponse get_all_template_diagram_components1(template_id, category, page=page, size=size, sort=sort)

Provides the components from a template's diagram metadata.

Provides the components from a template's diagram metadata. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted or - To have the permission **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template
category = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Category of the component
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Provides the components from a template's diagram metadata.
    api_response = api_instance.get_all_template_diagram_components1(template_id, category, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_template_diagram_components1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 
 **category** | [**str**](.md)| Category of the component | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelDiagramComponentResponse**](PagedModelDiagramComponentResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_template_diagram_risk_patterns**
> PagedModelDiagramRiskPatternResponse get_all_template_diagram_risk_patterns(template_id, component_id, page=page, size=size, sort=sort)

Provides the risk patterns of a component from the metadata of a template diagram.

Provides the risk patterns of a component from the metadata of a template diagram. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted or - To have the permission **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template
component_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the component
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Provides the risk patterns of a component from the metadata of a template diagram.
    api_response = api_instance.get_all_template_diagram_risk_patterns(template_id, component_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_template_diagram_risk_patterns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 
 **component_id** | [**str**](.md)| ID of the component | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelDiagramRiskPatternResponse**](PagedModelDiagramRiskPatternResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_template_diagram_trustzones**
> PagedModelDiagramTrustzoneResponse get_all_template_diagram_trustzones(template_id, page=page, size=size, sort=sort)

Provides the trustzones from a template's diagram metadata.

Provides the trustzones from a template's diagram metadata. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted or - To have the permission **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Provides the trustzones from a template's diagram metadata.
    api_response = api_instance.get_all_template_diagram_trustzones(template_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_template_diagram_trustzones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelDiagramTrustzoneResponse**](PagedModelDiagramTrustzoneResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_template_threat_comments**
> PagedModelTemplateThreatCommentResponse get_all_template_threat_comments(threat_id, page=page, size=size, sort=sort)

Gets the comments of a threat.

Gets the comments of a threat. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the threat.
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the comments of a threat.
    api_response = api_instance.get_all_template_threat_comments(threat_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_template_threat_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_id** | [**str**](.md)| Unique identifier of the threat. | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelTemplateThreatCommentResponse**](PagedModelTemplateThreatCommentResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_template_threat_references**
> PagedModelTemplateThreatReferenceResponse get_all_template_threat_references(threat_id, page=page, size=size, sort=sort)

Gets the threat references through the threat id.

Gets the threat references details. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the threat.
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the threat references through the threat id.
    api_response = api_instance.get_all_template_threat_references(threat_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_template_threat_references: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_id** | [**str**](.md)| Unique identifier of the threat. | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelTemplateThreatReferenceResponse**](PagedModelTemplateThreatReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_template_weakness_test_references**
> PagedModelGetTemplateWeaknessTestReferenceResponse get_all_template_weakness_test_references(test_id, filter=filter, page=page, size=size, sort=sort)

Gets the list of references related to a weakness test.

Gets the list of references related to a weakness test.  Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
test_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the weakness test.
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the list of references related to a weakness test.
    api_response = api_instance.get_all_template_weakness_test_references(test_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_template_weakness_test_references: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | [**str**](.md)| ID of the weakness test. | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelGetTemplateWeaknessTestReferenceResponse**](PagedModelGetTemplateWeaknessTestReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_template_weaknesses**
> PagedModelTemplateWeaknessResponse get_all_template_weaknesses(filter=filter, page=page, size=size, sort=sort)

Get all weaknesses for visible templates.

Get all weaknesses for visible templates. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Get all weaknesses for visible templates.
    api_response = api_instance.get_all_template_weaknesses(filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_template_weaknesses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelTemplateWeaknessResponse**](PagedModelTemplateWeaknessResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_templates_threats**
> PagedModelTemplateThreatResponse get_all_templates_threats(filter=filter, page=page, size=size, sort=sort)

Get all the threats for visible templates

Get all the threats for visible templates Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Get all the threats for visible templates
    api_response = api_instance.get_all_templates_threats(filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_templates_threats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelTemplateThreatResponse**](PagedModelTemplateThreatResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_weakness_by_template**
> PagedModelTemplateWeaknessResponse get_all_weakness_by_template(template_id, filter=filter, page=page, size=size, sort=sort)

Get the weaknesses that belong to the given template.

Get the weaknesses details.  Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Get the weaknesses that belong to the given template.
    api_response = api_instance.get_all_weakness_by_template(template_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_weakness_by_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelTemplateWeaknessResponse**](PagedModelTemplateWeaknessResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_weakness_by_template_threat**
> PagedModelTemplateWeaknessResponse get_all_weakness_by_template_threat(threat_id, filter=filter, page=page, size=size, sort=sort)

Get the weaknesses that belong to the given threat.

Get the weaknesses details.  Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the threat.
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Get the weaknesses that belong to the given threat.
    api_response = api_instance.get_all_weakness_by_template_threat(threat_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_weakness_by_template_threat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_id** | [**str**](.md)| Unique identifier of the threat. | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelTemplateWeaknessResponse**](PagedModelTemplateWeaknessResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_component_for_template_by_id**
> ComponentForTemplateResponse get_component_for_template_by_id(component_id)

Gets the template component.

Gets the template component. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
component_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the component.

try:
    # Gets the template component.
    api_response = api_instance.get_component_for_template_by_id(component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_component_for_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | [**str**](.md)| ID of the component. | 

### Return type

[**ComponentForTemplateResponse**](ComponentForTemplateResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_components_by_template**
> PagedModelComponentForTemplateResponse get_components_by_template(template_id, filter=filter, page=page, size=size, sort=sort)

Get all the components by template.

Get all the components by template. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Get all the components by template.
    api_response = api_instance.get_components_by_template(template_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_components_by_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelComponentForTemplateResponse**](PagedModelComponentForTemplateResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_risk_average**
> ProjectRiskAverageResponse get_project_risk_average(template_id)

Gets the risk average of a template.

Gets the risk average of a template.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Gets the risk average of a template.
    api_response = api_instance.get_project_risk_average(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_project_risk_average: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

[**ProjectRiskAverageResponse**](ProjectRiskAverageResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_weakness_test_distribution**
> CollectionModelGetWeaknessTestResultResponse get_project_weakness_test_distribution(template_id)

Gets the weakness test distribution of a template.

Gets the weakness test distribution of a template.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Gets the weakness test distribution of a template.
    api_response = api_instance.get_project_weakness_test_distribution(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_project_weakness_test_distribution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

[**CollectionModelGetWeaknessTestResultResponse**](CollectionModelGetWeaknessTestResultResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_alerts**
> PagedModelTemplateAlertResponse get_template_alerts(template_id, page=page, size=size, sort=sort)

Get all alerts for a template.

Get the list of alerts for a threat model

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Get all alerts for a template.
    api_response = api_instance.get_template_alerts(template_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelTemplateAlertResponse**](PagedModelTemplateAlertResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_architecture_questionnaire**
> ArchitectureQuestionnaireResultResponse get_template_architecture_questionnaire(template_id)

Retrieves the current status of the architecture questionnaire for the template.

Retrieves the current status of the architecture questionnaire for the template. Conditions to be able to perform the action:<ul><li>To have the permission **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.</li><li>The template must be synced.</li></ul>

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Retrieves the current status of the architecture questionnaire for the template.
    api_response = api_instance.get_template_architecture_questionnaire(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_architecture_questionnaire: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

[**ArchitectureQuestionnaireResultResponse**](ArchitectureQuestionnaireResultResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_artifact_by_id**
> ArtifactContentResponse get_template_artifact_by_id(artifact_id)

Return the details for an artifact id

Return the details for an artifact id

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
artifact_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the artifact.

try:
    # Return the details for an artifact id
    api_response = api_instance.get_template_artifact_by_id(artifact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_artifact_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_id** | [**str**](.md)| ID of the artifact. | 

### Return type

[**ArtifactContentResponse**](ArtifactContentResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_by_id**
> TemplateResponse get_template_by_id(template_id)

Retrieves the template that matches the id.

For a template id returns the template data and attributes.  Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Retrieves the template that matches the id.
    api_response = api_instance.get_template_by_id(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_component_questionnaire**
> QuestionnaireResultResponse get_template_component_questionnaire(component_id)

Retrieves the current status of the template component questionnaire.

Retrieves the current status of the template component questionnaire. Conditions to be able to perform the action:<ul><li>To have the permission **TEMPLATE_UPDATE** granted.</li><li>To have the permission **TEMPLATE_UPDATE_ALL** granted.</li><li>The template the component belongs to must not be undergoing synchronization.</li></ul>

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
component_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the component

try:
    # Retrieves the current status of the template component questionnaire.
    api_response = api_instance.get_template_component_questionnaire(component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_component_questionnaire: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | [**str**](.md)| ID of the component | 

### Return type

[**QuestionnaireResultResponse**](QuestionnaireResultResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_countermeasure_by_id**
> TemplateCountermeasureDetailResponse get_template_countermeasure_by_id(countermeasure_id)

Gets the details for a template countermeasure.

Gets the details for a template countermeasure. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the countermeasure.

try:
    # Gets the details for a template countermeasure.
    api_response = api_instance.get_template_countermeasure_by_id(countermeasure_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_countermeasure_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countermeasure_id** | [**str**](.md)| Unique identifier of the countermeasure. | 

### Return type

[**TemplateCountermeasureDetailResponse**](TemplateCountermeasureDetailResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_countermeasure_history**
> PagedModelHistoryResponse get_template_countermeasure_history(countermeasure_id, page=page, size=size, sort=sort)

Gets the history records for a countermeasure.

Gets the historical changes for a countermeasure, ordered by most recent by default. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the countermeasure.
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the history records for a countermeasure.
    api_response = api_instance.get_template_countermeasure_history(countermeasure_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_countermeasure_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countermeasure_id** | [**str**](.md)| Unique identifier of the countermeasure. | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelHistoryResponse**](PagedModelHistoryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_countermeasure_implementation_by_id**
> TemplateCountermeasureImplementationResponse get_template_countermeasure_implementation_by_id(implementation_id)

Gets the countermeasure implementation details.

Gets the countermeasure implementation details. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
implementation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure implementation.

try:
    # Gets the countermeasure implementation details.
    api_response = api_instance.get_template_countermeasure_implementation_by_id(implementation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_countermeasure_implementation_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **implementation_id** | [**str**](.md)| The id of the countermeasure implementation. | 

### Return type

[**TemplateCountermeasureImplementationResponse**](TemplateCountermeasureImplementationResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_countermeasure_reference_by_id**
> GetTemplateCountermeasureTestReferenceResponse get_template_countermeasure_reference_by_id(reference_id)

Gets a reference related to a countermeasure test.

Gets a reference related to a countermeasure test.  Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure test reference.

try:
    # Gets a reference related to a countermeasure test.
    api_response = api_instance.get_template_countermeasure_reference_by_id(reference_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_countermeasure_reference_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_id** | [**str**](.md)| The id of the countermeasure test reference. | 

### Return type

[**GetTemplateCountermeasureTestReferenceResponse**](GetTemplateCountermeasureTestReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_countermeasure_reference_by_id1**
> TemplateCountermeasureReferenceResponse get_template_countermeasure_reference_by_id1(reference_id)

Gets the countermeasure reference details.

Gets the countermeasure reference details. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure reference.

try:
    # Gets the countermeasure reference details.
    api_response = api_instance.get_template_countermeasure_reference_by_id1(reference_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_countermeasure_reference_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_id** | [**str**](.md)| The id of the countermeasure reference. | 

### Return type

[**TemplateCountermeasureReferenceResponse**](TemplateCountermeasureReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_countermeasure_standard_reference**
> TemplateCountermeasureStandardReferenceResponse get_template_countermeasure_standard_reference(standard_reference_id)

Gets a specific countermeasure standard reference of the template.

Gets a specific countermeasure standard reference of the template. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
standard_reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the countermeasure standard reference

try:
    # Gets a specific countermeasure standard reference of the template.
    api_response = api_instance.get_template_countermeasure_standard_reference(standard_reference_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_countermeasure_standard_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standard_reference_id** | [**str**](.md)| ID of the countermeasure standard reference | 

### Return type

[**TemplateCountermeasureStandardReferenceResponse**](TemplateCountermeasureStandardReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_countermeasure_state_distribution**
> CollectionModelCountermeasureStateDistributionResponse get_template_countermeasure_state_distribution(template_id)

Gets the number of countermeasures in each state for a template.

Gets the number of countermeasures in each state for a template.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Gets the number of countermeasures in each state for a template.
    api_response = api_instance.get_template_countermeasure_state_distribution(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_countermeasure_state_distribution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

[**CollectionModelCountermeasureStateDistributionResponse**](CollectionModelCountermeasureStateDistributionResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_countermeasure_test**
> TemplateCountermeasureTestResponse get_template_countermeasure_test(test_id)

Gets the test related to a countermeasure.

Gets the test related to a countermeasure.  Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
test_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure test.

try:
    # Gets the test related to a countermeasure.
    api_response = api_instance.get_template_countermeasure_test(test_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_countermeasure_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | [**str**](.md)| The id of the countermeasure test. | 

### Return type

[**TemplateCountermeasureTestResponse**](TemplateCountermeasureTestResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_countermeasure_test_history**
> PagedModelHistoryResponse get_template_countermeasure_test_history(test_id, page=page, size=size, sort=sort)

Gets the history records for a countermeasure test.

Gets the historical changes for a countermeasure test, ordered by most recent by default. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
test_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the test
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the history records for a countermeasure test.
    api_response = api_instance.get_template_countermeasure_test_history(test_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_countermeasure_test_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | [**str**](.md)| ID of the test | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelHistoryResponse**](PagedModelHistoryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_current_artifact**
> ArtifactContentResponse get_template_current_artifact(template_id)

Get the details of the current artifact of a template by template id.

Return the details of the current artifact of a template, including its content.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Get the details of the current artifact of a template by template id.
    api_response = api_instance.get_template_current_artifact(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_current_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

[**ArtifactContentResponse**](ArtifactContentResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_diagram_by_id**
> DiagramResponse get_template_diagram_by_id(template_id)

Get the diagram of a template.

Get the diagram and related info of a template by template id. Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Get the diagram of a template.
    api_response = api_instance.get_template_diagram_by_id(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_diagram_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

[**DiagramResponse**](DiagramResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_diagram_content_by_id**
> object get_template_diagram_content_by_id(template_id)

Get the raw diagram of a template.

Get the raw diagram template by template id. Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Get the raw diagram of a template.
    api_response = api_instance.get_template_diagram_content_by_id(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_diagram_content_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

**object**

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_diagram_metadata**
> DiagramMetadataResponse get_template_diagram_metadata(template_id)

Provides a template's diagram metadata.

Provides a template's diagram metadata. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted or - To have the permission **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Provides a template's diagram metadata.
    api_response = api_instance.get_template_diagram_metadata(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_diagram_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

[**DiagramMetadataResponse**](DiagramMetadataResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_risk_distribution**
> CollectionModelRiskDistributionResponse get_template_risk_distribution(template_id)

Obtains the template risk distribution.

Obtains the number of threats categorized by risk level for a template.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Obtains the template risk distribution.
    api_response = api_instance.get_template_risk_distribution(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_risk_distribution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

[**CollectionModelRiskDistributionResponse**](CollectionModelRiskDistributionResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_settings_by_id**
> TemplateSettingsResponse get_template_settings_by_id(template_id)

Get settings for a template.

Get settings for a template.  Conditions to be able to perform the action:  - To have the permission **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Get settings for a template.
    api_response = api_instance.get_template_settings_by_id(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_settings_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

[**TemplateSettingsResponse**](TemplateSettingsResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_summary**
> PagedModelTemplateSummaryResponse get_template_summary(filter=filter, page=page, size=size, sort=sort)

Retrieves a list of templates.

Retrieves a summary of all templates for all users.  The filters available are: - id - referenceId - name - labels (strict comparison, just as strings)

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Retrieves a list of templates.
    api_response = api_instance.get_template_summary(filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelTemplateSummaryResponse**](PagedModelTemplateSummaryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_threat_by_id**
> TemplateThreatWithCustomFieldsResponse get_template_threat_by_id(threat_id)

Get the threat details.

Get the threat details. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the threat.

try:
    # Get the threat details.
    api_response = api_instance.get_template_threat_by_id(threat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_threat_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_id** | [**str**](.md)| Unique identifier of the threat. | 

### Return type

[**TemplateThreatWithCustomFieldsResponse**](TemplateThreatWithCustomFieldsResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_threat_history**
> PagedModelHistoryResponse get_template_threat_history(threat_id, page=page, size=size, sort=sort)

Gets the history records for a threat.

Gets the historical changes for a threat, ordered by most recent by default. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the threat.
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Gets the history records for a threat.
    api_response = api_instance.get_template_threat_history(threat_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_threat_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_id** | [**str**](.md)| Unique identifier of the threat. | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelHistoryResponse**](PagedModelHistoryResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_threat_reference**
> TemplateThreatReferenceResponse get_template_threat_reference(reference_id)

Gets the threat reference through the id.

Gets the threat reference details. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of a reference.

try:
    # Gets the threat reference through the id.
    api_response = api_instance.get_template_threat_reference(reference_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_threat_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_id** | [**str**](.md)| ID of a reference. | 

### Return type

[**TemplateThreatReferenceResponse**](TemplateThreatReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_use_case_by_id**
> TemplateUseCaseResponse get_template_use_case_by_id(use_case_id)

Get the use case by ID.

Get the use case by ID. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
use_case_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the use case.

try:
    # Get the use case by ID.
    api_response = api_instance.get_template_use_case_by_id(use_case_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_use_case_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **use_case_id** | [**str**](.md)| ID of the use case. | 

### Return type

[**TemplateUseCaseResponse**](TemplateUseCaseResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_weakness_test**
> TemplateWeaknessTestResponse get_template_weakness_test(test_id)

Gets the test related to a weakness.

Gets the test related to a weakness. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
test_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the weakness test.

try:
    # Gets the test related to a weakness.
    api_response = api_instance.get_template_weakness_test(test_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_weakness_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | [**str**](.md)| ID of the weakness test. | 

### Return type

[**TemplateWeaknessTestResponse**](TemplateWeaknessTestResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_weakness_test_reference**
> GetTemplateWeaknessTestReferenceResponse get_template_weakness_test_reference(reference_id)

Gets the reference related to a weakness test.

Gets the reference related to a weakness test.  Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the weakness test reference.

try:
    # Gets the reference related to a weakness test.
    api_response = api_instance.get_template_weakness_test_reference(reference_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_weakness_test_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_id** | [**str**](.md)| ID of the weakness test reference. | 

### Return type

[**GetTemplateWeaknessTestReferenceResponse**](GetTemplateWeaknessTestReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_templates**
> PagedModelTemplateResponse get_templates(page=page, size=size, filter=filter)

Get the list of templates.

Get the list of templates for the current user. If the user has the permission TEMPLATE_UPDATE_ALL they can see all the templates. If the user has the permission TEMPLATE_UPDATE they will only be able to see those templates for which they have  visibility. If the user does not have any of the above permissions, no templates will be displayed.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)

try:
    # Get the list of templates.
    api_response = api_instance.get_templates(page=page, size=size, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 

### Return type

[**PagedModelTemplateResponse**](PagedModelTemplateResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threats_by_template**
> PagedModelTemplateThreatResponse get_threats_by_template(template_id, filter=filter, page=page, size=size, sort=sort)

Get all the threats of the template.

Get all the threats of the template Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Get all the threats of the template.
    api_response = api_instance.get_threats_by_template(template_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_threats_by_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelTemplateThreatResponse**](PagedModelTemplateThreatResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threats_by_template_use_case**
> PagedModelTemplateThreatResponse get_threats_by_template_use_case(use_case_id, filter=filter, page=page, size=size, sort=sort)

Get all the threats by use case.

Get all the threats by use case. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
use_case_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the use case.
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Get all the threats by use case.
    api_response = api_instance.get_threats_by_template_use_case(use_case_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_threats_by_template_use_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **use_case_id** | [**str**](.md)| ID of the use case. | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelTemplateThreatResponse**](PagedModelTemplateThreatResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_use_cases_by_template**
> PagedModelTemplateUseCaseResponse get_use_cases_by_template(template_id, filter=filter, page=page, size=size, sort=sort)

Get all the use cases by template.

Get all the use cases by template. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Get all the use cases by template.
    api_response = api_instance.get_use_cases_by_template(template_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_use_cases_by_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelTemplateUseCaseResponse**](PagedModelTemplateUseCaseResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_use_cases_by_template_component**
> PagedModelTemplateUseCaseResponse get_use_cases_by_template_component(component_id, filter=filter, page=page, size=size, sort=sort)

Get all the template use cases by component.

Get all the template use cases by component. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
component_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the component.
filter = 'filter_example' # str | Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | =        | Returns items where the property **equals** to the value           | /resources?filter=**'field'='value'** | | =NULL    | Returns items where the property **is null**, it has no value     | /resources?filter=**'field'=NULL** | | <>       | Returns items where the property is **not equal** to the value     | /resources?filter=**'field'<>'value'** | | <>NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter=**'field'<>NULL** | | >        | Returns items where the property is **bigger<sup>1</sup>** than the value   | /resources?filter=**'field'>'value'** | | <        | Returns items where the property is **smaller<sup>1</sup>** than the value  | /resources?filter=**'field'<'value'** | | >=       | Returns items where the property is **bigger<sup>1</sup> or equal** to the value      | /resources?filter=**'field'>='value'** | | <=       | Returns items where the property is **smaller<sup>1</sup> or equal** to the value     | /resources?filter=**'field'<='value'** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter=**'field'~'value'** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter=**'field'IN'value1,value2,...'** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter=**'field1'='value1':AND:'field2'<>'value2'** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter=**'field1'='value1':OR:'field2'<>'value2'** | ---  <sup>1</sup> Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: ``` /resources?filter=('field1'='value1':OR:'field2'='value2'):AND:('field3'<>'value3':OR:'field4'='value4') ``` (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # Get all the template use cases by component.
    api_response = api_instance.get_use_cases_by_template_component(component_id, filter=filter, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_use_cases_by_template_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | [**str**](.md)| ID of the component. | 
 **filter** | **str**| Filter to apply to the returned items. It is possible to filter by any property of the response.  The full filter string must be passed in a single **filter** query parameter. Providing multiple **filter** parameters will lead to unexpected results. Both the properties and values must be enclosed in single quotation marks. | Operator | Description | Example | | -------- | ----------- |-------- | | &#x3D;        | Returns items where the property **equals** to the value           | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;&#x27;value&#x27;** | | &#x3D;NULL    | Returns items where the property **is null**, it has no value     | /resources?filter&#x3D;**&#x27;field&#x27;&#x3D;NULL** | | &lt;&gt;       | Returns items where the property is **not equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;&#x27;value&#x27;** | | &lt;&gt;NULL   | Returns items where the property **is not null**, it has any value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&gt;NULL** | | &gt;        | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt;** than the value   | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x27;value&#x27;** | | &lt;        | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt;** than the value  | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x27;value&#x27;** | | &gt;&#x3D;       | Returns items where the property is **bigger&lt;sup&gt;1&lt;/sup&gt; or equal** to the value      | /resources?filter&#x3D;**&#x27;field&#x27;&gt;&#x3D;&#x27;value&#x27;** | | &lt;&#x3D;       | Returns items where the property is **smaller&lt;sup&gt;1&lt;/sup&gt; or equal** to the value     | /resources?filter&#x3D;**&#x27;field&#x27;&lt;&#x3D;&#x27;value&#x27;** | | ~        | Returns items where the string property **contains, ignorecase**, the value  | /resources?filter&#x3D;**&#x27;field&#x27;~&#x27;value&#x27;** | | IN       | Returns items where the list property **contains** any of the values | /resources?filter&#x3D;**&#x27;field&#x27;IN&#x27;value1,value2,...&#x27;** | | :AND:    | Returns items that comply with **both** filters                | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:AND:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | | :OR:     | Returns items that comply with **at least one** of the filters | /resources?filter&#x3D;**&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&lt;&gt;&#x27;value2&#x27;** | ---  &lt;sup&gt;1&lt;/sup&gt; Bigger and smaller according to normal sorting. Applicable to: dates, timestamps, numbers, strings. The following data types support filtering: - Boolean - String - Enumerations - Numeric - Dates - Timestamps  **AND** and **OR** operators can be combined. They can be grouped using parenthesis. Example: &#x60;&#x60;&#x60; /resources?filter&#x3D;(&#x27;field1&#x27;&#x3D;&#x27;value1&#x27;:OR:&#x27;field2&#x27;&#x3D;&#x27;value2&#x27;):AND:(&#x27;field3&#x27;&lt;&gt;&#x27;value3&#x27;:OR:&#x27;field4&#x27;&#x3D;&#x27;value4&#x27;) &#x60;&#x60;&#x60; | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PagedModelTemplateUseCaseResponse**](PagedModelTemplateUseCaseResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_weakness_by_id**
> TemplateWeaknessResponse get_weakness_by_id(weakness_id)

Get the weakness that matches the id.

Get the weakness details.  Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
weakness_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the weakness

try:
    # Get the weakness that matches the id.
    api_response = api_instance.get_weakness_by_id(weakness_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_weakness_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **weakness_id** | [**str**](.md)| ID of the weakness | 

### Return type

[**TemplateWeaknessResponse**](TemplateWeaknessResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_template**
> TemplateResponse import_template(file, reference_id, name)

Create a new template based on the uploaded XML file.

Create a new template based on the uploaded XML file.  Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
file = 'file_example' # str | 
reference_id = 'reference_id_example' # str | 
name = 'name_example' # str | 

try:
    # Create a new template based on the uploaded XML file.
    api_response = api_instance.import_template(file, reference_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->import_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **reference_id** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_template_into_template**
> AsyncOperationIdResponse import_template_into_template(body, x_irius_async, template_id)

Import the selected templates into a template.

Import the selected templates into a template. Conditions to be able to perform the action:<ul><li>To have the permission **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.</li><li>The template must be synced.</li><li>The templates to import must exists.</li></ul>  Also templates in read only mode cannot be updated.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = ['body_example'] # list[str] | List of template ids to import.
x_irius_async = true # bool | Sets whether the endpoint works asynchronously or not passed as parameter.
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Import the selected templates into a template.
    api_response = api_instance.import_template_into_template(body, x_irius_async, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->import_template_into_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| List of template ids to import. | 
 **x_irius_async** | **bool**| Sets whether the endpoint works asynchronously or not passed as parameter. | 
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

[**AsyncOperationIdResponse**](AsyncOperationIdResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_template_components_by_threat_filters**
> PagedModelComponentForTemplateResponse query_template_components_by_threat_filters(body, template_id, sort=sort, page=page, size=size)

Get all the components by template and threat filters.

Get all the components by template and threat filters. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.TemplateComponentQueryRequest() # TemplateComponentQueryRequest | 
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Available fields to sort by: id, referenceId, name, description, parent and diagram component id. Multiple sort criteria are supported. (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)

try:
    # Get all the components by template and threat filters.
    api_response = api_instance.query_template_components_by_threat_filters(body, template_id, sort=sort, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->query_template_components_by_threat_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemplateComponentQueryRequest**](TemplateComponentQueryRequest.md)|  | 
 **template_id** | [**str**](.md)| ID of the template | 
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Available fields to sort by: id, referenceId, name, description, parent and diagram component id. Multiple sort criteria are supported. | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]

### Return type

[**PagedModelComponentForTemplateResponse**](PagedModelComponentForTemplateResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_template_countermeasures**
> PagedModelTemplateCountermeasureResponse query_template_countermeasures(body, template_id, sort=sort, page=page, size=size)

Gets the countermeasures for a template, based on filters

Gets the countermeasures for a template, based on filters. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.TemplateCountermeasureQueryRequest() # TemplateCountermeasureQueryRequest | 
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Available fields to sort by: name, source, state, cost, issueId. Multiple sort criteria are supported. (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)

try:
    # Gets the countermeasures for a template, based on filters
    api_response = api_instance.query_template_countermeasures(body, template_id, sort=sort, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->query_template_countermeasures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemplateCountermeasureQueryRequest**](TemplateCountermeasureQueryRequest.md)|  | 
 **template_id** | [**str**](.md)| ID of the template | 
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Available fields to sort by: name, source, state, cost, issueId. Multiple sort criteria are supported. | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]

### Return type

[**PagedModelTemplateCountermeasureResponse**](PagedModelTemplateCountermeasureResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_template_threats_by_template**
> PagedModelTemplateThreatResponse query_template_threats_by_template(body, template_id, sort=sort, page=page, size=size)

Search the threats for a template, based on filters.

Search the threats for a template, based on filters. Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.TemplateThreatQueryRequest() # TemplateThreatQueryRequest | 
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Available fields to sort by: name, source, risk, inherentRisk, projectedRisk. Multiple sort criteria are supported. (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 20 # int | The size of the page to be returned (optional) (default to 20)

try:
    # Search the threats for a template, based on filters.
    api_response = api_instance.query_template_threats_by_template(body, template_id, sort=sort, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->query_template_threats_by_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemplateThreatQueryRequest**](TemplateThreatQueryRequest.md)|  | 
 **template_id** | [**str**](.md)| ID of the template | 
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Available fields to sort by: name, source, risk, inherentRisk, projectedRisk. Multiple sort criteria are supported. | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]

### Return type

[**PagedModelTemplateThreatResponse**](PagedModelTemplateThreatResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_template_weaknesses**
> PagedModelTemplateWeaknessResponse query_template_weaknesses(body, template_id, size=size)

Searches the weaknesses for a template, based on filters

Searches the weaknesses for a template, based on filters.  Conditions to be able to perform the action: - To have the permission **TEMPLATE_LIBRARY_VIEW** granted, or, - To have the permission **TEMPLATE_UPDATE_ALL** granted, or, - To have the permission **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.TemplateWeaknessQueryRequest() # TemplateWeaknessQueryRequest | 
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template
size = 20 # int | The size of the page to be returned (optional) (default to 20)

try:
    # Searches the weaknesses for a template, based on filters
    api_response = api_instance.query_template_weaknesses(body, template_id, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->query_template_weaknesses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemplateWeaknessQueryRequest**](TemplateWeaknessQueryRequest.md)|  | 
 **template_id** | [**str**](.md)| ID of the template | 
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]

### Return type

[**PagedModelTemplateWeaknessResponse**](PagedModelTemplateWeaknessResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_template_diagram_by_id**
> reset_template_diagram_by_id(template_id)

Restore an edited diagram where the threat model has not been updated

If a diagram was edited but the threat model is not updated yet, the previous  state of the diagram can be restored.  Conditions to be able to perform the action: - To have the permission **ARCHITECTURE_UPDATE** granted and - To have the permission **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Restore an edited diagram where the threat model has not been updated
    api_instance.reset_template_diagram_by_id(template_id)
except ApiException as e:
    print("Exception when calling TemplatesApi->reset_template_diagram_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simulate_template_architecture_questionnaire**
> ArchitectureQuestionnaireResultResponse simulate_template_architecture_questionnaire(body, template_id)

Executes a simulation of the outcome of running the architecture questionnaire.

Executes a simulation of the outcome of running the architecture questionnaire. Conditions to be able to perform the action:<ul><li>To have the permission **TEMPLATE_UPDATE** granted.</li><li>To have the permission **TEMPLATE_UPDATE_ALL** granted.</li></ul>

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateWizardQuestionnaireRequest() # UpdateWizardQuestionnaireRequest | 
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Executes a simulation of the outcome of running the architecture questionnaire.
    api_response = api_instance.simulate_template_architecture_questionnaire(body, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->simulate_template_architecture_questionnaire: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateWizardQuestionnaireRequest**](UpdateWizardQuestionnaireRequest.md)|  | 
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

[**ArchitectureQuestionnaireResultResponse**](ArchitectureQuestionnaireResultResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simulate_template_component_questionnaire**
> ComponentQuestionnaireResultResponse simulate_template_component_questionnaire(body, component_id)

Executes a simulation of the outcome of running this template component questionnaire.

Executes a simulation of the outcome of running this template component questionnaire. Conditions to be able to perform the action:<ul><li>To have the permission **TEMPLATE_UPDATE** granted.</li><li>To have the permission **TEMPLATE_UPDATE_ALL** granted.</li><li>The template the component belongs to must not be undergoing synchronization.</li></ul>

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateWizardQuestionnaireRequest() # UpdateWizardQuestionnaireRequest | 
component_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the component

try:
    # Executes a simulation of the outcome of running this template component questionnaire.
    api_response = api_instance.simulate_template_component_questionnaire(body, component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->simulate_template_component_questionnaire: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateWizardQuestionnaireRequest**](UpdateWizardQuestionnaireRequest.md)|  | 
 **component_id** | [**str**](.md)| ID of the component | 

### Return type

[**ComponentQuestionnaireResultResponse**](ComponentQuestionnaireResultResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_template**
> AsyncOperationIdResponse sync_template(x_irius_async, template_id)

Creates a new async operation to synchronize the template.

Creates a new async operation to synchronize the template. Conditions to be able to perform the action:<ul><li>To have the permission **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.</li></ul>

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
x_irius_async = true # bool | Sets whether the endpoint works asynchronously or not passed as parameter.
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Creates a new async operation to synchronize the template.
    api_response = api_instance.sync_template(x_irius_async, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->sync_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_irius_async** | **bool**| Sets whether the endpoint works asynchronously or not passed as parameter. | 
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

[**AsyncOperationIdResponse**](AsyncOperationIdResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_use_case**
> TemplateUseCaseResponse update_project_use_case(body, use_case_id)

Update a use case.

Update a use case. Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateTemplateUseCaseRequest() # UpdateTemplateUseCaseRequest | 
use_case_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the use case.

try:
    # Update a use case.
    api_response = api_instance.update_project_use_case(body, use_case_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_project_use_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTemplateUseCaseRequest**](UpdateTemplateUseCaseRequest.md)|  | 
 **use_case_id** | [**str**](.md)| ID of the use case. | 

### Return type

[**TemplateUseCaseResponse**](TemplateUseCaseResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template**
> TemplateResponse update_template(body, template_id)

Update the template that matches the id.

Modify the template. Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE** granted to update own templates. - To have the permission **TEMPLATE_UPDATE_ALL** granted to update any templates. To update the reference id of the template you will also need: - To have the permission **PRODUCT_ID_UPDATE** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateTemplateRequest() # UpdateTemplateRequest | The template to be updated.
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Update the template that matches the id.
    api_response = api_instance.update_template(body, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTemplateRequest**](UpdateTemplateRequest.md)| The template to be updated. | 
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_architecture_questionnaire**
> ArchitectureQuestionnaireResultResponse update_template_architecture_questionnaire(body, template_id)

Executes an update of the architecture questionnaire for the template.

Executes an update of the architecture questionnaire for the template. Conditions to be able to perform the action:<ul><li>To have the permission **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.</li><li>The project must be synchronized.</li></ul>

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateWizardQuestionnaireRequest() # UpdateWizardQuestionnaireRequest | 
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Executes an update of the architecture questionnaire for the template.
    api_response = api_instance.update_template_architecture_questionnaire(body, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_template_architecture_questionnaire: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateWizardQuestionnaireRequest**](UpdateWizardQuestionnaireRequest.md)|  | 
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

[**ArchitectureQuestionnaireResultResponse**](ArchitectureQuestionnaireResultResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_component_questionnaire**
> ComponentQuestionnaireResultResponse update_template_component_questionnaire(body, component_id)

Executes an update of the template component questionnaire.

Executes an update of the template component questionnaire. Conditions to be able to perform the action:<ul><li>To have the permission **TEMPLATE_UPDATE** granted.</li><li>To have the permission **TEMPLATE_UPDATE_ALL** granted.</li><li>The template the component belongs to must not be undergoing synchronization.</li></ul>

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateWizardQuestionnaireRequest() # UpdateWizardQuestionnaireRequest | 
component_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the component

try:
    # Executes an update of the template component questionnaire.
    api_response = api_instance.update_template_component_questionnaire(body, component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_template_component_questionnaire: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateWizardQuestionnaireRequest**](UpdateWizardQuestionnaireRequest.md)|  | 
 **component_id** | [**str**](.md)| ID of the component | 

### Return type

[**ComponentQuestionnaireResultResponse**](ComponentQuestionnaireResultResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_countermeasure**
> TemplateCountermeasureDetailResponse update_template_countermeasure(body, countermeasure_id)

Update a Template Countermeasure.

Updates the details of an existing template countermeasure using its ID. To perform the action the template must be editable: - It must not be read-only. - It must be visible for the User - User must have **TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** permissions.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateTemplateCountermeasureRequest() # UpdateTemplateCountermeasureRequest | 
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure.

try:
    # Update a Template Countermeasure.
    api_response = api_instance.update_template_countermeasure(body, countermeasure_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_template_countermeasure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTemplateCountermeasureRequest**](UpdateTemplateCountermeasureRequest.md)|  | 
 **countermeasure_id** | [**str**](.md)| The id of the countermeasure. | 

### Return type

[**TemplateCountermeasureDetailResponse**](TemplateCountermeasureDetailResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_countermeasure_implementation**
> TemplateCountermeasureImplementationResponse update_template_countermeasure_implementation(body, implementation_id)

Updates a countermeasure implementation.

Updates a countermeasure implementation. Conditions to be able to perform the action: - To have update permissions granted for the templates (**TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** with visibility over the template)

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateTemplateCountermeasureImplementationRequest() # UpdateTemplateCountermeasureImplementationRequest | 
implementation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure implementation.

try:
    # Updates a countermeasure implementation.
    api_response = api_instance.update_template_countermeasure_implementation(body, implementation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_template_countermeasure_implementation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTemplateCountermeasureImplementationRequest**](UpdateTemplateCountermeasureImplementationRequest.md)|  | 
 **implementation_id** | [**str**](.md)| The id of the countermeasure implementation. | 

### Return type

[**TemplateCountermeasureImplementationResponse**](TemplateCountermeasureImplementationResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_countermeasure_reference**
> TemplateCountermeasureReferenceResponse update_template_countermeasure_reference(body, reference_id)

Updates a reference for a countermeasure.

Updates a reference for a countermeasure. Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE** granted or - To have the permission **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateTemplateCountermeasureReferenceRequest() # UpdateTemplateCountermeasureReferenceRequest | 
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure reference.

try:
    # Updates a reference for a countermeasure.
    api_response = api_instance.update_template_countermeasure_reference(body, reference_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_template_countermeasure_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTemplateCountermeasureReferenceRequest**](UpdateTemplateCountermeasureReferenceRequest.md)|  | 
 **reference_id** | [**str**](.md)| The id of the countermeasure reference. | 

### Return type

[**TemplateCountermeasureReferenceResponse**](TemplateCountermeasureReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_countermeasure_standard_reference**
> TemplateCountermeasureStandardReferenceResponse update_template_countermeasure_standard_reference(body, standard_reference_id)

Updates a template countermeasure standard reference.

Updates a template countermeasure standard reference. Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE_ALL** granted, or</li> - To have the permission **TEMPLATE_UPDATE** granted.</li>

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateTemplateCountermeasureStandardReferenceRequest() # UpdateTemplateCountermeasureStandardReferenceRequest | 
standard_reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template countermeasure standard reference

try:
    # Updates a template countermeasure standard reference.
    api_response = api_instance.update_template_countermeasure_standard_reference(body, standard_reference_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_template_countermeasure_standard_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTemplateCountermeasureStandardReferenceRequest**](UpdateTemplateCountermeasureStandardReferenceRequest.md)|  | 
 **standard_reference_id** | [**str**](.md)| ID of the template countermeasure standard reference | 

### Return type

[**TemplateCountermeasureStandardReferenceResponse**](TemplateCountermeasureStandardReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_countermeasure_state**
> TemplateCountermeasureDetailResponse update_template_countermeasure_state(body, countermeasure_id)

Updates the status of a template countermeasure.

Updates the status of a template countermeasure. A reason must be given for these transitions: rejected or not-applicable.  To perform the action the template must be editable: - It must not be read-only. - It must be visible for the User - User must have **TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** permissions.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.CountermeasureidStateBody() # CountermeasureidStateBody | 
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure.

try:
    # Updates the status of a template countermeasure.
    api_response = api_instance.update_template_countermeasure_state(body, countermeasure_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_template_countermeasure_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CountermeasureidStateBody**](CountermeasureidStateBody.md)|  | 
 **countermeasure_id** | [**str**](.md)| The id of the countermeasure. | 

### Return type

[**TemplateCountermeasureDetailResponse**](TemplateCountermeasureDetailResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_countermeasure_test**
> TemplateCountermeasureTestResponse update_template_countermeasure_test(body, test_id)

Updates the test related to a countermeasure.

Updates the test related to a countermeasure. Conditions to be able to perform the action:<ul><li>To have the permission **TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** granted

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateTemplateCountermeasureTestRequest() # UpdateTemplateCountermeasureTestRequest | 
test_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure test.

try:
    # Updates the test related to a countermeasure.
    api_response = api_instance.update_template_countermeasure_test(body, test_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_template_countermeasure_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTemplateCountermeasureTestRequest**](UpdateTemplateCountermeasureTestRequest.md)|  | 
 **test_id** | [**str**](.md)| The id of the countermeasure test. | 

### Return type

[**TemplateCountermeasureTestResponse**](TemplateCountermeasureTestResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_countermeasure_test_reference**
> GetTemplateCountermeasureTestReferenceResponse update_template_countermeasure_test_reference(body, reference_id)

Updates a reference for a countermeasure test.

Updates a reference for a countermeasure test. Conditions to be able to perform the action:<ul><li>To have the permission **TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** granted</li></ul>

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateTemplateCountermeasureTestReferenceRequest() # UpdateTemplateCountermeasureTestReferenceRequest | 
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure test reference.

try:
    # Updates a reference for a countermeasure test.
    api_response = api_instance.update_template_countermeasure_test_reference(body, reference_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_template_countermeasure_test_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTemplateCountermeasureTestReferenceRequest**](UpdateTemplateCountermeasureTestReferenceRequest.md)|  | 
 **reference_id** | [**str**](.md)| The id of the countermeasure test reference. | 

### Return type

[**GetTemplateCountermeasureTestReferenceResponse**](GetTemplateCountermeasureTestReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_diagram_by_id**
> update_template_diagram_by_id(body, keep_state, template_id)

Update the diagram of a template.

Update the diagram of a template. Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = " <mxGraphModel><root><mxCell id=\"0\"/><mxCell id=\"1\" parent=\"0\"/></root></mxGraphModel>" # object | Payload to update a template diagram in XML format
keep_state = true # bool | Allow to save the diagram while keeping the draft mode.
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Update the diagram of a template.
    api_instance.update_template_diagram_by_id(body, keep_state, template_id)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_template_diagram_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Payload to update a template diagram in XML format | 
 **keep_state** | **bool**| Allow to save the diagram while keeping the draft mode. | 
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_settings_by_id**
> TemplateSettingsResponse update_template_settings_by_id(body, template_id)

Update the settings of a template.

Update the settings of a template. Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateTemplateSettingsRequest() # UpdateTemplateSettingsRequest | 
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Update the settings of a template.
    api_response = api_instance.update_template_settings_by_id(body, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_template_settings_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTemplateSettingsRequest**](UpdateTemplateSettingsRequest.md)|  | 
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

[**TemplateSettingsResponse**](TemplateSettingsResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_threat_by_id**
> TemplateThreatWithCustomFieldsResponse update_template_threat_by_id(body, threat_id)

Modify the threat details.

Modify the threat details. To perform the action the template must be editable: - It must not be read-only. - It must be visible for the User - User must have **TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** permissions.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateTemplateThreatRequest() # UpdateTemplateThreatRequest | 
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the threat.

try:
    # Modify the threat details.
    api_response = api_instance.update_template_threat_by_id(body, threat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_template_threat_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTemplateThreatRequest**](UpdateTemplateThreatRequest.md)|  | 
 **threat_id** | [**str**](.md)| Unique identifier of the threat. | 

### Return type

[**TemplateThreatWithCustomFieldsResponse**](TemplateThreatWithCustomFieldsResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_threat_countermeasure_mitigation**
> UpdateTemplateThreatCountermeasureMitigationResponse update_template_threat_countermeasure_mitigation(body, threat_id, countermeasure_id)

Update the mitigation value of a countermeasure of a threat.

Update the mitigation value of a countermeasure of a threat. Conditions to be able to perform the action: - To have update permissions granted for the templates (**TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** with visibility over the template)

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateTemplateThreatCountermeasureMitigationRequest() # UpdateTemplateThreatCountermeasureMitigationRequest | 
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the threat.
countermeasure_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the countermeasure.

try:
    # Update the mitigation value of a countermeasure of a threat.
    api_response = api_instance.update_template_threat_countermeasure_mitigation(body, threat_id, countermeasure_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_template_threat_countermeasure_mitigation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTemplateThreatCountermeasureMitigationRequest**](UpdateTemplateThreatCountermeasureMitigationRequest.md)|  | 
 **threat_id** | [**str**](.md)| Unique identifier of the threat. | 
 **countermeasure_id** | [**str**](.md)| The id of the countermeasure. | 

### Return type

[**UpdateTemplateThreatCountermeasureMitigationResponse**](UpdateTemplateThreatCountermeasureMitigationResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_threat_reference**
> TemplateThreatReferenceResponse update_template_threat_reference(body, reference_id)

Updates a reference for a threat.

Updates a reference for a threat. Conditions to be able to perform the action: - To have the permission **TEMPLATE_UPDATE** granted or - To have the permission **TEMPLATE_UPDATE_ALL** granted.

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateTemplateThreatReferenceRequest() # UpdateTemplateThreatReferenceRequest | 
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of a reference.

try:
    # Updates a reference for a threat.
    api_response = api_instance.update_template_threat_reference(body, reference_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_template_threat_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTemplateThreatReferenceRequest**](UpdateTemplateThreatReferenceRequest.md)|  | 
 **reference_id** | [**str**](.md)| ID of a reference. | 

### Return type

[**TemplateThreatReferenceResponse**](TemplateThreatReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_weakness**
> TemplateWeaknessResponse update_template_weakness(body, weakness_id)

Updates the weakness.

Updates the weakness. Conditions to be able to perform the action:<ul><li>To have the permission **TEMPLATE_UPDATE** granted, or</li><li> To have the permission **TEMPLATE_UPDATE_ALL** granted.</li></ul>

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateTemplateWeaknessRequest() # UpdateTemplateWeaknessRequest | 
weakness_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the weakness

try:
    # Updates the weakness.
    api_response = api_instance.update_template_weakness(body, weakness_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_template_weakness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTemplateWeaknessRequest**](UpdateTemplateWeaknessRequest.md)|  | 
 **weakness_id** | [**str**](.md)| ID of the weakness | 

### Return type

[**TemplateWeaknessResponse**](TemplateWeaknessResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_weakness_test**
> TemplateWeaknessTestResponse update_template_weakness_test(body, test_id)

Updates the test related to a weakness.

Updates the test related to a weakness. Conditions to be able to perform the action:<ul><li>To have the permission **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.</li></ul>

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateTemplateWeaknessTestRequest() # UpdateTemplateWeaknessTestRequest | 
test_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the weakness test.

try:
    # Updates the test related to a weakness.
    api_response = api_instance.update_template_weakness_test(body, test_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_template_weakness_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTemplateWeaknessTestRequest**](UpdateTemplateWeaknessTestRequest.md)|  | 
 **test_id** | [**str**](.md)| ID of the weakness test. | 

### Return type

[**TemplateWeaknessTestResponse**](TemplateWeaknessTestResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_weakness_test_reference**
> GetTemplateWeaknessTestReferenceResponse update_template_weakness_test_reference(body, reference_id)

Updates a reference related to a weakness test.

Updates a reference related to a weakness test. Conditions to be able to perform the action:<ul><li>To have the permission **TEMPLATE_UPDATE_ALL** or **TEMPLATE_UPDATE** granted</li></ul>

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
body = iriusrisk_python_client_lib.UpdateTemplateWeaknessTestReferenceRequest() # UpdateTemplateWeaknessTestReferenceRequest | 
reference_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the weakness test reference.

try:
    # Updates a reference related to a weakness test.
    api_response = api_instance.update_template_weakness_test_reference(body, reference_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_template_weakness_test_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTemplateWeaknessTestReferenceRequest**](UpdateTemplateWeaknessTestReferenceRequest.md)|  | 
 **reference_id** | [**str**](.md)| ID of the weakness test reference. | 

### Return type

[**GetTemplateWeaknessTestReferenceResponse**](GetTemplateWeaknessTestReferenceResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_with_file_template**
> TemplateResponse update_with_file_template(file, template_id)

Updates an existing template from an XML file

Updates an existing template from an XML file. Conditions to be able to perform the action: - To have one of the permissions **TEMPLATE_UPDATE** or **TEMPLATE_UPDATE_ALL** granted.  By default you will only be able to update the templates assigned to your own business units (TEMPLATE_UPDATE), so to update any template in the system you must have alternative permissions (TEMPLATE_UPDATE_ALL).

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
api_instance = iriusrisk_python_client_lib.TemplatesApi(iriusrisk_python_client_lib.ApiClient(configuration))
file = 'file_example' # str | 
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the template

try:
    # Updates an existing template from an XML file
    api_response = api_instance.update_with_file_template(file, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_with_file_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **template_id** | [**str**](.md)| ID of the template | 

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

