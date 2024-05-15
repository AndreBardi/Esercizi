"""

s : int = input()
print(type(s))
if s.isdigit():
    s = int(s)
    print(f"Il tipo di s è {type(s)} col contenuto {s}")
else:
    print("Boh allora me ne vado via")
"""

d = {'h': 5, 'a': 2, 'b': 8, 's': 1}
# in output voglio
# dl = {'a':2/16, 'h':5/16, 'b': 0.5, 's': 1/16}
# dove 16 è 5+2+8+1
somma = 0
for key in d:
    somma += d[key]
dl = {}
for key in d:
    dl[key] = d[key] / somma

#d[chiave] = valore