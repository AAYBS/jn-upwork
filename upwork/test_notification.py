import datetime as dt
import unittest
from .notification import Job, Config, UpworkClient


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
        self.job = Job(
          "Expert", dt.date(2001, 1, 1), "developers", "…",
          "Lead Android Developer",
          "https://www.upwork.com/job/test",
        )

    def test_init(self):
        self.assertEqual(self.job.budget, "Expert")
        self.assertEqual(self.job.date, dt.date(2001, 1, 1))

    def test_job_info(self):
        self.assertEqual(str(self.job),
          "New job: Lead Android Developer \nType: developers\n" +\
          "Budget : Expert $ \nCreated on: 2001-01-01 " +\
          "Informations: … \nLink: https://www.upwork.com/job/test"
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
