import csv
import json
import time


def main():
    csv_filename = input('Enter csv filename: ')
    if not csv_filename.endswith('.csv'):
        raise ValueError('Invalid filename. Must be CSV file.')
    
    # csv_file = open(csv_filename, 'rt', encoding='utf-8')
    with open(csv_filename, 'rt', encoding='utf-8') as csv_file:
        # when this block is exited, csv_file.close() is automatically called
        reader = csv.DictReader(csv_file)
        customers = [c for c in reader]
        
    json_filename = f'{csv_filename[:-4]}_{round(time.time())}.json'
    with open(json_filename, 'wt', encoding='utf-8') as json_file:
        json.dump(customers, json_file, indent=3)

    print(f'content from {csv_filename} is written in JSON format in {json_filename}.')


if __name__ == '__main__':
    main()
