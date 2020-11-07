# class BaseMeta(type):
#     def __new__(cls, name, bases, body):
#         if 'bar' not in body:
#             raise TypeError("bad user class")
#         return super().__new__(cls, name, bases, body)

# class Base(metaclass=BaseMeta):
class Base:
    def foo(self):
        return 'foo'

    def __init_subclass__(cls, *a, **kw):
        print ('init_subclass', a, kw)
        return super().__init_subclass__( *a, **kw)