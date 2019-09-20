import datetime as dt
import unittest
from .notification import Job, Config, UpworkClient
import json

config = Config("test_configuration.ini").config
api_key = config['upwork']['api_key']
api_secret = config['upwork']['api_key']
job_skill = config['upwork']['job_skill']
job_query = dict(
    skills=[job_skill],
    budget='[100 TO 100000]',
    duration=['week', 'month', 'ongoing']
)


class TestJob(unittest.TestCase):

    def setUp(self):
        job_string = '{"budget": "750", "category2": "Web & Mobile Development", "date_created": "2014-06-30T23:50:17+0000", ' \
            '"url": "https://www.upwork.com/job/test", "job_type": "Fixed", ' \
            '"title": "Looking for highly skilled web developer"}'
        json_object = json.loads(job_string)
        self.job = Job(json_object)

    def test_init(self):
        self.assertEqual(self.job.job_info['budget'], "750")
        self.assertEqual(dt.datetime.strptime(self.job.job_info['date_created'], '%Y-%m-%dT%H:%M:%S%z').date(), dt.date(2014, 6, 30))

    def test_job_info(self):
        self.assertEqual(str(self.job),
          "New job: Looking for highly skilled web developer \nType: Fixed\n" +\
          "Budget : 750 $ \nCreated on: 2014-06-30T23:50:17+0000 " +\
          "Informations: Web & Mobile Development \nLink: https://www.upwork.com/job/test"
        )

class TestConfig(unittest.TestCase):

    def setUp(self):
        self.config = config

    def test_init(self):
        # self.assertRaises(Exception)
        self.assertEqual(self.config['upwork']['api_key'], api_key)
        self.assertEqual(self.config['upwork']['api_secret'], api_secret)


class TestUpworkClient(unittest.TestCase):

    def setUp(self):
        self.upworkclient = UpworkClient(api_key, api_secret)

    @unittest.skip("Cannot setup because upwork.Client doesn’t exist")
    def test_search_jobs(self):
        self.assertEqual(self.upworkclient.search_jobs(job_query), "/Need to fill in here: Does Upwork has a live test job?/")
