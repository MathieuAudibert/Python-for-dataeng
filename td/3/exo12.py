class Livre:
    __titre = ""
    __auteur = ""
    __isbn = 0
    __disponible = True
    __reservations = []

    def __init__(self, titre, auteur, isbn, disponible):
        self.__titre = titre
        self.__auteur = auteur
        self.__isbn = isbn
        self.__disponible = disponible

    @property 
    def titre(self):
        return self.__titre
    @titre.setter
    def titre(self, t):
        self.__titre = t
    
    @property
    def auteur(self):
        return self.__auteur
    @auteur.setter
    def auteur(self, a):
        self.__auteur = a

    @property
    def isbn(self):
        return self.__isbn
    @isbn.setter
    def isbn(self, i):
        self.__isbn = i

    @property
    def disponible(self):
        return self.__disponible
    @disponible.setter
    def disponible(self, d):
        self.__disponible = d

    def afficher_infos(self):
        print(f"titre: {self.__titre}")
        print(f"auteur: {self.__auteur}")
        print(f"isbn: {self.__isbn}")
        print(f"disponible?: {self.__disponible}")
    
    def emprunter(self):
        self.__disponible = False

    def remettre(self):
        self.__disponible = True
    
    def reserver(self, abonne):
        if abonne not in self.__reservations:
            self.__reservations.append(abonne)

    @property
    def reservations(self):
        return self.__reservations

class LivrePhysique(Livre):
    __emplacement = ""
    __nombre_pages = 0

    def __init__(self, titre, auteur, isbn, disponible, emplacement, nombre_pages):
        super().__init__(titre, auteur, isbn, disponible)
        self.__emplacement = emplacement
        self.__nombre_pages = nombre_pages
        
    @property
    def emplacement(self):
        return self.__emplacement
    @emplacement.setter
    def emplacement(self, e):
        self.__emplacement = e

    @property
    def nombre_pages(self):
        return self.__nombre_pages
    @nombre_pages.setter
    def nombre_pages(self, n):
        if n < 0 :
            raise ValueError("Nombre pages doit etre > 0")
        self.__nombre_pages = n
    
    def afficher_infos(self):
        print(f"titre: {self.titre}")
        print(f"auteur: {self.auteur}")
        print(f"isbn: {self.isbn}")
        print(f"disponible?: {self.disponible}")
        print(f"emplacement: {self.emplacement}")
        print(f"nombre_pages: {self.nombre_pages}")

class LivreNumerique(Livre):
    __taille_fichier = 0
    __format = ""

    def __init__(self, titre, auteur, isbn, disponible, taille_fichier, format):
        super().__init__(titre, auteur, isbn, disponible)
        self.__taille_fichier = taille_fichier
        self.__format = format
    
    @property
    def taille_fichier(self):
        return self.__taille_fichier
    @taille_fichier.setter
    def emplacement(self, t):
        self.__taille_fichier = t

    @property
    def format(self):
        return self.__format
    @format.setter
    def format(self, f):
        self.__format = f
    
    def afficher_infos(self):
        print(f"titre: {self.titre}")
        print(f"auteur: {self.auteur}")
        print(f"isbn: {self.isbn}")
        print(f"disponible?: {self.disponible}")
        print(f"taille_fichier: {self.taille_fichier}")
        print(f"format: {self.format}")

class Abonne:
    __nom = ""
    __id = 0
    __email = ""

    def __init__(self, nom, id, email):
        self.__nom = nom
        self.__id = id
        self.__email = email

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def emplacement(self, n):
        self.__nom = n

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, i):
        self.__id = i
    
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, e):
        if "@" not in e:
            raise ValueError("Manque @ dans le mail")
        self.__email = e
    
    def afficher_infos(self):
        print(f"nom: {self.nom}")
        print(f"id: {self.id}")
        print(f"email: {self.email}")

