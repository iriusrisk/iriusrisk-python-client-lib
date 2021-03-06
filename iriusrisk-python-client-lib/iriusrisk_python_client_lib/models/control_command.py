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


class ControlCommand(object):
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
        'mitigation': 'int',
        'test': 'TestCommand',
        'state': 'str',
        'cost_rating': 'str',
        'standards': 'list[ControlCommandStandards]'
    }

    attribute_map = {
        'ref': 'ref',
        'name': 'name',
        'desc': 'desc',
        'mitigation': 'mitigation',
        'test': 'test',
        'state': 'state',
        'cost_rating': 'costRating',
        'standards': 'standards'
    }

    def __init__(self, ref=None, name=None, desc=None, mitigation=None, test=None, state=None, cost_rating=None, standards=None):  # noqa: E501
        """ControlCommand - a model defined in Swagger"""  # noqa: E501

        self._ref = None
        self._name = None
        self._desc = None
        self._mitigation = None
        self._test = None
        self._state = None
        self._cost_rating = None
        self._standards = None
        self.discriminator = None

        if ref is not None:
            self.ref = ref
        if name is not None:
            self.name = name
        if desc is not None:
            self.desc = desc
        if mitigation is not None:
            self.mitigation = mitigation
        if test is not None:
            self.test = test
        if state is not None:
            self.state = state
        if cost_rating is not None:
            self.cost_rating = cost_rating
        if standards is not None:
            self.standards = standards

    @property
    def ref(self):
        """Gets the ref of this ControlCommand.  # noqa: E501

        Reference field value  # noqa: E501

        :return: The ref of this ControlCommand.  # noqa: E501
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this ControlCommand.

        Reference field value  # noqa: E501

        :param ref: The ref of this ControlCommand.  # noqa: E501
        :type: str
        """

        self._ref = ref

    @property
    def name(self):
        """Gets the name of this ControlCommand.  # noqa: E501

        Name field value  # noqa: E501

        :return: The name of this ControlCommand.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ControlCommand.

        Name field value  # noqa: E501

        :param name: The name of this ControlCommand.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def desc(self):
        """Gets the desc of this ControlCommand.  # noqa: E501

        Description field value  # noqa: E501

        :return: The desc of this ControlCommand.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this ControlCommand.

        Description field value  # noqa: E501

        :param desc: The desc of this ControlCommand.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def mitigation(self):
        """Gets the mitigation of this ControlCommand.  # noqa: E501

        Mitigation  # noqa: E501

        :return: The mitigation of this ControlCommand.  # noqa: E501
        :rtype: int
        """
        return self._mitigation

    @mitigation.setter
    def mitigation(self, mitigation):
        """Sets the mitigation of this ControlCommand.

        Mitigation  # noqa: E501

        :param mitigation: The mitigation of this ControlCommand.  # noqa: E501
        :type: int
        """

        self._mitigation = mitigation

    @property
    def test(self):
        """Gets the test of this ControlCommand.  # noqa: E501


        :return: The test of this ControlCommand.  # noqa: E501
        :rtype: TestCommand
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this ControlCommand.


        :param test: The test of this ControlCommand.  # noqa: E501
        :type: TestCommand
        """

        self._test = test

    @property
    def state(self):
        """Gets the state of this ControlCommand.  # noqa: E501

        Countermeasure state  # noqa: E501

        :return: The state of this ControlCommand.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ControlCommand.

        Countermeasure state  # noqa: E501

        :param state: The state of this ControlCommand.  # noqa: E501
        :type: str
        """
        allowed_values = ["not-applicable", "rejected", "recommended", "required", "implemented"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def cost_rating(self):
        """Gets the cost_rating of this ControlCommand.  # noqa: E501

        Countermeasure cost  # noqa: E501

        :return: The cost_rating of this ControlCommand.  # noqa: E501
        :rtype: str
        """
        return self._cost_rating

    @cost_rating.setter
    def cost_rating(self, cost_rating):
        """Sets the cost_rating of this ControlCommand.

        Countermeasure cost  # noqa: E501

        :param cost_rating: The cost_rating of this ControlCommand.  # noqa: E501
        :type: str
        """
        allowed_values = ["low", "medium", "high"]  # noqa: E501
        if cost_rating not in allowed_values:
            raise ValueError(
                "Invalid value for `cost_rating` ({0}), must be one of {1}"  # noqa: E501
                .format(cost_rating, allowed_values)
            )

        self._cost_rating = cost_rating

    @property
    def standards(self):
        """Gets the standards of this ControlCommand.  # noqa: E501

        List of standards  # noqa: E501

        :return: The standards of this ControlCommand.  # noqa: E501
        :rtype: list[ControlCommandStandards]
        """
        return self._standards

    @standards.setter
    def standards(self, standards):
        """Sets the standards of this ControlCommand.

        List of standards  # noqa: E501

        :param standards: The standards of this ControlCommand.  # noqa: E501
        :type: list[ControlCommandStandards]
        """

        self._standards = standards

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
        if issubclass(ControlCommand, dict):
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
        if not isinstance(other, ControlCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
