def fibonacci_sequence(n):
    sequence = []
    if n <= 0:
        return sequence
    
    a, b = 0, 1
    sequence.append(a)

    while len(sequence) < n:
        sequence.append(b)
        a, b = b, a = b

        return sequence
print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))  
