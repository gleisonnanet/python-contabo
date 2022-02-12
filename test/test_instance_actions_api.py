# coding: utf-8

"""
    Contabo API


    OpenAPI spec version: 1.0.0
    Contact: support@contabo.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import pfruck_contabo
from pfruck_contabo.api.instance_actions_api import InstanceActionsApi  # noqa: E501
from pfruck_contabo.rest import ApiException


class TestInstanceActionsApi(unittest.TestCase):
    """InstanceActionsApi unit test stubs"""

    def setUp(self):
        self.api = InstanceActionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_restart(self):
        """Test case for restart

        Restart a compute instance / resource identified by its id  # noqa: E501
        """
        pass

    def test_start(self):
        """Test case for start

        Start a compute instance / resource identified by its id  # noqa: E501
        """
        pass

    def test_stop(self):
        """Test case for stop

        Stop compute instance / resource by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
