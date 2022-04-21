# Django Heroku Deployed Website
An easy to use car dealer website currently using Django version 4.0.2 Deployed on Heroku https://mikeyisme-car-dealer.herokuapp.com/


## Split Settings Structure

Settings are stored now in a `settings/` directory in the config folder and split into 3 modules:
1. **base.py**: For base settings that are used both locally and in production.
2. **dev.py**: For settings only used in development (like `DEBUG = True`)
3. **prod.py**: For settings only used in production (like `DEBUG = False`) 

---
## Heroku Settings

```python
import django_on_heroku
import dj_database_url
from dotenv import load_dotenv, find_dotenv
from decouple import config

# In base.py

INSTALLED_APPS = [
    # ...
    'django_extensions',
    # ...
]

load_dotenv(find_dotenv())

DATABASES = {'default': dj_database_url.config(default='sqlite3:///db.sqlite', conn_max_age=600)}


# In prod.py

SECRET_KEY = config('SECRET_KEY')

DEBUG_PROPAGATE_EXCEPTIONS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'MYAPP': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

django_on_heroku.settings(locals(), staticfiles=False)
del DATABASES['default']['OPTIONS']['sslmode']
```