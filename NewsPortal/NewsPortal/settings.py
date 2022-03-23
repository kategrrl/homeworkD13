
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v5u84e&n^$^(cg767+t!e0_pe5^!y^xu2pea^f8kpt!%*c2qs!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sites',
    'fpages',
    'news.apps.NewsConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'NewsPortal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


SITE_ID = 1


WSGI_APPLICATION = 'NewsPortal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]


LOGGING = {
    'version': 1,  # всегда 1
    'disable_existing_loggers': False,  # 2

# ФОРМАТИРОВЩИКИ
    'formatters': {
        # для DEBUG - (время), (уровень), (сообщения)
        'debug_console': {
            'format': '%(asctime)s %(levelname)s %(message)s',
        },
        # для WARNING - (время), (уровень), (путь к событию - pathname), (сообщение)
        'warning_console': {
            'format': '%(asctime)s %(levelname)s %(pathname)s %(message)s'
        },
        # для ERROR и CRITICAL - (время), (уровень), (путь к событию), (сообщение), (стэк ошибки)
        'error_critical': {
            'format': '%(asctime)s %(levelname)s %(pathname)s %(message)s %(exc_info)s'
        },

        # 2-4 пункт задания - (время), (уровень), (модуль), (сообщение). для файлов general.log и security.log
        'general_security_log': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },

        # для задания 5 -  (время), (уровень), (путь к событию), (сообщение)
        # для уровня ERROR, для отправки по почте
        'mail_log': {
            'format': '%(asctime)s %(levelname)s %(pathname)s %(message)s'
        }
    },


# ФИЛЬТРЫ
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },


# ОБРАБОТЧИКИ (ХЭНДЛЕРЫ)
    'handlers': {

        # 1 пункт задания - уровень DEBUG, фильтр DEBUG = True везде, кроме отправки по почте и
        # записи в файл general.log
        'console_debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler', #консоль
            'formatter': 'debug_console'
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler', #консоль
            'formatter': 'warning_console'
        },

        # 2 - INFO, фильтр DEBUG = False
        'file_general': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler', #файл
            'filename': 'general.log',
            'formatter': 'general_security_log'
        },

        # 4 - уровень INFO
        'file_security': {
            'level': 'INFO',
            'class': 'logging.FileHandler', #файл
            'filename': 'security.log',
            'formatter': 'general_security_log'
        },

        # 3 - ERROR, вывод в файл errors.log
        'file_errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler', #файл
            'filename': 'errors.log',
            'formatter': 'error_critical'
        },

        # 3 - CRITICAL, вывод в файл errors.log
        'file_critical': {
            'level': 'CRITICAL',
            'class': 'logging.FileHandler', #файл
            'filename': 'errors.log',
            'formatter': 'error_critical'
        },

        # 5 -  ERROR, отправка по почте
        'mail_admin': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler', #по электронной почте
            'formatter': 'mail_log'
        }
    },

#  Логгеры
    'loggers': {

        # 1, 2 пункт задания
        'django': {
            'handlers': ['console_debug', 'console_warning', 'file_general'],
            'propagate': True,
        },

        # 3 пункт задания
        'django.template': {
            'handlers': ['file_errors', 'file_critical'],
            'propagate': True,
        },

        # 3 пункт задания
        'django.db_backends': {
            'handlers': ['file_errors', 'file_critical'],
            'propagate': True,
        },

        # 4 пункт задания
        'django.security': {
            'handlers': ['file_security'],
            'propagate': True,
        },

        # 5, 3 пункт задания
        'django.request': {
            'handlers': ['file_errors', 'file_critical', 'mail_admin'],
            'propagate': True,
        },

        # 5, 3 пункт задания
        'django.server': {
            'handlers': ['file_errors', 'file_critical', 'mail_admin'],
            'propagate': True,
        }
    }
}