#!/usr/bin/python3
"""Console module for AirBnB clone"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.place import Place


classes = {
    "BaseModel": BaseModel,
    "State": State,
    "Place": Place
}


def parse_value(value):
    """Parse a string value into int, float, or string"""
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1].replace("_", " ").replace('\\"', '"')
    try:
        if "." in value:
            return float(value)
        return int(value)
    except Exception:
        return None


class HBNBCommand(cmd.Cmd):
    """Command processor for AirBnB clone"""
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance with optional parameters"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in classes:
            print("** class doesn't exist **")
            return
        kwargs = {}
        for pair in args[1:]:
            if "=" in pair:
                k, v = pair.split("=", 1)
                val = parse_value(v)
                if val is not None:
                    kwargs[k] = val
        obj = classes[cls_name](**kwargs)
        obj.save()
        print(obj.id)

    def do_quit(self, arg):
        """Quit the console"""
        return True

    def do_EOF(self, arg):
        """Handle EOF to exit the console"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
