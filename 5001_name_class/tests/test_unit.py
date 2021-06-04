from flask import url_for
from flask_testing import TestCase
from app import app, names, classes, races


class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_gen_name(self):
        for _ in range(20):    
            response = self.client.get(url_for('gen_name'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(response.data.decode(), names)
    
    def test_gen_class(self):
        for _ in range(20):
            response = self.client.get(url_for('gen_class'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(response.data.decode(), classes)
    
    def test_gen_race(self):
        for _ in range(20):
            response = self.client.get(url_for('gen_race'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(response.data.decode(), races)

