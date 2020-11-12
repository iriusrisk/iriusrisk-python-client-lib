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


class ProductsrefcomponentscomponentReftestscweControl(object):
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
        'component': 'str',
        'project': 'str'
    }

    attribute_map = {
        'name': 'name',
        'component': 'component',
        'project': 'project'
    }

    def __init__(self, name=None, component=None, project=None):  # noqa: E501
        """ProductsrefcomponentscomponentReftestscweControl - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._component = None
        self._project = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if component is not None:
            self.component = component
        if project is not None:
            self.project = project

    @property
    def name(self):
        """Gets the name of this ProductsrefcomponentscomponentReftestscweControl.  # noqa: E501


        :return: The name of this ProductsrefcomponentscomponentReftestscweControl.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductsrefcomponentscomponentReftestscweControl.


        :param name: The name of this ProductsrefcomponentscomponentReftestscweControl.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def component(self):
        """Gets the component of this ProductsrefcomponentscomponentReftestscweControl.  # noqa: E501


        :return: The component of this ProductsrefcomponentscomponentReftestscweControl.  # noqa: E501
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this ProductsrefcomponentscomponentReftestscweControl.


        :param component: The component of this ProductsrefcomponentscomponentReftestscweControl.  # noqa: E501
        :type: str
        """

        self._component = component

    @property
    def project(self):
        """Gets the project of this ProductsrefcomponentscomponentReftestscweControl.  # noqa: E501


        :return: The project of this ProductsrefcomponentscomponentReftestscweControl.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ProductsrefcomponentscomponentReftestscweControl.


        :param project: The project of this ProductsrefcomponentscomponentReftestscweControl.  # noqa: E501
        :type: str
        """

        self._project = project

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
        if issubclass(ProductsrefcomponentscomponentReftestscweControl, dict):
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
        if not isinstance(other, ProductsrefcomponentscomponentReftestscweControl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other