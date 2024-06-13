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

