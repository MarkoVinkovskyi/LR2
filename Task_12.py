from typing import List

def read_sequence() -> List[int]:
    sequence = []
    number = int(input())
    while number != 0:
        sequence.append(number)
        number = int(input())
    return sequence

def find_max(sequence: List[int]) -> int:
    return max(sequence)

def main():
    sequence = read_sequence()
    max_element = find_max(sequence)
    print(max_element)

if __name__ == "__main__":
    main()
