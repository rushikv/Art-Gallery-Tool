# Art-Gallery-Tool
# Introduction
This is a Pedagogical tool for solving the Art Gallery problem using Triangulation and 3-coloring.
The Art gallery problem is the problem of determining the minimum number of guards required to guard an Art gallery room.
The room is a simple polygon (polygon with no holes and no crossings), and the guards are a set of points inside, on the edges or on the vertices of the polygon.<br>
Finding the exact number of point guards required to guard the entire room is an NP-Hard problem.<br>
Steve Fisk claims that to guard a simple polygonal room with n vertices, you never need more than floor(n/3) vertex guards.
In this tool, we find the sufficient number of vertex guards (points placed on the vertices of the polygon) required to guard the polygonal room with n vertices in O(n log n) time using Fisk’s proof.

# Implementation
We have used the following algorithms in this tool:
* Ear Clipping Algorithm for Triangulation [1]
* M-coloring using backtracking for 3-coloring [2]
* Polygon Visibility

# Installation for Windows
* Download the 'Art Gallery setup.exe' file from the '/dist/' folder and run it to install the Art Gallery Tool.
* Run the Art Gallery Tool by executing 'Art Gallery Pedagogical Tool.exe' from desktop shortcut or the location chosen to install the program.

# For Mac OS, Linux
## Requirements
* Python 3+ 
### Python Libraries
* Pygame
* EasyGui
* NumPy
