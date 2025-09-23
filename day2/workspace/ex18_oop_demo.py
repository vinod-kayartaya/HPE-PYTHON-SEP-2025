"""

Elements of OOP: 

4 major elements:
- Modularity
- Abstraction
- Encapsulation
- Hierarchy (code reusability)
    - Aggregation (HAS-A) whole-part association
    - Inheritance (IS-A) type-of or generalization/specialization association
        - Polymorphism is a side-effect of inheritance
3 minor elements:
- Typing
- Persistence
- Concurrency


class Animal {
    roar(){}
}
class Tiger extends Animal {
    roar(){ // tiger specific roaring}
}
class Lion extends Animal {
    roar(){ // lion specific roaring}
}

Animal a1;

animal_sound(Animal x){
    x.roar()
}

animal_sound(new Tiger());
animal_sound(new Lion());
"""


# create a class (template for creating objects)
class Book:
    # python calls this method automatically, after allocating memory for an object
    def __init__(self):
        print('Book.__init__ called')
        self.title = None       # create a new member called `title`
        self.price = 0.0
        self.no_of_pages = 0


if __name__ == '__main__':
    # create an object of a class
    b1 = Book()     # In Java/C#, Book b1 = new Book()
    # print(f'{type(b1)}')
    print(dir(b1))
    b2 = Book()
    print(b1)
    print(b2)