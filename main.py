def input_error(handler):
    def wrapped(*args):
        try:
            return handler(*args)
        except KeyError as e:
            return f"Error: {e} not found."
        except ValueError as e:
            return "Error: invalid value provided."
        except IndexError as e:
            return "Error: not enough parameters."
    return wrapped

@input_error
def hello(*args):
    return "How can I help you?"

@input_error
def add_contact(*args):
    if len(args) < 2:
        raise IndexError("To add a contact, you need to specify a name and a phone number.")
    name, phone = args
    contacts[name] = phone
    return f"Added contact {name}"

@input_error
def change_phone(*args):
    if len(args) < 2:
        raise IndexError("To change a contact, you need to specify a name and a new phone number.")
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Changed phone for {name}"
    else:
        raise KeyError(name)

@input_error
def show_phone(*args):
    if len(args) < 1:
        raise IndexError("To show a phone, you need to specify a name.")
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError(name)

@input_error
def show_all(*args):
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

handlers = {
    "hello": hello,
    "add": add_contact,
    "change": change_phone,
    "phone": show_phone,
    "show all": show_all,
}

def main():
    while True:
        user_input = input("Enter command: ").strip().lower()
        command_parts = user_input.split()

        if not command_parts:
            print("No command entered. Try again.")
            continue

        command_name = command_parts[0]
        data = command_parts[1:]

        if command_name in ["good bye", "close", "exit"]:
            print("Good bye!")
            break

        handler = handlers.get(command_name)

        if not handler:
            print("Invalid command! Available commands are: hello, add, change, phone, show all.")
            continue

        try:
            result = handler(*data)
            print(result)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    contacts = {}
    main()
