# About this repository

An example to send email using SendGrid Web API.

# How to run

First of all, you need to [create an account](https://signup.sendgrid.com/) in SendGrid, then [create an API key](https://docs.sendgrid.com/ui/account-and-settings/api-keys) and update the development environment with your SENDGRID_API_KEY inside .env (see .env.example).

To send an email will be necessary to [create a sender](https://app.sendgrid.com/settings/sender_auth/senders/new) and verify it on SendGrid.

After that, follow the steps:

1. [Create a virtual environment](https://docs.python.org/3/library/venv.html):

```
$ python3 -m venv venv
```

2. Active the virtual enviroment:

```
$ source venv/bin/activate
```

3. Install all [requirements](/requirements.txt):

```
$ pip install requirements.txt
```

4. Now you can run the [main script](main.py) using:

```
$ python main.py
```
