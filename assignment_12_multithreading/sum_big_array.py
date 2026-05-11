import sys
from typing import List
import multiprocessing


def chunk_sum(numbers_list: List[int]) -> int:
    """Calculate the sum of all numbers in list."""
    return sum(numbers_list)


def split_list(numbers_list: List[int], chunks_count: int) -> List[List[int]]:
    """Splits a list of numbers into several chunks."""
    chunk_size = len(numbers_list) // chunks_count
    chunks_list = []

    for i in range(chunks_count):
        start = i * chunk_size
        end = None if i == chunks_count - 1 else (i + 1) * chunk_size
        chunks_list.append(numbers[start:end])

    return chunks_list


if __name__ == '__main__':
    numbers = list(range(1, 10_000_000))
    processes_count = multiprocessing.cpu_count()

    chunks = split_list(numbers, processes_count)

    with multiprocessing.Pool(processes_count) as pool:
        partial_sums = pool.map(chunk_sum, chunks)

    total_sum = sum(partial_sums)
    sys.stdout.write(f"Total sum: {total_sum}")
