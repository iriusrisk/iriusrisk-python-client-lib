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


class ComponentDefinition(object):
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
        'category_ref': 'str',
        'risk_patterns': 'list[ComponentDefinitionRiskPatterns]'
    }

    attribute_map = {
        'ref': 'ref',
        'name': 'name',
        'desc': 'desc',
        'category_ref': 'categoryRef',
        'risk_patterns': 'riskPatterns'
    }

    def __init__(self, ref=None, name=None, desc=None, category_ref=None, risk_patterns=None):  # noqa: E501
        """ComponentDefinition - a model defined in Swagger"""  # noqa: E501

        self._ref = None
        self._name = None
        self._desc = None
        self._category_ref = None
        self._risk_patterns = None
        self.discriminator = None

        if ref is not None:
            self.ref = ref
        if name is not None:
            self.name = name
        if desc is not None:
            self.desc = desc
        if category_ref is not None:
            self.category_ref = category_ref
        if risk_patterns is not None:
            self.risk_patterns = risk_patterns

    @property
    def ref(self):
        """Gets the ref of this ComponentDefinition.  # noqa: E501

        Unique identifier of the Component Definition  # noqa: E501

        :return: The ref of this ComponentDefinition.  # noqa: E501
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this ComponentDefinition.

        Unique identifier of the Component Definition  # noqa: E501

        :param ref: The ref of this ComponentDefinition.  # noqa: E501
        :type: str
        """

        self._ref = ref

    @property
    def name(self):
        """Gets the name of this ComponentDefinition.  # noqa: E501

        Name of the Component Definition  # noqa: E501

        :return: The name of this ComponentDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentDefinition.

        Name of the Component Definition  # noqa: E501

        :param name: The name of this ComponentDefinition.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def desc(self):
        """Gets the desc of this ComponentDefinition.  # noqa: E501

        Description of the Component Definition  # noqa: E501

        :return: The desc of this ComponentDefinition.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this ComponentDefinition.

        Description of the Component Definition  # noqa: E501

        :param desc: The desc of this ComponentDefinition.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def category_ref(self):
        """Gets the category_ref of this ComponentDefinition.  # noqa: E501

        Reference of the category of the component  # noqa: E501

        :return: The category_ref of this ComponentDefinition.  # noqa: E501
        :rtype: str
        """
        return self._category_ref

    @category_ref.setter
    def category_ref(self, category_ref):
        """Sets the category_ref of this ComponentDefinition.

        Reference of the category of the component  # noqa: E501

        :param category_ref: The category_ref of this ComponentDefinition.  # noqa: E501
        :type: str
        """

        self._category_ref = category_ref

    @property
    def risk_patterns(self):
        """Gets the risk_patterns of this ComponentDefinition.  # noqa: E501


        :return: The risk_patterns of this ComponentDefinition.  # noqa: E501
        :rtype: list[ComponentDefinitionRiskPatterns]
        """
        return self._risk_patterns

    @risk_patterns.setter
    def risk_patterns(self, risk_patterns):
        """Sets the risk_patterns of this ComponentDefinition.


        :param risk_patterns: The risk_patterns of this ComponentDefinition.  # noqa: E501
        :type: list[ComponentDefinitionRiskPatterns]
        """

        self._risk_patterns = risk_patterns

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
        if issubclass(ComponentDefinition, dict):
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
        if not isinstance(other, ComponentDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
