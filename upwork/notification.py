from datetime import datetime, timedelta
import configparser
import smtplib


class Job(object):
    def __init__(self, budget, date_created, job_type, info, title, url):
        self.budget = budget
        self.date = date_created
        self.type = job_type
        self.info = info
        self.title = title
        self.url = url

    def __str__(self):
        job_info = "New job: %s \nType: %s" %(self.title, self.type)
        job_info += "\nBudget : %s $ \nCreated on: %s " % (
            self.budget, self.date)
        job_info += "Informations: %s \nLink: %s" % (self.info, self.url)
        return job_info


class UpworkClient(object):
    def __init__(self, public_key, secret_key):
        self.public_key = public_key
        self.secret_key = secret_key

    def __client(self):
        '''
        Authenticate to Upwork API
        :return: uwpork client obj
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
            print("Error: unable to authenticate " + e.message)

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
            print("Error: unable to connect " + e.message)

        jobs = []
        current_time = datetime.now() - timedelta(hours=1)
        # Get only few parameters instead of a whole payload
        for job in upwork_jobs:
            created = datetime.strptime(job['date_created'],
                                         "%Y-%m-%dT%H:%M:%S+0000")
            # check if job is posted in the last hour if not skip it
            if created < current_time:
                jobs.append(Job(job['budget'],
                                job['date_created'],
                                job['job_type'],
                                job['snippet'],
                                job['title'],
                                job['url']))
        self.__send_mail(jobs)
        return jobs


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("configuration.ini")
    api_key = config['uwpork']['api_key']
    api_secret = config['uwpork']['api_key']
    job_skill = config['upwork']['job_skill']

    upwork = UpworkClient(api_key, api_secret)
    job_query = dict(
        skills=[job_skill],
        budget='[100 TO 100000]',
        duration=['week', 'month', 'ongoing']
    )
    upwork.search_jobs(job_query)
