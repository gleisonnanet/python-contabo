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
from pfruck_contabo.model.pagination_meta import PaginationMeta
from pfruck_contabo.model.tag_audit_response import TagAuditResponse
globals()['Links'] = Links
globals()['PaginationMeta'] = PaginationMeta
globals()['TagAuditResponse'] = TagAuditResponse
from pfruck_contabo.model.list_tag_audits_response import ListTagAuditsResponse


class TestListTagAuditsResponse(unittest.TestCase):
    """ListTagAuditsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListTagAuditsResponse(self):
        """Test ListTagAuditsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListTagAuditsResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
