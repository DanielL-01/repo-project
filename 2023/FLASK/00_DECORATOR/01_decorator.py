def decorator_function(original_function):

    def run_my_function():
        print("wrapper executed before {}".format(original_function.__name__))
        return original_function()
    return run_my_function()


def display():
    print("display function ran well.")

decorator_function(display)