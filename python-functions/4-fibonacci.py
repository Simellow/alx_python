def fibonacci_sequence(n):
    if n <= 2:
        return [0, 1][:n]
    sequence = fibonacci_sequence(n - 1)
    sequence.append(sum(sequence[-2:]))
    return sequence
