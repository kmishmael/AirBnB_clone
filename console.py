#!/usr/bin/env python3
"""HBNB Console"""


import cmd
from models import storage, valid_models


class HBNBCommand(cmd.Cmd):
    """HBNB Console Definition
    """
    prompt = '(hbnb) '

    def default(self, line):
        """Override the default method to handle <class name>.all() format.
        """
        sections = line.split(".")
        if len(sections) == 2 and sections[1] == 'all()':
            class_name = sections[0]
            if class_name in valid_models.keys():
                command = "{}".format(class_name)
                self.do_all(command)
            else:
                print("** class doesn't exist **")
        elif len(sections) == 2 and sections[1] == 'count()':
            class_name = sections[0]
            if class_name in valid_models.keys():
                command = "{}".format(class_name)
                self.do_count(command)
            else:
                print("** class doesn't exis         t **")
        elif sections[1].startswith('show(') and sections[1].endswith(')'):
            class_name = sections[0]
            id = str(sections[1][6:-2])

            if class_name in valid_models.keys():
                instances = storage.all()
                key = class_name + "." + id
                if key in instances:
                    print(instances[key])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif sections[1].startswith('destroy(') and sections[1].endswith(')'):
            class_name = sections[0]
            id = str(sections[1][5:-1]).strip()

            if class_name in valid_models.keys():
                instances = storage.all()
                key = class_name + "." + id
                if key in instances:
                    instances.pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

        elif sections[1].startswith('update(') and sections[1].endswith(')'):
            print('update function')
            args = [arg.strip() for arg in sections[1][7:-1].split(', ')]
            if len(args) >= 3:
                class_name = sections[0]
                id_part = args[0][1:-1]
                if class_name in valid_models:
                    instances = storage.all()
                    key = class_name + "." + id_part
                    if key in instances:
                        instance = instances[key]
                        attr_name = args[1][1:-1]
                        attr_value = args[2]
                        setattr(instance, attr_name, attr_value)
                        instance.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            else:
                print("** not enough arguments **")

        elif sections[1].startswith('update(') and sections[1].endswith(')'):
            args = [arg.strip() for arg in sections[1][7:-1].split(', ')]
            if len(args) >= 2:
                class_name = sections[0]
                id_part = args[0][1:-1]
                if class_name in valid_models:
                    instances = storage.all()
                    key = class_name + "." + id_part
                    if key in instances:
                        instance = instances[key]
                        try:
                            dict_repr = eval(args[1])
                        except (NameError, SyntaxError):
                            print("** invalid dictionary representation **")
                            return
                        if type(dict_repr) == dict:
                            for attr, value in dict_repr.items():
                                setattr(instance, attr, value)
                            instance.save()
                        else:
                            print("** invalid dictionary representation **")
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            else:
                print("** not enough arguments **")
        else:
            print("*** Unknown syntax: {}".format(line))

    def do_quit(self, arg):
        """Usage: quit

        Quit command to exit the program

        Args:
            arg - input argument
        """
        return True

    def do_EOF(self, arg):
        """Usage: `ctrl + D`  or `EOF`

        Exit the program with Ctrl+D (EOF)
        """
        print()
        return True

    def emptyline(self):
        """Usage: <empty line>

        Do nothing when an empty line is entered
        """
        pass

    def help_quit(self):
        """Usage: `help quit`

        Display help for the quit command
        """
        print("Quit command to exit the program")
        print("Usage: help quit")

    def do_create(self, model_name):
        """Usage: create <class>

        Create a new instance of Model, save it, and print the id

        Args:
            model_name {string} - name of Model to be created
        """
        args = model_name.split()
        if args is None or len(args) == 0:
            print("** class name missing **")
        elif args[0] not in list(valid_models.keys()):
            print("** class doesn't exist **")
        else:
            new_instance = valid_models[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, class_name):
        """Usage: show <class>

        Print the string representation of an instance

        Args:
            class_name {string} - the name of model to print it's string
            representation
        """
        args = class_name.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in list(valid_models.keys()):
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            instances = storage.all()
            if key in instances:
                print(instances[key])
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Usage: all

        Print all instances of a class or all instances in general
        """
        args = arg.split()
        instances = storage.all()
        if len(args) == 0:
            print([str(value) for value in instances.values()])
        elif args[0] not in list(valid_models.keys()):
            print("** class doesn't exist **")
        else:
            class_instances = [str(value) for key, value in instances.items()
                               if args[0] in key]
            print(class_instances)

    def do_count(self, arg):
        """Usage: all

        Print all instances of a class or all instances in general
        """
        args = arg.split()
        instances = storage.all()
        if len(args) == 0:
            print(len([str(value) for value in instances.values()]))
        elif args[0] not in list(valid_models.keys()):
            print("** class doesn't exist **")
        else:
            class_instances_count = len([str(value)
                                         for key, value in instances.items()
                                         if args[0] in key])
            print(class_instances_count)

    def do_update(self, arg):
        """Usage: update <model.id>

        Update an instance based on class name and id
        """
        args = arg.split()
        print('updating')
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in list(valid_models.keys()):
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            instances = storage.all()
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
