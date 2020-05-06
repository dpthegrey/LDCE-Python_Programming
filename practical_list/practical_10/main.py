class Value:
    def __init__(self, a):
        self.a = a

    def mul(self, t):
        return self.a * t.a

obj1 = Value(3)
obj2 = Value(9)
print("4 * 6 =", obj1.mul(obj2))
obj3 = Value('pop')
obj4 = Value(4)

print("'A' * 8 =", obj3.mul(obj4))
