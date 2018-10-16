import datetime as dt
import unittest
import configparser
from upwork.notifications import Job
from upwork.notifications import UpworkClient


class TestJob(unittest.TestCase):

    def setUp(self):
        self.job = Job(
          "Expert", dt.date(2001, 1, 1), "developers", "…",
          "Lead Android Developer", 
          "https://www.upwork.com/job/Lead-Android-Developer-Full-Time_~01f6da1b38a626ea53/",
        )

    def test_init(self):
        self.assertEqual(self.job.budget, "Expert")
        self.assertEqual(self.job.date, dt.date(2001, 1, 1))

    def test_jobinfo(self):
        self.assertEqual(self.job.jobinfo(),
          "New job: Lead Android Developer \nType: developers" +\
          "\nBudget : Expert $ \nCreated on: 2001-01-01 " +\
          "Informations: … \nLink: https://www.upwork.com/job/Lead-Android-Developer-Full-Time_~01f6da1b38a626ea53/"
        )


class TestUpworkClient(unittest.TestCase):

    api_key = config['uwpork']['api_key']
    api_secret = config['uwpork']['api_key']
    job_skill = config['upwork']['job_skill']
    job_query = dict(
        skills=[job_skill],
        budget='[100 TO 100000]',
        duration=['week', 'month', 'ongoing']
    )
    
    def setUp(self):
        self.upworkclient = UpworkClient(api_key, api_secret)

    def test_search_jobs(self):
        self.assertEqual(self.upworkclient.search_jobs(job_query), "/Need to fill in here: Does Upwork has a live test job?/")
