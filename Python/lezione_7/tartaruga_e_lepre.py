import random

def position(t_position: int, h_position: int) -> list[str]:
    path = ["_"] * 70
    if t_position < len(path):
        path[t_position] = "T"
    if h_position < len(path):
        path[h_position] = "H"
    if t_position == h_position:
        path[t_position] = "OUCH!!!"
        path[h_position] = "OUCH!!!"
    return path

def t_move(t_position: int, weather) -> int:
    i = random.randint(1, 10)
    if weather == 'rainy':
        t_position -= 1    
    if 1 <= i <= 5:
        t_position += 3
    if 6 <= i <= 7:
        t_position -= 6
    if 8 <= i <= 10:
        t_position += 1
    
    if i < 1:
        t_position = 1
    if i > 70:
        t_position = 70
    return t_position

def h_move(h_position: int, weather) -> int:
    i = random.randint(1, 10)
    if weather == 'rainy':
        h_position -= 2    
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

    if i < 1:
        h_position = 1
    if i > 70:
        h_position = 70
    return h_position

def begin_race():
    t_position = 1
    h_position = 1
    weather = 'sunny'
    tick = 0

    print("BANG !!!!! AND THEY'RE OFF !!!!!")

    while True:
        t_position = t_move(t_position, weather)
        h_position = h_move(h_position, weather)
        path = position(t_position, h_position)
        tick += 1
        new_weather = meteo(tick)

        print("".join(path))

        if t_position >= 70:
            print("TORTOISE WINS | YAY!!!")
            break
        if h_position >= 70:
            print("HARE WINS | YUCH!!!")
            break
        if t_position >= 70 and h_position >= 70:
            print("IT'S A TIE!!!")
            break
        if new_weather:
            weather = new_weather
            print("The weather has changed!")
            

def meteo(tick):
    if tick % 10 == 0:
        return random.choice(['rainy', 'sunny'])
    return None

begin_race()