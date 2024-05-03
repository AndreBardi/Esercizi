def visiting_tree_iterative(tree: dict[int, list[int]], root: int):
    result = {}
    node_number = {}
    curr_level = {}
    node_number_per_level = {}
    stack: list[int] = [(root, 0)]
    while stack: # while len(stack) != 0
     """   curr_node = stack.pop(0)
        result[curr_level] = result.get(curr_level, 0) + curr_level
        node_number_per_level[curr_level] = node_number_per_level.get(curr_level, 0) + 1
        if curr_node:
            print(curr_node)
            left_child, right_child = tree[curr_node]
            if left_child:
                stack.append(left_child,)
            if right_child:
                stack.append(right_child)
    return result """