class Book:
    available_genres = ['Thriller', 'Comedy', 'Romance']

    def __init__(self, title, price, genre='Romance'):
        self.title = title
        self.price = price

        if genre not in Book.available_genres:
            self.genre = 'General'
        else:
            self.genre = genre

    def __str__(self):
        return f'Book(title={self.title!r},price={self.price!r},genre={self.genre!r})'
    
if __name__ == '__main__':
    b1 = Book('Kill bill', 799, 'Thriller')
    b2 = Book('Guns and roses', 555)
    b3 = Book('Let us C', 789, 'Computers')

    print(b1)
    print(b2)
    print(b3)

    print(f'{b1.available_genres = }')
    print(f'{b2.available_genres = }')
    print(f'{b3.available_genres = }')

    b1.available_genres.append('Computers')

    print(f'{b1.available_genres = }')
    print(f'{b2.available_genres = }')
    print(f'{b3.available_genres = }')
