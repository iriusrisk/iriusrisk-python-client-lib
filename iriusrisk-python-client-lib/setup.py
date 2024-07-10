# coding: utf-8

"""
    IriusRisk API

    IriusRisk provides this featured API to allow for deeper customer integrations as well as enable very flexible automations within the many varied environments IriusRisk needs to operate.  **Beta Version Disclaimer:** Please note that this version of the API is currently in beta. While it offers advanced features for deeper integrations and flexible automations, we reserve the right to make breaking changes during this phase. Backwards compatibility may not be maintained. We encourage users to explore its capabilities but recommend caution in production environments as the API may undergo significant modifications.  # noqa: E501

    OpenAPI spec version: 2.0.0-beta.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "iriusrisk-python-client-lib"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="IriusRisk API",
    author_email="",
    url="",
    keywords=["Swagger", "IriusRisk API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    IriusRisk provides this featured API to allow for deeper customer integrations as well as enable very flexible automations within the many varied environments IriusRisk needs to operate.  **Beta Version Disclaimer:** Please note that this version of the API is currently in beta. While it offers advanced features for deeper integrations and flexible automations, we reserve the right to make breaking changes during this phase. Backwards compatibility may not be maintained. We encourage users to explore its capabilities but recommend caution in production environments as the API may undergo significant modifications.  # noqa: E501
    """
)
