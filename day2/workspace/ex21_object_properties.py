class Book:
    def __init__(self, **kwargs):
        self.title = kwargs.get('title')            # calls setter for `title`
        self.price = kwargs.get('price')            # calls setter for `price`
        self.page_count = kwargs.get('page_count')  # calls setter for `page_count`

    def __str__(self):
        return f'Book(title={self.__title!r}, price={self.__price!r}, page_count={self.__page_count!r})'

    # property called `title` (getter)
    @property
    def title(self):
        return self.__title
    # setter for the property `title`
    @title.setter
    def title(self, value):
        if value is None:
            self.__title = None
        elif isinstance(value, str):
            if len(value.strip()) == 0:
                raise ValueError('Cannot assign empty string')
            self.__title = value
        else:
            raise TypeError('Invalid type of value assigned. Must be a `str` or None')

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value is None:
            self.__price = None
        elif type(value) in (int, float):
            if value < 0:
                raise ValueError('Price cannot be negative')
            self.__price = value
        else:
            raise TypeError('Price must be a number')
        
    @property
    def page_count(self):
        return self.__page_count
    
    @page_count.setter
    def page_count(self, value):
        if value is None:
            self.__page_count = None
        elif isinstance(value, int):
            if value < 50:
                raise ValueError('Book should have at least 50 pages')
            if value > 10000:
                raise ValueError('Book cannot have more than 10000 pages')
            self.__page_count = value
        else:
            raise TypeError('Page count must be a number')


def main():
    b1 = Book(title='Let us C', price=599, page_count=298)
    b2 = Book()
    b2.title = 'Learn Python'
    b2.price = 999.99
    b2.page_count = 345

    print(f'{b1.title = }')
    print(f'{b1.price = }')
    print(f'{b1.page_count = }')
    print(b1)
    print(b2)

    # AttributeError: 'Book' object has no attribute '__title'. Did you mean: 'title'?
    # print(f'{b1.__title = }')
    # print(f'{b1.__price = }')
    # print(f'{b1.__page_count = }')
    


if __name__ == '__main__':
    main()