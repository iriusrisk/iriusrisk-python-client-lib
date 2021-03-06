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
from iriusrisk_python_client_lib.api.templates_api import TemplatesApi  # noqa: E501
from iriusrisk_python_client_lib.rest import ApiException


class TestTemplatesApi(unittest.TestCase):
    """TemplatesApi unit test stubs"""

    def setUp(self):
        self.api = iriusrisk_python_client_lib.api.templates_api.TemplatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_products_upload_post(self):
        """Test case for products_upload_post

        Creates a new product, library or template from a XML file upload.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
