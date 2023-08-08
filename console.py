#!/usr/bin/env python3
"""HBNB cmd Definition"""


import cmd
import models
class HBNBCommand(cmd.Cmd):
    """Representation of HBNB command"""

    
    prompt = '(hbnb) '
    valid_classes = ["BaseModel"]
    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True
    def do_EOF(self, arg):
        """
        Exit the program with Ctrl+D (EOF)
        """
        print()
        return True
    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass
    def help_quit(self):
        """
        Display help for the quit command
        """
        print("Quit command to exit the program")
    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it, and print the id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = models.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)
    def do_show(self, arg):
        """
        Print the string representation of an instance
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            instances = models.storage.all()
            if key in instances:
                print(instances[key])
            else:
                print("** no instance found **")
    def do_destroy(self, arg):
        """
        Delete an instance based on class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            instances = models.storage.all()
            if key in instances:
                instances.pop(key)
                models.storage.save()
            else:
                print("** no instance found **")
    def do_all(self, arg):
        """
        Print all instances of a class or all instances in general
        """
        args = arg.split()
        instances = models.storage.all()
        if len(args) == 0:
            print([str(value) for value in instances.values()])
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        else:
            class_instances = [str(value) for key, value in instances.items() if args[0] in key]
            print(class_instances)
    def do_update(self, arg):
        """
        Update an instance based on class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            instances = models.storage.all()
            if key in instances:
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    instance = instances[key]
                    attribute_name = args[2]
                    attribute_value = args[3]
                    setattr(instance, attribute_name, attribute_value)
                    instance.save()
            else:
                print("** no instance found **")
if __name__ == '__main__':
    HBNBCommand().cmdloop()