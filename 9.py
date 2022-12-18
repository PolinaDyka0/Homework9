contact_dict = {'name': 'phone_number', 'Polina': '0962154928'}
bool_var = True


def input_error(func):
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            if func.__name__ == 'add' or func.__name__ == 'change':
                return "Give me name and phone please"
            if func.__name__ == 'phone':
                return "Give me name for finding phone"
            else:
                return 'IndexError'
        except KeyError:
            if func.__name__ == 'phone':
                return 'No such phone'
            return "No such command"
        except ValueError:
            return 'There no such name'
    return inner_function


def split_command_line(inp):
    if inp == 'show all' or inp == 'good bye':
        return [inp]
    return inp.split(' ')


@input_error
def hello():
    return 'How can I help you?'


@input_error
def add(inp):
    contact_dict.update({inp[0]: inp[1]})
    return 'DONE!'


@input_error
def change(inp):
    if contact_dict.get(inp[0]) != None:
        contact_dict[inp[0]] = inp[1]
    else:
        raise ValueError
    return 'DONE!'


@ input_error
def phone(inp):
    return contact_dict[inp[0]]


@ input_error
def show_all():
    return '\n'.join(f'{key}: {value}' for key,
                     value in contact_dict.items())


@ input_error
def close():
    global bool_var
    bool_var = False
    return 'Good bye!'


@input_error
def handler(name, arguments):
    def add_func():
        return add(arguments)

    def change_func():
        return change(arguments)

    def phone_func():
        return phone(arguments)

    commands = {'hello': hello,
                'add': add_func,
                'change': change_func,
                'phone': phone_func,
                'show all': show_all,
                'close': close,
                'exit': close,
                'good bye': close,
                '.': close}

    return commands[name]


def main():
    while bool_var:
        inp = input('Type:\n')
        command, *arguments = split_command_line(inp.lower())
        operation = handler(command, arguments)
        if isinstance(operation, str):
            print(operation)
        else:
            print(operation())


if __name__ == "__main__":
    main()
