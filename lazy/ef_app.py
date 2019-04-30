def EfApp(function):
    def f(*arg, **kwargs):
        return function().excute()
    return f()
