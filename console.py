#!/usr/bin/python3
"""Defines the HBnB console."""
import re
import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models.place import Place


def parser(arg):
    """parser using regular expressions"""

    curls = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)

    if curls is None:
        if brackets is None:
            return [i.strip(",") for e in arg.split(',')]
        else:
            tool1 = arg[:brackets.span()[0]].split(',')
            parsed = [i.strip(",") for e in tool1]
            parsed.append(brackets.group())
            return parsed
    else:
        tool1 = arg[:curls.span()[0]].split(',')
        parsed = [i.strip(",") for e in tool1]
        parsed.append(curls.group())
        return parsed


class HBNBCommand(cmd.Cmd):
    """Defines command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb)|:) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def noline(self):
        """Do nothing if empty line."""
        pass

    def default(self, arg):
        """Default cmd module when input is invalid"""
        args_di = {
            "show": self.do_show,
            "count": self.do_count,
            "update": self.do_update,
            "all": self.do_all,
            "destroy": self.do_destroy
        }
        fits = re.search(r"\.", arg)
        if fits is not None:
            xtra = [arg[:match.span()[0]], arg[match.span()[1]:]]
            fits = re.search(r"\((.*?)\)", xtra[1])
            if fits is not None:
                mando = [xtra[1][:match.span()[0]], match.group()[1:-1]]
                if mando[0] in args_di.keys():
                    ctruct = "{} {}".format(argl[0], mando[1])
                    return args_di[mando[0]](ctruct)
        print("*** Unknown syntax: {}, type help for usage".format(arg))
        return False

    def do_quit(self, arg):
        """Quits command to exit the program."""
        print("why must you end meee...")
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("..nooo..")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Creates new instance prints id.
        """
        croted = parse(arg)
        if len(croted) == 0:
            print("** class name missing **")
        elif croted[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(croted[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string rep of instance of given id.
        """
        croted = parse(arg)
        objdict = storage.all()
        if len(croted) == 0:
            print("** class name missing **")
        elif croted[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(croted) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(croted[0], croted[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(croted[0], croted[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete class instance of a given id."""
        croted = parse(arg)
        objdict = storage.all()
        if len(croted) == 0:
            print("** class name missing **")
        elif croted[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(croted) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(croted[0], croted[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(croted[0], croted[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display str rep of all instances of a given class"""
        croted = parse(arg)
        if len(croted) > 0 and croted[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obgyn1 = []
            for obj in storage.all().values():
                if len(croted) > 0 and croted[0] == obj.__class__.__name__:
                    obgynl.append(obj.__str__())
                elif len(croted) == 0:
                    obgyn1.append(obj.__str__())
            print(obgyn1)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve number of instances of a given class."""
        croted = parse(arg)
        track = 0
        for obj in storage.all().values():
            if croted[0] == obj.__class__.__name__:
                track += 1
        print(track)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id"""
        croted = parse(arg)
        objdict = storage.all()

        if len(croted) == 0:
            print("** class name missing **")
            return False
        if croted[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(croted) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(croted[0], croted[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(croted) == 2:
            print("** attribute name missing **")
            return False
        if len(croted) == 3:
            try:
                type(eval(croted[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(croted) == 4:
            obj = objdict["{}.{}".format(croted[0], croted[1])]
            if croted[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[croted[2]])
                obj.__dict__[croted[2]] = valtype(croted[3])
            else:
                obj.__dict__[croted[2]] = croted[3]
        elif type(eval(croted[2])) == dict:
            obj = objdict["{}.{}".format(croted[0], croted[1])]
            for k, v in eval(croted[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
