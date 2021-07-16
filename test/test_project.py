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
from sysml_v2_api_client.models.project import Project  # noqa: E501
from sysml_v2_api_client.rest import ApiException

class TestProject(unittest.TestCase):
    """Project unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Project
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sysml_v2_api_client.models.project.Project()  # noqa: E501
        if include_optional :
            return Project(
                id = '0', 
                type = 'Project', 
                default_branch = sysml_v2_api_client.models.project_default_branch.Project_defaultBranch(
                    @id = '0', ), 
                description = '0', 
                name = '0'
            )
        else :
            return Project(
        )

    def testProject(self):
        """Test Project"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
