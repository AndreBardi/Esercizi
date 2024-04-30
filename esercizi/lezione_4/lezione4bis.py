def is_palindrome(x : int) -> bool:


    s:str= str(x)
    i:int= 0
    s_len= len(s)
    while i < (s_len // 2):
        j = s_len - (i+1)
        if s[i] != s[j]:
          return False
        i += 1

    return True
print(is_palindrome(32323))

#def subtract (x : int, y : int):
#    z:int = x-y
#    return z
#print(subtract(10,5))
