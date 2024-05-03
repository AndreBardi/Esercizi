"""
Date due stringhe note e magazine, restituisci true se note può essere
costruita utilizzando le lettere di magazine e false in caso contrario.
Ogni lettera nella magazine può essere utilizzata solo una volta in note.
"""

def ransom(note: str, magazine: str) -> bool:
    char_count: dict[str, int] = {}
    for char in magazine:
        char_count[char] = char_count.get(char, 0) + 1
        """if char in char_count:
            char_count[char] = char_count[char] + 1
        else:
            char_count[char] = 0"""
    for char in note:
        if char_count.get(char, 0) == 0:
            return False
        char_count[char] -= 1

    return True

print(ransom("a", "b")) #False
print(ransom("aa", "ab")) #False
print(ransom("aa", "aab")) #True
print(ransom("tu sei figo", "bella per te stai zitto, figo di qua e di là"))