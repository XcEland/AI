import heapq
import tkinter as tk
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

# Create a dictionary to store the city names

# Create a dictionary to store the city names
city_names = {
    'A': 'Harare',
    'B': 'Bulawayo',
    'C': 'Mutare',
    'D': 'Masvingo',
    'E': 'Gweru',
    'F': 'Kwekwe',
    'G': 'Chinhoyi',
    'H': 'Kadoma',
    'J': 'Zvishavane',
    'K': 'Marondera',
    'L': 'Rusape',
    'M': 'Beitbridge',
    'N': 'Chiredzi',
    'P': 'Birchenough Bridge'
}


# Create the graph
graph = {
    'A': [('D', 295), ('G', 116), ('H', 172), ('K', 75)],
    'B': [('M', 323), ('J', 184), ('E', 182)],
    'C': [('P', 127), ('L', 92.6), ('K', 189)],
    'D': [('M', 290), ('N', 204), ('P', 170), ('J', 97.1), ('A', 295), ('F', 200), ('E', 183)],
    'E': [('B', 182), ('D', 183), ('F',76), ('J', 119)],
    'F': [('E', 76), ('H', 84.2), ('D', 200)],
    'G': [('A', 116), ('H', 126)],
    'H': [('A', 172), ('G', 126), ('F', 84.2)],
    'J': [('B', 184), ('D', 97.1), ('E', 119), ('M', 335)],
    'K': [('A', 75), ('C', 189), ('L', 96)],
    'L': [('C', 92.6), ('K', 96)],
    'M': [('B', 323), ('D', 290), ('N', 246), ('J', 335)],
    'N': [('P', 197), ('M', 246), ('D', 204)],
    'P': [('C', 127), ('D', 170), ('N', 197)]
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
    A int representing the estimated cost of reaching the goal node from the current node.
  """

  # Calculate the Manhattan distance between the current node and the goal node.
  x1, y1 = node_coord[node]
  x2, y2 = node_coord[goal]
  manhattan_distance = abs(x1 - x2) + abs(y1 - y2)
  return int(manhattan_distance * 100)
  

# Create the GUI
root = tk.Tk()
root.title("Shortest Path Finder")

# Set the window size and position
root.geometry("800x600")
root.resizable(width=True, height=True)

# Set the background image
# Load the image
image = Image.open("E:/AI/bg.jpg")

# Create a canvas widget
canvas = tk.Canvas(root, width=image.width, height=image.height)
canvas.pack()

# Create a PhotoImage object from the image
photo_image = ImageTk.PhotoImage(image)

# Display the image on the canvas widget
canvas.create_image(0, 0, image=photo_image)
# Position the canvas behind other components
canvas.place(x=0, y=0)

# Define the font and size for the text and buttons
font_style = ("Arial", 18)

# Add a header with the author's name
header_label = tk.Label(root, text="Shortest Path Between Zimbabwean Cities", font=("Arial", 24), bg="white")
header_label.pack(pady=20)

author_label = tk.Label(root, text="A* Search Group 12", font=("Arial", 18), bg="white")
author_label.pack()

# Create a frame to hold the canvas and buttons
frame = tk.Frame(root)
frame.pack(side=tk.BOTTOM, pady=20)

# Create the canvas to draw the graph
canvas = tk.Canvas(root, width=1000, height=800)
canvas.pack(side=tk.TOP, padx=20, pady=20)

# Create a dictionary to store the coordinates of the nodes
node_coord = {
  'A': (-17.8292, 31.0522),
  #'A': (-17.8292, 31.0522),
  'B': (-20.1700, 28.5800),
  'C': (-18.9667, 32.6333),
  'D': (-20.0744, 30.8328),
  'E': (-19.4614, 29.8022),
  'F': (-18.9167, 29.8167),
  'G': (-17.3497, 30.1944),
  'H': (-18.3400, 29.9000),
  'J': (-20.3392, 29.9817),
  'K': (-18.1897, 31.5467),
  'L': (-18.4681, 32.6000),
  'M': (-22.2167, 30.0667),
  'N': (-20.6833, 31.5167),
  'P': (-20.3333, 32.7833)
}

#for display
node_coords = {
  'A': (500, 70),
  'B': (80, 450.0),
  'C': (800.0, 220.0),
  'D': (540.0, 260.0),
  'E': (200.0, 380.0),
  'F': (270.0, 300.0),
  'G': (300.0, 30.0),
  'H': (200.0, 200.0),
  'J': (330.0, 400.0),
  'K': (660.0, 100.0),
  'L': (670.0, 190.0),
  'M': (540.0, 480.0),
  'N': (680.0, 400.0),
  'P': (700.0, 300.0)
}

# Draw the nodes of the graph
node_radius = 10

# Draw the nodes of the graph
for node, coord in node_coords.items():
    x, y = coord
    canvas.create_oval(x - node_radius, y - node_radius, x + node_radius, y + node_radius, fill="blue")
    canvas.create_text(x, y, text=city_names[node], font=font_style)

# Draw the edges of the graph
for node, edges in graph.items():
    x1, y1 = node_coords[node]
    for edge, distance in edges:
        x2, y2 = node_coords[edge]
        # Draw the line
        canvas.create_line(x1, y1, x2, y2)
        # Retrieve the actual distance from the graph dictionary
        actual_distance = None
        for e, dist in graph[node]:
            if e == edge:
                actual_distance = dist
                break
        # Calculate the text coordinates
        text_x = (x1 + x2) / 2
        text_y = (y1 + y2) / 2 - 10
        # Display the distance value
        canvas.create_text(text_x, text_y, text=str(actual_distance), font=font_style)
        
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
    
    # Calculate the total actual distance along the shortest path
    total_distance = 0
    for i in range(len(shortest_path) - 1):
            node1 = shortest_path[i]
            node2 = shortest_path[i + 1]
            for edge, distance in graph[node1]:
                if edge == node2:
                    total_distance += distance
                    break
                  
    result_label.config(text=f"Shortest path: {path_str} (Total Distance: {total_distance} km.)")
    
    # Calculate the heuristic costs for each node
    heuristic_costs = {}
    for node in graph:
        heuristic_costs[node] = heuristic(node, end)
        
    # Clear the old heuristic costs from the canvas
    canvas.delete("heuristic_costs")
    
    # Display the heuristic costs on the nodes
    for node, coord in node_coords.items():
        x, y = coord
        canvas.create_text(x, y - 20, text=f"{heuristic_costs[node]}", font=font_style, fill="green", tags="heuristic_costs")
    
    # Highlight the shortest path on the graph
    canvas.delete("highlight")
    for i in range(len(shortest_path) - 1):
      node1 = shortest_path[i]
      node2 = shortest_path[i+1]
      x1, y1 = node_coords[node1]
      x2, y2 = node_coords[node2]
      canvas.create_line(x1, y1, x2, y2, width=3, fill="red", tags="highlight")
  else:
    result_label.config(text="No path found")
    canvas.delete("highlight")


find_button = tk.Button(frame, text="Calculate", command=find_shortest_path)
find_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Create the label to display the result
result_label = tk.Label(frame, text="")
result_label.pack(side=tk.RIGHT, padx=10, pady=10)

root.mainloop()