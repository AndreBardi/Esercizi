def visit_tree(d: dict[int, list[int]], n: int):
    print(n)
    left_child, right_child = tree[n]
    if left_child:
        visit_tree(tree, left_child)
    if right_child:
        visit_tree(tree, right_child)


tree = {1:[2,3], 2:[4,5], 3:[None, None], 4:[None, None], 5:[None, None]}
visit_tree(tree, 1)