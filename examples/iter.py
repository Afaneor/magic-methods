class Iterator(object):

    def __init__(self, value: int):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > 10:
            raise StopIteration()
        self.value += 1
        return self.value


iterator = Iterator(1)

for object_value in iterator:
    print(object_value)
