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


class Commit(object):
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
        'change': 'list[DataVersion]',
        'owning_project': 'BranchOwningProject',
        'previous_commit': 'BranchHead'
    }

    attribute_map = {
        'id': '@id',
        'type': '@type',
        'change': 'change',
        'owning_project': 'owningProject',
        'previous_commit': 'previousCommit'
    }

    def __init__(self, id=None, type=None, change=None, owning_project=None, previous_commit=None, local_vars_configuration=None):  # noqa: E501
        """Commit - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._change = None
        self._owning_project = None
        self._previous_commit = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if change is not None:
            self.change = change
        if owning_project is not None:
            self.owning_project = owning_project
        if previous_commit is not None:
            self.previous_commit = previous_commit

    @property
    def id(self):
        """Gets the id of this Commit.  # noqa: E501


        :return: The id of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Commit.


        :param id: The id of this Commit.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Commit.  # noqa: E501


        :return: The type of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Commit.


        :param type: The type of this Commit.  # noqa: E501
        :type: str
        """
        allowed_values = ["Commit"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def change(self):
        """Gets the change of this Commit.  # noqa: E501


        :return: The change of this Commit.  # noqa: E501
        :rtype: list[DataVersion]
        """
        return self._change

    @change.setter
    def change(self, change):
        """Sets the change of this Commit.


        :param change: The change of this Commit.  # noqa: E501
        :type: list[DataVersion]
        """

        self._change = change

    @property
    def owning_project(self):
        """Gets the owning_project of this Commit.  # noqa: E501


        :return: The owning_project of this Commit.  # noqa: E501
        :rtype: BranchOwningProject
        """
        return self._owning_project

    @owning_project.setter
    def owning_project(self, owning_project):
        """Sets the owning_project of this Commit.


        :param owning_project: The owning_project of this Commit.  # noqa: E501
        :type: BranchOwningProject
        """

        self._owning_project = owning_project

    @property
    def previous_commit(self):
        """Gets the previous_commit of this Commit.  # noqa: E501


        :return: The previous_commit of this Commit.  # noqa: E501
        :rtype: BranchHead
        """
        return self._previous_commit

    @previous_commit.setter
    def previous_commit(self, previous_commit):
        """Sets the previous_commit of this Commit.


        :param previous_commit: The previous_commit of this Commit.  # noqa: E501
        :type: BranchHead
        """

        self._previous_commit = previous_commit

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
        if not isinstance(other, Commit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Commit):
            return True

        return self.to_dict() != other.to_dict()
