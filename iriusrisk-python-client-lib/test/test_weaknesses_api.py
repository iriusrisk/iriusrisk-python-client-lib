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
from iriusrisk_python_client_lib.api.weaknesses_api import WeaknessesApi  # noqa: E501
from iriusrisk_python_client_lib.rest import ApiException


class TestWeaknessesApi(unittest.TestCase):
    """WeaknessesApi unit test stubs"""

    def setUp(self):
        self.api = iriusrisk_python_client_lib.api.weaknesses_api.WeaknessesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put(self):
        """Test case for libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_put

        Associates weakness to a threat in a risk pattern.  # noqa: E501
        """
        pass

    def test_libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put(self):
        """Test case for libraries_library_ref_riskpatterns_risk_pattern_ref_usecases_use_case_ref_threats_threat_ref_weaknesses_weakness_ref_countermeasures_put

        Associates a countermeasure to a weakness in a risk pattern.  # noqa: E501
        """
        pass

    def test_libraries_library_ref_riskpatterns_risk_pattern_ref_weaknesses_post(self):
        """Test case for libraries_library_ref_riskpatterns_risk_pattern_ref_weaknesses_post

        Creates a new weakness in a risk pattern  # noqa: E501
        """
        pass

    def test_products_ref_weaknesses_get(self):
        """Test case for products_ref_weaknesses_get

        Gets a list of all weaknesses of a product  # noqa: E501
        """
        pass

    def test_products_ref_weaknesses_test_state_get(self):
        """Test case for products_ref_weaknesses_test_state_get

        Gets a list of all weaknesses of a product filtered by test state  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
