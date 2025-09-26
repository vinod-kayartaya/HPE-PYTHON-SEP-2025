class Employee:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.salary = kwargs.get('salary')
        self.department = kwargs.get('department')
        self.email = kwargs.get('email')

        self.fields = ['name', 'salary', 'email', 'department']
        self.n = 0

    def __str__(self):
        return f'Employee({self.name!r}, {self.salary!r}, {self.department!r}, {self.email!r})'
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n < len(self.fields):
            field = self.fields[self.n]
            self.n += 1
            return self.__dict__.get(field)
        raise StopIteration

def main():
    e1 = Employee(name='Ramesh', email='ramesh@xmpl.com', salary=45000, department='ASDF')
    print(e1)

    # print(next(e1))
    # print(next(e1))
    # print(next(e1))
    # print(next(e1))
    # print(next(e1))

    for info in e1:
        print(info)


if __name__ == '__main__':
    main()
