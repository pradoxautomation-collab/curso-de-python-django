import os
from pathlib import Path

# 1. Definição do Diretório Base (PRECISA vir antes de ser usado)
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Configurações de Segurança
SECRET_KEY = 'django-insecure-+h3lgs-bnx2+)&ht)!cbg!a0#6-5%cbu5&#o#@xw_&!i8xop#9'
DEBUG = True
ALLOWED_HOSTS = []

# 3. Aplicativos Instalados
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'courses',   # Seu app de cursos
    'tinymce',   # Editor de texto rico
]

# 4. Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'admmin.urls'

# 5. Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media', # Adicionado para ajudar nas imagens
            ],
        },
    },
]

WSGI_APPLICATION = 'admmin.wsgi.application'

# 6. Banco de Dados (MariaDB/MySQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'celke',
        'USER': 'pradox',
        'PASSWORD': '123456!!',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# 7. Validação de Senhas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 8. Internacionalização
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# 9. Arquivos Estáticos (CSS, JS)
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] # Opcional, mas recomendado

# 10. Arquivos de Mídia (Imagens dos Cursos)
# O MEDIA_ROOT aponta para a pasta que você criou manualmente
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'imagens_testes')

# 11. Outras configurações
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'