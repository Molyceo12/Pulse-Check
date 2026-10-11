# Product Vision

Pulse Check is a high-reliability monitoring system that tracks remote device
heartbeats and triggers critical alerts when communication falls silent. Built
with Django REST Framework, Celery, and Redis, it registers devices, accepts
periodic heartbeats to reset watchdog timers, and automatically fires email
alerts when a device misses its communication window. It also provides a
status API for real-time health checks and supports pausing monitoring for
maintenance.

## Technologies

- Django REST Framework
- Celery
- Redis
- Docker
- PostgreSQL