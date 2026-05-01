from datetime import datetime

def simple_decorator(func):
    def wrapper():
        if datetime.now().hour >= 21 or datetime.now().hour < 6:
            print("its bedtime bro don't shout.")
        else:
            func()
    
    return wrapper

def say_loud():
    print('I am the best.')

say_loud = simple_decorator(say_loud)

say_loud()

def do_twice(func):
    def wrapper():
        func()
        func()
    return wrapper

@do_twice
def greet():
    print('hello user')

greet()


def do_twices(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@do_twices
def greetName(name):
    print("hello {}".format(name))

greetName('rahul')