class Init(object):

    def __init__(self, my_attr: str):
        print('inited')
        self.my_attr = my_attr


init = Init('attr')
print(init.my_attr)
