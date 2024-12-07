from heapq import heappush, heappop
import heapq
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple, Optional


class Node:
    def __init__(self, position: Tuple[int, int], parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Estimated cost from current node to goal
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f


class MuseumEvacuation:
    def __init__(self):
        self.layout = [
            ['0', '0', '1', '0', 'E'],
            ['0', '1', '0', '1', '0'],
            ['P', '0', '0', '0', '0'],
            ['0', '1', '1', '1', '0'],
            ['0', '0', '0', '0', 'E']
        ]
        self.rows = len(self.layout)
        self.cols = len(self.layout[0])

    def find_person_and_exits(self) -> Tuple[Tuple[int, int], List[Tuple[int, int]]]:
        """Find the position of the person (P) and all emergency exits (E)."""
        person_position = None
        exit_positions = []

        for row_index in range(self.rows):
            for col_index in range(self.cols):
                cell = self.layout[row_index][col_index]
                if cell == 'P':
                    person_position = (row_index, col_index)
                elif cell == 'E':
                    exit_positions.append((row_index, col_index))

        return person_position, exit_positions

    def manhattan_distance(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> int:
        """Calculate Manhattan distance between two points"""
    
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) 

    def get_neighbors(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Get valid neighboring positions"""
        neighbors = []
        row, col = position
        
        #  left, down, right, up
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        for dx, dy in directions:
            new_col = col + dy
            new_row = row + dx
            
            # Limit Boundaries
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                if self.layout[new_row][new_col] != '1':
                    neighbors.append((new_row, new_col))
        
        return neighbors

    def find_evacuation_path(self) -> Optional[List[Tuple[int, int]]]:
        """Find shortest path to nearest emergency exit using A*"""
        start_pos, exits = self.find_person_and_exits()
        start = Node(start_pos)
        
        open_set = []
        closed_set = set()
        
        # Map function from position to node
        position_to_node = {start_pos: start}
        
        heappush(open_set, start)
        
        while open_set:
            current = heappop(open_set)
            # Exit Found
            if current.position in exits:
                path = []
                while current:
                    path.append(current.position)
                    current = current.parent
                return path[::-1]  # Reverse path to get start->goal
            
            closed_set.add(current.position)
            
            # Check all neighbors
            for neighbor_pos in self.get_neighbors(current.position):
                if neighbor_pos in closed_set:
                    continue
                    
                tentative_g = current.g + 1
                
                # Find the minimum h score to any exit
                h = min(self.manhattan_distance(neighbor_pos, exit_pos) for exit_pos in exits)
                
                neighbor = position_to_node.get(neighbor_pos)
                if neighbor is None:
                    neighbor = Node(neighbor_pos, current)
                    position_to_node[neighbor_pos] = neighbor
                elif tentative_g >= neighbor.g:
                    continue
                    
                neighbor.parent = current
                neighbor.g = tentative_g
                neighbor.h = h
                neighbor.f = neighbor.g + neighbor.h
                
                if neighbor not in open_set:
                    heappush(open_set, neighbor)
        
        return None  

    def display_path(self, path: List[Tuple[int, int]]):
        """Display the evacuation path on the museum layout"""
        # TODO: Implement this method
        pass
    
    def visualize(self, path: List[Tuple[int, int]] = None):
        """
        Visualize the museum layout with matplotlib.
        If path is provided, it will be shown in green.
        """
        # Create figure with smaller size and better cell proportion
        fig, ax = plt.subplots(figsize=(6, 6))
        
        # Create color map with distinct colors
        cmap = plt.cm.colors.ListedColormap(['#FFFFFF', '#404040', '#FF4444', '#4444FF', '#FFCC00'])
        
        # Convert layout to numeric array for visualization
        numeric_layout = np.zeros((self.rows, self.cols))
        text_annotations = []  # Store text annotations for cells
        
        for i in range(self.rows):
            for j in range(self.cols):
                if self.layout[i][j] == '1':  # Wall
                    numeric_layout[i][j] = 1
                    text_annotations.append((i, j, ''))
                elif self.layout[i][j] == 'E':  # Exit
                    numeric_layout[i][j] = 2
                    text_annotations.append((i, j, 'EXIT'))
                elif self.layout[i][j] == 'P':  # Person
                    numeric_layout[i][j] = 3
                    text_annotations.append((i, j, 'P'))
                else:  # Free space
                    text_annotations.append((i, j, ''))
        
        # Add path if provided
        if path:
            for row, col in path[1:-1]:  # Skip start and end positions
                numeric_layout[row][col] = 4
                text_annotations.append((row, col, '→'))

        # Plot the layout
        im = ax.imshow(numeric_layout, cmap=cmap)
        
        # Add cell borders
        for i in range(self.rows + 1):
            ax.axhline(i - 0.5, color='black', linewidth=1)
        for j in range(self.cols + 1):
            ax.axvline(j - 0.5, color='black', linewidth=1)
        
        # Add text annotations
        for i, j, text in text_annotations:
            if text:  # Only add non-empty text
                color = 'white' if numeric_layout[i,j] in [1, 2, 3] else 'black'
                ax.text(j, i, text, ha='center', va='center', color=color, 
                       fontweight='bold', fontsize=10)
        
        # Remove ticks but keep grid lines
        ax.set_xticks([])
        ax.set_yticks([])
        
        # Add legend with smaller patches
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='#FFFFFF', edgecolor='black', label='Free Space'),
            Patch(facecolor='#404040', edgecolor='black', label='Wall'),
            Patch(facecolor='#FF4444', edgecolor='black', label='Exit'),
            Patch(facecolor='#4444FF', edgecolor='black', label='Person'),
        ]
        if path:
            legend_elements.append(Patch(facecolor='#FFCC00', edgecolor='black', label='Path'))
            
        ax.legend(handles=legend_elements, 
                 loc='center left',
                 bbox_to_anchor=(1.05, 0.5),
                 title='Legend',
                 frameon=True,
                 fontsize='small')
        
        plt.title('Museum Layout', pad=10)
        plt.tight_layout()
        plt.show()



def left(position: Tuple[int, int]) -> Tuple[int, int]:
    return (position[0], position[1] - 1)

def right(position: Tuple[int, int]) -> Tuple[int, int]:
    return (position[0], position[1] + 1)

def top(position: Tuple[int, int]) -> Tuple[int, int]:
    return (position[0] - 1, position[1])

def bottom(position: Tuple[int, int]) -> Tuple[int, int]:
    return (position[0] + 1, position[1])
