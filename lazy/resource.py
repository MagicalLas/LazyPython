from .effect import lazy


class Resource(object):

    def __init__(self, f, g, middle):
        self.f = f
        self.g = g
        self.middle = middle

    def use(self, executer):
        @lazy
        def dummy():
            self.file = self.f.execute
            return executer(self.file)
        self.middle = dummy()
        return self

    def map(self, f):
        self.middle = self.middle & f
        return self

    def flatMap(self, f):
        self.middle = self.middle << f
        return self

    @property
    def execute(self):
        result = self.middle.execute
        self.g(self.file)
        return result

    @staticmethod
    def make(f):
        return Resource._relese(f)

    @staticmethod
    def _relese(f):
        _f = f

        def relese(g):
            return Resource(_f, g, lazy(lambda x: x))
        return relese
