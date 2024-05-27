import random

def position(t_position: int,
             h_position: int,
             path: list[int]):
    
    path: list[int] = ["_"] * 70
    path[t_position[0]] = "T"
    path[h_position[0]] = "H"

def t_move(t_position):
    i = random.randint(1, 10)
    if 1 <= i <= 5:
        t_position += 3
    if 6 <= i <= 7:
        t_position -= 6
    if 8 <= i <= 10:
        t_position += 1
    return t_position        

def h_move(h_position):
    i = random.randint(1, 10)
    if 1 <= i <= 2:
        h_position += 0
    if 3 <= i <= 4:
        h_position += 9
    if i == 5:
        h_position -= 12
    if 6 <= i <= 8:
        h_position += 1
    if 9 <= i <= 10:
        h_position -= 2

def begin_race():
    t_position = 1
    h_position = 1

    print("BANG !!!!! AND THEY'RE OFF !!!!!")

    while True:
        pass