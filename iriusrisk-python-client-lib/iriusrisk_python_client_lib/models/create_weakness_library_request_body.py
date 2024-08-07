# coding: utf-8

"""
    IriusRisk API

    Products API  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreateWeaknessLibraryRequestBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ref': 'str',
        'name': 'str',
        'desc': 'str',
        'impact': 'str',
        'test': 'TestCommand'
    }

    attribute_map = {
        'ref': 'ref',
        'name': 'name',
        'desc': 'desc',
        'impact': 'impact',
        'test': 'test'
    }

    def __init__(self, ref=None, name=None, desc=None, impact=None, test=None):  # noqa: E501
        """CreateWeaknessLibraryRequestBody - a model defined in Swagger"""  # noqa: E501

        self._ref = None
        self._name = None
        self._desc = None
        self._impact = None
        self._test = None
        self.discriminator = None

        if ref is not None:
            self.ref = ref
        if name is not None:
            self.name = name
        if desc is not None:
            self.desc = desc
        if impact is not None:
            self.impact = impact
        if test is not None:
            self.test = test

    @property
    def ref(self):
        """Gets the ref of this CreateWeaknessLibraryRequestBody.  # noqa: E501

        Reference field value  # noqa: E501

        :return: The ref of this CreateWeaknessLibraryRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this CreateWeaknessLibraryRequestBody.

        Reference field value  # noqa: E501

        :param ref: The ref of this CreateWeaknessLibraryRequestBody.  # noqa: E501
        :type: str
        """

        self._ref = ref

    @property
    def name(self):
        """Gets the name of this CreateWeaknessLibraryRequestBody.  # noqa: E501

        Name field value  # noqa: E501

        :return: The name of this CreateWeaknessLibraryRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateWeaknessLibraryRequestBody.

        Name field value  # noqa: E501

        :param name: The name of this CreateWeaknessLibraryRequestBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def desc(self):
        """Gets the desc of this CreateWeaknessLibraryRequestBody.  # noqa: E501

        Description field value  # noqa: E501

        :return: The desc of this CreateWeaknessLibraryRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this CreateWeaknessLibraryRequestBody.

        Description field value  # noqa: E501

        :param desc: The desc of this CreateWeaknessLibraryRequestBody.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def impact(self):
        """Gets the impact of this CreateWeaknessLibraryRequestBody.  # noqa: E501

        Impact  # noqa: E501

        :return: The impact of this CreateWeaknessLibraryRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._impact

    @impact.setter
    def impact(self, impact):
        """Sets the impact of this CreateWeaknessLibraryRequestBody.

        Impact  # noqa: E501

        :param impact: The impact of this CreateWeaknessLibraryRequestBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "low", "medium", "high", "very-high"]  # noqa: E501
        if impact not in allowed_values:
            raise ValueError(
                "Invalid value for `impact` ({0}), must be one of {1}"  # noqa: E501
                .format(impact, allowed_values)
            )

        self._impact = impact

    @property
    def test(self):
        """Gets the test of this CreateWeaknessLibraryRequestBody.  # noqa: E501


        :return: The test of this CreateWeaknessLibraryRequestBody.  # noqa: E501
        :rtype: TestCommand
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this CreateWeaknessLibraryRequestBody.


        :param test: The test of this CreateWeaknessLibraryRequestBody.  # noqa: E501
        :type: TestCommand
        """

        self._test = test

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CreateWeaknessLibraryRequestBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateWeaknessLibraryRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
