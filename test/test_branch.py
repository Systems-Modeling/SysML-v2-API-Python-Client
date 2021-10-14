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
from sysml_v2_api_client.models.branch import Branch  # noqa: E501
from sysml_v2_api_client.rest import ApiException

class TestBranch(unittest.TestCase):
    """Branch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Branch
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sysml_v2_api_client.models.branch.Branch()  # noqa: E501
        if include_optional :
            return Branch(
                id = '0', 
                type = 'Branch', 
                head = sysml_v2_api_client.models.branch_head.Branch_head(
                    @id = '0', ), 
                name = '0', 
                owning_project = sysml_v2_api_client.models.branch_owning_project.Branch_owningProject(
                    @id = '0', ), 
                referenced_commit = sysml_v2_api_client.models.branch_head.Branch_head(
                    @id = '0', ), 
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return Branch(
        )

    def testBranch(self):
        """Test Branch"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
