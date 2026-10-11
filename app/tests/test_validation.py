from unittest.mock import patch
from django.test import TestCase
from rest_framework.test import APIClient
from app.models import Monitor
from app.serializers import MonitorSerializer


class ValidationTests(TestCase):
    """US2: Validation rejects negative timeouts, empty IDs, and invalid emails."""

    def test_negative_timeout_rejected(self):
        """Serializer rejects timeout <= 0."""
        serializer = MonitorSerializer(data={
            'id': 'device-01',
            'timeout': -5,
            'alert_email': 'admin@critmon.com'
        })
        self.assertFalse(serializer.is_valid())
        self.assertIn('timeout', serializer.errors)

    def test_empty_id_rejected(self):
        """Serializer rejects blank device ID."""
        serializer = MonitorSerializer(data={
            'id': '   ',
            'timeout': 60,
            'alert_email': 'admin@critmon.com'
        })
        self.assertFalse(serializer.is_valid())
        self.assertIn('id', serializer.errors)

    def test_invalid_email_rejected(self):
        """Serializer rejects malformed email addresses."""
        serializer = MonitorSerializer(data={
            'id': 'device-01',
            'timeout': 60,
            'alert_email': 'not-an-email'
        })
        self.assertFalse(serializer.is_valid())
        self.assertIn('alert_email', serializer.errors)

    @patch('app.views.cache.set')
    @patch('app.views.start_monitor_timer')
    def test_endpoint_rejects_invalid_email(self, mock_timer, mock_cache):
        """API returns 400 for invalid email via the register endpoint."""
        client = APIClient()
        response = client.post('/register_monitor', {
            'id': 'device-01',
            'timeout': 60,
            'alert_email': 'not-an-email'
        }, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertFalse(Monitor.objects.filter(id='device-01').exists())