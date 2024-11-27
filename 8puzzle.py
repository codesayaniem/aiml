import heapq
import time
import os
import psutil
import uuid
import re  # Add this import

class Puzzle:
    def __init__(self, board, goal):
        self.board = board
        self.goal = goal
        self.n = len(board)
        self.empty = self.find_empty()

    def find_empty(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def is_goal(self):
        return self.board == self.goal

    def get_neighbors(self):
        neighbors = []
        x, y = self.empty
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                neighbors.append(Puzzle(new_board, self.goal))
        return neighbors

    def manhattan_distance(self):
        distance = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] != 0:
                    x, y = divmod(self.board[i][j] - 1, self.n)
                    distance += abs(x - i) + abs(y - j)
        return distance

    def __lt__(self, other):
        return self.manhattan_distance() < other.manhattan_distance()

def a_star(initial, goal):
    open_set = []
    heapq.heappush(open_set, (0, initial))
    came_from = {}
    g_score = {str(initial.board): 0}
    f_score = {str(initial.board): initial.manhattan_distance()}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current.is_goal():
            return reconstruct_path(came_from, current)

        for neighbor in current.get_neighbors():
            tentative_g_score = g_score[str(current.board)] + 1
            if str(neighbor.board) not in g_score or tentative_g_score < g_score[str(neighbor.board)]:
                came_from[str(neighbor.board)] = current
                g_score[str(neighbor.board)] = tentative_g_score
                f_score[str(neighbor.board)] = tentative_g_score + neighbor.manhattan_distance()
                heapq.heappush(open_set, (f_score[str(neighbor.board)], neighbor))

    return None

def reconstruct_path(came_from, current):
    path = []
    while str(current.board) in came_from:
        path.append(current.board)
        current = came_from[str(current.board)]
    path.append(current.board)
    path.reverse()
    return path

def get_mac_address():
    return ':'.join(re.findall('..', '%012x' % uuid.getnode()))

def main():
    initial_state = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
    goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

    initial_puzzle = Puzzle(initial_state, goal_state)

    start_time = time.time()
    solution = a_star(initial_puzzle, goal_state)
    end_time = time.time()

    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()

    print("MAC Address:", get_mac_address())
    print("Memory Consumed:", memory_info.rss, "bytes")
    print("Time Consumed:", end_time - start_time, "seconds")

    if solution:
        for step in solution:
            for row in step:
                print(row)
            print()
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()

