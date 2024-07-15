def len_of_last_word(s: str) -> int:
    l: list[str] = s.split()
    s: str = ''.join(reversed(s))
    i: int = 0
    return len(l(-1))
 
 
"""   curr_len: int = 0
    while i < len(s):
        if s[i] != " ":
            curr_len += 1
        else:
            break
        i += 1
    return curr_len
"""