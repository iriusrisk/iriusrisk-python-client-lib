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
from iriusrisk_python_client_lib.api.risks_api import RisksApi  # noqa: E501
from iriusrisk_python_client_lib.rest import ApiException


class TestRisksApi(unittest.TestCase):
    """RisksApi unit test stubs"""

    def setUp(self):
        self.api = iriusrisk_python_client_lib.api.risks_api.RisksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_products_ref_risks_get(self):
        """Test case for products_ref_risks_get

        Gets the risks summary of a product  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
