"""Enum unit tests."""
import unittest
from .. import enum
import pickle


class TestEnum(unittest.TestCase):
    """Test enum."""

    days1 = enum.enum("Monday Tuesday Wednesday Thursday Friday Saturday Sunday")
    days2 = enum.enum("Monday Tuesday Wednesday Thursday Friday Saturday Sunday")
    days3 = enum.enum("Monday Tuesday Wednesday Thursday Friday Saturday Sunday", name="Days")
    days4 = enum.enum("Monday Tuesday Wednesday Thursday Friday Saturday Sunday", start=1)

    def test_enum_characteristics(self):
        """Test general characteristics of the enum object."""

        self.assertEqual(self.days1.Monday.name, "Monday")
        self.assertEqual(self.days1.Monday.value, 0)

        self.assertEqual(self.days1._name, 'enum')
        self.assertEqual(self.days3._name, 'Days')

    def test_enum_indexes(self):
        """Test indexing values in the enum."""

        self.assertEqual(self.days1.Monday, self.days1[0])
        self.assertEqual(self.days1.Monday, self.days1("Monday"))

        self.assertNotEqual(self.days1.Monday, 0)
        self.assertNotEqual(self.days1[0], 0)
        self.assertNotEqual(self.days1("Monday"), 0)

        self.assertEqual(int(self.days1.Monday), 0)
        self.assertEqual(int(self.days1[0]), 0)
        self.assertEqual(int(self.days1("Monday")), 0)

        self.assertEqual(int(self.days1.Sunday), 6)

        self.assertEqual(int(self.days4.Monday), 1)
        self.assertEqual(int(self.days4.Sunday), 7)

    def test_enum_equality(self):
        """Test enum equality."""

        self.assertIs(self.days1, self.days1)
        self.assertIsNot(self.days1, self.days2)

        self.assertEqual(self.days1, self.days2)
        self.assertNotEqual(self.days1, self.days3)
        self.assertNotEqual(self.days1, self.days4)

    def test_enum_value_equality(self):
        """Test the equality of the enum value sub object."""

        self.assertIs(self.days1.Monday, self.days1.Monday)
        self.assertIsNot(self.days1.Monday, self.days2.Monday)

        self.assertEqual(self.days1.Monday, self.days1.Monday)
        self.assertEqual(self.days1.Monday, self.days2.Monday)
        self.assertNotEqual(self.days1.Monday, self.days4.Monday)

    def test_pickle(self):
        """Test pickling of the enum."""

        pdays1 = pickle.dumps(self.days1)
        days1 = pickle.loads(pdays1)

        self.assertEqual(days1, self.days1)
