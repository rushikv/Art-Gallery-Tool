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

# Run on Windows
* Download the ```Art Gallery setup.exe``` file from the ```dist``` folder and run it to install the Art Gallery Tool.
* Run the Art Gallery Tool by executing ```Art Gallery Pedagogical Tool.exe``` from desktop shortcut or the location chosen to install the program.

# Run on Mac OS, Linux
## Requirements
* Python 3+ ([Python 3.6](https://www.python.org/downloads/release/python-363/))
### Python Libraries (use pip to download and install these libraries)
* Pygame  (```pip3 install pygame``` or ```pip install pygame```)
* EasyGui (```pip3 install easygui``` or ```pip install easygui```)
* NumPy (```pip3 install numpy``` or ```pip install numpy```)

## Steps to run
* Download all Python scripts from ```scripts``` folder.
* Open terminal in the folder that contains the scripts.
* Run command ```python3 ArtGallery.py``` or ```python ArtGallery.py``` to run the tool.

# Polygon Visibility from Vertex Algorithm
```
Given a simple polygon and a vertex
Maintain a list for storing invisible_edges = []
For every other vertex V:
	if V is visible:
    	if no invisible edges between previous visible vertex and V:
        	Add V to solution
        else:
        	Find the closest intersection point of the invisible edges
            with line[vertex, previous visible V] and line[vertex, V]
            from the vertex such that the V or previous visible V is
            on the segment[vertex, intersection]
            
            if the 2 edges that meet at previous visible V are on
            same sides of line[vertex, previous visible V]:
            	if the line from closest intersection point for 
                line[vertex, previous visible V] to previous visible V
                is in polygon:
                	Add closest intersection point to solution
             
            if the 2 edges that meet at previous visible V are on
            same sides of line[vertex, V]:
            	if the line from closest intersection point for 
                line[vertex, V] to V
                is in polygon:
                	Add closest intersection point to solution
            
            Add V to solution
    else if V is not visible:
    	add V to invisible_edges
```
    	

# Credits
* Ear Clipping Triangulation ([Polytri](https://github.com/bjorkegeek/polytri)). Thanks to David Björkevik ([bjorkegeek](https://github.com/bjorkegeek))
* M-Coloring using backtracking ([M-Coloring](https://github.com/divyanshumehta/graph-algo)). Thanks to Divyanshu Mehta ([divyanshumehta](https://github.com/divyanshumehta/graph-algo))

