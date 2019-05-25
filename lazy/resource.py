from .effect import lazy


class Resource(object):


    def use(self, executer):

    def map(self, f):

    def flatMap(self, f):

    @property
    def attempt(self):

    @property
    def execute(self):
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
