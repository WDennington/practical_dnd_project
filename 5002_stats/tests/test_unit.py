from flask import url_for
from flask_testing import TestCase
from app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_gen_stats(self):
        for _ in range(20):
            response = self.client.get(url_for('gen_stats'))
            self.assertEqual(response.status_code, 200)
            for stat in response.json:
                self.assertIn(stat, range(13,29))
