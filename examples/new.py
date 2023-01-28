class New(object):

    def __new__(cls, *args, **kwargs):
        """Метод вызывается при создании объекта."""
        print('created')
        return super().__new__(cls)


new = New()
