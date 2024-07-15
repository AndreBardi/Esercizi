def classifica_numeri(lista: int) -> dict[str:list[int]]:
    nums = {'pari': [],
            'dispari': []
}
    for num in lista:
        if num % 2 == 0:
            nums['pari'].append(num)
        else:
            nums['dispari'].append(num)
    return nums

print("-----------------")


def somma_condizionale(numeri: list[int]) -> int :
    
    somma = 0
    for num in numeri:
         if num % 2 == 0 and num % 3 == 0:
             somma += num
    return somma

print("-----------------")

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    for i,n in da_rimuovere.items():
        for m in range(n):
            if i in lista:
                lista.remove(i)
    return lista

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    voti_studente = {}
    for voto in voti:
        nome = voto["nome"]
        voto_val = voto["voto"]
        if nome in voti_studente:
            voti_studente[nome].append(voto_val)
        else:
            voti_studente[nome] = [voto_val]
        return voti_studente