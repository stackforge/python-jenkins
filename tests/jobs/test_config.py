from mock import patch

import jenkins
from tests.jobs.base import JenkinsJobsTestBase


class JenkinsGetJobConfigTest(JenkinsJobsTestBase):

    @patch.object(jenkins.Jenkins, 'jenkins_open')
    def test_encodes_job_name(self, jenkins_mock):
        self.j.get_job_config(u'Test Job')

        self.assertEqual(
            jenkins_mock.call_args[0][0].url,
            u'http://example.com/job/Test%20Job/config.xml')
        self._check_requests(jenkins_mock.call_args_list)
