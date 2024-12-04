set -e

run flask --app src.app db upgrade
run gunicorn src.wsgi:app