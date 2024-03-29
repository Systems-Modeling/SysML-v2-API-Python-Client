# coding: utf-8

"""
    SysML v2 API and Services

    REST/HTTP binding (PSM) for the SysML v2 standard API.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from sysml_v2_api_client.configuration import Configuration


class Branch(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'type': 'str',
        'head': 'BranchHead',
        'name': 'str',
        'owning_project': 'BranchOwningProject',
        'referenced_commit': 'BranchHead',
        'timestamp': 'datetime'
    }

    attribute_map = {
        'id': '@id',
        'type': '@type',
        'head': 'head',
        'name': 'name',
        'owning_project': 'owningProject',
        'referenced_commit': 'referencedCommit',
        'timestamp': 'timestamp'
    }

    def __init__(self, id=None, type=None, head=None, name=None, owning_project=None, referenced_commit=None, timestamp=None, local_vars_configuration=None):  # noqa: E501
        """Branch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._head = None
        self._name = None
        self._owning_project = None
        self._referenced_commit = None
        self._timestamp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if head is not None:
            self.head = head
        if name is not None:
            self.name = name
        if owning_project is not None:
            self.owning_project = owning_project
        if referenced_commit is not None:
            self.referenced_commit = referenced_commit
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def id(self):
        """Gets the id of this Branch.  # noqa: E501


        :return: The id of this Branch.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Branch.


        :param id: The id of this Branch.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Branch.  # noqa: E501


        :return: The type of this Branch.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Branch.


        :param type: The type of this Branch.  # noqa: E501
        :type: str
        """
        allowed_values = ["Branch"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def head(self):
        """Gets the head of this Branch.  # noqa: E501


        :return: The head of this Branch.  # noqa: E501
        :rtype: BranchHead
        """
        return self._head

    @head.setter
    def head(self, head):
        """Sets the head of this Branch.


        :param head: The head of this Branch.  # noqa: E501
        :type: BranchHead
        """

        self._head = head

    @property
    def name(self):
        """Gets the name of this Branch.  # noqa: E501


        :return: The name of this Branch.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Branch.


        :param name: The name of this Branch.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def owning_project(self):
        """Gets the owning_project of this Branch.  # noqa: E501


        :return: The owning_project of this Branch.  # noqa: E501
        :rtype: BranchOwningProject
        """
        return self._owning_project

    @owning_project.setter
    def owning_project(self, owning_project):
        """Sets the owning_project of this Branch.


        :param owning_project: The owning_project of this Branch.  # noqa: E501
        :type: BranchOwningProject
        """

        self._owning_project = owning_project

    @property
    def referenced_commit(self):
        """Gets the referenced_commit of this Branch.  # noqa: E501


        :return: The referenced_commit of this Branch.  # noqa: E501
        :rtype: BranchHead
        """
        return self._referenced_commit

    @referenced_commit.setter
    def referenced_commit(self, referenced_commit):
        """Sets the referenced_commit of this Branch.


        :param referenced_commit: The referenced_commit of this Branch.  # noqa: E501
        :type: BranchHead
        """

        self._referenced_commit = referenced_commit

    @property
    def timestamp(self):
        """Gets the timestamp of this Branch.  # noqa: E501


        :return: The timestamp of this Branch.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Branch.


        :param timestamp: The timestamp of this Branch.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Branch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Branch):
            return True

        return self.to_dict() != other.to_dict()
