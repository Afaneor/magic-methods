class Deleted(object):

    def __del__(self):
        print('deleted')


deleted = Deleted()
del deleted
