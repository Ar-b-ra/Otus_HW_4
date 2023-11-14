from commands.base_command import BaseCommand
from ship import Ship


class CheckFuelCommand(BaseCommand):
    def __init__(self, ship: Ship, fuel_amount_to_check: int = 0):
        self.ship = ship
        self.fuel_amount_to_check = fuel_amount_to_check

    def execute(self):
        return self.ship.check_fuel(self.fuel_amount_to_check)

    def undo(self):
        pass
