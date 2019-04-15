class Either(object):

    def __init__(self, right, left):
        self.right = right
        self.left = left

    @staticmethod
    def right(effect):
        rEffect = effect
        return Either(rEffect, None)

    @staticmethod
    def left(effect):
        lEffect = effect
        return Either(None, lEffect)
