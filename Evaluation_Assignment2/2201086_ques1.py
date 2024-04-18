import heapq
import queue

class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = 0 if parent is None else parent.depth + 1
        self.cost = self.depth + self.heuristic()

    def __lt__(self, other):
        return self.cost < other.cost

    def blank_position(self):
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] == 0:
                    return i, j
        return None

    def state_copy(self):
        return [row[:] for row in self.state]

    def goal_state(self):
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.state == goal

    def heuristic(self):
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        misplaced = sum(s != g for row_s, row_g in zip(self.state, goal) for s, g in zip(row_s, row_g))
        return misplaced

    def expand(self):
        children = []
        empty_row, empty_col = self.blank_position()
        if empty_row > 0:
            new_state = self.state_copy()
            new_state[empty_row][empty_col], new_state[empty_row - 1][empty_col] = new_state[empty_row - 1][empty_col], new_state[empty_row][empty_col]
            children.append(Node(new_state, parent=self, action='up'))
        if empty_row < 2:
            new_state = self.state_copy()
            new_state[empty_row][empty_col], new_state[empty_row + 1][empty_col] = new_state[empty_row + 1][empty_col], new_state[empty_row][empty_col]
            children.append(Node(new_state, parent=self, action='down'))
        if empty_col > 0:
            new_state = self.state_copy()
            new_state[empty_row][empty_col], new_state[empty_row][empty_col - 1] = new_state[empty_row][empty_col - 1], new_state[empty_row][empty_col]
            children.append(Node(new_state, parent=self, action='left'))
        if empty_col < 2:
            new_state = self.state_copy()
            new_state[empty_row][empty_col], new_state[empty_row][empty_col + 1] = new_state[empty_row][empty_col + 1], new_state[empty_row][empty_col]
            children.append(Node(new_state, parent=self, action='right'))

        return children

    def a_star(self):
        nodes_expanded = 0
        nodes_generated = 1
        max_queue_length = 1
        queue = [(self.cost, self)]
        while queue:
            _, node = heapq.heappop(queue)
            if node.goal_state():
                return node.state, nodes_expanded, nodes_generated, max_queue_length, node.depth
            nodes_expanded += 1
            children = node.expand()
            nodes_generated += len(children)
            max_queue_length = max(max_queue_length, len(children))
            for child in children:
                heapq.heappush(queue, (child.cost, child))
        return None, nodes_expanded, nodes_generated, max_queue_length, self.depth


    def iterative_deepening_search(self):
     nodes_expanded = 0
     nodes_generated = 1
     max_queue_length = 1
     max_depth = 10
     while True:
        search_queue = queue.Queue()
        search_queue.put(self)
        depth_limit = max_depth
        while not search_queue.empty():
            node = search_queue.get()
            if node.goal_state():
                return node.state, nodes_expanded, nodes_generated, max_queue_length, node.depth
            if node.depth < depth_limit:
                nodes_expanded += 1
                children = node.expand()
                nodes_generated += len(children)
                max_queue_length = max(max_queue_length, len(children))
                for child in children:
                    search_queue.put(child)
        max_depth += 1
        return None, nodes_expanded, nodes_generated, max_queue_length, self.depth



initial_state = [[1,0,3], [4,2,5], [7,8,6]]
node = Node(initial_state)

# A* Search
result, nodes_expanded, nodes_generated, max_queue_length, solution_length = node.a_star()
print("A* Search:")
print("Solution: ", result)
print("Total number of nodes expanded: ", nodes_expanded)
print("Total number of nodes generated: ", nodes_generated)
print("Maximum length of the queue: ", max_queue_length)
print("Length of the solution path: ", solution_length)



result, nodes_expanded, nodes_generated, max_queue_length, solution_length = node.iterative_deepening_search()
print("Iterative Deepening Search:")
print("Solution: ", result)
print("Total number of nodes expanded: ", nodes_expanded)
print("Total number of nodes generated: ", nodes_generated)
print("Maximum length of the queue: ", max_queue_length)
print("Length of the solution path: ", solution_length)
