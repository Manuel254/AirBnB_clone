#!/usr/bin/python3
"""This is a module that implements the console
to be used for interaction with objects
"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """This is a console that processes commands"""

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    def do_create(self, arg):
        """Creates a new instance of BaseModel
        class, saves it to the JSON file and prints
        the id if successfull else prints error message.

        Args:
            class_name (class): BaseModel class
        """
        if arg:
            if arg in HBNBCommand.classes:
                my_model = HBNBCommand.classes[arg]()
                my_model.save()
                print("{}".format(my_model.id))
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id else prints error
        message.

        Args:
            arg: argument to be passed to command
        """
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        if len(args) == 1:
            class_name = args[0]
            if class_name in HBNBCommand.classes:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        if len(args) == 2:
            class_name, obj_id = args
            if class_name in HBNBCommand.classes:
                all_objs = storage.all()
                my_model = None
                for obj in all_objs.values():
                    obj = obj.to_dict()
                    if obj["id"] == obj_id:
                        my_model = HBNBCommand.classes[class_name](**obj)
                if my_model is not None:
                    print(my_model)
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        else prints error message.

        Args:
            arg: argument to be passed to command
        """
        if len(parse(arg)) == 0:
            print("** class name missing **")
        if len(parse(arg)) == 1:
            class_name = parse(arg)[0]
            if class_name == "BaseModel":
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        if len(parse(arg)) == 2:
            class_name, obj_id = parse(arg)
            if class_name == "BaseModel":
                all_objs = storage.all()
                for obj in all_objs.values():
                    obj = obj.to_dict()
                    key = "{}.{}".format(class_name, obj_id)
                    if obj["id"] == obj_id:
                        key = "{}.{}".format(class_name, obj_id)
                        del all_objs[key]

    def do_all(self, class_name):
        pass

    def update(self, class_name, obj_id, att_name, att_val):
        pass

    def emptyline(self):
        return

    def do_EOF(self, line):
        """End of file command"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        sys.exit(0)

def parse(arg):
    return arg.split()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
