# if you want to change between heuristics, change line 60 and 150.

#imports
import copy
import time
import heapq

class Node:
    def __init__(self, state, cost, path):
        self.state = state
        self.cost = cost
        self.path = path

    # used to define 'less than' at the heap comparation, it is native from python.
    def __lt__(self, other):
        return self.cost < other.cost

# my heap implemented at a class to use node class.
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, node):
        heapq.heappush(self.heap, node)

    def pop(self):
        return heapq.heappop(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

# counter heuristic
def counter_heuristic(state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                count += 1
    # math represantion of manhattan_counter_heuristic.
    return count

# manhattan heuristic
def manhattan_counter_heuristic(state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    count = 0
    distance = 0
    for i in range(3):
        for j in range(3):
            row = (state[i][j] - 1) // 3
            col = (state[i][j] - 1) % 3
            distance += abs(row - i) + abs(col - j)

            if state[i][j] != goal_state[i][j]:
                count += 1
    # math represantion of manhattan_counter_heuristic.
    return distance + (count * 0.1)

# variables
initial_state = Node([[8, 7, 6], [5, 4, 3], [2, 1, 0]], manhattan_counter_heuristic([[8, 7, 6], [5, 4, 3], [2, 1, 0]]), 'start')
queue = PriorityQueue()
already_visited = []
movements = []
moves = [
    ('up_move', (-1, 0)),
    ('down_move', (1, 0)),
    ('left_move', (0, -1)),
    ('right_move', (0, 1))
]

# func to find the blank space
def find_blank_tile(state):
    for row in range(3):
        for column in range(3):
            if state[row][column] == 0:
                possible_movements(row, column)
                return row, column

# func to find the possible movements
def possible_movements(row, column):
    for move, (x, y) in moves:
        new_row, new_col = row + x, column + y
        
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            movements.append(move)

# func to count how many movements we did.
def count_movements(movements_str):
    return len(movements_str.split())

# up move func
def up_move(new_state, black_row, black_column):
    new = copy.deepcopy(new_state)
    new.state[black_row][black_column], new.state[black_row - 1][black_column] = new.state[black_row - 1][black_column], 0
    new.path += ' up'
    return new

# down move func
def down_move(new_state, black_row, black_column):
    new = copy.deepcopy(new_state)
    new.state[black_row][black_column], new.state[black_row + 1][black_column] = new.state[black_row + 1][black_column], 0
    new.path += ' down'
    return new

# right move func
def right_move(new_state, black_row, black_column):
    new = copy.deepcopy(new_state)
    new.state[black_row][black_column], new.state[black_row][black_column + 1] = new.state[black_row][black_column + 1], 0
    new.path += ' right'
    return new

# left move func
def left_move(new_state, black_row, black_column):
    new = copy.deepcopy(new_state)
    new.state[black_row][black_column], new.state[black_row][black_column - 1] = new.state[black_row][black_column - 1], 0
    new.path += ' left'
    return new

# func to manage the function above
move_functions = {
    'up_move': up_move,
    'down_move': down_move,
    'left_move': left_move,
    'right_move': right_move
}

# the main algorithm
def starA(nodo_inicial):
    queue.insert(nodo_inicial)
    already_visited.append(nodo_inicial.state)

    while queue:
        movements.clear()
        current_state = queue.pop()

        if (current_state.state[0][0] == 1 and current_state.state[0][1] == 2 and current_state.state[0][2] == 3 and
            current_state.state[1][0] == 4 and current_state.state[1][1] == 5 and current_state.state[1][2] == 6
            and current_state.state[2][0] == 7 and current_state.state[2][1] == 8 and current_state.state[2][2] == 0):
                timer_stop = time.time()

                print('Nodos Visitados: ', len(already_visited))
                print(' ')
                print('victory path: ', current_state.path)
                print(' ')
                # this '-1' is here to not count the 'start'
                print('Number of movements: ', count_movements(current_state.path) - 1)
                print(' ')
                print('time in seconds: ', round(timer_stop - timer_start, 2))

                exit()

        row, column = find_blank_tile(current_state.state)

        for move in movements:
            new_state = move_functions[move](current_state, row, column)

            new_state.cost = manhattan_counter_heuristic(new_state.state)

            if new_state.state not in already_visited:
                queue.insert(new_state)
                already_visited.append(new_state.state)

timer_start = time.time()
starA(initial_state)
