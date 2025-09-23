from ex17_kwargs_demo import line

class Employee:
    # class/shared variable
    __count = 0     # using _ or __ as a prefix is informative for the developers as private

    def __init__(self, **kwargs):
        Employee.__count += 1
        self.empid = Employee.__count
        self.name = kwargs.get('name')
        self.salary = kwargs.get('salary', 25_000)
        self.department = kwargs.get('department', 'ACCOUNTING')
        self.email = kwargs.get('email')

    # for textual representation of an object of this class
    def __str__(self):
        return f'Employee(empid={self.empid!r}, name={self.name!r}, salary={self.salary!r}, department={self.department!r}, email={self.email!r})'
        
    def print(self):
        print(f'ID          : {self.empid}')
        print(f'Name        : {self.name}')
        print(f'Email       : {self.email}')
        print(f'Salary      : {self.salary}')
        print(f'Department  : {self.department}')
        line()

    # overrides the == operator
    # e1 == e3
    # e1.__eq__(e3)
    def __eq__(self, other):
        return self.empid == other.empid and \
            self.name == other.name and \
            self.department == other.department and \
            self.salary == other.salary


if __name__ == '__main__':
    e1 = Employee(name='Rajesh', department='ADMIN')
    e2 = Employee(name='Anil', salary=32000)

    e3 = Employee(name='Rajesh', department='ADMIN')
    e1.empid = e3.empid     # making e1 and e3 same

    print(e1)
    print(e3)

    print(f'{e1==e3 = }')
    print(f'e1!=e3 = {e1!=e3}')

    # print(e1)   # print(e1.__str__())
    # print(e2)

    # e1.print()
    # e2.print()
