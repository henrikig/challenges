import functools


def null_decorator(func):
    return func


def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


def strong(func):
    @functools.wraps(func)
    def wrapper():
        return '<strong>' + func() + '<strong>'
    return wrapper


def emphasis(func):
    @functools.wraps(func)
    def wrapper():
        return '<em>' + func() + '<em>'
    return wrapper


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
              f'with {args}, {kwargs}')

        original_result = func(*args, **kwargs)

        print(f'TRACE: {func.__name__}() '
              f'returned {original_result!r}')

        return original_result
    return wrapper


@trace
def say(name, line):
    """Returns line said by name nicely formatted"""
    return f'{name}: {line}'


@strong
@emphasis
@uppercase
def greet():
    """Return a friendly greeting"""
    return 'Hello!'


if __name__ == '__main__':
    print(say("Jane", "Hello, World!"))
    print(f'{say.__name__!r}')
    print(f'{say.__doc__!r}')
