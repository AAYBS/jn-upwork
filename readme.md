[![BCH compliance](https://bettercodehub.com/edge/badge/AAYBS/jn-upwork?branch=master)](https://bettercodehub.com/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ca6b7f100fe040308ef5ba460000a7ce)](https://app.codacy.com/app/ZoranPandovski/jn-upwork?utm_source=github.com&utm_medium=referral&utm_content=AAYBS/jn-upwork&utm_campaign=Badge_Grade_Dashboard)
[![Known Vulnerabilities](https://snyk.io/test/github/AAYBS/GIC/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/AAYBS/GIC?targetFile=requirements.txt)
# Upwork jobs notification

Get notified when a job that is interesting to you (i.e. meets certain criteria) is posted on upwork.

## Installation
Create new virtual environment
```
virtualenv -p python3 upwork
```
Inside virtual env install dependencies:

```
pip install -r requirements.txt
```
Setup cron job to run notification.py script( recomended in 1h).
```
0 * * * * /jn-upwork/upwork/notification.py
```

## Config Settings
Before you start using Upwork API, you need to register your application and obtain your client credentials. Checkout [official documentation](https://developers.upwork.com/?lang=python#getting-started).
After that add required configuration options.
```
# Upwork API
[uwpork]
api_key=
api_secret=
job_skill=

# email options
[email]
smtp_host =
mail_from =
mail_to = test@mail.com
smtp_user =
smtp_pass =
smtp_port =
smtp_tls =
smtp_ssl =
```