class Etudiant(Abonne):
    __classe = ""
    __specialite = ""

    def __init__(self, nom, id, email, classe, specialite):
        super().__init__(nom, id, email)
        self.__classe = classe
        self.__specialite = specialite
    
    @property
    def classe(self):
        return self.__classe
    @classe.setter
    def classe(self, c):
        self.__classe = c
    
    @property
    def specialite(self):
        return self.__specialite
    @specialite.setter
    def specialite(self, s):
        self.__specialite = s

    def afficher_infos(self):
        print(f"nom: {self.nom}")
        print(f"id: {self.id}")
        print(f"email: {self.email}")
        print(f"classe: {self.classe}")
        print(f"specialite: {self.specialite}")

class Professeur(Abonne):
    __classe = ""
    __specialite = ""

    def __init__(self, nom, id, email, classe, specialite):
        super().__init__(nom, id, email)
        self.__classe = classe
        self.__specialite = specialite

    @property
    def classe(self):
        return self.__classe
    @classe.setter
    def classe(self, c):
        self.__classe = c
    
    @property
    def specialite(self):
        return self.__specialite
    @specialite.setter
    def specialite(self, s):
        self.__specialite = s

    def afficher_infos(self):
        print(f"nom: {self.nom}")
        print(f"id: {self.id}")
        print(f"email: {self.email}")
        print(f"classe: {self.classe}")
        print(f"specialite: {self.specialite}")

class Bibliotheque:
    __abonnes = []
    __liste_livre = []

    def __init__(self, abonnes, liste_livre):
        self.__abonnes = abonnes
        self.__liste_livre = liste_livre

    @property
    def abonnes(self):
        return self.__abonnes
    @abonnes.setter
    def abonnes(self, a):
        self.__abonnes = a
    
    @property
    def liste_livre(self):
        return self.__liste_livre
    @liste_livre.setter
    def liste_livre(self, l):
        self.__liste_livre = l

    def ajouter_livre(self, l):
        self.__liste_livre.append(l)

    def ajouter_abonne(self, a):
        self.__abonnes.append(a)

    def afficher_livres_disponibles(self):
        for livre in self.__liste_livre:
            if livre.__disponible == True:
                print(livre)
    
    def emprunter_livre(self, abonne, livre):
        for l in self.__liste_livre:
            if l == livre and l.disponible:
                if not hasattr(abonne, "_emprunts"):
                    abonne._emprunts = []
                if len(abonne._emprunts) >= 5:
                    print("Max 5")
                    return
                l.emprunter()
                abonne._emprunts.append(l)
                print(f"{abonne.nom} emprunte '{l.titre}'.")
                return
        print(f"livre '{livre.titre}' pas dispo.")
    
    def rendre_livre(self, abonne, livre):
        if hasattr(abonne, "_emprunts") and livre in abonne._emprunts:
            livre.remettre()
            abonne._emprunts.remove(livre)
            print(f"{abonne.nom} rends '{livre.titre}'.")
        else:
            print(f"{abonne.nom} emprunte '{livre.titre}'.")
    
    def afficher_emprunts(self, abonne):
        if hasattr(abonne, "_emprunts") and abonne._emprunts:
            print(f"A emprunte {abonne.nom}:")
            for livre in abonne._emprunts:
                print(f"- {livre.titre}")
            else:
                print(f"{abonne.nom} a pas emprunte")

etudiant1 = Etudiant("Mathieu", 1, "mathieu@a.com", "MSC", "Data Science")
professeur1 = Professeur("Mathieu2", 2, "math2@b.com", "MSC", "Computer Science")

livre1 = LivrePhysique("Python for dataeng", "Mathieu3", 12345, True, "A4", 250)
livre2 = LivreNumerique("Data Science", "Mathieu4", 67890, True, 5, "PDF")

biblio = Bibliotheque([etudiant1, professeur1], [livre1, livre2])

etudiant1.afficher_infos()
professeur1.afficher_infos()
livre1.afficher_infos()
livre2.afficher_infos()

biblio.emprunter_livre(etudiant1, livre1)
biblio.afficher_emprunts(etudiant1)
biblio.rendre_livre(etudiant1, livre1)
biblio.afficher_emprunts(etudiant1)

livre2.reserver(etudiant1)
print(livre2.reservations)

