import csv


filename = 'customers.csv'

def read_from_csv_file():
    with open(filename, 'rt', encoding='utf-8') as file:
        for line in file:
            row = [int(f) if f.isnumeric() else f for f in line.strip().split(',')]
            print(row)


def read_from_csv_file_using_csv_module():
    with open(filename, 'rt', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            row = [int(f) if f.isnumeric() else f for f in row]
            print(row)

def read_from_csv_file_into_dict():
    with open(filename, 'rt', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for d in reader:
            print(d)
        # file.close() is called automatically here

def main():
    # read_from_csv_file()
    # read_from_csv_file_using_csv_module()
    read_from_csv_file_into_dict()


if __name__ == '__main__':
    main()
