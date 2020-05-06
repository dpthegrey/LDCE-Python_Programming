class Student1:
    def __init__(self, a):
        self.a = a

    def marks_a(self):
        print('Mark from Student1:', self.a)


class Student2:
    def __init__(self, b):
        self.b = b

    def marks_b(self):
        print('Mark from Student2:', self.b)


class Teacher(Student1, Student2):
    def __init__(self, a, b, c):
        Student1.__init__(self, a)
        Student2.__init__(self, b)
        self.c = c

    def marks_a_and_b(self):
        print('Mark from Teacher :', self.c)


obj = Teacher(81, 72, 93)
obj.marks_a()
obj.marks_b()
obj.marks_a_and_b()
