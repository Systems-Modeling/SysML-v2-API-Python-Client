# coding: utf-8

"""
    SysML v2 API and Services

    REST/HTTP binding (PSM) for the SysML v2 standard API.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import sysml_v2_api_client
from sysml_v2_api_client.models.element import Element  # noqa: E501
from sysml_v2_api_client.rest import ApiException

class TestElement(unittest.TestCase):
    """Element unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Element
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sysml_v2_api_client.models.element.Element()  # noqa: E501
        if include_optional :
            return Element(
                id = '0', 
                type = '0', 
                identifier = '0'
            )
        else :
            return Element(
        )

    def testElement(self):
        """Test Element"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
