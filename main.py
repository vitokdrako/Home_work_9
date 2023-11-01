def input_error(handler):
    def wrapped(command, *args):
        try:
            return handler(command, *args)
        except KeyError as e:
            return f"Error: {e} not found."
        except ValueError as e:
            return "Error: invalid value provided."
        except IndexError as e:
            return "Error: not enough parameters."
    return wrapped

@input_error
def add_contact(command, *args):
    name, phone = args
    contacts[name] = phone
    return f"Added contact {name}"

@input_error
def change_phone(command, *args):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Changed phone for {name}"
    else:
        raise KeyError(name)

@input_error
def show_phone(command, *args):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError(name)

@input_error
def show_all(command, *args):
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    while True:
        command = input("Enter command: ").strip().lower()
        command_parts = command.split()
        if not command_parts:
            continue
        command_name, *data = command_parts

        if command_name == "exit":
            print("Good bye!")
            break

        handler = globals().get(command_name)
        if not handler:
            print("Invalid command!")
            continue

        print(handler(command_name, *data))

if __name__ == "__main__":
    contacts = {} 
    main()