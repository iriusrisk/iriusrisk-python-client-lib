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
from swagger_client.api.roles_api import RolesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestRolesApi(unittest.TestCase):
    """RolesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.roles_api.RolesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_roles_post(self):
        """Test case for roles_post

        Creates a new Role  # noqa: E501
        """
        pass

    def test_roles_role_name_delete(self):
        """Test case for roles_role_name_delete

        Deletes an existing role  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()