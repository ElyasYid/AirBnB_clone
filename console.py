#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb):|] "

    def do_quit(self, arg):
        """Quits program"""
        print("Quitting...")
        return True

    def do_EOF(self, arg):
        """EOF program"""
        print("")
        return True
    
    def help_quit(self):
        """Help Message for quit cmd"""
        print("Quits the CI.")

    def help_EOF(self):
        """Help message for EOF(Ctrl+D) cmd"""
        print("Exits the program on EOF.")

    def help_help(self):
        """Help message for help command."""
        print("show/list for specific/all commands")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
