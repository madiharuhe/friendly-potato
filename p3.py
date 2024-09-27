def bfs(src, target):
    queue, visited = [src], set()

    while queue:
        state = queue.pop(0)
        visited.add(tuple(state))
        if state == target: return print("Success:", state)
        for d in (-3, 3, -1, 1):
            b = state.index(0)
            if 0 <= b + d < 9 and (b % 3 != 2 or d != 1) and (b % 3 != 0 or d != -1):
                new_state = state[:]
                new_state[b], new_state[b + d] = new_state[b + d], new_state[b]
                if tuple(new_state) not in visited: queue.append(new_state)

src = [1, 2, 3, 4, 5, 6, 0, 7, 8]
target = [1, 2, 3, 4, 5, 6, 7, 8, 0]
bfs(src, target)
