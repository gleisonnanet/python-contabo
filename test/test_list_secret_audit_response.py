"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pfruck_contabo
from pfruck_contabo.model.list_secret_audit_response_links import ListSecretAuditResponseLinks
from pfruck_contabo.model.list_user_response_pagination import ListUserResponsePagination
from pfruck_contabo.model.secret_audit_response import SecretAuditResponse
globals()['ListSecretAuditResponseLinks'] = ListSecretAuditResponseLinks
globals()['ListUserResponsePagination'] = ListUserResponsePagination
globals()['SecretAuditResponse'] = SecretAuditResponse
from pfruck_contabo.model.list_secret_audit_response import ListSecretAuditResponse


class TestListSecretAuditResponse(unittest.TestCase):
    """ListSecretAuditResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListSecretAuditResponse(self):
        """Test ListSecretAuditResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListSecretAuditResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
