from app.tests.test_base import BaseMonitorTestCase
from app.models import Monitor


class PauseMonitoringTests(BaseMonitorTestCase):
    """US6: Unit tests for the pause monitoring endpoint."""

    def setUp(self):
        super().setUp()
        Monitor.objects.create(
            id='device-01',
            timeout=60,
            alert_email='admin@critmon.com',
            status=Monitor.Status.ACTIVE
        )

    def test_pause_sets_status_to_paused(self):
        """POST /monitors/{id}/pause sets status to paused."""
        response = self.client.post('/monitors/device-01/pause', {}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['success'])
        monitor = Monitor.objects.get(id='device-01')
        self.assertEqual(monitor.status, Monitor.Status.PAUSED)

    def test_pause_already_paused_returns_success(self):
        """Pausing an already paused device returns success."""
        monitor = Monitor.objects.get(id='device-01')
        monitor.status = Monitor.Status.PAUSED
        monitor.save()

        response = self.client.post('/monitors/device-01/pause', {}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['success'])

    def test_pause_unknown_device_returns_404(self):
        """Pausing an unknown device returns 404."""
        response = self.client.post('/monitors/unknown/pause', {}, format='json')
        self.assertEqual(response.status_code, 404)