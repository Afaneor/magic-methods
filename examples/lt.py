class Lt(object):

    def __init__(self, value: int):
        self.value = value

    def __lt__(self, other):
        return self.value * 3 < other


print(Lt(2) < 7)
