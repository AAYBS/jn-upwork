import os
from datetime import datetime, timedelta
import configparser
import smtplib
import upwork


class Job(object):
    def __init__(self, job_info):
        self.job_info = job_info

    def __str__(self):
        job_info = "New job: %s \nType: %s" %(self.job_info['title'],
                                              self.job_info['job_type'])
        job_info += "\nBudget : %s $ \nCreated on: %s " % (
            self.job_info['budget'], self.job_info['date_created'])
        job_info += "Informations: %s \nLink: %s" % (self.job_info['category2'],
                                                     self.job_info['url'])
        return job_info


class Config(object):
    def __init__(self, source_path='', content=''):
        config = configparser.ConfigParser()
        if len(source_path) > 0:
            script_dir = os.path.dirname(__file__)
            abs_file_path = os.path.join(script_dir, source_path)
            config.read_file(open(abs_file_path))
        elif len(content) > 0:
            config.read_string(content)
        else:
            raise Exception("Specify a configuration file path, or content.")
        self.config = config

class UpworkClient(object):
    def __init__(self, public_key, secret_key):
        if (len(public_key) > 0) & (len(secret_key) > 0):
            self.public_key = public_key
            self.secret_key = secret_key
        else:
            raise Exception("No Authentication key\n" +\
            "Go to https://developers.upwork.com/?lang=python#getting-started")

    def __client(self):
        '''
        Authenticate to Upwork API
        :return: upwork client obj
        '''
        try:
            upwork_client = upwork.Client(
                self.public_key, self.secret_key)
            verifier = upwork_client.auth.get_authorize_url()
            oauth_access_token, oauth_access_token_secret = \
                upwork_client.auth.get_access_token(verifier)
            client = upwork.Client(
                self.public_key, self.secret_key,
                oauth_access_token=oauth_access_token,
                oauth_access_token_secret=oauth_access_token_secret)
        except Exception as e:
            print("Error: unable to authenticate ", e)
            raise

        return client

    @classmethod
    def __send_mail(self, message):
        config = configparser.ConfigParser()
        config.read("configuration.ini")
        sender = config['email']['mail_from']
        receivers = config['email']['mail_to']

        try:
            smtpObj = smtplib.SMTP('localhost')
            smtpObj.sendmail(sender, receivers, message)
            print("Successfully sent email")
        except Exception as e:
            print("Error: unable to send email " + e.message)

    def search_jobs(self, job_query):
        '''
        Call search job with specific search job query
        :param job_query:
        :return: list of jobs
        '''
        try:
            upwork = self.__client()
            upwork_jobs = \
                upwork.provider_v2.search_jobs(job_query, page_size=20)
        except Exception as e:
            print("Error: unable to connect {e!s}")
            raise

        jobs = []
        current_time = datetime.now() - timedelta(hours=1)
        # Get only few parameters instead of a whole payload
        for job in upwork_jobs:
            created = datetime.strptime(job['date_created'],
                                         "%Y-%m-%dT%H:%M:%S+0000")
            # check if job is posted in the last hour if not skip it
            if created < current_time:
                jobs.append(Job(job))
        self.__send_mail(jobs)
        return jobs


if __name__ == "__main__":
    config = Config("configuration.ini")
    # Define local parameters
    api_key = config['upwork']['api_key']
    api_secret = config['upwork']['api_key']
    job_skill = config['upwork']['job_skill']

    upwork = UpworkClient(api_key, api_secret)
    job_query = dict(
        skills=[job_skill],
        budget='[100 TO 100000]',
        duration=['week', 'month', 'ongoing']
    )
    upwork.search_jobs(job_query)
