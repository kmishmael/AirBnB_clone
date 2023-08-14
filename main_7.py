#!/usr/bin/python3
import console
import inspect
import io
import sys
import cmd
import shutil

"""
 Cleanup file storage
"""
import os
file_path = "file.json"
if not os.path.exists(file_path):
    try:
        from models.engine.file_storage import FileStorage
        file_path = FileStorage._FileStorage__file_path
    except:
        pass
if os.path.exists(file_path):
    os.remove(file_path)

"""
 Backup console file
"""
if os.path.exists("tmp_console_main.py"):
    shutil.copy("tmp_console_main.py", "console.py")
shutil.copy("console.py", "tmp_console_main.py")

"""
 Updating console to remove "__main__"
"""
with open("tmp_console_main.py", "r") as file_i:
    console_lines = file_i.readlines()
    with open("console.py", "w") as file_o:
        in_main = False
        for line in console_lines:
            if "__main__" in line:
                in_main = True
            elif in_main:
                if "cmdloop" not in line:
                    file_o.write(line.lstrip("    "))
            else:
                file_o.write(line)


"""
 Create console
"""
console_obj = "HBNBCommand"
for name, obj in inspect.getmembers(console):
    if inspect.isclass(obj) and issubclass(obj, cmd.Cmd):
        console_obj = obj

my_console = console_obj(stdout=io.StringIO(), stdin=io.StringIO())
my_console.use_rawinput = False

"""
 Exec command
"""


def exec_command(my_console, the_command, last_lines=1):
    my_console.stdout = io.StringIO()
    real_stdout = sys.stdout
    sys.stdout = my_console.stdout
    my_console.preloop()
    the_command = my_console.precmd(the_command)
    my_console.onecmd(the_command)
    sys.stdout = real_stdout
    lines = my_console.stdout.getvalue().split("\n")
    return "\n".join(lines[(-1*(last_lines+1)):-1])


"""
 Tests
"""
model_class = "BaseModel"
model_id = "Nop"
dict_update = {'attribute_name_dict': "string_value_dict"}

result = exec_command(my_console, "{}.update(\"{}\", {})".format(
    model_class, model_id, dict_update))
is_error = False
if result is None or result == "":
    pass
elif result == "** no instance found **":
    is_error = True

if not is_error:
    result = exec_command(my_console, "{}.update({}, {})".format(
        model_class, model_id, dict_update))
    if result is None or result == "":
        pass
    elif result == "** no instance found **":
        is_error = True

if not is_error:
    result = exec_command(my_console, "{}.update(\"{}.{}\", {})".format(
        model_class, model_class, model_id, dict_update))
    if result is None or result == "":
        pass
    elif result == "** no instance found **":
        is_error = True

if not is_error:
    result = exec_command(my_console, "{}.update({}.{}, {})".format(
        model_class, model_class, model_id, dict_update))
    if result is None or result == "":
        pass
    elif result == "** no instance found **":
        is_error = True

if not is_error:
    print("FAIL: not found")

print("OK", end="")

shutil.copy("tmp_console_main.py", "console.py")
