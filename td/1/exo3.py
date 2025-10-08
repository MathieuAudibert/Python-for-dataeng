def perfect_number():
    perfect = []  
    for n in range(1, 10000):
        somme = sum(i for i in range(1, n) if n % i == 0)
        if somme == n:
            perfect.append(n)
    print(perfect)
perfect_number()