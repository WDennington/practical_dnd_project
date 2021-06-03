import unittest
from flask import url_for
from flask_testing import TestCase
from app import app, db, Characters

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///data.db",
                DEBUG=True
        )
        return app

    def setUp(self):
        """
        Will be called before everytest
        """
        db.create_all()
        test_character = Characters(
            name = 'droop',
            char_class='Bard',
            race = 'Halfling',
            strength = 14,
            dexterity = 16,
            constitution = 12,
            intelligence = 8,
            wisdom = 18,
            charisma = 5
        )
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all() 
