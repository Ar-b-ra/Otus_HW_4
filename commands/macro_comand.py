from typing import List

from commands.base_command import BaseCommand
from ship import CommandException


class MacroCommand:
    def __init__(self, commands: List[BaseCommand]):
        self.commands = commands

    def execute(self):
        for command in self.commands:
            try:
                command.execute()
            except CommandException as e:
                print(e)

    def undo(self):
        for command in reversed(self.commands):
            command.undo()