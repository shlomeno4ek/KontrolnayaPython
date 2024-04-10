import model.commands as cmd
import model.functions as fun


def change_commands(command):
    if command == cmd.Commands.all.name:
        fun.show(cmd.Commands.all.value)
    elif command == cmd.Commands.add.name:
        fun.add()
    elif command == cmd.Commands.delete.name:
        fun.delete()
    elif command == cmd.Commands.edit.name:
        fun.edit()
    elif command == cmd.Commands.date.name:
        fun.show(cmd.Commands.date.value)
    elif command == cmd.Commands.id.name:
        fun.show(cmd.Commands.id.value)


def is_valid_command(command):
    for com in cmd.Commands:
        if com.name == command:
            return True
    return False


def is_exit(command):
    if command == cmd.Commands.exit.name:
        return True
    return False
