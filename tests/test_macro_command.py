import unittest
from unittest.mock import MagicMock

from abs_implementation.implementation import RealPosition, RealVelocity, Vector
from commands.macro_comand import MacroCommand
from ship import Ship


class TestExecute(unittest.TestCase):
    def setUp(self):
        position = RealPosition()
        velocity = RealVelocity()
        vector = Vector(position, velocity)
        self.ship = Ship(vector)

    def test_check_fuel_with_valid_amount(self):
        # Arrange
        ship = Ship()
        fuel_amount_to_check = 100
        expected_result = True
        ship.check_fuel.return_value = expected_result

        # Act
        result = execute(ship, fuel_amount_to_check)

        # Assert
        self.assertEqual(result, expected_result)
        ship.check_fuel.assert_called_once_with(fuel_amount_to_check)

    def test_check_fuel_with_invalid_amount(self):
        # Arrange
        ship = MagicMock()
        fuel_amount_to_check = -10
        expected_result = False
        ship.check_fuel.return_value = expected_result

        # Act
        result = execute(ship, fuel_amount_to_check)

        # Assert
        self.assertEqual(result, expected_result)
        ship.check_fuel.assert_called_once_with(fuel_amount_to_check)
