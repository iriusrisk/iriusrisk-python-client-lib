# coding: utf-8

"""
    IriusRisk API

    Products API  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import iriusrisk_python_client_lib
from iriusrisk_python_client_lib.api.tests_api import TestsApi  # noqa: E501
from iriusrisk_python_client_lib.rest import ApiException


class TestTestsApi(unittest.TestCase):
    """TestsApi unit test stubs"""

    def setUp(self):
        self.api = iriusrisk_python_client_lib.api.tests_api.TestsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_products_ref_components_component_ref_tests_cwe_put(self):
        """Test case for products_ref_components_component_ref_tests_cwe_put

        Updates a single test to a component.  # noqa: E501
        """
        pass

    def test_products_ref_components_component_ref_tests_test_type_upload_post(self):
        """Test case for products_ref_components_component_ref_tests_test_type_upload_post

        Imports test results from different sources to a component  # noqa: E501
        """
        pass

    def test_products_ref_tests_test_type_upload_post(self):
        """Test case for products_ref_tests_test_type_upload_post

        Imports test results from different sources to a product.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
