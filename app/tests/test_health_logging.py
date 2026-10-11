import logging
from django.test import TestCase
from rest_framework.test import APIClient
from app.tests.test_base import BaseMonitorTestCase


class HealthEndpointTests(BaseMonitorTestCase):
    """US4: Health endpoint returns status ok."""

    def test_health_returns_ok(self):
        """GET /health/ returns {"status": "ok"} with HTTP 200."""
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 'ok')


class LoggingTests(TestCase):
    """US5: Console logging is configured and emits lines."""

    def setUp(self):
        self.client = APIClient()

    def test_health_endpoint_logs_request(self):
        """GET /health/ produces an INFO log line."""
        with self.assertLogs('app', level='INFO') as logs:
            self.client.get('/health')
        self.assertTrue(
            any('GET /health' in msg for msg in logs.output),
            f"Expected 'GET /health' in logs, got: {logs.output}"
        )

    def test_error_log_emits_at_error_level(self):
        """The app logger can emit ERROR-level messages."""
        logger = logging.getLogger('app')
        with self.assertLogs('app', level='ERROR') as logs:
            logger.error('something went wrong')
        self.assertTrue(
            any('something went wrong' in msg for msg in logs.output),
            f"Expected error message in logs, got: {logs.output}"
        )