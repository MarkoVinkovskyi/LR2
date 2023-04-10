from functools import wraps

def count_sequence_length():
    @wraps(count_sequence_length)
    def wrapper():
        sequence_length = 0
        while True:
            n = int(input())
            if n != 0:
                sequence_length += 1
            else:
                break
        return sequence_length
    return wrapper

count_sequence_length = count_sequence_length()

print(count_sequence_length())


