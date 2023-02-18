import json
import argparse
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument('--output', type=str, required=True, help='Output folder for chunked JSON files')
parser.add_argument('--filename', type=str, required=True, help='Name of the BloodHound JSON file')
parser.add_argument('--chunks', type=int, default=100, help='Number of chunks to split the BloodHound JSON file into')

args = parser.parse_args()

def main(args):
    data = import_json(args.filename)

    count = data['meta']['count']
    data_type = data['meta']['type']
    version = data['meta']['version']

    chunks = json_chunks(data, args.chunks)
    idx = 0

    for chunked in chunks:
        new_file = {
            "data": [],
            "meta": {
                "type": data_type,
                "version": version,
                "count": 0
            }
        }
        for chunk in chunked:
            new_file['data'].append(chunk)
            new_file['meta']['count'] += 1

        new_path = f'{args.output}/chunk_{idx}.json'
        write_json(new_file, new_path)
        idx += 1

def write_json(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

def import_json(filename):
    with open(filename) as f:
        data = json.load(f)
    return data

def json_chunks(data, chunks):
    total_count = data['meta']['count']
    chunk_size = total_count // chunks
    chunks_list = []
    for i in range(0, total_count, chunk_size):
        chunks_list.append(data['data'][i:i + chunk_size])
    return chunks_list

if __name__ == '__main__':
    main(args)
