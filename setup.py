from distutils.core import setup

setup(
   name='jn-upwork',
   version='1.0.0',
   url = 'https://github.com/AAYBS/jn-upwork',
   description='Module for getting Upwork new jobs notification send to your email',
   author='Zoran Pandovski',
   author_email='zoran.pandovski@gmail.com',
   packages=['jnupwork'],
   install_requires=['python-upwork', 'smtplib']
)