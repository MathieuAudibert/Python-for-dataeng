#!bin/bash/env/python3
from random import randrange

def main():
    result = input('resultat: ')
    randomizer = lambda a, b : a + b
    result_random = randomizer(randrange(10), randrange(10))
    if result == result_random:
        print(result_random)
        print("+ 1000 pts")
    else: 
        print(result_random)
        print("Naaan")
    
if __name__ == "__main__":
    main()