"""Calculating the factorial of large numbers."""
import sys
from typing import Tuple
from multiprocessing import Pool
import math

NUMBER = 30

def partial_factorial(range_tuple: Tuple) -> int:
    """Calculates the product of numbers from start to end included."""
    start, end = range_tuple
    result = 1
    for num in range(start, end + 1):
        result *= num
    return result


if __name__ == "__main__":
    num_processes = 4
    part_size = NUMBER // num_processes
    ranges = []

    for i in range(num_processes):
        start_num = i * part_size + 1
        end_num = (i + 1) * part_size if i < num_processes - 1 else NUMBER
        ranges.append((start_num, end_num))

    with Pool(processes=num_processes) as pool:
        partial_results = pool.map(partial_factorial, ranges)

    factorial_result = 1
    for pr in partial_results:
        factorial_result *= pr

    sys.stdout.write(f"{NUMBER}! = {factorial_result}\n")
    sys.stdout.write(f"Check with math.factorial: {math.factorial(NUMBER)}")