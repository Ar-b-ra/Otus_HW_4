from abs_implementation.implementation import Vector, RealPosition, RealVelocity
from abstracts.rotate import Rotate
from commands.burn_fuel_command import BurnFuelCommand
from commands.check_fuel_command import CheckFuelCommand
from commands.macro_comand import MacroCommand
from commands.move_command import MoveCommand
from commands.rotate_command import ChangeVelocityCommand
from ship import Ship, RotatableShip

if __name__ == "__main__":
    ship_to_test = Ship(Vector(RealPosition(1, 2), RealVelocity(3, -4)))
    fuel_to_burn = 70
    macro_command = MacroCommand()
    macro_command.add_command(CheckFuelCommand(ship_to_test, fuel_to_burn))
    macro_command.add_command(MoveCommand(ship_to_test))
    macro_command.add_command(BurnFuelCommand(ship_to_test, fuel_to_burn))

    macro_command.execute()

    print(ship_to_test.get_position())

    rotatable_ship_to_test = RotatableShip(Vector(RealPosition(1, 2), RealVelocity(3, -4)), Rotate(90))
    print(rotatable_ship_to_test.fuel_level)
    macro_command_with_rotate = MacroCommand()
    macro_command_with_rotate.add_command(CheckFuelCommand(rotatable_ship_to_test, fuel_to_burn))
    macro_command_with_rotate.add_command(ChangeVelocityCommand(rotatable_ship_to_test, 25))
    macro_command_with_rotate.add_command(MoveCommand(rotatable_ship_to_test))
    macro_command_with_rotate.add_command(BurnFuelCommand(rotatable_ship_to_test, fuel_to_burn))

    macro_command_with_rotate.execute()
    print(rotatable_ship_to_test.get_position())
