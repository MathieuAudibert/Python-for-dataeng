def sont_identiques(f1, f2):
    try:
        with open(f1, 'rb') as file1, open(f2, 'rb') as file2:
            while True:
                chunk1 = file1.read(1024)
                chunk2 = file2.read(1024)
                if chunk1 != chunk2:
                    return False
                if not chunk1:
                    return True
    except FileNotFoundError:
        print("introuvable")
        return False
    except IOError as e:
        print(f"Erreur: {e}")
        return False
    
print(sont_identiques('fichier2.txt', 'fichier2.txt'))