from .effect import lazy
from .either import Either


class Resource(object):

    def __init__(self, maker, function_chain, closer):
        self.maker = maker
        self.function_chain = function_chain
        self.closer = closer

    def use(self, f):
        return Resource(self.maker, f, self.closer)

    def map(self, f):
        def dummy(resource):
            return f(self.function_chain(resource))
        return Resource(self.maker, dummy, self.closer)

    def flatMap(self, f):
        def dummy(resource):
            return f(self.function_chain(resource)).execute
        return Resource(self.maker, dummy, self.closer)

    @property
    def attempt(self):
        def dummy(resource):
            try:
                return Either.left(self.function_chain(resource))
            except Exception as e:
                return Either.right(e)
        return Resource(self.maker, dummy, self.closer)

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
        maker = f

        def relese(closer):
            return Resource(maker, lazy(lambda x: x), closer)
        return relese
