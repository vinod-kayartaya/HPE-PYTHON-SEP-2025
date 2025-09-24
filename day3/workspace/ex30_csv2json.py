import argparse
import time
import csv
import json


def main():
    parser = argparse.ArgumentParser(description="Convert a CSV file into a JSON file")
    parser.add_argument("--source", help="CSV file for converting into JSON", required=True)
    parser.add_argument("--target", help="JSON filename. If not given, will be auto-generated")

    args = parser.parse_args()
    # print(f'{args = }')
    # print(f'{args.source = }')
    # print(f'{args.target = }')

    csv_filename = args.source
    if not csv_filename.endswith('.csv'):
        print('Invalid filename. Must be CSV file.')
        exit(1)
    
    json_filename = f'{csv_filename[:-4]}_{round(time.time())}.json' if args.target is None \
        else args.target
    
    with open(csv_filename, encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        data = [c for c in reader]
        
    with open(json_filename, 'wt', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=3)

    print(f'content from {csv_filename} is written in JSON format in {json_filename}.')

if __name__ == '__main__':
    main()
