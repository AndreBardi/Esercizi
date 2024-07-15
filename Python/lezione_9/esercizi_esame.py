"""def anagram(s: str, t: str) -> bool:
    
    s = s.lower()
    t = t.lower()
    return sorted(s) == sorted(t)

print("---------------------------")

class Account:
    def __init__(self, account_id):
        self.account_id = account_id
        self.balance = 0.0
    
    def deposit(self, amount):
        self.balance += amount
    
    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self, accounts: dict[str, Account]):
        self.accounts = accounts
        
    def create_account(account_id):
        ()


def construct(current,wordDict, memo={}):
        
    if current in memo:
        return memo[current]

    if not current:
        return True

    for word in wordDict:
        if current.startswith(word):
            new_current = current[len(word):]
            memo[current] = True
            if construct(new_current,wordDict,memo):
                
                return True

    memo[current] = False
    return False

    return construct(s,wordDict)


def valid_sudoku(board: list[list[str]]) -> bool:

    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
        
            num = board[i][j]
            if num != '.':                
                box_index = (i // 3) * 3 + (j // 3)                
                if num in rows[i]:
                    return False
                if num in columns[j]:
                    return False
                if num in boxes[box_index]:
                    return False

                rows[i].add(num)
                columns[j].add(num)
                boxes[box_index].add(num)
    
    return True

 	

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(valid_sudoku(board))


board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(valid_sudoku(board))

"""

"""class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next

def reverse(head: ListNode) -> list[int]:
    reversed_list: list[int] = []
    queue: list[ListNode] = [head]

    while queue:
        curr_node = queue.pop()
        if curr_node:
            reversed_list.append(curr_node.val)
            reverse(curr_node.next, reversed_list)

head = ListNode(val=0,
                next=ListNode(val=1,
                              next=ListNode(val=5,
                                            next=ListNode(val=6))))
print(reverse(head))"""
