class Student:
    def __init__(self, name, age, email, course, grade="N/A"):
        self.name   = name
        self.age    = age
        self.email  = email
        self.course = course
        self.grade  = grade

    def display(self):
        print(f"""
  ┌─────────────────────────────┐
  │  Name   : {self.name}
  │  Age    : {self.age}
  │  Email  : {self.email}
  │  Course : {self.course}
  │  Grade  : {self.grade}
  └─────────────────────────────┘""")

    def __str__(self):
        return f"Student({self.name}, {self.course}, Grade: {self.grade})"


class Course:
    def __init__(self, name, duration_months, instructor):
        self.name             = name
        self.duration_months  = duration_months
        self.instructor       = instructor

    def display(self):
        print(f"""
  Course    : {self.name}
  Duration  : {self.duration_months} months
  Instructor: {self.instructor}""")