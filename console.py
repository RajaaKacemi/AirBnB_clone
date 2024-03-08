#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command: exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command: exit the program"""
        print("Exiting...")
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass
    
    def do_create(self, arg):
        """
        A methode to Create new instance of BaseModel and save it to the JSON file.
        Usage: create <class_name>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
	else:
	      try:
              new_instance = globals()[commands[0]]()
              storage.save(new_instance)
              print(new_instance.id)
                except Exception as e:
                   print(f"Error: {e}")

	def do_show(self, arg):
        """
        A method to Show the string representation of an instance.
        Usage: show <class_name> <id>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")
	
	def do_destroy(self, arg):
        """
        A method to Delete an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

	def do_all(self, arg):
        """
        A method to Print the string representation of all instances or a specific class.
        Usage: <User>.all()
                <User>.show()
        """
        objects = storage.all()

        commands = shlex.split(arg)

        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

	def do_update(self, arg):
        """
        A method to Update an instance by adding or updating an attribute.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                curly_braces = re.search(r"\{(.*?)\}", arg)

                if curly_braces:
                    try:
                        str_data = curly_braces.group(1)

                        arg_dict = ast.literal_eval("{" + str_data + "}")

                        attribute_names = list(arg_dict.keys())
                        attribute_values = list(arg_dict.values())
                        try:
                            attr_name1 = attribute_names[0]
                            attr_value1 = attribute_values[0]
                            setattr(obj, attr_name1, attr_value1)
                        except Exception:
                            pass
                        try:
                            attr_name2 = attribute_names[1]
                            attr_value2 = attribute_values[1]
                            setattr(obj, attr_name2, attr_value2)
                        except Exception:
                            pass
                    except Exception:
                        pass
                else:

                    attr_name = commands[2]
                    attr_value = commands[3]

                    try:
                        attr_value = eval(attr_value)
                    except Exception:
                        pass
                    setattr(obj, attr_name, attr_value)

                obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
