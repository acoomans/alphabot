import unittest
from project import MyClass

class TestProject(unittest.TestCase):

    def setUp(self):
        self.myclass = MyClass()

    def testMessage(self):
        self.assertEqual(self.myclass.message, 'hello')
