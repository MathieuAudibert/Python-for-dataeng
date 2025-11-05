def main():
    input_file = "tables.txt"
    output_file = "fichier2.txt"

    with open(input_file, "r") as file:
        lines = file.readlines()

    with open(output_file, "w") as file:
        file.writelines(reversed(lines))

if __name__ == "__main__":
    main()