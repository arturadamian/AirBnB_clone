#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel
from models import storage
import json
import shlex
from models.user import User
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """"""
    prompt = '(hbnb) '
    class_list = {"BaseModel", "User"}

    def emptyline(self):
        """doesn't do anything when type Enter
        """
        pass

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        return True

    def do_create(self, arg):
        """createsa new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        argv = arg.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            new_model = eval(argv[0])()
            new_model.save()
            print(new_model.id)

    def do_show(self, arg):
        """prints representation of an object
        """
        argv = arg.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = argv[0] + "." + argv[1]
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """destroys the instance, but saves the changes in JSON file
        """
        argv = arg.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        else:
            store = storage.all()
            key = "{}.{}".format(argv[0], argv[1])
            if key in store:
                del store[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        """
        objects = storage.all()
        object_list = []
        if not arg:
            for key in objects:
                object_list.append(str(objects[key]))
            print(object_list)
            return
        argv = arg.split(" ")
        if argv[0] in self.class_list:
            for key in objects:
                if key[0:len(argv[0])] == argv[0]:
                    object_list.append(str(objects[key]))
            print(object_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """update instance attribute based on class name and id
        """
        #argv = arg.split()
        argv = shlex.split(arg)
        if len(argv) < 5:
            if len(argv) == 0:
                print("** class name missing **")
            elif argv[0] not in self.class_list:
                print("** class doesn't exist **")
            elif len(argv) == 1:
                print("** instance id missing **")
            elif len(argv) == 2:
                print("** attribute name missing **")
            elif len(argv) == 3:
                print("** value missing **")
            else:
                store = storage.all()
                key = "{}.{}".format(argv[0], argv[1])
                if key in store:
                    setattr(store[key], argv[2], argv[3])
                    storage.save()
                else:
                    print("** no instance found **")
                    #storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
