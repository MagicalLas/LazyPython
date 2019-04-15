from .lazy import lazy


class Resource(object):

    def __init__(self, f, g):
        self.f = f
        self.g = g

    def use(self, excuter):
        @lazy
        def dummy():
            self.file = self.f()
            return excuter(self.file)
        self.middle = dummy()
        return self

    def map(self, f):
        self.middle = self.middle & f
        return self

    def flatMap(self, f):
        self.middle = self.middle << f
        return self

    def excute(self):
        result = self.middle.excute()
        self.g(self.file)
        return result

    @staticmethod
    def make(f):
        return Resource._relese(f)

    @staticmethod
    def _relese(f):
        _f = f
        def relese(g):
            return Resource(_f, g)
        return relese
