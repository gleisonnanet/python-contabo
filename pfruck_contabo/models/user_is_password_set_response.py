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

class UserIsPasswordSetResponse(object):
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
        'tenant_id': 'str',
        'customer_id': 'str',
        'is_password_set': 'bool'
    }

    attribute_map = {
        'tenant_id': 'tenantId',
        'customer_id': 'customerId',
        'is_password_set': 'isPasswordSet'
    }

    def __init__(self, tenant_id=None, customer_id=None, is_password_set=None):  # noqa: E501
        """UserIsPasswordSetResponse - a model defined in Swagger"""  # noqa: E501
        self._tenant_id = None
        self._customer_id = None
        self._is_password_set = None
        self.discriminator = None
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if customer_id is not None:
            self.customer_id = customer_id
        if is_password_set is not None:
            self.is_password_set = is_password_set

    @property
    def tenant_id(self):
        """Gets the tenant_id of this UserIsPasswordSetResponse.  # noqa: E501

        Your customer tenant id  # noqa: E501

        :return: The tenant_id of this UserIsPasswordSetResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this UserIsPasswordSetResponse.

        Your customer tenant id  # noqa: E501

        :param tenant_id: The tenant_id of this UserIsPasswordSetResponse.  # noqa: E501
        :type: str
        """
        if tenant_id is None:
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501

        self._tenant_id = tenant_id

    @property
    def customer_id(self):
        """Gets the customer_id of this UserIsPasswordSetResponse.  # noqa: E501

        Your customer number  # noqa: E501

        :return: The customer_id of this UserIsPasswordSetResponse.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this UserIsPasswordSetResponse.

        Your customer number  # noqa: E501

        :param customer_id: The customer_id of this UserIsPasswordSetResponse.  # noqa: E501
        :type: str
        """
        if customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def is_password_set(self):
        """Gets the is_password_set of this UserIsPasswordSetResponse.  # noqa: E501

        Indicates if the user has set a password for his account  # noqa: E501

        :return: The is_password_set of this UserIsPasswordSetResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_password_set

    @is_password_set.setter
    def is_password_set(self, is_password_set):
        """Sets the is_password_set of this UserIsPasswordSetResponse.

        Indicates if the user has set a password for his account  # noqa: E501

        :param is_password_set: The is_password_set of this UserIsPasswordSetResponse.  # noqa: E501
        :type: bool
        """
        if is_password_set is None:
            raise ValueError("Invalid value for `is_password_set`, must not be `None`")  # noqa: E501

        self._is_password_set = is_password_set

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
        if issubclass(UserIsPasswordSetResponse, dict):
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
        if not isinstance(other, UserIsPasswordSetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
