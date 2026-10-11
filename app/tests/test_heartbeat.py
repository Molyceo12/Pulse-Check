from app.tests.test_base import BaseMonitorTestCase
from app.models import Monitor


class HeartbeatTests(BaseMonitorTestCase):
    """US3: Unit tests for the heartbeat endpoint."""

    def setUp(self):
        super().setUp()
        Monitor.objects.create(
            id='device-01',
            timeout=60,
            alert_email='admin@critmon.com',
            status=Monitor.Status.ACTIVE
        )

    def test_heartbeat_resets_timer_and_updates_status(self):
        """Heartbeat updates last_heartbeat and returns success."""
        monitor = Monitor.objects.get(id='device-01')
        monitor.status = Monitor.Status.DOWN
        monitor.save()

        response = self.client.post(
            '/monitors/device-01/heartbeat', {}, format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['success'])
        monitor.refresh_from_db()
        self.assertEqual(monitor.status, Monitor.Status.ACTIVE)
        self.assertIsNotNone(monitor.last_heartbeat)

    def test_heartbeat_returns_404_for_unknown_device(self):
        """Unknown device returns 404."""
        response = self.client.post(
            '/monitors/unknown/heartbeat', {}, format='json'
        )
        self.assertEqual(response.status_code, 404)