def fibonacci(n):
    fib_seq = [0, 1]
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    
    return fib_seq, n in fib_seq

numero = int(input("Informe um número: "))
sequencia, pertence = fibonacci(numero)

print(f"Sequência de Fibonacci até {numero}: {sequencia}")
if pertence:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")