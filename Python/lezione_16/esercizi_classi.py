#es1
"""class Contatore:
    def __init__(self) -> None:
        self.conteggio = 0

    def setZero(self):
        self.conteggio = 0

    def add1(self):
        self.conteggio += 1

    def sub1(self):
        if self.conteggio > 0:
            self.conteggio -= 1
        else:
            print(f'Non è possibile eseguire la sottrazione')
    
    def get(self):
        return self.conteggio
    
    def mostra(self):
        print(f'Conteggio attuale: {self.conteggio}')

c = Contatore()  
c.add1() 
c.mostra()

c = Contatore()  
c.sub1()  
c.mostra()

c = Contatore() 
c.add1()
c.add1()
c.add1()
c.add1()
c.sub1()  
c.add1()
c.add1()
z  = c.get()
print(z)"""

#es2
"""class RecipeManager:
    def __init__(self) -> None:
        self.recipes = {}

    def create_recipe(self, name: str, ingredients: list[str]):
        if name in self.recipes:
            return f"{name} già esiste"
        self.recipes[name] = ingredients
        return {name: ingredients}

    def add_ingredient(self, recipe_name: str, ingredient: str):
        if recipe_name not in self.recipes:
            return f"{recipe_name} non esiste"
        if ingredient in self.recipes[recipe_name]:
            return f"{ingredient} è già presente nella lista"
        self.recipes[recipe_name].append(ingredient)
        return {recipe_name: self.recipes[recipe_name]}

    def remove_ingredient(self, recipe_name: str, ingredient: str):
        if recipe_name not in self.recipes:
            return f"{recipe_name} non esiste"
        if ingredient not in self.recipes[recipe_name]:
            return f"{ingredient} non esiste nella lista degli ingredienti"
        self.recipes[recipe_name].remove(ingredient)
        return {recipe_name: self.recipes[recipe_name]}
    
    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str):
        if recipe_name not in self.recipes:
            return f"{recipe_name} non esiste"
        if old_ingredient not in self.recipes[recipe_name]:
            return f"{old_ingredient} non esiste nella lista degli ingredienti di {recipe_name}"
        if new_ingredient in self.recipes[recipe_name]:
            return f"{new_ingredient} è già presente nella lista degli ingredienti di {recipe_name}"
        for i in range(len(self.recipes[recipe_name])):
            if self.recipes[recipe_name][i] == old_ingredient:
                self.recipes[recipe_name][i] = new_ingredient
                break
        return {recipe_name: self.recipes[recipe_name]}
    
    def list_recipes(self):
        return list(self.recipes.keys())
    
    def list_ingredients(self, recipe_name: str):
        if recipe_name not in self.recipes:
            return f"{recipe_name} non esiste"
        return self.recipes[recipe_name]
    
    def search_recipe_by_ingredient(self, ingredient: str):
        found_recipes = {}
        for name, ingredients in self.recipes.items():
            if ingredient in ingredients:
                found_recipes[name] = ingredients
        return found_recipes
"""
#es3
"""class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
    
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")


class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte
    
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}")


class Moto(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self.tipo = tipo
    
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")
"""
#es4

class Specie:
    def __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float):
        self.nome = nome 
        self.popolazione = popolazione_iniziale
        self.tasso_crescita = tasso_crescita

    def cresci(self):
        """Calcola la popolazione dell'anno successivo."""
        self.popolazione = int(self.popolazione * (1 + self.tasso_crescita / 100))

    def anni_per_superare(self, altra_specie: 'Specie') -> int:
        """Determina in quanti anni la popolazione di questa specie supererà quella dell'altra."""
        anni = 0  # int: Contatore degli anni
        while self.popolazione <= altra_specie.popolazione:  # Loop finché questa popolazione non supera l'altra
            self.cresci()  # Incrementa la popolazione di questa specie
            altra_specie.cresci()  # Incrementa la popolazione dell'altra specie
            anni += 1  # Incrementa il contatore degli anni
            if anni > 1000:  # Impostiamo un limite per evitare loop infiniti
                return f"{self.nome} non supererà mai {altra_specie.nome}"  # Ritorna un messaggio se il limite è raggiunto
        return anni  # Ritorna il numero di anni necessari
    
    def getDensita(self, area_kmq: float) -> int:
        """Calcola gli anni necessari per raggiungere una densità di 1 individuo per km quadrato."""
        if not area_kmq:  # Controlla se l'area è specificata
            return "Area non specificata"  # Ritorna un messaggio di errore
        anni = 0  # int: Contatore degli anni
        while self.popolazione / area_kmq < 1:  # Loop finché la densità è inferiore a 1 individuo/km²
            self.cresci()  # Incrementa la popolazione
            anni += 1  # Incrementa il contatore degli anni
        return anni  # Ritorna il numero di anni necessari

# Sottoclasse per Bufalo Klingon
class BufaloKlingon(Specie):
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__("Bufalo Klingon", popolazione_iniziale, tasso_crescita)  # Inizializza la classe base

# Sottoclasse per Elefante
class Elefante(Specie):
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__("Elefante", popolazione_iniziale, tasso_crescita)  # Inizializza la classe base

# Creazione delle istanze delle specie
bufalo_klingon = BufaloKlingon(100, 15)  # Crea un'istanza di BufaloKlingon con popolazione 100 e tasso di crescita 15%
elefante = Elefante(10, 35)  # Crea un'istanza di Elefante con popolazione 10 e tasso di crescita 35%

# Calcolo degli anni necessari per superare
anni_necessari = elefante.anni_per_superare(bufalo_klingon)  # Calcola gli anni necessari affinché gli elefanti superino i bufali Klingon
print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}")

# Calcolo della densità di popolazione per i Bufali Klingon
anni_densita = bufalo_klingon.getDensita(1500)  # Calcola gli anni necessari per raggiungere una densità di 1 bufalo Klingon per km²
print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: {anni_densita}")