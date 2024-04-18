from collections import deque

def jug_filling_problem(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque([((0, 0), 0, [])])  # (jug1_current, jug2_current), steps, sequence

    while queue:
        (jug1_current, jug2_current), steps, sequence = queue.popleft()

        if jug1_current == target or jug2_current == target or jug1_current + jug2_current == target:
            return steps, sequence

        if (jug1_current, jug2_current) in visited:
            continue

        visited.add((jug1_current, jug2_current))

        # Fill jug1
        queue.append(((jug1_capacity, jug2_current), steps + 1, sequence + ['Fill jug1']))

        # Fill jug2
        queue.append(((jug1_current, jug2_capacity), steps + 1, sequence + ['Fill jug2']))

        # Empty jug1
        queue.append(((0, jug2_current), steps + 1, sequence + ['Empty jug1']))

        # Empty jug2
        queue.append(((jug1_current, 0), steps + 1, sequence + ['Empty jug2']))

        # Pour jug1 to jug2
        pour_amount = min(jug1_current, jug2_capacity - jug2_current)
        queue.append(((jug1_current - pour_amount, jug2_current + pour_amount), steps + 1, sequence + ['Pour jug1 to jug2']))

        # Pour jug2 to jug1
        pour_amount = min(jug2_current, jug1_capacity - jug1_current)
        queue.append(((jug1_current + pour_amount, jug2_current - pour_amount), steps + 1, sequence + ['Pour jug2 to jug1']))
   
    return -1, []  # No solution found

# Example usage
jug1_capacity = 5
jug2_capacity = 3
target = 4

steps, sequence = jug_filling_problem(jug1_capacity, jug2_capacity, target)
print(f"Minimum steps required: {steps}")
print("Sequence of actions:")
for action in sequence:
    print(action)