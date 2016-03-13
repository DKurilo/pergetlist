# Preiscope.tv user's broadcasts list project.
Gives last broadcasts from list of users.

Database settings are in pertest/settings_dev.py
It look like:
```python
import os


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        "HOST": '127.0.0.1',
        "NAME": 'django',
        "USER": 'django',
        "PASSWORD": 'eGtZ8ik32zo9TakLV7fQ', #Ups! I forgot to remove my password. Now I need to change it! You should not do as I did!
    }
}
```