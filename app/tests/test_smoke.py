from django.test import TestCase
from app.tests.test_base import BaseMonitorTestCase


class EnvironmentSmokeTests(BaseMonitorTestCase):
    """Verify the test environment works before writing real tests."""

    def test_environment_setup_works(self):
        """Trivial test to confirm APIClient, mocks, and DB all work."""
        from app.models import Monitor
        Monitor.objects.create(
            id='smoke-test',
            timeout=60,
            alert_email='test@critmon.com'
        )
        self.assertEqual(Monitor.objects.count(), 1)