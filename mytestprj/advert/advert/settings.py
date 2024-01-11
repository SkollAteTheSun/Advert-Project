from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-8)f1y@^*5e6zigd+j34ik2k*kemqustl&glma=^=@&u+%xygk@'
#SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True
#DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = []
#ALLOWED_HOSTS = list(os.environ.get('ALLOWED_HOSTS'))

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'drf_spectacular',

    'authentication',
    'api',
]


REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Advert API',
    'DESCRIPTION': 'API веб-приложения для создания объявлений',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

JET_THEMES = [
    {
        'theme': 'default',
        'color': '#47bac1',
        'title': 'Default'
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

JET_DEFAULT_THEME = 'light-violet'

JET_SIDE_MENU_COMPACT = True

JET_SIDE_MENU_ITEMS = [
    {'label': 'API', 'app_label': 'api', 'items': [
        {'name': 'category', 'label': ('Категории')},
        {'name': 'advert', 'label': ('Объявления')},
        {'name': 'proposal', 'label': ('Заявки')},
    ]},
    {'label': 'Authentication', 'app_label': 'authentication', 'items': [
        {'name': 'customuser', 'label': ('Пользователи')},
    ]}
]

JET_CHANGE_FORM_SIBLING_LINKS = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'advert.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'advert.wsgi.application'

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'USER': 'postgres',
         'PASSWORD':'root',
         'NAME': 'new',
         'PORT': '5432',
         'HOST': 'localhost',
     }
}

#DATABASES = {
#    'default': {
#        'ENGINE': os.environ.get('DB_ENGINE'),
#        'USER': os.environ.get('DB_USER'),
#        'PASSWORD': os.environ.get('DB_PASSWORD'),
#        'NAME': os.environ.get('DB_NAME'),
#        'PORT': os.environ.get('DB_PORT'),
#        'HOST': os.environ.get('DB_HOST'),
#    }
#}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'debug.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
}
