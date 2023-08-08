#!/usr/bin/python3
"""
Module for the command interpreter.
"""
import cmd
import models
class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """
    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file),
        and prints the id.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = models.classes[arg]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on
        the class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")
                
    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file).
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")
    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on
        the class name.
        Usage: all [<class name>]
        """
        args = arg.split()
        objects = models.storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        elif args[0] in models.classes:
            print([str(obj) for key, obj in objects.items() if args[0] == key.split('.')[0]])
        else:
            print("** class doesn't exist **")
    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key in models.storage.all():
                instance = models.storage.all()[key]
                setattr(instance, args[2], args[3].strip("\"'"))
                instance.save()
            else:
                print("** no instance found **")
    def do_quit(self, arg):
        """
        Exits the program.
        Usage: quit
        """
        return True
    def do_EOF(self, arg):
        """
        Exits the program with EOF (Ctrl+D).
        """
        return True
    def emptyline(self):
        """
        Does nothing when an empty line is entered.
        """
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()