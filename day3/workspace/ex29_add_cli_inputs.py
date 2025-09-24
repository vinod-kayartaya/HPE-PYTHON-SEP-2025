import sys


def main():
    # print(f'{type(sys.argv) = }')
    # print(f'{sys.argv = }')
    args = sys.argv[1:]
    nums = [int(n) for n in args if n.isnumeric()]
    # print(f'{nums = }')
    total = sum(nums)
    print(f'{nums = }, {total = }')


if __name__ == '__main__':
    main()
