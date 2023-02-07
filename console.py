#!/usr/bin/python3
"""This is a module that implements the console
to be used for interaction with objects
"""
import cmd
import sys


class Console(cmd.Cmd):
    """This is a console that processes commands"""

    intro = "Welcome to the Console"
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """End of file command"""
        return True

    def do_quit(self, line):
        """Quits the console"""
        sys.exit(0)


if __name__ == '__main__':
    Console().cmdloop()
