#es1
def find_element(lst: list[int], element: int) -> bool:
   
    if element in lst:
        return True
    else: 
        return False
        

print(find_element([1, 2, 3, 4, 5], 5))
print(find_element([1, 2, 3, 4, 5], 6))
print(find_element([10, 20, 30], 20))
print("-------------------------------")

#es2
def frequency_dict(elements: list) -> dict:
    frequency_map = {}
    for element in elements:
        frequency_map[element] = frequency_map.get(element, 0) +1
    return frequency_map

print(frequency_dict(['mela', 'banana', 'mela']))
print("-------------------------------")

#es3
def is_magic_number(num: int) -> bool:
    num_s = str(num)
    if "7" not in num_s:
        return False
    else:
        return True
#es4
def countdown(n: int) -> int:
    for i in range(n, -1, -1):
        print(i)
#es5
def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return sum(numbers) * len(numbers) 
    else:
        return sum(numbers) / len(numbers) 
#es6
def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    
    if conditionA is True:
        return "Operazione permessa"
    elif conditionB and conditionC == True:
        return "Operazione permessa"
    else:
        return "Operazione negata"
print(check_combination(True, False, True))
#es7
def check_parentheses(expression: str) -> bool:
    lst1:list = []
    lst2:list = []
    
    for i in expression:
        if len(lst2)>len(lst1):
             return False
        if i == ')':
            lst2.append(i)
        elif i == '(':
            lst1.append(i)
        else:
            continue
    
    return True 
#es8
def count_isolated(num:int) -> int:
    count = 0
    for i in range(len(num)):
        if i == 0 and num[i] != num[i+1]:
            count+=1
        elif i == len(num)-1 and num[i] != num[i-1]:
            count+=1
        elif num[i] != num[i-1] and num[i] != num[i+1]:
            count+=1
    return count
#es9
def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
   return original_set - set(elements_to_remove)
#es10
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    dict3 = dict1 | dict2
    for i in dict3:
        if i in dict1 and i in dict2:
            dict3[i] = dict1[i] + dict2[i]
    return dict3