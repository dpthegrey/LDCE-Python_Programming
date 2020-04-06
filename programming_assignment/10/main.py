class Student():

    def __init__(self, r_no, name, age, marks):
        self.r_no = r_no
        self.name = name
        self.age = age
        self.marks = marks

    def displayStudent(self):
        print("Roll no : ", self.r_no, "Name : ", self.r_no,
              "Age : ", self.age,  "Marks : ", self.marks)

    def __str__(self):
        return f"{self.r_no},{self.name},{self.age},{self.marks}"

    def __eq__(self, other):
        return self.marks == other.marks


stu = []

for i in range(1, 3):
    print("Enter Details for Students %d" % (i))
    r_no = int(input("Enter Roll no:"))
    name = input("Enter Name:")
    age = int(input("Enter Age:"))
    marks = input("Enter Marks:")
    stu.append(Student(r_no, name, age, marks))

for s in stu:
    s.displayStudent()
