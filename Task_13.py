

from typing import List, Tuple

def read_sequence() -> List[int]:
    sequence = []
    number = int(input())
    while number != 0:
        sequence.append(number)
        number = int(input())
    return sequence

def find_second_largest(sequence: List[int]) -> int:
    max_one = max(sequence)
    sequence.remove(max_one)
    max_two = max(sequence)
    return max_two

def main():
    sequence = read_sequence()
    second_largest = find_second_largest(sequence)
    print(second_largest)

if __name__ == "__main__":
    main()
