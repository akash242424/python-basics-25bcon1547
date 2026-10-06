class Student:
    def __init__(self):
        self.name = ""
        self.roll = 0
        self.marks = 0.0


s1 = Student()

s1.name = "rahul"
s1.roll = 101
s1.marks = 87.5

print(f"Name: {s1.name}")
print(f"Roll: {s1.roll}")
print(f"Marks: {s1.marks:.2f}")