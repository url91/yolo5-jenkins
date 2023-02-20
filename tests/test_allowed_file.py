import collections
import sys
if sys.version_info.major == 3 and sys.version_info.minor >= 10:
    from collections.abc import MutableMapping
else:
    from collections import MutableMapping
import unittest
from app import allowed_file, ALLOWED_EXTENSIONS


class TestBacklogPerInstanceMetric(unittest.TestCase):
    def test_valid_filename(self):
        for ext in ALLOWED_EXTENSIONS:
            self.assertTrue(allowed_file(f'test.{ext}'))

    def test_invalid_filename(self):
        self.assertFalse(allowed_file(f'file'))
        self.assertFalse(allowed_file(f'file.csv'))

