"""
Sistema di Prenotazione Cinema
Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. 
Il cinema ha diverse sale, ognuna con un diverso film in programmazione. 
Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.

Classi:
- Film: Rappresenta un film con titolo e durata.
 
- Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.
Metodi:

    - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
    - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
- Cinema: Gestisce le operazioni legate alla gestione delle sale.
Metodi:

    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.

Test case:
Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
Un cliente sceglie un film e prenota un certo numero di posti.
Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.
"""

class Film:
    def __init__(self, titolo: str, durata: float):
        self.titolo = titolo
        self.durata = durata

    def __str__(self):
        return f"Film: {self.titolo}, Durata: {self.durata} minuti"

class Sala:
    def __init__(self, num_id: int, film: Film, posti_totali: int):
        self.num_id = num_id
        self.film = film
        self.posti_totali = posti_totali
        self.posti_prenotati = 0

    def prenota_posti(self, num_posti: int):
        if num_posti <= 0:
            return 'Numero di posti non valido.'
        if self.posti_prenotati + num_posti > self.posti_totali:
            return 'Errore: posti insufficienti disponibili.'
        self.posti_prenotati += num_posti
        return f'{num_posti} posti prenotati con successo.'

    def posti_disponibili(self):
        return self.posti_totali - self.posti_prenotati

    def __str__(self):
        return (f"Sala {self.num_id}, Film in programmazione: {self.film.titolo}, "
                f"Posti totali: {self.posti_totali}, Posti prenotati: {self.posti_prenotati}, "
                f"Posti disponibili: {self.posti_disponibili()}")

class Cinema:
    def __init__(self):
        self.nuova_sala = []

    def aggiungi_sala(self, sala: Sala):
        self.nuova_sala.append(sala)
        return f"Sala {sala.num_id} aggiunta con successo."

    def prenota_film(self, titolo_film: str, num_posti: int):
        for sala in self.nuova_sala:
            if sala.film.titolo == titolo_film:
                return sala.prenota_posti(num_posti)
        return f'Errore: film "{titolo_film}" non trovato.'

    def __str__(self):
        return "\n".join(str(sala) for sala in self.nuova_sala)

film1 = Film("Inception", 148)
film2 = Film("The Matrix", 136)

sala1 = Sala(1, film1, 100)
sala2 = Sala(2, film2, 150)

cinema = Cinema()
print(cinema.aggiungi_sala(sala1) + "\n")
print(cinema.aggiungi_sala(sala2) + "\n")

print(str(cinema) + "\n")

print(cinema.prenota_film("Inception", 30) + "\n")
print(cinema.prenota_film("The Matrix", 160) + "\n")
print(cinema.prenota_film("The Matrix", 120) + "\n")
print(cinema.prenota_film("Avatar", 50) + "\n")

print(str(cinema) + "\n")

"""
Gestione di un magazzino
Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino, 
cercare prodotti per nome e verificare la disponibilità di un prodotto.

Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 
Test case:
- Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. Successivamente, aggiunge i prodotti al magazzino.
- Il sistema cerca un prodotto per verificare se esiste nell'inventario.
- Il sistema verifica la disponibilità dei prodotti in inventario.
"""

class Prodotto:
    def __init__(self, nome: str, quantita: int):
        self.nome = nome
        self.quantita = quantita

class Magazzino:
    def __init__(self):
        self.scaffali = []

    def aggiungi_prodotto(self, prodotto: Prodotto):
        for p in self.scaffali:
            if p.nome == prodotto.nome:
                p.quantita += prodotto.quantita
                return
        self.prodotti.append(prodotto)

    def cerca_prodotto(self, nome: str) -> Prodotto:
        for p in self.scaffali:
            if p.nome == nome:
                return p
        return None
    
    def verifica_disponibilità(self, nome: str) -> str:
        prodotto = self.cerca_prodotto[nome]

        if prodotto:
            return f'{prodotto} è disponibile in magazzino in {prodotto.quantita} pezzi'
        else:
            return f'{prodotto} non è disponibile in magazzino'
        
magazzino = Magazzino()
magazzino.aggiungi_prodotto(Prodotto("Mela", 50))
magazzino.aggiungi_prodotto(Prodotto("Banana", 30))
magazzino.aggiungi_prodotto(Prodotto("Mela", 20)) 


prodotto = magazzino.cerca_prodotto("Mela")
if prodotto:
    print(prodotto)
else:
    print("Prodotto non trovato.")


print(magazzino.verifica_disponibilità("Mela"))
print(magazzino.verifica_disponibilità("Arancia"))