#!/usr/bin/python3
"""
The console, to manage everything
"""
import cmd
import re

from models.base_model import BaseModel

from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from models import storage


class HBNBCommand(cmd.Cmd):
    """Contains functionality of the console"""

    intro = "Welcome to the interpreter! Type help or ? to list commands.\n"
    prompt = "(hbnb) "
    __More_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        dict_adv = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[: match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][: match.span()[0]], match.group()[1:-1]]
                if command[0] in dict_adv.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return dict_adv[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_create(self, line):
        """Creates a new object"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in self.__class__.__More_classes.keys():
            print("** class doesn't exist **")
        else:
            obj = self.__class__.__More_classes[line]()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        class_object = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif class_object[0] not in self.__class__.__More_classes.keys():
            print("** class doesn't exist **")
            return
        elif len(class_object) == 1:
            print("** instance id missing **")
            return
        else:
            key = class_object[0] + "." + class_object[1]
            instancesssss = storage.all()
            if key not in instancesssss.keys():
                print("** no instance found **")
            else:
                obj = instancesssss[key]
                print(str(obj))

    def do_destroy(self, args):
        """Destroys an object based on the Class Name and ID"""

        target_list = args.split(" ")
        if len(args) == 0:
            print("** class name missing **")
            return
        elif target_list[0] not in self.__class__.__More_classes.keys():
            print("** class doesn't exist **")
            return
        elif len(target_list) == 1:
            print("** instance id missing **")
            return
        else:
            key = target_list[0] + "." + target_list[1]
            all_instances = storage.all()
            if key not in all_instances.keys():
                print("** no instance found **")
            else:
                del all_instances[key]
                storage.save()

    def do_all(self, line):
        """Print string representation of all instances"""
        li_obj = []
        objs = storage.all()
        try:
            if len(line) != 0:
                eval(line)
            else:
                pass
        except NameError:
            print("** class doesn't exist **")
            return
        line.strip()
        for key, val in objs.items():
            if len(line) != 0:
                if type(val) is eval(line):
                    val = str(objs[key])
                    li_obj.append(val)
            else:
                val = str(objs[key])
                li_obj.append(val)
        print(li_obj)

    def do_update(self, line):
        """Updates attributes of an object"""
        updatesss = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif updatesss[0] not in __class__.__More_classes.keys():
            print("** class doesn't exist **")
            return
        elif len(updatesss) == 1:
            print("** instance id missing **")
            return
        elif len(updatesss) == 2:
            print("** attribute name missing **")
        elif len(updatesss) == 3:
            print("** value missing **")
        else:
            k = updatesss[0] + "." + updatesss[1]
            inst_ssss = storage.all()
            if k not in inst_ssss.keys():
                print("** no instance found **")
            else:
                obj = inst_ssss[k]
                setattr(obj, updatesss[2], updatesss[3])
                storage.save()

    def do_count(self, arg):
        """Count all instances of a class"""
        arggg = arg.split(" ")
        cou = 0
        for vall in storage.all().values():
            if arggg[0] == type(vall).__name__:
                cou += 1
        print(cou)

    def do_quit(self, args):
        """Quits the interpreter"""
        raise SystemExit

    def emptyline(self):
        """Overwrite default behavior to repeat last cmd"""
        pass

    def do_EOF(self, arg):
        """Handles EOF to exit program"""
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
