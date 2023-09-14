from functools import reduce
import operator
from pprint import pprint

def num_of_connections_complete_g(n):
    return (n*n - n) / 2

def get_overlaps(bucket):
    overlaps = 0
    for key, value in bucket.items():
        overlaps += num_of_connections_complete_g(value)
    return overlaps

def get_hash_overlaps(buckets):
    overlaps = {}
    for bucket, value in buckets.items():
        overlaps[bucket] = get_overlaps(value)
    return overlaps

def get_bucket_hash_collisions(bucket):
    hash_matches = num_of_connections_complete_g(sum(bucket.values()))
    hash_collisions = hash_matches - get_overlaps(bucket)
    return hash_collisions

def get_hash_collisions(file_strings):
    buckets = get_double_hash_buckets(file_strings)
    collisions = sum(map(get_bucket_hash_collisions,buckets.values()))
    return int(collisions)

def get_cardinality(file_strings):
    return len(set(file_strings))

def get_double_hash_buckets(file_strings):
    hash_buckets = {}
    for f in file_strings:
        hash_byte = file_hash(f)
        bucket = hash_buckets.get(hash_byte, {})
        bucket[f] = bucket.get(f, 0) + 1
        hash_buckets[hash_byte] = bucket
    return hash_buckets

def file_hash(file_str):
    file_ascii_bytes = bytearray([ord(c) for c in file_str])
    file_xor_hash = reduce(operator.xor,file_ascii_bytes)
    return file_xor_hash
    

def get_files(num_files):
    files = []
    for _ in range(0,num_files):
        file_text = input()
        files.append(file_text)
    return files

def get_test_cases():
    test_cases = []
    while True:
        num_files = int(input())
        if num_files == 0:
            break
        test_cases.append(get_files(num_files))
    return test_cases


test_cases = get_test_cases()

for test_case in test_cases:
    for f in test_case:
        hash_byte = file_hash(f)
        # print(hex(hash_byte))

    buckets = get_double_hash_buckets(test_case)
    cardinality = get_cardinality(test_case)
    collisions = get_hash_collisions(test_case)
    print(cardinality, collisions)
    # print(f'unique files: {cardinality}')
    # print(f'hash_collisions:{collisions}')
    # pprint(buckets)
    # pprint(get_hash_overlaps(buckets))