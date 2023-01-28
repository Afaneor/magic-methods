class Add(object):

    def __init__(self, value: int):
        self.value = value

    def __add__(self, other):
        return (self.value + other) * 2


add = Add(3)
print(add + 3)
