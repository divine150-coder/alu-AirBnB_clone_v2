#!/usr/bin/python3
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage


class TestConsoleCreateParams(unittest.TestCase):

    def tearDown(self):
        storage._FileStorage__objects.clear()

    def test_create_state_with_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
            obj_id = f.getvalue().strip()
        key = "State." + obj_id
        self.assertIn(key, storage.all())
        state = storage.all()[key]
        self.assertEqual(state.name, "California")

    def test_create_place_with_int(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place number_rooms=4')
            obj_id = f.getvalue().strip()
        place = storage.all()["Place." + obj_id]
        self.assertEqual(place.number_rooms, 4)
        self.assertIsInstance(place.number_rooms, int)

    def test_create_place_with_float(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place latitude=37.77')
            obj_id = f.getvalue().strip()
        place = storage.all()["Place." + obj_id]
        self.assertEqual(place.latitude, 37.77)
        self.assertIsInstance(place.latitude, float)

    def test_create_place_with_string_spaces(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place name="My_little_house"')
            obj_id = f.getvalue().strip()
        place = storage.all()["Place." + obj_id]
        self.assertEqual(place.name, "My little house")

    def test_invalid_param_skipped(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="Rwanda" badparam')
            obj_id = f.getvalue().strip()
        state = storage.all()["State." + obj_id]
        self.assertEqual(state.name, "Rwanda")
