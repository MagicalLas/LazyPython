from .effect import lazy


class Resource(object):

    def __init__(self, maker, function_chain, closer):
        self.maker = maker
        self.function_chain = function_chain
        self.closer = closer

    def use(self, f):
        return Resource(self.maker, f, self.closer)

    def map(self, f):

    def flatMap(self, f):

    @property
    def attempt(self):

    @property
    def execute(self):
        resource = self.maker.execute
        result = self.function_chain(resource)
        self.closer(resource)
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
