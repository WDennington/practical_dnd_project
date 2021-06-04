import unittest
from flask import url_for
from flask_testing import TestCase
from app import app, db
from requests_mock import mock

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            DEBUG=TRUE
        )
        return app
    def setUp(self):
            db.create_all()
    def tearDown(self):
        db.drop_all()

        

class Testhome(TestBase):
    def test_home(self):
        with mock() as m:
            m.get('http://name_class:5001/gen_name', text='Droop')
            m.get('http://name_class:5001/gen_class', text='Barbarian')
            m.get('http://name_class:5001/gen_race', text='Halfling')
            m.post('http://stats:5002/gen_stats', json={'strength' : 10, 'dexterity' : 12, 'constitution' : 13, 'wisdom' : 18, 'intelligence' : 12, 'charisma' : 5})

            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)  