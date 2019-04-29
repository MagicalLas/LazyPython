class Either(object):
    @staticmethod
    def right(effect):
        rEffect = effect
        return Right(rEffect)

    @staticmethod
    def left(effect):
        lEffect = effect
        return Left(lEffect)


class Left(object):
    def __init__(self, value):
        self.left = value


class Right(object):
    def __init__(self, value):
        self.right = value
