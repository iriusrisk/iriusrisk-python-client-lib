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


class LibraryThreat(object):
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
        'risk': 'int',
        'inherent_risk': 'int',
        'projected_risk': 'int',
        'risk_rating': 'RiskRating',
        'references': 'list[Reference]',
        'weaknesses': 'list[ThreatWeakness]',
        'controls': 'list[ThreatControl]',
        'udts': 'list[Udt]'
    }

    attribute_map = {
        'ref': 'ref',
        'name': 'name',
        'desc': 'desc',
        'mitigation': 'mitigation',
        'risk': 'risk',
        'inherent_risk': 'inherentRisk',
        'projected_risk': 'projectedRisk',
        'risk_rating': 'riskRating',
        'references': 'references',
        'weaknesses': 'weaknesses',
        'controls': 'controls',
        'udts': 'udts'
    }

    def __init__(self, ref=None, name=None, desc=None, mitigation=None, risk=None, inherent_risk=None, projected_risk=None, risk_rating=None, references=None, weaknesses=None, controls=None, udts=None):  # noqa: E501
        """LibraryThreat - a model defined in Swagger"""  # noqa: E501

        self._ref = None
        self._name = None
        self._desc = None
        self._mitigation = None
        self._risk = None
        self._inherent_risk = None
        self._projected_risk = None
        self._risk_rating = None
        self._references = None
        self._weaknesses = None
        self._controls = None
        self._udts = None
        self.discriminator = None

        if ref is not None:
            self.ref = ref
        if name is not None:
            self.name = name
        if desc is not None:
            self.desc = desc
        if mitigation is not None:
            self.mitigation = mitigation
        if risk is not None:
            self.risk = risk
        if inherent_risk is not None:
            self.inherent_risk = inherent_risk
        if projected_risk is not None:
            self.projected_risk = projected_risk
        if risk_rating is not None:
            self.risk_rating = risk_rating
        if references is not None:
            self.references = references
        if weaknesses is not None:
            self.weaknesses = weaknesses
        if controls is not None:
            self.controls = controls
        if udts is not None:
            self.udts = udts

    @property
    def ref(self):
        """Gets the ref of this LibraryThreat.  # noqa: E501


        :return: The ref of this LibraryThreat.  # noqa: E501
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this LibraryThreat.


        :param ref: The ref of this LibraryThreat.  # noqa: E501
        :type: str
        """

        self._ref = ref

    @property
    def name(self):
        """Gets the name of this LibraryThreat.  # noqa: E501


        :return: The name of this LibraryThreat.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LibraryThreat.


        :param name: The name of this LibraryThreat.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def desc(self):
        """Gets the desc of this LibraryThreat.  # noqa: E501


        :return: The desc of this LibraryThreat.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this LibraryThreat.


        :param desc: The desc of this LibraryThreat.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def mitigation(self):
        """Gets the mitigation of this LibraryThreat.  # noqa: E501


        :return: The mitigation of this LibraryThreat.  # noqa: E501
        :rtype: int
        """
        return self._mitigation

    @mitigation.setter
    def mitigation(self, mitigation):
        """Sets the mitigation of this LibraryThreat.


        :param mitigation: The mitigation of this LibraryThreat.  # noqa: E501
        :type: int
        """

        self._mitigation = mitigation

    @property
    def risk(self):
        """Gets the risk of this LibraryThreat.  # noqa: E501


        :return: The risk of this LibraryThreat.  # noqa: E501
        :rtype: int
        """
        return self._risk

    @risk.setter
    def risk(self, risk):
        """Sets the risk of this LibraryThreat.


        :param risk: The risk of this LibraryThreat.  # noqa: E501
        :type: int
        """

        self._risk = risk

    @property
    def inherent_risk(self):
        """Gets the inherent_risk of this LibraryThreat.  # noqa: E501


        :return: The inherent_risk of this LibraryThreat.  # noqa: E501
        :rtype: int
        """
        return self._inherent_risk

    @inherent_risk.setter
    def inherent_risk(self, inherent_risk):
        """Sets the inherent_risk of this LibraryThreat.


        :param inherent_risk: The inherent_risk of this LibraryThreat.  # noqa: E501
        :type: int
        """

        self._inherent_risk = inherent_risk

    @property
    def projected_risk(self):
        """Gets the projected_risk of this LibraryThreat.  # noqa: E501


        :return: The projected_risk of this LibraryThreat.  # noqa: E501
        :rtype: int
        """
        return self._projected_risk

    @projected_risk.setter
    def projected_risk(self, projected_risk):
        """Sets the projected_risk of this LibraryThreat.


        :param projected_risk: The projected_risk of this LibraryThreat.  # noqa: E501
        :type: int
        """

        self._projected_risk = projected_risk

    @property
    def risk_rating(self):
        """Gets the risk_rating of this LibraryThreat.  # noqa: E501


        :return: The risk_rating of this LibraryThreat.  # noqa: E501
        :rtype: RiskRating
        """
        return self._risk_rating

    @risk_rating.setter
    def risk_rating(self, risk_rating):
        """Sets the risk_rating of this LibraryThreat.


        :param risk_rating: The risk_rating of this LibraryThreat.  # noqa: E501
        :type: RiskRating
        """

        self._risk_rating = risk_rating

    @property
    def references(self):
        """Gets the references of this LibraryThreat.  # noqa: E501


        :return: The references of this LibraryThreat.  # noqa: E501
        :rtype: list[Reference]
        """
        return self._references

    @references.setter
    def references(self, references):
        """Sets the references of this LibraryThreat.


        :param references: The references of this LibraryThreat.  # noqa: E501
        :type: list[Reference]
        """

        self._references = references

    @property
    def weaknesses(self):
        """Gets the weaknesses of this LibraryThreat.  # noqa: E501


        :return: The weaknesses of this LibraryThreat.  # noqa: E501
        :rtype: list[ThreatWeakness]
        """
        return self._weaknesses

    @weaknesses.setter
    def weaknesses(self, weaknesses):
        """Sets the weaknesses of this LibraryThreat.


        :param weaknesses: The weaknesses of this LibraryThreat.  # noqa: E501
        :type: list[ThreatWeakness]
        """

        self._weaknesses = weaknesses

    @property
    def controls(self):
        """Gets the controls of this LibraryThreat.  # noqa: E501


        :return: The controls of this LibraryThreat.  # noqa: E501
        :rtype: list[ThreatControl]
        """
        return self._controls

    @controls.setter
    def controls(self, controls):
        """Sets the controls of this LibraryThreat.


        :param controls: The controls of this LibraryThreat.  # noqa: E501
        :type: list[ThreatControl]
        """

        self._controls = controls

    @property
    def udts(self):
        """Gets the udts of this LibraryThreat.  # noqa: E501


        :return: The udts of this LibraryThreat.  # noqa: E501
        :rtype: list[Udt]
        """
        return self._udts

    @udts.setter
    def udts(self, udts):
        """Sets the udts of this LibraryThreat.


        :param udts: The udts of this LibraryThreat.  # noqa: E501
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
        if issubclass(LibraryThreat, dict):
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
        if not isinstance(other, LibraryThreat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
