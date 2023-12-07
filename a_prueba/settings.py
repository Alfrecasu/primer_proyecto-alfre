from pathlib import Path
from django.urls import reverse_lazy

#-----------------------------------------------------------------------------------------------------
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#-----------------------------------------------------------------------------------------------------
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-8hrp3(zry#-v4oj+38rz36c@2p*g*^(-k!@&j*emig8ya$vb*="
#-----------------------------------------------------------------------------------------------------
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#-----------------------------------------------------------------------------------------------------
ALLOWED_HOSTS = []
#-----------------------------------------------------------------------------------------------------
AUTH_USER_MODEL = 'usuarios.Usuarios'
#-----------------------------------------------------------------------------------------------------
LOGIN_URL = reverse_lazy('apps.usuarios:iniciar_sesion')
LOGIN_REDIRECT_URL = reverse_lazy('inicio')
LOGOUT_REDIRECT_URL = reverse_lazy('inicio')
#-----------------------------------------------------------------------------------------------------
# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    #Aplicaciones propias definidas
    "apps.usuarios",
    "apps.discos",
    "apps.opiniones",
]
#-----------------------------------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
#-----------------------------------------------------------------------------------------------------
ROOT_URLCONF = "a_prueba.urls"
#-----------------------------------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [ BASE_DIR / "templates" ],
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
#-----------------------------------------------------------------------------------------------------
WSGI_APPLICATION = "a_prueba.wsgi.application"
#-----------------------------------------------------------------------------------------------------
# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "db_disco",
        "USER": "root",
        "PASSWORD": "root",
        "HOST" : "localhost",
        "PORT" : "3306",
    }
}
#-----------------------------------------------------------------------------------------------------
# Password validation
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
#-----------------------------------------------------------------------------------------------------
# Internationalization
LANGUAGE_CODE = "es-ar"
#-----------------------------------------------------------------------------------------------------
TIME_ZONE = "America/Argentina/Buenos_Aires"
#-----------------------------------------------------------------------------------------------------
USE_I18N = True
#-----------------------------------------------------------------------------------------------------
USE_TZ = True
#-----------------------------------------------------------------------------------------------------
# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'
#-----------------------------------------------------------------------------------------------------
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / 'media'
#-----------------------------------------------------------------------------------------------------
# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
