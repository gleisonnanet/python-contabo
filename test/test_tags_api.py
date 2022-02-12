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
from pfruck_contabo.api.tags_api import TagsApi  # noqa: E501
from pfruck_contabo.rest import ApiException


class TestTagsApi(unittest.TestCase):
    """TagsApi unit test stubs"""

    def setUp(self):
        self.api = TagsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_tag(self):
        """Test case for create_tag

        Create a new tag  # noqa: E501
        """
        pass

    def test_delete_tag(self):
        """Test case for delete_tag

        Delete existing tag by id  # noqa: E501
        """
        pass

    def test_retrieve_tag(self):
        """Test case for retrieve_tag

        Get specific tag by id  # noqa: E501
        """
        pass

    def test_retrieve_tag_list(self):
        """Test case for retrieve_tag_list

        List tags  # noqa: E501
        """
        pass

    def test_update_tag(self):
        """Test case for update_tag

        Update specific tag by id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
