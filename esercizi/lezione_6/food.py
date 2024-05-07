class Food:
    def __init__(self, name, price, descriptions):
        self.name: str = name
        self.price: float = price
        self.descriptions: str = descriptions

class Menu:
    def __init__(self, foods: list[Food] = []):
        self.foods: list[Food] = foods
        
    def addFood(self, food:Food):
        self.foods.append(food)

    def removeFood(self, food:Food):
        if food in self.foods:
            self.foods.remove(food)

    def __str__(self) -> str:
        repr:str = ""
        for food in self.foods:
            repr += "\n" + food.__str__()
        return repr

food1 = Food(name="Pizza", price=8.90, descriptions="Margherita")
food2 = Food(name="Pasta", price= 6.90, descriptions="Cacio e Pepe")
food3 = Food(name="Steak", price=11.90, descriptions="Fiorentina")

menu = Menu((food1, food2, food3))

menu.addFood(Food("Fish", 12.90, "Sgombro"))
menu.addFood(Food("Vegetable", 5.90, "Iceberg"))

menu.removeFood(Food("Fish"))

print(menu)