import unittest
from flask import url_for
from flask_testing import TestCase
from app import app, db
from requests_mock import mock

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            DEBUG=True
        )
        return app
    def setUp(self):
        db.create_all()
    def tearDown(self):
        db.drop_all()

        

class Testhome(TestBase):
    def test_home(self):
        with mock() as m:
            m.get('http://practical_dnd_project_name_class:5001/gen_name', text='Droop')
            m.get('http://practical_dnd_project_name_class:5001/gen_class', text='Barbarian')
            m.get('http://practical_dnd_project_name_class:5001/gen_race', text='Human')
            m.get('http://practical_dnd_project_stats:5002/gen_stats', json=[10,12,13,12,18,5])
            m.post('http://practical_dnd_project_character:5003/gen_char', json =[11,13,14,13,19,6])
                



            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Name: Droop', response.data) 
            self.assertIn(b'Race: Human', response.data)
            self.assertIn(b'Strength: 11', response.data)
            self.assertIn(b'Dexterity: 13', response.data)
            self.assertIn(b'Constitution: 14', response.data)
            self.assertIn(b'Intelligence: 13', response.data)
            self.assertIn(b'Wisdom: 19', response.data)
            self.assertIn(b'Charisma: 6', response.data)
