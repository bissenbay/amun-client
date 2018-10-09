# coding: utf-8

"""
    Amun API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InspectionSpecificationPython(object):
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
        'requirements': 'object',
        'requirements_locked': 'object'
    }

    attribute_map = {
        'requirements': 'requirements',
        'requirements_locked': 'requirements_locked'
    }

    def __init__(self, requirements=None, requirements_locked=None):  # noqa: E501
        """InspectionSpecificationPython - a model defined in Swagger"""  # noqa: E501

        self._requirements = None
        self._requirements_locked = None
        self.discriminator = None

        self.requirements = requirements
        self.requirements_locked = requirements_locked

    @property
    def requirements(self):
        """Gets the requirements of this InspectionSpecificationPython.  # noqa: E501

        Pipfile stating software stack (direct dependencies) of an application.  # noqa: E501

        :return: The requirements of this InspectionSpecificationPython.  # noqa: E501
        :rtype: object
        """
        return self._requirements

    @requirements.setter
    def requirements(self, requirements):
        """Sets the requirements of this InspectionSpecificationPython.

        Pipfile stating software stack (direct dependencies) of an application.  # noqa: E501

        :param requirements: The requirements of this InspectionSpecificationPython.  # noqa: E501
        :type: object
        """
        if requirements is None:
            raise ValueError("Invalid value for `requirements`, must not be `None`")  # noqa: E501

        self._requirements = requirements

    @property
    def requirements_locked(self):
        """Gets the requirements_locked of this InspectionSpecificationPython.  # noqa: E501

        Pipfile.lock with fully pinned down and resolved software stack.  # noqa: E501

        :return: The requirements_locked of this InspectionSpecificationPython.  # noqa: E501
        :rtype: object
        """
        return self._requirements_locked

    @requirements_locked.setter
    def requirements_locked(self, requirements_locked):
        """Sets the requirements_locked of this InspectionSpecificationPython.

        Pipfile.lock with fully pinned down and resolved software stack.  # noqa: E501

        :param requirements_locked: The requirements_locked of this InspectionSpecificationPython.  # noqa: E501
        :type: object
        """
        if requirements_locked is None:
            raise ValueError("Invalid value for `requirements_locked`, must not be `None`")  # noqa: E501

        self._requirements_locked = requirements_locked

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
        if issubclass(InspectionSpecificationPython, dict):
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
        if not isinstance(other, InspectionSpecificationPython):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
