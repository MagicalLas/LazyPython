def EfApp(function):
    def f(*arg, **kwargs):
        return function().execute
    return f()
