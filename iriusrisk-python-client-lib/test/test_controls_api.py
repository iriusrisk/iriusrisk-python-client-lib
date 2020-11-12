# coding: utf-8

"""
    IriusRisk API

    Products API  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.controls_api import ControlsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestControlsApi(unittest.TestCase):
    """ControlsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.controls_api.ControlsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_products_ref_components_component_ref_controls_control_ref_status_put(self):
        """Test case for products_ref_components_component_ref_controls_control_ref_status_put

        Sets the desired status to a countermeasure  # noqa: E501
        """
        pass

    def test_products_ref_controls_get(self):
        """Test case for products_ref_controls_get

        Gets a list of all product countermeasures  # noqa: E501
        """
        pass

    def test_products_ref_controls_implemented_get(self):
        """Test case for products_ref_controls_implemented_get

        Gets a list of all implemented countermeasures of a product.  # noqa: E501
        """
        pass

    def test_products_ref_controls_required_get(self):
        """Test case for products_ref_controls_required_get

        Gets a list of all required countermeasures of a product  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()