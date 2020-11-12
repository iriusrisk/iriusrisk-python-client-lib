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
from swagger_client.api.groups_api import GroupsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestGroupsApi(unittest.TestCase):
    """GroupsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.groups_api.GroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_groups_get(self):
        """Test case for groups_get

        Gets a list of all Groups  # noqa: E501
        """
        pass

    def test_groups_group_ref_delete(self):
        """Test case for groups_group_ref_delete

        Deletes a users group  # noqa: E501
        """
        pass

    def test_groups_group_ref_get(self):
        """Test case for groups_group_ref_get

        Gets the group details.  # noqa: E501
        """
        pass

    def test_groups_group_ref_put(self):
        """Test case for groups_group_ref_put

        Update a users group  # noqa: E501
        """
        pass

    def test_groups_group_users_delete(self):
        """Test case for groups_group_users_delete

        Unassign a list of users from a group  # noqa: E501
        """
        pass

    def test_groups_group_users_get(self):
        """Test case for groups_group_users_get

        List users from a group  # noqa: E501
        """
        pass

    def test_groups_group_users_put(self):
        """Test case for groups_group_users_put

        Assigns users to a group  # noqa: E501
        """
        pass

    def test_groups_group_users_user_delete(self):
        """Test case for groups_group_users_user_delete

        Removes a user from a group  # noqa: E501
        """
        pass

    def test_groups_post(self):
        """Test case for groups_post

        Creates a new user group  # noqa: E501
        """
        pass

    def test_products_ref_groups_delete(self):
        """Test case for products_ref_groups_delete

        Unassigns a list of user groups from a product.  # noqa: E501
        """
        pass

    def test_products_ref_groups_get(self):
        """Test case for products_ref_groups_get

        List all groups assigned to a product  # noqa: E501
        """
        pass

    def test_products_ref_groups_put(self):
        """Test case for products_ref_groups_put

        Assigns groups of users to a product.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()