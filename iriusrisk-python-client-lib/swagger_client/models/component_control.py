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


class ComponentControl(object):
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
        'issue_id': 'str',
        'platform': 'str',
        'cost': 'int',
        'risk': 'int',
        'state': 'str',
        'owner': 'str',
        'desc': 'str',
        'source': 'str',
        'mitigation': 'str',
        'library': 'str',
        'implementations': 'list[Implementation]',
        'threats': 'list[ThreatNameAndRef]',
        'weaknesses': 'list[WeaknessNameAndRef]',
        'references': 'list[Reference]',
        'standards': 'list[Standard]',
        'udts': 'list[Udt]',
        'test': 'Test'
    }

    attribute_map = {
        'ref': 'ref',
        'name': 'name',
        'issue_id': 'issueId',
        'platform': 'platform',
        'cost': 'cost',
        'risk': 'risk',
        'state': 'state',
        'owner': 'owner',
        'desc': 'desc',
        'source': 'source',
        'mitigation': 'mitigation',
        'library': 'library',
        'implementations': 'implementations',
        'threats': 'threats',
        'weaknesses': 'weaknesses',
        'references': 'references',
        'standards': 'standards',
        'udts': 'udts',
        'test': 'test'
    }

    def __init__(self, ref=None, name=None, issue_id=None, platform=None, cost=None, risk=None, state=None, owner=None, desc=None, source=None, mitigation=None, library=None, implementations=None, threats=None, weaknesses=None, references=None, standards=None, udts=None, test=None):  # noqa: E501
        """ComponentControl - a model defined in Swagger"""  # noqa: E501

        self._ref = None
        self._name = None
        self._issue_id = None
        self._platform = None
        self._cost = None
        self._risk = None
        self._state = None
        self._owner = None
        self._desc = None
        self._source = None
        self._mitigation = None
        self._library = None
        self._implementations = None
        self._threats = None
        self._weaknesses = None
        self._references = None
        self._standards = None
        self._udts = None
        self._test = None
        self.discriminator = None

        if ref is not None:
            self.ref = ref
        if name is not None:
            self.name = name
        if issue_id is not None:
            self.issue_id = issue_id
        if platform is not None:
            self.platform = platform
        if cost is not None:
            self.cost = cost
        if risk is not None:
            self.risk = risk
        if state is not None:
            self.state = state
        if owner is not None:
            self.owner = owner
        if desc is not None:
            self.desc = desc
        if source is not None:
            self.source = source
        if mitigation is not None:
            self.mitigation = mitigation
        if library is not None:
            self.library = library
        if implementations is not None:
            self.implementations = implementations
        if threats is not None:
            self.threats = threats
        if weaknesses is not None:
            self.weaknesses = weaknesses
        if references is not None:
            self.references = references
        if standards is not None:
            self.standards = standards
        if udts is not None:
            self.udts = udts
        if test is not None:
            self.test = test

    @property
    def ref(self):
        """Gets the ref of this ComponentControl.  # noqa: E501


        :return: The ref of this ComponentControl.  # noqa: E501
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this ComponentControl.


        :param ref: The ref of this ComponentControl.  # noqa: E501
        :type: str
        """

        self._ref = ref

    @property
    def name(self):
        """Gets the name of this ComponentControl.  # noqa: E501


        :return: The name of this ComponentControl.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentControl.


        :param name: The name of this ComponentControl.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def issue_id(self):
        """Gets the issue_id of this ComponentControl.  # noqa: E501


        :return: The issue_id of this ComponentControl.  # noqa: E501
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        """Sets the issue_id of this ComponentControl.


        :param issue_id: The issue_id of this ComponentControl.  # noqa: E501
        :type: str
        """

        self._issue_id = issue_id

    @property
    def platform(self):
        """Gets the platform of this ComponentControl.  # noqa: E501


        :return: The platform of this ComponentControl.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this ComponentControl.


        :param platform: The platform of this ComponentControl.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def cost(self):
        """Gets the cost of this ComponentControl.  # noqa: E501


        :return: The cost of this ComponentControl.  # noqa: E501
        :rtype: int
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this ComponentControl.


        :param cost: The cost of this ComponentControl.  # noqa: E501
        :type: int
        """

        self._cost = cost

    @property
    def risk(self):
        """Gets the risk of this ComponentControl.  # noqa: E501


        :return: The risk of this ComponentControl.  # noqa: E501
        :rtype: int
        """
        return self._risk

    @risk.setter
    def risk(self, risk):
        """Sets the risk of this ComponentControl.


        :param risk: The risk of this ComponentControl.  # noqa: E501
        :type: int
        """

        self._risk = risk

    @property
    def state(self):
        """Gets the state of this ComponentControl.  # noqa: E501


        :return: The state of this ComponentControl.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ComponentControl.


        :param state: The state of this ComponentControl.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def owner(self):
        """Gets the owner of this ComponentControl.  # noqa: E501


        :return: The owner of this ComponentControl.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ComponentControl.


        :param owner: The owner of this ComponentControl.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def desc(self):
        """Gets the desc of this ComponentControl.  # noqa: E501


        :return: The desc of this ComponentControl.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this ComponentControl.


        :param desc: The desc of this ComponentControl.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def source(self):
        """Gets the source of this ComponentControl.  # noqa: E501


        :return: The source of this ComponentControl.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ComponentControl.


        :param source: The source of this ComponentControl.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def mitigation(self):
        """Gets the mitigation of this ComponentControl.  # noqa: E501


        :return: The mitigation of this ComponentControl.  # noqa: E501
        :rtype: str
        """
        return self._mitigation

    @mitigation.setter
    def mitigation(self, mitigation):
        """Sets the mitigation of this ComponentControl.


        :param mitigation: The mitigation of this ComponentControl.  # noqa: E501
        :type: str
        """

        self._mitigation = mitigation

    @property
    def library(self):
        """Gets the library of this ComponentControl.  # noqa: E501

        Reference of the Library  # noqa: E501

        :return: The library of this ComponentControl.  # noqa: E501
        :rtype: str
        """
        return self._library

    @library.setter
    def library(self, library):
        """Sets the library of this ComponentControl.

        Reference of the Library  # noqa: E501

        :param library: The library of this ComponentControl.  # noqa: E501
        :type: str
        """

        self._library = library

    @property
    def implementations(self):
        """Gets the implementations of this ComponentControl.  # noqa: E501


        :return: The implementations of this ComponentControl.  # noqa: E501
        :rtype: list[Implementation]
        """
        return self._implementations

    @implementations.setter
    def implementations(self, implementations):
        """Sets the implementations of this ComponentControl.


        :param implementations: The implementations of this ComponentControl.  # noqa: E501
        :type: list[Implementation]
        """

        self._implementations = implementations

    @property
    def threats(self):
        """Gets the threats of this ComponentControl.  # noqa: E501


        :return: The threats of this ComponentControl.  # noqa: E501
        :rtype: list[ThreatNameAndRef]
        """
        return self._threats

    @threats.setter
    def threats(self, threats):
        """Sets the threats of this ComponentControl.


        :param threats: The threats of this ComponentControl.  # noqa: E501
        :type: list[ThreatNameAndRef]
        """

        self._threats = threats

    @property
    def weaknesses(self):
        """Gets the weaknesses of this ComponentControl.  # noqa: E501


        :return: The weaknesses of this ComponentControl.  # noqa: E501
        :rtype: list[WeaknessNameAndRef]
        """
        return self._weaknesses

    @weaknesses.setter
    def weaknesses(self, weaknesses):
        """Sets the weaknesses of this ComponentControl.


        :param weaknesses: The weaknesses of this ComponentControl.  # noqa: E501
        :type: list[WeaknessNameAndRef]
        """

        self._weaknesses = weaknesses

    @property
    def references(self):
        """Gets the references of this ComponentControl.  # noqa: E501


        :return: The references of this ComponentControl.  # noqa: E501
        :rtype: list[Reference]
        """
        return self._references

    @references.setter
    def references(self, references):
        """Sets the references of this ComponentControl.


        :param references: The references of this ComponentControl.  # noqa: E501
        :type: list[Reference]
        """

        self._references = references

    @property
    def standards(self):
        """Gets the standards of this ComponentControl.  # noqa: E501


        :return: The standards of this ComponentControl.  # noqa: E501
        :rtype: list[Standard]
        """
        return self._standards

    @standards.setter
    def standards(self, standards):
        """Sets the standards of this ComponentControl.


        :param standards: The standards of this ComponentControl.  # noqa: E501
        :type: list[Standard]
        """

        self._standards = standards

    @property
    def udts(self):
        """Gets the udts of this ComponentControl.  # noqa: E501


        :return: The udts of this ComponentControl.  # noqa: E501
        :rtype: list[Udt]
        """
        return self._udts

    @udts.setter
    def udts(self, udts):
        """Sets the udts of this ComponentControl.


        :param udts: The udts of this ComponentControl.  # noqa: E501
        :type: list[Udt]
        """

        self._udts = udts

    @property
    def test(self):
        """Gets the test of this ComponentControl.  # noqa: E501


        :return: The test of this ComponentControl.  # noqa: E501
        :rtype: Test
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this ComponentControl.


        :param test: The test of this ComponentControl.  # noqa: E501
        :type: Test
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
        if issubclass(ComponentControl, dict):
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
        if not isinstance(other, ComponentControl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
