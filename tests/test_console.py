#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertIsNone(self.console.onecmd(""))

    def test_help_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help quit")
            output = f.getvalue().strip()
            self.assertIn("Quit command to exit the program", output)

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User")
            output = f.getvalue().strip()
            self.assertIn("** instance id missing **", output)

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User")
            output = f.getvalue().strip()
            self.assertIn("** instance id missing **", output)

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all User")
            output = f.getvalue().strip()
            # self.assertIn("[]", output)

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User")
            output = f.getvalue().strip()
            self.assertIn("** instance id missing **", output)

    """
    def test_update_with_dict(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create User')
            result = f.getvalue().strip()
            instance_id = result.split()[-1]
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('update User ' + instance_id +
            'first_name "John"')
            self.console.onecmd('show User ' + instance_id)
            output = f.getvalue().strip()
            self.assertIn("first_name: 'John'", output)
            """


if __name__ == '__main__':
    unittest.main()
