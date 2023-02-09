#!/usr/bin/python3
"""This is a module that implements the console
to be used for interaction with objects
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """This is a console that processes commands"""

    prompt = "(hbnb) "

    def emptyline(self):
        return

    def do_EOF(self, line):
        """End of file command"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        sys.exit(0)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
