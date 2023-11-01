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