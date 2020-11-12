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


class CreateProduct(object):
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
        'tags': 'str',
        'udts': 'list[Udt]'
    }

    attribute_map = {
        'ref': 'ref',
        'name': 'name',
        'desc': 'desc',
        'tags': 'tags',
        'udts': 'udts'
    }

    def __init__(self, ref=None, name=None, desc=None, tags=None, udts=None):  # noqa: E501
        """CreateProduct - a model defined in Swagger"""  # noqa: E501

        self._ref = None
        self._name = None
        self._desc = None
        self._tags = None
        self._udts = None
        self.discriminator = None

        if ref is not None:
            self.ref = ref
        if name is not None:
            self.name = name
        if desc is not None:
            self.desc = desc
        if tags is not None:
            self.tags = tags
        if udts is not None:
            self.udts = udts

    @property
    def ref(self):
        """Gets the ref of this CreateProduct.  # noqa: E501


        :return: The ref of this CreateProduct.  # noqa: E501
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this CreateProduct.


        :param ref: The ref of this CreateProduct.  # noqa: E501
        :type: str
        """

        self._ref = ref

    @property
    def name(self):
        """Gets the name of this CreateProduct.  # noqa: E501


        :return: The name of this CreateProduct.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateProduct.


        :param name: The name of this CreateProduct.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def desc(self):
        """Gets the desc of this CreateProduct.  # noqa: E501


        :return: The desc of this CreateProduct.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this CreateProduct.


        :param desc: The desc of this CreateProduct.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def tags(self):
        """Gets the tags of this CreateProduct.  # noqa: E501


        :return: The tags of this CreateProduct.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateProduct.


        :param tags: The tags of this CreateProduct.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def udts(self):
        """Gets the udts of this CreateProduct.  # noqa: E501


        :return: The udts of this CreateProduct.  # noqa: E501
        :rtype: list[Udt]
        """
        return self._udts

    @udts.setter
    def udts(self, udts):
        """Sets the udts of this CreateProduct.


        :param udts: The udts of this CreateProduct.  # noqa: E501
        :type: list[Udt]
        """

        self._udts = udts

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
        if issubclass(CreateProduct, dict):
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
        if not isinstance(other, CreateProduct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
