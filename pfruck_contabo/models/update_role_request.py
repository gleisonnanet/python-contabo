# coding: utf-8

"""
    Contabo API


    OpenAPI spec version: 1.0.0
    Contact: support@contabo.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UpdateRoleRequest(object):
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
        'api_permissions': 'list[ApiPermissionsResponse]',
        'resource_permissions': 'list[int]'
    }

    attribute_map = {
        'name': 'name',
        'api_permissions': 'apiPermissions',
        'resource_permissions': 'resourcePermissions'
    }

    def __init__(self, name=None, api_permissions=None, resource_permissions=None):  # noqa: E501
        """UpdateRoleRequest - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._api_permissions = None
        self._resource_permissions = None
        self.discriminator = None
        self.name = name
        if api_permissions is not None:
            self.api_permissions = api_permissions
        self.resource_permissions = resource_permissions

    @property
    def name(self):
        """Gets the name of this UpdateRoleRequest.  # noqa: E501

        The name of the role. There is a limit of 255 characters per role.  # noqa: E501

        :return: The name of this UpdateRoleRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateRoleRequest.

        The name of the role. There is a limit of 255 characters per role.  # noqa: E501

        :param name: The name of this UpdateRoleRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def api_permissions(self):
        """Gets the api_permissions of this UpdateRoleRequest.  # noqa: E501


        :return: The api_permissions of this UpdateRoleRequest.  # noqa: E501
        :rtype: list[ApiPermissionsResponse]
        """
        return self._api_permissions

    @api_permissions.setter
    def api_permissions(self, api_permissions):
        """Sets the api_permissions of this UpdateRoleRequest.


        :param api_permissions: The api_permissions of this UpdateRoleRequest.  # noqa: E501
        :type: list[ApiPermissionsResponse]
        """

        self._api_permissions = api_permissions

    @property
    def resource_permissions(self):
        """Gets the resource_permissions of this UpdateRoleRequest.  # noqa: E501

        The IDs of tags. Only if those tags are assgined to a resource the user with that role will be able to access the resource.  # noqa: E501

        :return: The resource_permissions of this UpdateRoleRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._resource_permissions

    @resource_permissions.setter
    def resource_permissions(self, resource_permissions):
        """Sets the resource_permissions of this UpdateRoleRequest.

        The IDs of tags. Only if those tags are assgined to a resource the user with that role will be able to access the resource.  # noqa: E501

        :param resource_permissions: The resource_permissions of this UpdateRoleRequest.  # noqa: E501
        :type: list[int]
        """
        if resource_permissions is None:
            raise ValueError("Invalid value for `resource_permissions`, must not be `None`")  # noqa: E501

        self._resource_permissions = resource_permissions

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
        if issubclass(UpdateRoleRequest, dict):
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
        if not isinstance(other, UpdateRoleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
