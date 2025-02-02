from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-x*)5s_om!jooy5ewy8n*oqjc#6ziymj=2%a5jdjg^urmp*e8k5"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

# DJANGO_APPS
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # THRIRTY APPS
    # PARA VUE (cuando deployemos)
    # 'webpack_loader',
    # PARA POSGRESS
    "django.contrib.postgres",
    # Django REST framework
    "rest_framework",
    "rest_framework.authtoken",
    # Djoser
    'djoser',
    # CORS
    "corsheaders",
    # LOCAL APPS
    # "users",
    "Socios",
    "Mutuales",
    "Profesionales",
    "Farmacias",
    "Medicamentos",
    "Ordenes",
    "Cobradores",
    "Cuotas",
    "Estudios",
    "GastosSalientes",
    "Cirugias",
    "Institutos",
    "Lentes",
    "VentasOpticas",
    'Vendedores',
    'PagadoProfesionales',
    'Cristales',

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
    #     "rest_framework.authentication.BasicAuthentication",
    #     "rest_framework.authentication.SessionAuthentication",
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSIONS_CLASSES": ("rest_framework.permissions.IsAuthenticated"),
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
}


# CORS
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_ORIGIN = [
    "http://localhost:8080",
]
CORS_ORIGIN_WHITELIST = ["http://localhost:8080"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'federacion_mutuales',
    #     'USER': 'postgres',
    #     'PASSWORD': 'leonel',
    #     'HOST': '127.0.0.1',
    #     'DATABASE_PORT': '5432',
    # }
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "federacion",
        "USER": "admin",
        "PASSWORD": "contraseniasegura",
        "HOST": "database",
        "DATABASE_PORT": "5430",
    },
    # "postgres_leonel": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": "federacion",
    #     "USER": "postgres",
    #     "PASSWORD": "leonel",
    #     "HOST": "127.0.0.1",
    #     "DATABASE_PORT": "5432",
    # },
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# AUTH_USER_MODEL = "users.User"


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "es-ar"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ("JWT", "Bearer", "Token"),
}
