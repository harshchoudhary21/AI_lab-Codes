import heapq

def heuristic(state):
    num_attacking_pairs = 0
    for (r1, c1) in enumerate(state):
        for (r2, c2) in enumerate(state):
            if (r1, c1) != (r2, c2):
                if r1 == r2 or c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
                    num_attacking_pairs += 1
    return num_attacking_pairs // 2

def a_star():
    initial_state = tuple(range(8))
    frontier = [(heuristic(initial_state), initial_state)]
    while frontier:
        _, state = heapq.heappop(frontier)
        if heuristic(state) == 0:
            return state
        for next_state in successors(state):
            heapq.heappush(frontier, (heuristic(next_state), next_state))
    return None

def gbfs():
    initial_state = tuple(range(8))
    frontier = [(heuristic(initial_state), initial_state)]
    while frontier:
        _, state = heapq.heappop(frontier)
        if heuristic(state) == 0:
            return state
        for next_state in successors(state):
            heapq.heappush(frontier, (heuristic(next_state), next_state))
    return None

def successors(state):
    for r1 in range(8):
        for r2 in range(8):
            if r1 != r2:
                next_state = list(state)
                next_state[r1], next_state[r2] = next_state[r2], next_state[r1]
                yield tuple(next_state)

print("A* Solution:", a_star())
print("GBFS Solution:", gbfs())