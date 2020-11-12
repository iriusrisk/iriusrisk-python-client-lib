# coding: utf-8

"""
    IriusRisk API

    Products API  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TestsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def products_ref_components_component_ref_tests_cwe_put(self, api_token, ref, component_ref, cwe, update_status_test_request_body, **kwargs):  # noqa: E501
        """Updates a single test to a component.  # noqa: E501

        Updates a single test to a component. Conditions to be able to perform the action:   - To have the permission **TEST_UPDATE** granted.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_ref_components_component_ref_tests_cwe_put(api_token, ref, component_ref, cwe, update_status_test_request_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_token: Authentication token (required)
        :param str ref: ID for product (required)
        :param str component_ref: ID for component (required)
        :param str cwe: countermeasure or weakness CWE (required)
        :param UpdateStatusTestRequestBody update_status_test_request_body: JSON data that contains the information to update test (required)
        :return: list[InlineResponse2001]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.products_ref_components_component_ref_tests_cwe_put_with_http_info(api_token, ref, component_ref, cwe, update_status_test_request_body, **kwargs)  # noqa: E501
        else:
            (data) = self.products_ref_components_component_ref_tests_cwe_put_with_http_info(api_token, ref, component_ref, cwe, update_status_test_request_body, **kwargs)  # noqa: E501
            return data

    def products_ref_components_component_ref_tests_cwe_put_with_http_info(self, api_token, ref, component_ref, cwe, update_status_test_request_body, **kwargs):  # noqa: E501
        """Updates a single test to a component.  # noqa: E501

        Updates a single test to a component. Conditions to be able to perform the action:   - To have the permission **TEST_UPDATE** granted.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_ref_components_component_ref_tests_cwe_put_with_http_info(api_token, ref, component_ref, cwe, update_status_test_request_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_token: Authentication token (required)
        :param str ref: ID for product (required)
        :param str component_ref: ID for component (required)
        :param str cwe: countermeasure or weakness CWE (required)
        :param UpdateStatusTestRequestBody update_status_test_request_body: JSON data that contains the information to update test (required)
        :return: list[InlineResponse2001]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_token', 'ref', 'component_ref', 'cwe', 'update_status_test_request_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method products_ref_components_component_ref_tests_cwe_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_token' is set
        if ('api_token' not in params or
                params['api_token'] is None):
            raise ValueError("Missing the required parameter `api_token` when calling `products_ref_components_component_ref_tests_cwe_put`")  # noqa: E501
        # verify the required parameter 'ref' is set
        if ('ref' not in params or
                params['ref'] is None):
            raise ValueError("Missing the required parameter `ref` when calling `products_ref_components_component_ref_tests_cwe_put`")  # noqa: E501
        # verify the required parameter 'component_ref' is set
        if ('component_ref' not in params or
                params['component_ref'] is None):
            raise ValueError("Missing the required parameter `component_ref` when calling `products_ref_components_component_ref_tests_cwe_put`")  # noqa: E501
        # verify the required parameter 'cwe' is set
        if ('cwe' not in params or
                params['cwe'] is None):
            raise ValueError("Missing the required parameter `cwe` when calling `products_ref_components_component_ref_tests_cwe_put`")  # noqa: E501
        # verify the required parameter 'update_status_test_request_body' is set
        if ('update_status_test_request_body' not in params or
                params['update_status_test_request_body'] is None):
            raise ValueError("Missing the required parameter `update_status_test_request_body` when calling `products_ref_components_component_ref_tests_cwe_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ref' in params:
            path_params['ref'] = params['ref']  # noqa: E501
        if 'component_ref' in params:
            path_params['componentRef'] = params['component_ref']  # noqa: E501
        if 'cwe' in params:
            path_params['cwe'] = params['cwe']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_token' in params:
            header_params['api-token'] = params['api_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_status_test_request_body' in params:
            body_params = params['update_status_test_request_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/products/{ref}/components/{componentRef}/tests/{cwe}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse2001]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def products_ref_components_component_ref_tests_test_type_upload_post(self, api_token, ref, component_ref, test_type, **kwargs):  # noqa: E501
        """Imports test results from different sources to a component  # noqa: E501

        Imports test results from different sources (OWASP ZAP, Cucumber, Micro Focus Fortify) into the specified component. More than one file can be attached to the call. Conditions to be able to perform the action:   - To have the permission **TEST_UPDATE** granted.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_ref_components_component_ref_tests_test_type_upload_post(api_token, ref, component_ref, test_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_token: Authentication token (required)
        :param str ref: ID for product (required)
        :param str component_ref: ID for component (required)
        :param str test_type: Type of test to be imported (zap|cucumber|junit|hp-fortify) (required)
        :param file file_name: File to upload
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.products_ref_components_component_ref_tests_test_type_upload_post_with_http_info(api_token, ref, component_ref, test_type, **kwargs)  # noqa: E501
        else:
            (data) = self.products_ref_components_component_ref_tests_test_type_upload_post_with_http_info(api_token, ref, component_ref, test_type, **kwargs)  # noqa: E501
            return data

    def products_ref_components_component_ref_tests_test_type_upload_post_with_http_info(self, api_token, ref, component_ref, test_type, **kwargs):  # noqa: E501
        """Imports test results from different sources to a component  # noqa: E501

        Imports test results from different sources (OWASP ZAP, Cucumber, Micro Focus Fortify) into the specified component. More than one file can be attached to the call. Conditions to be able to perform the action:   - To have the permission **TEST_UPDATE** granted.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_ref_components_component_ref_tests_test_type_upload_post_with_http_info(api_token, ref, component_ref, test_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_token: Authentication token (required)
        :param str ref: ID for product (required)
        :param str component_ref: ID for component (required)
        :param str test_type: Type of test to be imported (zap|cucumber|junit|hp-fortify) (required)
        :param file file_name: File to upload
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_token', 'ref', 'component_ref', 'test_type', 'file_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method products_ref_components_component_ref_tests_test_type_upload_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_token' is set
        if ('api_token' not in params or
                params['api_token'] is None):
            raise ValueError("Missing the required parameter `api_token` when calling `products_ref_components_component_ref_tests_test_type_upload_post`")  # noqa: E501
        # verify the required parameter 'ref' is set
        if ('ref' not in params or
                params['ref'] is None):
            raise ValueError("Missing the required parameter `ref` when calling `products_ref_components_component_ref_tests_test_type_upload_post`")  # noqa: E501
        # verify the required parameter 'component_ref' is set
        if ('component_ref' not in params or
                params['component_ref'] is None):
            raise ValueError("Missing the required parameter `component_ref` when calling `products_ref_components_component_ref_tests_test_type_upload_post`")  # noqa: E501
        # verify the required parameter 'test_type' is set
        if ('test_type' not in params or
                params['test_type'] is None):
            raise ValueError("Missing the required parameter `test_type` when calling `products_ref_components_component_ref_tests_test_type_upload_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ref' in params:
            path_params['ref'] = params['ref']  # noqa: E501
        if 'component_ref' in params:
            path_params['componentRef'] = params['component_ref']  # noqa: E501
        if 'test_type' in params:
            path_params['testType'] = params['test_type']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_token' in params:
            header_params['api-token'] = params['api_token']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'file_name' in params:
            local_var_files['fileName'] = params['file_name']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/products/{ref}/components/{componentRef}/tests/{testType}/upload', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2011',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def products_ref_tests_test_type_upload_post(self, api_token, ref, test_type, **kwargs):  # noqa: E501
        """Imports test results from different sources to a product.  # noqa: E501

        Imports test results from different sources (OWASP ZAP, Cucumber, Micro Focus Fortify) uploading files. More than one file can be attached to the call. Conditions to be able to perform the action:   - To have the permission **TEST_UPDATE** granted.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_ref_tests_test_type_upload_post(api_token, ref, test_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_token: Authentication token (required)
        :param str ref: ID for product (required)
        :param str test_type: Type of test to be imported (zap|cucumber|junit|hp-fortify) (required)
        :param file file_name: File to upload
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.products_ref_tests_test_type_upload_post_with_http_info(api_token, ref, test_type, **kwargs)  # noqa: E501
        else:
            (data) = self.products_ref_tests_test_type_upload_post_with_http_info(api_token, ref, test_type, **kwargs)  # noqa: E501
            return data

    def products_ref_tests_test_type_upload_post_with_http_info(self, api_token, ref, test_type, **kwargs):  # noqa: E501
        """Imports test results from different sources to a product.  # noqa: E501

        Imports test results from different sources (OWASP ZAP, Cucumber, Micro Focus Fortify) uploading files. More than one file can be attached to the call. Conditions to be able to perform the action:   - To have the permission **TEST_UPDATE** granted.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_ref_tests_test_type_upload_post_with_http_info(api_token, ref, test_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_token: Authentication token (required)
        :param str ref: ID for product (required)
        :param str test_type: Type of test to be imported (zap|cucumber|junit|hp-fortify) (required)
        :param file file_name: File to upload
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_token', 'ref', 'test_type', 'file_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method products_ref_tests_test_type_upload_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_token' is set
        if ('api_token' not in params or
                params['api_token'] is None):
            raise ValueError("Missing the required parameter `api_token` when calling `products_ref_tests_test_type_upload_post`")  # noqa: E501
        # verify the required parameter 'ref' is set
        if ('ref' not in params or
                params['ref'] is None):
            raise ValueError("Missing the required parameter `ref` when calling `products_ref_tests_test_type_upload_post`")  # noqa: E501
        # verify the required parameter 'test_type' is set
        if ('test_type' not in params or
                params['test_type'] is None):
            raise ValueError("Missing the required parameter `test_type` when calling `products_ref_tests_test_type_upload_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ref' in params:
            path_params['ref'] = params['ref']  # noqa: E501
        if 'test_type' in params:
            path_params['testType'] = params['test_type']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_token' in params:
            header_params['api-token'] = params['api_token']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'file_name' in params:
            local_var_files['fileName'] = params['file_name']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/products/{ref}/tests/{testType}/upload', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2011',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)