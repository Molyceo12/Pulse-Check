from unittest.mock import patch
from django.test import TestCase
from rest_framework.test import APIClient


class BaseMonitorTestCase(TestCase):
    """Base test case that mocks Redis cache and Celery timers.

    This prevents external dependency errors (Redis connection, Celery broker)
    from crashing unit tests. Subclasses can use the patched views as normal.
    """

    def setUp(self):
        super().setUp()
        self.client = APIClient()
        patchers = [
            patch('app.views.cache.set'),
            patch('app.views.cache.delete'),
            patch('app.views.start_monitor_timer'),
            patch('app.views.cancel_monitor_timer'),
        ]
        self.mocks = [p.start() for p in patchers]
        for p in patchers:
            self.addCleanup(p.stop)