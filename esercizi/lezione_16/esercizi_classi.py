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

class RecipeManager:
    def __init__(self) -> None:
        self.recipes = {}

    def create_recipe(self, name: str, ingredients: list[str]):
        self.name = name
        self.ingredients = ingredients
        ingredients = []

        if name not in self.recipes and ingredients not in self.recipes:
            self.recipes[name] = ingredients
            return self.recipes
        elif name and ingredients in self.recipes:
            print("Ricetta già esistente")
    
    def add_ingredient(self, recipe_name: str, ingredient: str):

        recipe_name = self.name
        if ingredient not in self.ingredients:
            self.ingredients.append(ingredient)
            return self.ingredients
        else:
            print("L'ingrediente è già presente nella lista")

    def remove_ingredient(self, recipe_name: str, ingredient: str):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)
        else:
            print("L'ingrediente non esiste")
    
    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str):
        for i in range(len(self.ingredients)):
            if self.ingredients[i] == old_ingredient:
                self.ingredients[i] = new_ingredient
                return self.ingredients
        print("L'ingrediente non esiste")
        return self.ingredients