from django.test import TestCase
from rest_framework.test import APITestClient
from app.models import Monitor


class RegisterMonitorTests(TestCase):
    """US1: Unit tests for the register monitor endpoint."""

    def setUp(self):
        self.client = APITestClient()
        self.url = '/register_monitor'

    def test_register_creates_device_successfully(self):
        """Valid registration returns 201 and creates the device."""
        payload = {
            'id': 'device-01',
            'timeout': 60,
            'alert_email': 'admin@critmon.com'
        }
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Monitor.objects.filter(id='device-01').exists())
        monitor = Monitor.objects.get(id='device-01')
        self.assertEqual(monitor.status, Monitor.Status.ACTIVE)
        self.assertIsNone(monitor.last_heartbeat)

    def test_register_rejects_negative_timeout(self):
        """Negative timeout returns 400 and no device is created."""
        payload = {
            'id': 'device-02',
            'timeout': -5,
            'alert_email': 'admin@critmon.com'
        }
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertFalse(Monitor.objects.filter(id='device-02').exists())