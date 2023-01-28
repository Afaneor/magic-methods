class Enter(object):

    def __enter__(self):
        print('enter')
        return 'enter_value'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exited')


enter = Enter()

with enter as string:
    print(string)
