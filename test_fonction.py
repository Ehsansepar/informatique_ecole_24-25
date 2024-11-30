def fibonacci(n) : 
    liste = [0, 1]

    for i in range(2, n) :
        next_fib = liste[-1] + liste[-2]
        liste.append(next_fib)
    return liste
print(
fibonacci(10)
)