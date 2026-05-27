# decorators is the way of changing  functions without affecting the orginal codes
# the gift orginal code
# the wrapper the decorator
def decorator(func):

    def wrapper(name):
        print("Before")

        func(name)

        print("After")

    return wrapper


@decorator
def greet(name):
    print("Hello", name)

greet("Gaelle")