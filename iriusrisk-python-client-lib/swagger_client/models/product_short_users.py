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


class ProductShortUsers(object):
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
        'revision': 'int',
        'type': 'str',
        'status': 'str',
        'priority': 'int',
        'tags': 'str',
        'workflow_state': 'str',
        'udts': 'list[Udt]',
        'users': 'list[str]'
    }

    attribute_map = {
        'ref': 'ref',
        'name': 'name',
        'revision': 'revision',
        'type': 'type',
        'status': 'status',
        'priority': 'priority',
        'tags': 'tags',
        'workflow_state': 'workflowState',
        'udts': 'udts',
        'users': 'users'
    }

    def __init__(self, ref=None, name=None, revision=1, type=None, status=None, priority=0, tags=None, workflow_state=None, udts=None, users=None):  # noqa: E501
        """ProductShortUsers - a model defined in Swagger"""  # noqa: E501

        self._ref = None
        self._name = None
        self._revision = None
        self._type = None
        self._status = None
        self._priority = None
        self._tags = None
        self._workflow_state = None
        self._udts = None
        self._users = None
        self.discriminator = None

        if ref is not None:
            self.ref = ref
        if name is not None:
            self.name = name
        if revision is not None:
            self.revision = revision
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if priority is not None:
            self.priority = priority
        if tags is not None:
            self.tags = tags
        if workflow_state is not None:
            self.workflow_state = workflow_state
        if udts is not None:
            self.udts = udts
        if users is not None:
            self.users = users

    @property
    def ref(self):
        """Gets the ref of this ProductShortUsers.  # noqa: E501


        :return: The ref of this ProductShortUsers.  # noqa: E501
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this ProductShortUsers.


        :param ref: The ref of this ProductShortUsers.  # noqa: E501
        :type: str
        """

        self._ref = ref

    @property
    def name(self):
        """Gets the name of this ProductShortUsers.  # noqa: E501


        :return: The name of this ProductShortUsers.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductShortUsers.


        :param name: The name of this ProductShortUsers.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def revision(self):
        """Gets the revision of this ProductShortUsers.  # noqa: E501


        :return: The revision of this ProductShortUsers.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this ProductShortUsers.


        :param revision: The revision of this ProductShortUsers.  # noqa: E501
        :type: int
        """

        self._revision = revision

    @property
    def type(self):
        """Gets the type of this ProductShortUsers.  # noqa: E501


        :return: The type of this ProductShortUsers.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProductShortUsers.


        :param type: The type of this ProductShortUsers.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def status(self):
        """Gets the status of this ProductShortUsers.  # noqa: E501


        :return: The status of this ProductShortUsers.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProductShortUsers.


        :param status: The status of this ProductShortUsers.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def priority(self):
        """Gets the priority of this ProductShortUsers.  # noqa: E501


        :return: The priority of this ProductShortUsers.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ProductShortUsers.


        :param priority: The priority of this ProductShortUsers.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def tags(self):
        """Gets the tags of this ProductShortUsers.  # noqa: E501


        :return: The tags of this ProductShortUsers.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ProductShortUsers.


        :param tags: The tags of this ProductShortUsers.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def workflow_state(self):
        """Gets the workflow_state of this ProductShortUsers.  # noqa: E501


        :return: The workflow_state of this ProductShortUsers.  # noqa: E501
        :rtype: str
        """
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, workflow_state):
        """Sets the workflow_state of this ProductShortUsers.


        :param workflow_state: The workflow_state of this ProductShortUsers.  # noqa: E501
        :type: str
        """

        self._workflow_state = workflow_state

    @property
    def udts(self):
        """Gets the udts of this ProductShortUsers.  # noqa: E501


        :return: The udts of this ProductShortUsers.  # noqa: E501
        :rtype: list[Udt]
        """
        return self._udts

    @udts.setter
    def udts(self, udts):
        """Sets the udts of this ProductShortUsers.


        :param udts: The udts of this ProductShortUsers.  # noqa: E501
        :type: list[Udt]
        """

        self._udts = udts

    @property
    def users(self):
        """Gets the users of this ProductShortUsers.  # noqa: E501


        :return: The users of this ProductShortUsers.  # noqa: E501
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this ProductShortUsers.


        :param users: The users of this ProductShortUsers.  # noqa: E501
        :type: list[str]
        """

        self._users = users

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
        if issubclass(ProductShortUsers, dict):
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
        if not isinstance(other, ProductShortUsers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
