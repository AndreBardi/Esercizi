class Media:
    def __init__(self, title: str) -> None:
        self.title = title
        self.reviews: list = []

    def set_title(self, title: str):
        self.title = title
    
    def get_title(self):
        return self.title
    
    def aggiungiValutazione(self, voto: int):        
        if 1 <= voto <= 5:
            self.reviews.append(voto)
        else:
            print('Error: Il voto non è valido')

    def getMedia(self) -> float:
        return sum(self.reviews) / len(self.reviews)
    
    def getRate(self):
        
        if self.getMedia() == 1:
            return "Terribile"
        elif 1 > self.getMedia() <= 2:
            return "Brutto"
        elif 2 > self.getMedia() <= 3:
            return "Normale"
        elif 3 > self.getMedia() <= 4:
            return "Bello"
        elif 4 > self.getMedia() <= 5:
            return "Grandioso"
        
    def ratePercentage(self, voto):
        x = self.reviews.count(voto)
        return x * 100 / len(self.reviews)
    
    def recensione(self):
        print(f'Titolo= {self.title}\nMedia voto={self.getMedia()}\nGiudizio= {self.getRate}\nTerribile={self.ratePercentage(1)}',
              f'\nBrutto={self.ratePercentage(2)}\nNormale={self.ratePercentage(3)}\nBello={self.ratePercentage(4)}\nGrandioso={self.ratePercentage(5)}')



class Film(Media):
    def __init__(self, title: str) -> None:
        super().__init__(title)

film1: Film = Film()

