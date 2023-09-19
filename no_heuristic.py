# imports
import copy
import time

# variables
initial_state = {
    'value': [[0, 2, 3], [1, 5, 6], [4, 7, 8]], 
    'path': 'start'
}
queue = []
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
    new['value'][black_row][black_column], new['value'][black_row - 1][black_column] = new['value'][black_row - 1][black_column], 0
    new['path'] += ' up'
    return new

# down move func
def down_move(new_state, black_row, black_column):
    new = copy.deepcopy(new_state)
    new['value'][black_row][black_column], new['value'][black_row + 1][black_column] = new['value'][black_row + 1][black_column], 0
    new['path'] += ' down'
    return new

# right move func
def right_move(new_state, black_row, black_column):
    new = copy.deepcopy(new_state)
    new['value'][black_row][black_column], new['value'][black_row][black_column + 1] = new['value'][black_row][black_column + 1], 0
    new['path'] += ' right'
    return new

# left move func
def left_move(new_state, black_row, black_column):
    new = copy.deepcopy(new_state)
    new['value'][black_row][black_column], new['value'][black_row][black_column - 1] = new['value'][black_row][black_column - 1], 0
    new['path'] += ' left'
    return new

# func to manage the function above
move_functions = {
    'up_move': up_move,
    'down_move': down_move,
    'left_move': left_move,
    'right_move': right_move
}

# the main algorithm
def starA(state):
    queue.append(state)
    already_visited.append(state)

    while queue:
        movements.clear()
        current_state = queue.pop(0)

        if (current_state['value'][0][0] == 1 and current_state['value'][0][1] == 2 and current_state['value'][0][2] == 3 and
            current_state['value'][1][0] == 4 and current_state['value'][1][1] == 5 and current_state['value'][1][2] == 6
            and current_state['value'][2][0] == 7 and current_state['value'][2][1] == 8 and current_state['value'][2][2] == 0):
                timer_stop = time.time()

                print('Nodos Visitados: ', len(already_visited))
                print(' ')
                print('victory path: ', current_state['path'])
                print(' ')
                # this '-1' is here to not count the 'start'
                print('Number of movements: ', count_movements(current_state['path']) - 1)
                print(' ')
                print('time in seconds: ', round(timer_stop - timer_start, 2))

                exit()

        row, column = find_blank_tile(current_state['value'])

        for move in movements:
            new_state = move_functions[move](current_state, row, column)

            if new_state not in already_visited:
                queue.append(new_state)
                already_visited.append(new_state)

timer_start = time.time()
starA(initial_state)
