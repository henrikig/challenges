from functools import wraps


def write_to_file(func):
    """Decorator to write result to file"""
    @wraps(func)  # preserves function meta data
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open(f'{func.__name__}.txt', 'a') as f:
            f.write(f'{result}\n')
        return func(*args, **kwargs)
        # do stuff after func
    return wrapper


@write_to_file
def quote_maker(name, quote):
    """Function which formats quotes"""
    return f'{name}: {quote!r}'


if __name__ == '__main__':
    print(quote_maker("Brené Brown", "If you own this story you get to make the ending."))
    print(quote_maker("Confucius", "Wherever you go, go with all your heart."))
    print(quote_maker("Norman Vincent Peale", "Change your thoughts and you change your world."))
    print(f'{quote_maker.__name__}')
    print(f'{quote_maker.__doc__}')
