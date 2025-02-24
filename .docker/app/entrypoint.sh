#!/bin/sh

# echo "Waiting for postgres..."

# while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
#   sleep 0.1
# done

# echo "PostgresSQL started"

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
django-admin compilemessages

exec "$@"