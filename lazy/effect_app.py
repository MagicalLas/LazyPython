def EfApp(function):
    def f(*arg, **kwargs):
        function().excute()
    return f()
