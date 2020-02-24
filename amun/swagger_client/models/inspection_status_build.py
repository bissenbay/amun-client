# coding: utf-8

"""
    Amun API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.6.0-dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from amun.swagger_client.configuration import Configuration


class InspectionStatusBuild(object):
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
        'container': 'str',
        'exit_code': 'int',
        'finished_at': 'str',
        'reason': 'str',
        'started_at': 'str',
        'state': 'str'
    }

    attribute_map = {
        'container': 'container',
        'exit_code': 'exit_code',
        'finished_at': 'finished_at',
        'reason': 'reason',
        'started_at': 'started_at',
        'state': 'state'
    }

    def __init__(self, container=None, exit_code=None, finished_at=None, reason=None, started_at=None, state=None, local_vars_configuration=None):  # noqa: E501
        """InspectionStatusBuild - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._container = None
        self._exit_code = None
        self._finished_at = None
        self._reason = None
        self._started_at = None
        self._state = None
        self.discriminator = None

        self.container = container
        self.exit_code = exit_code
        self.finished_at = finished_at
        self.reason = reason
        self.started_at = started_at
        self.state = state

    @property
    def container(self):
        """Gets the container of this InspectionStatusBuild.  # noqa: E501

        SHA of container image in which the inspection is done.  # noqa: E501

        :return: The container of this InspectionStatusBuild.  # noqa: E501
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this InspectionStatusBuild.

        SHA of container image in which the inspection is done.  # noqa: E501

        :param container: The container of this InspectionStatusBuild.  # noqa: E501
        :type: str
        """

        self._container = container

    @property
    def exit_code(self):
        """Gets the exit_code of this InspectionStatusBuild.  # noqa: E501

        Return code of the process performing inspection (user supplied script return value).   # noqa: E501

        :return: The exit_code of this InspectionStatusBuild.  # noqa: E501
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """Sets the exit_code of this InspectionStatusBuild.

        Return code of the process performing inspection (user supplied script return value).   # noqa: E501

        :param exit_code: The exit_code of this InspectionStatusBuild.  # noqa: E501
        :type: int
        """

        self._exit_code = exit_code

    @property
    def finished_at(self):
        """Gets the finished_at of this InspectionStatusBuild.  # noqa: E501

        Datetime in ISO format informing about when the inspection has finished.   # noqa: E501

        :return: The finished_at of this InspectionStatusBuild.  # noqa: E501
        :rtype: str
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this InspectionStatusBuild.

        Datetime in ISO format informing about when the inspection has finished.   # noqa: E501

        :param finished_at: The finished_at of this InspectionStatusBuild.  # noqa: E501
        :type: str
        """

        self._finished_at = finished_at

    @property
    def reason(self):
        """Gets the reason of this InspectionStatusBuild.  # noqa: E501

        Reasoning on finished inspection run.  # noqa: E501

        :return: The reason of this InspectionStatusBuild.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this InspectionStatusBuild.

        Reasoning on finished inspection run.  # noqa: E501

        :param reason: The reason of this InspectionStatusBuild.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def started_at(self):
        """Gets the started_at of this InspectionStatusBuild.  # noqa: E501

        Datetime in ISO format informing about when the inspection has started.   # noqa: E501

        :return: The started_at of this InspectionStatusBuild.  # noqa: E501
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this InspectionStatusBuild.

        Datetime in ISO format informing about when the inspection has started.   # noqa: E501

        :param started_at: The started_at of this InspectionStatusBuild.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and started_at is None:  # noqa: E501
            raise ValueError("Invalid value for `started_at`, must not be `None`")  # noqa: E501

        self._started_at = started_at

    @property
    def state(self):
        """Gets the state of this InspectionStatusBuild.  # noqa: E501


        :return: The state of this InspectionStatusBuild.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InspectionStatusBuild.


        :param state: The state of this InspectionStatusBuild.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

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
        if not isinstance(other, InspectionStatusBuild):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InspectionStatusBuild):
            return True

        return self.to_dict() != other.to_dict()