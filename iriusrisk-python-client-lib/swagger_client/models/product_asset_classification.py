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


class ProductAssetClassification(object):
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
        'name': 'str',
        'desc': 'str',
        'confidentiality': 'int',
        'integrity': 'int',
        'availability': 'int'
    }

    attribute_map = {
        'name': 'name',
        'desc': 'desc',
        'confidentiality': 'confidentiality',
        'integrity': 'integrity',
        'availability': 'availability'
    }

    def __init__(self, name=None, desc=None, confidentiality=None, integrity=None, availability=None):  # noqa: E501
        """ProductAssetClassification - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._desc = None
        self._confidentiality = None
        self._integrity = None
        self._availability = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if desc is not None:
            self.desc = desc
        if confidentiality is not None:
            self.confidentiality = confidentiality
        if integrity is not None:
            self.integrity = integrity
        if availability is not None:
            self.availability = availability

    @property
    def name(self):
        """Gets the name of this ProductAssetClassification.  # noqa: E501


        :return: The name of this ProductAssetClassification.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductAssetClassification.


        :param name: The name of this ProductAssetClassification.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def desc(self):
        """Gets the desc of this ProductAssetClassification.  # noqa: E501


        :return: The desc of this ProductAssetClassification.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this ProductAssetClassification.


        :param desc: The desc of this ProductAssetClassification.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def confidentiality(self):
        """Gets the confidentiality of this ProductAssetClassification.  # noqa: E501


        :return: The confidentiality of this ProductAssetClassification.  # noqa: E501
        :rtype: int
        """
        return self._confidentiality

    @confidentiality.setter
    def confidentiality(self, confidentiality):
        """Sets the confidentiality of this ProductAssetClassification.


        :param confidentiality: The confidentiality of this ProductAssetClassification.  # noqa: E501
        :type: int
        """

        self._confidentiality = confidentiality

    @property
    def integrity(self):
        """Gets the integrity of this ProductAssetClassification.  # noqa: E501


        :return: The integrity of this ProductAssetClassification.  # noqa: E501
        :rtype: int
        """
        return self._integrity

    @integrity.setter
    def integrity(self, integrity):
        """Sets the integrity of this ProductAssetClassification.


        :param integrity: The integrity of this ProductAssetClassification.  # noqa: E501
        :type: int
        """

        self._integrity = integrity

    @property
    def availability(self):
        """Gets the availability of this ProductAssetClassification.  # noqa: E501


        :return: The availability of this ProductAssetClassification.  # noqa: E501
        :rtype: int
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this ProductAssetClassification.


        :param availability: The availability of this ProductAssetClassification.  # noqa: E501
        :type: int
        """

        self._availability = availability

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
        if issubclass(ProductAssetClassification, dict):
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
        if not isinstance(other, ProductAssetClassification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
