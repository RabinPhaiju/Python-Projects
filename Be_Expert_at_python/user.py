from library import Base

# assert hasattr(Base, 'foo'), 'foo method doesnt exist.'

class Derived(Base):
    def bar(self):
        return self.foo()


d1 = Derived()
print(d1.bar())