class Squares:
    def __init__(self, max):
        self.max = max
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            result = self.n ** 2
            self.n += 1
            return result
        else:
            raise StopIteration
        

def main():
    sq = Squares(15)
    # print(next(sq))
    # print(next(sq))
    # print(next(sq))
    # print(next(sq))
    # print(next(sq))
    # print(next(sq))
    for s in sq:
        print(s)

if __name__ == '__main__':
    main()
