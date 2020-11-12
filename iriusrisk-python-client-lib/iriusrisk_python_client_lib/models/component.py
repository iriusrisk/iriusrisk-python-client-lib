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


class Component(object):
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
        'group_name': 'str',
        'tags': 'list[str]',
        'position': 'int',
        'questions': 'list[Question]',
        'trust_zones': 'list[ComponentTrustZone]',
        'assets': 'list[ComponentAsset]',
        'weaknesses': 'list[ComponentWeakness]',
        'controls': 'list[ComponentControl]',
        'usecases': 'list[ComponentUseCase]'
    }

    attribute_map = {
        'ref': 'ref',
        'name': 'name',
        'desc': 'desc',
        'group_name': 'groupName',
        'tags': 'tags',
        'position': 'position',
        'questions': 'questions',
        'trust_zones': 'trustZones',
        'assets': 'assets',
        'weaknesses': 'weaknesses',
        'controls': 'controls',
        'usecases': 'usecases'
    }

    def __init__(self, ref=None, name=None, desc=None, group_name=None, tags=None, position=None, questions=None, trust_zones=None, assets=None, weaknesses=None, controls=None, usecases=None):  # noqa: E501
        """Component - a model defined in Swagger"""  # noqa: E501

        self._ref = None
        self._name = None
        self._desc = None
        self._group_name = None
        self._tags = None
        self._position = None
        self._questions = None
        self._trust_zones = None
        self._assets = None
        self._weaknesses = None
        self._controls = None
        self._usecases = None
        self.discriminator = None

        if ref is not None:
            self.ref = ref
        if name is not None:
            self.name = name
        if desc is not None:
            self.desc = desc
        if group_name is not None:
            self.group_name = group_name
        if tags is not None:
            self.tags = tags
        if position is not None:
            self.position = position
        if questions is not None:
            self.questions = questions
        if trust_zones is not None:
            self.trust_zones = trust_zones
        if assets is not None:
            self.assets = assets
        if weaknesses is not None:
            self.weaknesses = weaknesses
        if controls is not None:
            self.controls = controls
        if usecases is not None:
            self.usecases = usecases

    @property
    def ref(self):
        """Gets the ref of this Component.  # noqa: E501


        :return: The ref of this Component.  # noqa: E501
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this Component.


        :param ref: The ref of this Component.  # noqa: E501
        :type: str
        """

        self._ref = ref

    @property
    def name(self):
        """Gets the name of this Component.  # noqa: E501


        :return: The name of this Component.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Component.


        :param name: The name of this Component.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def desc(self):
        """Gets the desc of this Component.  # noqa: E501


        :return: The desc of this Component.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this Component.


        :param desc: The desc of this Component.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def group_name(self):
        """Gets the group_name of this Component.  # noqa: E501

        This field always returns null. All group names have been transformed into tags.  # noqa: E501

        :return: The group_name of this Component.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this Component.

        This field always returns null. All group names have been transformed into tags.  # noqa: E501

        :param group_name: The group_name of this Component.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def tags(self):
        """Gets the tags of this Component.  # noqa: E501

        List of all tags  # noqa: E501

        :return: The tags of this Component.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Component.

        List of all tags  # noqa: E501

        :param tags: The tags of this Component.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def position(self):
        """Gets the position of this Component.  # noqa: E501


        :return: The position of this Component.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Component.


        :param position: The position of this Component.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def questions(self):
        """Gets the questions of this Component.  # noqa: E501


        :return: The questions of this Component.  # noqa: E501
        :rtype: list[Question]
        """
        return self._questions

    @questions.setter
    def questions(self, questions):
        """Sets the questions of this Component.


        :param questions: The questions of this Component.  # noqa: E501
        :type: list[Question]
        """

        self._questions = questions

    @property
    def trust_zones(self):
        """Gets the trust_zones of this Component.  # noqa: E501


        :return: The trust_zones of this Component.  # noqa: E501
        :rtype: list[ComponentTrustZone]
        """
        return self._trust_zones

    @trust_zones.setter
    def trust_zones(self, trust_zones):
        """Sets the trust_zones of this Component.


        :param trust_zones: The trust_zones of this Component.  # noqa: E501
        :type: list[ComponentTrustZone]
        """

        self._trust_zones = trust_zones

    @property
    def assets(self):
        """Gets the assets of this Component.  # noqa: E501


        :return: The assets of this Component.  # noqa: E501
        :rtype: list[ComponentAsset]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this Component.


        :param assets: The assets of this Component.  # noqa: E501
        :type: list[ComponentAsset]
        """

        self._assets = assets

    @property
    def weaknesses(self):
        """Gets the weaknesses of this Component.  # noqa: E501


        :return: The weaknesses of this Component.  # noqa: E501
        :rtype: list[ComponentWeakness]
        """
        return self._weaknesses

    @weaknesses.setter
    def weaknesses(self, weaknesses):
        """Sets the weaknesses of this Component.


        :param weaknesses: The weaknesses of this Component.  # noqa: E501
        :type: list[ComponentWeakness]
        """

        self._weaknesses = weaknesses

    @property
    def controls(self):
        """Gets the controls of this Component.  # noqa: E501


        :return: The controls of this Component.  # noqa: E501
        :rtype: list[ComponentControl]
        """
        return self._controls

    @controls.setter
    def controls(self, controls):
        """Sets the controls of this Component.


        :param controls: The controls of this Component.  # noqa: E501
        :type: list[ComponentControl]
        """

        self._controls = controls

    @property
    def usecases(self):
        """Gets the usecases of this Component.  # noqa: E501


        :return: The usecases of this Component.  # noqa: E501
        :rtype: list[ComponentUseCase]
        """
        return self._usecases

    @usecases.setter
    def usecases(self, usecases):
        """Sets the usecases of this Component.


        :param usecases: The usecases of this Component.  # noqa: E501
        :type: list[ComponentUseCase]
        """

        self._usecases = usecases

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
        if issubclass(Component, dict):
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
        if not isinstance(other, Component):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other