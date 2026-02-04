class Student:
    def _init_(self, name, course):
        self.name = name
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Course:", self.course)

s1 = Student("Sandhya", "MCA")
s1.display()
