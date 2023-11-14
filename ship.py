from abs_implementation.implementation import Vector
from abs_implementation.move import Move
from abs_implementation.rotatable_move import RotatableMove
from abstracts.rotate import Rotate
from abstracts.vector import Position


class CommandException(Exception):
    pass


class Ship(Move):
    def __init__(self, vector: Vector):
        super().__init__(vector)
        self.fuel_level = 100

    def go_to_position(self, new_position: Position):
        self.vector.set_position(new_position)

    def check_fuel(self, fuel):
        if self.fuel_level >= fuel:
            return True
        else:
            raise CommandException(f"Not enough fuel for this command")


class RotatableShip(RotatableMove):
    def __init__(self, vector: Vector, rotator: Rotate):
        super().__init__(vector, rotator)

    def go_to_position(self, new_position: Position):
        self.vector.set_position(new_position)

    def rotate(self, angle):
        self.angle = angle
        self.get_new_velocity(angle)
