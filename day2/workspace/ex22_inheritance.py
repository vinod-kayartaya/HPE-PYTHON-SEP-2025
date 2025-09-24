class Person:
    def __init__(self, name=None, city=None):
        self.name = name
        self.city = city

    def print(self):
        print(f'Name    : {self.name}')
        print(f'City    : {self.city}')


class Employee(Person):
    def  __init__(self, name=None, city=None, salary=None, department=None):
        super().__init__(name, city)
        self.salary = salary
        self.department = department

    def print(self):
        print('----------------')
        print('EMPLOYEE DETAILS')
        print("================")
        super().print()
        print(f'Salary  : {self.salary}')
        print(f'Dept    : {self.department}')


# create a new sub-class of `Person` called `Student`.
# Student has fields - name, city, college, cgpa
# Student has initializer and a print function to print student details

class Student(Person):
    def  __init__(self, name=None, city=None, college=None, cgpa=None):
        super().__init__(name, city)
        self.college = college
        self.cgpa = cgpa

    def print(self):
        print('---------------')
        print('STUDENT DETAILS')
        print("===============")
        super().print()
        print(f'College : {self.college}')
        print(f'CGPA    : {self.cgpa}')


def print_persons_details(persons):
    for person in persons:
        if not isinstance(person, Person):
            continue
        person.print()


def main():
    people = [
        Student('Ram', 'Delhi', 'XYZ University', 7.5),
        'Kumar, Kerala, 45000, "FINANCE"',
        Employee('Vishal', 'Mysore', 45000, 'ADMIN'),
        Student('Shyam', 'Delhi', 'XYZ University', 4.5),
        Employee('Kishore', 'Vasco', 66780, 'PRODCTION'),
        Employee('Kiran', 'Bangalore', 35000, 'ACCOUNTING'),
        Student('Hemanth', 'Mumbai', 'BITS', 6.3),
    ]

    print_persons_details(people)


def main_1():
    p1 = Person('Vinod', 'Bangalore')
    p1.print()
    print('-' * 50)

    e1 = Employee('Vishal', 'Mysore', 45000, 'ADMIN')
    e1.print()
    print('-' * 50)

    s1 = Student('Amar', 'Delhi', 'XYZ University', 5.6)
    s1.print()
    print('-' * 50)


if __name__ == '__main__':
    main()
