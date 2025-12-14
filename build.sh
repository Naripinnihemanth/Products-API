set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

python manage.py shell << EOF
from django.contrib.auth.models import User
import os

username = os.environ.get("DJANGO_SUPERUSER_USERNAME")

if username and not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username,
        email=os.environ.get("DJANGO_SUPERUSER_EMAIL"),
        password=os.environ.get("DJANGO_SUPERUSER_PASSWORD")
    )
EOF