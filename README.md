# Pulse-Check-API (The "Watchdog" Sentinel)

A high-reliability monitoring system that tracks remote device heartbeats and
triggers critical alerts when communication falls silent. Built with Django
REST Framework, Celery, and Redis for distributed background processing.

## Prerequisites

- Python 3.10+
- Docker Desktop (for Redis and PostgreSQL)

## Setup

```bash
docker compose up --build
```

The API will be available at `http://127.0.0.1:8000`.

## Docker Commands

### Start the project

```bash
docker compose up --build
```

### Stop the project

```bash
docker compose down
```

### Restart the project

```bash
docker compose restart
```

### View logs

```bash
docker compose logs -f
```

### Run database migrations

```bash
docker compose exec web python manage.py migrate
```

### Open a shell inside the web container

```bash
docker compose exec web bash
```

### Rebuild the containers without starting them

```bash
docker compose build
```

### Start only the web service

```bash
docker compose up -d web
```

### View running containers

```bash
docker compose ps

## API Endpoints

### 1. Register Monitor

POST `http://127.0.0.1:8000/register_monitor`

Register a new device to the monitoring system.

Request body:
```json
{
  "id": "device-01",
  "timeout": 60,
  "alert_email": "admin@critmon.com"
}
```

Response:
```json
{
  "id": "device-01",
  "timeout": 60,
  "alert_email": "admin@critmon.com",
  "status": "active",
  "last_heartbeat": null
}
```

### 2. Device Heartbeat

POST `http://127.0.0.1:8000/monitors/device-01/heartbeat`

Reset the watchdog timer for an active device. Replace `device-01` with your
device ID.

Request body:
```json
{}
```

Response:
```json
{
  "success": true,
  "message": "Heartbeat received. Device is active.",
  "id": "device-01"
}
```

### 3. Check Device Status

GET `http://127.0.0.1:8000/monitors/device-01/status`

Retrieve the real-time health status of a device.

Response:
```json
{
  "id": "device-01",
  "timeout": 60,
  "alert_email": "admin@critmon.com",
  "status": "active",
  "last_heartbeat": "2026-04-27T15:53:42Z"
}
```

### 4. Pause Monitoring

POST `http://127.0.0.1:8000/monitors/device-01/pause`

Temporarily stop monitoring for maintenance.

Request body:
```json
{}
```

Response:
```json
{
  "success": true,
  "message": "Monitoring paused for device-01."
}
```

### 5. Health Check

GET `http://127.0.0.1:8000/health`

Verify the API is running.

Response:
```json
{
  "status": "ok"
}
```

### 6. List All Monitors

GET `http://127.0.0.1:8000/get-monitors`

Retrieve a list of all registered devices.

Response:
```json
[
  {
    "id": "device-01",
    "timeout": 60,
    "alert_email": "admin@critmon.com",
    "status": "active",
    "last_heartbeat": "2026-04-27T15:53:42Z"
  }
]
```