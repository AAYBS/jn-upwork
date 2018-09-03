
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
