def main():
    entier = int(input("entier: "))
    
    if entier < 2:
        print("nan")

    with open("tables.txt", "w") as file:
        for i in range(11):
            result = i*entier
            file.write(f"{str(result)}\n")

main()