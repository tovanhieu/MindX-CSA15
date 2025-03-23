class Example:
    def __init__(self, content):
        self.content = content
    def __str__(self):
        return self.content
    def __add__(self, value):
        return self.content + value
    def __eq__(self, value):
        return self.content == value
    def __sub__(self,value):
        return self.content - value

    
ex1 = Example("Xin chào các bạn")
print("Print cách một")
print(ex1.__str__())
print("Print cách hai")
print(ex1)

print(ex1.__add__( " Mình tên là Elsa"))

ex2 = Example(3)
print(ex2.__add__(5))
print(ex2.__eq__(3))
print(ex2.__sub__(4))
# Xem các special method trong class hoặc object
# print(dir(Example))
# print(dir(ex1))

print("\n Kế thừa trong python \n")

class Person():
    def __init__(self, name) -> None:
        self.name = name
    def printName(self):
        print('Tên tôi là ',self.name)

class Student(Person):
    def __init__(self, name, grade) -> None:
        super().__init__(name)
        self.grade = grade
    def printGrade(self):
        print('Tôi học lớp ',self.grade)

    def printName(self):
        print("My name is: ",self.name)

class Worker(Person):
    def __init__(self, name, companyName) -> None:
        super().__init__(name)
        self.companyName = companyName
    def printCompanyName(self):
        print("Tôi làm tại công ty ",self.companyName)


p1 = Person("Khoa")
p1.printName()
p2 = Student("Hải Anh",12)
p2.printName()
p2.printGrade
p2.printGrade()

p3 = Worker("Hiệu","MindX Technology School")
p3.printName()
p3.printCompanyName()
        
        