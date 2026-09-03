#!/usr/bin/python3
"""Defines the entry point of the command interpreter for the AirBnB
clone project.

This module implements HBNBCommand, a class based on Python's cmd
module, which provides the interactive (and non-interactive) shell
used to create, inspect, and manage the project's models.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project."""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        return False

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """EOF signal (Ctrl+D) to exit the program."""
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
