"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pfruck_contabo
from pfruck_contabo.model.list_image_response_data import ListImageResponseData
from pfruck_contabo.model.list_image_response_links import ListImageResponseLinks
from pfruck_contabo.model.list_user_response_pagination import ListUserResponsePagination
globals()['ListImageResponseData'] = ListImageResponseData
globals()['ListImageResponseLinks'] = ListImageResponseLinks
globals()['ListUserResponsePagination'] = ListUserResponsePagination
from pfruck_contabo.model.list_image_response import ListImageResponse


class TestListImageResponse(unittest.TestCase):
    """ListImageResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListImageResponse(self):
        """Test ListImageResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListImageResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
