"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pfruck_contabo
from pfruck_contabo.model.links import Links
from pfruck_contabo.model.list_instances_response_data import ListInstancesResponseData
from pfruck_contabo.model.pagination_meta import PaginationMeta
globals()['Links'] = Links
globals()['ListInstancesResponseData'] = ListInstancesResponseData
globals()['PaginationMeta'] = PaginationMeta
from pfruck_contabo.model.list_instances_response import ListInstancesResponse


class TestListInstancesResponse(unittest.TestCase):
    """ListInstancesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListInstancesResponse(self):
        """Test ListInstancesResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListInstancesResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
