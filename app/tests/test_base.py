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
        patcher_cache = patch('app.views.cache.set')
        patcher_timer = patch('app.views.start_monitor_timer')
        self.mock_cache = patcher_cache.start()
        self.mock_timer = patcher_timer.start()
        self.addCleanup(patcher_cache.stop)
        self.addCleanup(patcher_timer.stop)