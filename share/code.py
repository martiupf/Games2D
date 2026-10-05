from typing import Optional

def map(key: str, value: str):
    lines = value.split('\n')
    for line in lines:
        yield line.split()[2], 1

def reduce(key: str, values: list) -> str:
    return str(len(values))


def partitioner(key: str, partition_count: int) -> str:
    hash_value = 0
    for i, char in enumerate(key):
        hash_value = (hash_value * 16777619 + ord(char)) % partition_count
    return str(hash_value)