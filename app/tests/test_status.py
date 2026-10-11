from app.tests.test_base import BaseMonitorTestCase
from app.models import Monitor


class StatusEndpointTests(BaseMonitorTestCase):
    """US7: Unit tests for the status endpoint."""

    def setUp(self):
        super().setUp()
        Monitor.objects.create(
            id='device-01',
            timeout=60,
            alert_email='admin@critmon.com',
            status=Monitor.Status.ACTIVE
        )

    def test_status_returns_device_details(self):
        """GET /monitors/{id}/status returns device health data."""
        response = self.client.get('/monitors/device-01/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], 'device-01')
        self.assertEqual(response.data['status'], 'active')
        self.assertEqual(response.data['timeout'], 60)
        self.assertEqual(response.data['alert_email'], 'admin@critmon.com')

    def test_status_returns_404_for_unknown_device(self):
        """GET /monitors/{id}/status returns 404 for unknown device."""
        response = self.client.get('/monitors/unknown/status')
        self.assertEqual(response.status_code, 404)