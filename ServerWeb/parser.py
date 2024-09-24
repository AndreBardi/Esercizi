import ast
import json

mylist_1 = "['mario', 'gino', 'lucrezia']"

mylist_2 = ['mario', 'gino','lucrezia']



def SerializzaLista(res) -> str:
   res =  ast.literal_eval(mylist_1)
   return res



def Deserializzazione(mylist_2) -> str:
    return str(mylist_2)

def1 = SerializzaLista(mylist_1)
print(def1)
print(type(def1))

def2 = Deserializzazione(mylist_2)
print(def2)
print(type(def2))


def SerializzaJson1(dData,file_path):
    sData = json.dumps(dData)


def SerializzaJson2(dData,file_path):
    try:
        with open(file_path, "w") as myfile:
            json.dump(dData,myfile)
            return True
    except:
        return False
    

mydict_1 = { "brand": "Ford",
"electric": False,
"year": 1964,
"colors": ["red", "white", "blue"]}

mydict_2 = "{ 'brand':   'Ford'," + \
"'electric': False," + \
"'year': 1964," + \
"'colors': ['red', 'white', 'blue']}"

def SerializaJson(dData,file_path)-> bool:
    pass

def DeserializeJson(file_path) -> dict:
    json.dump()
    str1 = json.dumps(mydict_1)

    json.load
    dict_1 = json.loads(mydict_2)


    
def DeserializeJson1(sFilePath):
    sData = ""
    sAppo = ""
    try:
        with open(sFilePath, "r") as myfile:
            sAppo = myfile.read(500)
            while len(sAppo) == 500:
                sData += sAppo
                sAppo = myfile.read(500)
            if len(sAppo) > 0:
                sData += sAppo
        
        if len(sData) > 0:
            dData = json.loads(sData)
            return dData
        else:
            return None
            
    except:
        return None