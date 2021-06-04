from flask import url_for
from flask_testing import TestCase
from app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_gen_char_dwarf(self):        
        payload = dict(char_class='Dwarf',stats = [12, 13, 15, 6, 8, 10])
        response = self.client.post(url_for('gen_char'), json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,[12,13,17,6,8,10])

    def test_gen_char_elf(self):        
        payload = dict(char_class='Elf',stats = [12, 13, 15, 6, 8, 10])
        response = self.client.post(url_for('gen_char'), json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,[12,15,15,6,8,10])
    
    def test_gen_char_gnome(self):        
        payload = dict(char_class='Gnome',stats = [12, 13, 15, 6, 8, 10])
        response = self.client.post(url_for('gen_char'), json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,[12,13,15,8,8,10])
    
    def test_gen_char_Human(self):        
        payload = dict(char_class='Human',stats = [12, 13, 15, 6, 8, 10])
        response = self.client.post(url_for('gen_char'), json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,[13,14,16,7,9,11])