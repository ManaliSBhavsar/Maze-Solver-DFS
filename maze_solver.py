from collections import defaultdict
import tkinter as tk


def convert(a):
    adjList = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == ' ':
                adjList[i, j] = []
                if a[i][j + 1] == ' ':
                    adjList[i, j].append((i, j + 1))
                if a[i][j - 1] == ' ':
                    adjList[i, j].append((i, j - 1))
                if a[i - 1][j] == ' ':
                    adjList[i, j].append((i - 1, j))

                if a[i + 1][j] == ' ':
                    adjList[i, j].append((i + 1, j))
    return adjList


goal = (12, 15)


def dfs(visited, graph, node):
    if node == goal:
        print("Reached")
        print(visited)
        canvas.create_oval(6 * 30 + 5, 3 * 30 + 5, 7 * 30 - 5, 4 * 30 - 5, fill='white')
        root.update_idletasks()
        root.update()
        canvas.after(300)
        exit()
    elif node not in visited:
        c1 = canvas.create_oval(node[1] * 30 + 5, node[0] * 30 + 5, (node[1] + 1) * 30 - 5, (node[0] + 1) * 30 - 5, fill='white')
        print(node)
        root.update_idletasks()
        root.update()
        canvas.after(300)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
        canvas.after(1000, canvas.delete(c1))
        root.update_idletasks()
        root.update()

maze = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "X    X      X X         X",
    "XXXX XXXXXX X X XXXXXXX X",
    "X         X X X    X XX X",
    "XXXXXXXXX X X X XXXX XXXX",
    "X         X   X        XX",
    "XXXXXXX XXXX XXXXX XXXXXX",
    "X     X X X      X      X",
    "X XXX       XXXXXXXXX X X",
    "X     XXXXXXXXXX X  X X X",
    "XXXXX    X            X X",
    "X  X  XXXXXXX XXXXXXX XXX",
    "X XXX           X    X XX",
    "X X XX X XXXXXX XXXX X XX",
    "X X    X         X     XX",
    "X XXXX XXXX XXXX XXXXXXXX",
    "X     X      X    XX    X",
    "XXXXXXXXXXXX XXXX X XXXXX",
    "XX        X  X      X   X",
    "XXX XXXX XXXEXXXXXX XXXXX",
    "X   XX X  XXXX   X     XX",
    "XXXX XXX XX    XXXX XXXXX",
    "X         X             X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]
root = tk.Tk()
WIDTH = 750
HEIGHT = 720
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.configure(background='black')
graph = convert(maze)
visited = []
canvas.pack()
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == 'X':
            canvas.create_rectangle(j * 30, i * 30, (j + 1) * 30, (i + 1) * 30, fill='blue')
canvas.create_oval(6 * 30, 3 * 30, 7 * 30, 4 * 30, fill='yellow')
canvas.create_oval(15 * 30, 12 * 30, 16 * 30, 13 * 30, fill='red')
dfs(visited, graph, (3, 6))
