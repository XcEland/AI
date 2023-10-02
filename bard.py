import heapq
import math
import tkinter as tk
from tkinter import *
from tkinter import ttk

# Create a dictionary to store the city names
city_names = {
    'A': 'Harare',
    'B': 'Gweru',
    'C': 'Mutare',
    'D': 'Masvingo',
    'E': 'Bulawayo',
    'H': 'Beitbridge',
    'Z': 'Zvishavane'
}

# Create the graph
graph = {
    'A': [('D', 295), ('C', 216)],
    'B': [('C', 261), ('D', 183), ('E', 162), ('Z', 119)],
    'C': [('A', 216), ('B', 261)],
    'D': [('B', 183), ('A', 295), ('H', 290), ('Z', 97.1)],
    'E': [('B', 162), ('Z', 184), ('H', 323)],
    'H': [('E', 323), ('D', 290), ('Z', 335)],
    'Z': [('B', 119), ('D', 97.1), ('E', 184), ('H', 335)]
}

# Define the astar function
def astar(graph, start, end):
  """Finds the shortest path between two nodes in a graph using the A* search algorithm.

  Args:
    graph: A dictionary mapping node names to lists of neighboring nodes and edge costs.
    start: The name of the start node.
    end: The name of the end node.

  Returns:
    A list of node names representing the shortest path from the start node to the end node, or
    None if no path exists.
  """

  # Create a dictionary to store the distance to each vertex.
  distances = {vertex: float('infinity') for vertex in graph}
  distances[start] = 0

  # Create a dictionary to store the previous vertex in the path.
  previous_vertices = {
      vertex: None for vertex in graph
  }

  # Create a priority queue to store vertices that need to be visited.
  priority_queue = [(0, start)]

  while len(priority_queue) > 0:
    # Get the vertex with the smallest total cost from the priority queue.
    current_cost, current_vertex = heapq.heappop(priority_queue)

    # If we have reached the end vertex, we can stop.
    if current_vertex == end:
      path = []

      # Follow the previous_vertices dictionary to build the shortest path.
      while previous_vertices[current_vertex] is not None:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]

      # Add the start vertex to the path and return it in reverse order.
      path.append(start)
      return path[::-1]

    # If we haven't reached the end vertex yet, visit its neighbors.
    for neighbor, distance in graph[current_vertex]:
      # Calculate the total cost of visiting the neighbor vertex.
      new_cost = current_cost + distance + heuristic(neighbor, end)

      # If we have found a shorter path to the neighbor vertex, update its distance.
      if new_cost < distances[neighbor]:
        distances[neighbor] = new_cost
        previous_vertices[neighbor] = current_vertex
        heapq.heappush(priority_queue, (new_cost, neighbor))

  # If we have visited all the vertices and haven't found the end vertex, there is no path.
  return None

def heuristic(node, goal):
  """Estimates the cost of reaching the goal node from a given node.

  Args:
    node: The name of the current node.
    goal: The name of the goal node.

  Returns:
    A float representing the estimated cost of reaching the goal node from the current node.
  """

  # Calculate the Manhattan distance between the current node and the goal node.
  x1, y1 = node_coords[node]
  x2, y2 = node_coords[goal]
  manhattan_distance = abs(x1 - x2) + abs(y1 - y2)

  return manhattan_distance

# Create the GUI
root = tk.Tk()
root.title("Shortest Path Finder")

# Set the window size and position
root.geometry("800x600")
root.resizable(width=True, height=True)

# Set the background color
root.configure(bg="lightblue")

# Define the font and size for the text and buttons
font_style = ("Arial", 18)

# Add a header with the author's name
header_label = tk.Label(root, text="Shortest Path Between Cities", font=("Arial", 24), bg="white")
header_label.pack(pady=20)

author_label = tk.Label(root, text="UZ Campus", font=("Arial", 18), bg="white")
author_label.pack()

# Create a frame to hold the canvas and buttons
frame = tk.Frame(root)
frame.pack(side=tk.BOTTOM, pady=20)

# Create the canvas to draw the graph
canvas = tk.Canvas(root, width=600, height=500, bg="white")
canvas.pack(side=tk.TOP, padx=20, pady=20)

# Create a dictionary to store the coordinates of the nodes
node_coords = {
    'A': (100, 100),
    'B': (200, 200),
    'C': (300, 100),
    'D': (100, 300),
    'E': (400, 200),
    'H': (500, 100),
    'Z': (500, 300)
}

# Draw the nodes of the graph
node_radius = 20
for node, coord in node_coords.items():
    x, y = coord
    canvas.create_oval(x - node_radius, y - node_radius, x + node_radius, y + node_radius, fill="lightgray")
    canvas.create_text(x, y, text=city_names[node], font=font_style)

# Draw the edges of the graph
for node, edges in graph.items():
    x1, y1 = node_coords[node]
    for edge, distance in edges:
        x2, y2 = node_coords[edge]
        canvas.create_line(x1, y1, x2, y2)

# Create the source city label and combo box
source_label = tk.Label(frame, text="Start City:")
source_label.pack(side=tk.LEFT, padx=10, pady=10)
source_var = tk.StringVar(root)
source_var.set('Harare')
source_combo = tk.ttk.Combobox(frame, textvariable=source_var, values=list(city_names.values()))
source_combo.pack(side=tk.LEFT, padx=10, pady=10)

# Create the destination city label and combo box
dest_label = tk.Label(frame, text="Destination City:")
dest_label.pack(side=tk.LEFT, padx=10, pady=10)
dest_var = tk.StringVar(root)
dest_var.set('Gweru')
dest_combo = tk.ttk.Combobox(frame, textvariable=dest_var, values=list(city_names.values()))
dest_combo.pack(side=tk.LEFT, padx=10, pady=10)

# Create the button to find the shortest path
def find_shortest_path():
  start = None
  end = None

  # Get the source and destination cities from the dropdown menus
  for key, value in city_names.items():
    if value == source_var.get():
      start = key
    if value == dest_var.get():
      end = key

  # Find the shortest path and display it
  shortest_path = astar(graph, start, end)
  if shortest_path:
    path_str = ' -> '.join([city_names[vertex] for vertex in shortest_path])
    result_label.config(text=f"Shortest path: {path_str}")
    
    # Calculate the heuristic costs for each node
    heuristic_costs = {}
    for node in graph:
        heuristic_costs[node] = heuristic(node, end)
        
    # Clear the old heuristic costs from the canvas
    canvas.delete("heuristic_costs")
    
    # Display the heuristic costs on the nodes
    for node, coord in node_coords.items():
        x, y = coord
        canvas.create_text(x, y - 20, text=f"{heuristic_costs[node]}", font=font_style, tags="heuristic_costs")
    
    # Highlight the shortest path on the graph
    canvas.delete("highlight")
    for i in range(len(shortest_path) - 1):
      node1 = shortest_path[i]
      node2 = shortest_path[i+1]
      x1, y1 = node_coords[node1]
      x2, y2 = node_coords[node2]
      canvas.create_line(x1, y1, x2, y2, width=3, fill="blue", tags="highlight")
  else:
    result_label.config(text="No path found")
    canvas.delete("highlight")

find_button = tk.Button(frame, text="Calculate", command=find_shortest_path)
find_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Create the label to display the result
result_label = tk.Label(frame, text="")
result_label.pack(side=tk.RIGHT, padx=10, pady=10)

root.mainloop()