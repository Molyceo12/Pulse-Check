#!/bin/sh

# Wait for database to be ready
echo "Waiting for database..."
python -c "
import socket, time
while True:
    try:
        sock = socket.create_connection(('db', 5432), timeout=1)
        sock.close()
        print('Database is ready.')
        break
    except (socket.error, OSError):
        time.sleep(1)
"

# Run Database Migrations
echo "Applying database migrations..."
python manage.py migrate

# Execute the CMD from Dockerfile or docker-compose
exec "$@"