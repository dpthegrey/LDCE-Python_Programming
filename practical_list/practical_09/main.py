class SuperClass:
    def fun(self):
        print('SuperClass')

class SubClass(SuperClass):
    def fun(self):
        print('Subclass')

print('Method called using object of Super class')
SuperClass().fun()
print('Method with same name called using object of Sub class')
SubClass().fun()