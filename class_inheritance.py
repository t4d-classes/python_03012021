

class Person:

    @classmethod
    def create(cls, name):
        first_name, last_name = name.split(" ")
        return Person(first_name, last_name)

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    # encapsulation
    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

person = Person.create("Anastasia Anderson")
print(person.full_name())
print(person.create("Sam Thomas"))

print(id(Person), Person)
print(id(Person.create), Person.create)
print(id(person), person)

            # inheritance
class Student(Person):

    def __init__(self, student_id, first_name, last_name):
        Person.__init__(self, first_name, last_name)
        self.student_id = student_id

    # polymorphism
    def full_name(self):
        base_method_result = super().full_name()
        return f"Override: {base_method_result}"

    def record_info(self):
        return f"{self.student_id} {self.last_name}, {self.first_name}"

student = Student(1, "Bob", "Smith")
print(student.full_name())
print(student.record_info())

class Instructor(Person):

    def __init__(self, instructor_id, first_name, last_name):
        Person.__init__(self, first_name, last_name)
        self.instructor_id = instructor_id

    def employee_info(self):
        return f"{self.instructor_id} {self.last_name}, {self.first_name}"

instructor = Instructor(1, "Sally", "Timmons")
print(instructor.full_name())
print(instructor.employee_info())

class Member(Student, Instructor):

    def __init__(self, member_id, first_name, last_name):
        Student.__init__(self, member_id, first_name, last_name)
        Instructor.__init__(self, member_id, first_name, last_name)

    def member_info(self):
        return f"Member: {self.first_name}"


member = Member(1, "Alison", "Page")

print(member.full_name())
print(member.record_info())
print(member.employee_info())
print(member.member_info())

print(Member.__mro__)