INSTALLED_APPS = [
    # ...
    'corsheaders',
    # ...
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # ...
]

CORS_ALLOW_ALL_ORIGINS = True
ALLOWED_HOSTS = ["*"]

# If using environment variables (12-factor style):
# import os
# SECRET_KEY = os.getenv('SECRET_KEY', 'replace_me_in_production')
# DEBUG = True if os.getenv('DEBUG', 'False').lower() == 'true' else False
