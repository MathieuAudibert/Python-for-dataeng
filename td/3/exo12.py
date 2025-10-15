class Livre:
    __titre = ""
    __auteur = ""
    __isbn = 0
    __disponible = False

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
        self.__nombre_pages = n

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
        self.__email = e

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
