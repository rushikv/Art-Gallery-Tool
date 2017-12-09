"""
PolygonVisibility.py
authors:
Rushik Vartak (rv9981@g.rit.edu)
Yeshwanth Raja (yr8662@g.rit.edu)
description: Compute Visibility polygon for a vertex
"""

import math as m
from sympy.solvers import solve
from sympy import Symbol

def isclose(a, b, rel_tol=1e-04, abs_tol=0.0):
    """
    Function to compare if 2 values are equal with a precision
    :param a: Value 1
    :param b: Value 2
    :return:
    """
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def findST(S1x, S1y, D1x, D1y, S2x, S2y, D2x, D2y):
    """
    Find params 'S' & 'T' for 2 line segments
    :param S1x: x coordinate of segment 1's start point
    :param S1y: y coordinate of segment 1's start point
    :param D1x: x coordinate of segment 1's end point
    :param D1y: y coordinate of segment 1's end point
    :param S2x: x coordinate of segment 2's start point
    :param S2y: y coordinate of segment 2's start point
    :param D2x: x coordinate of segment 2's end point
    :param D2y: y coordinate of segment 2's end point
    :return: params S & T
    """
    s=Symbol('s')
    t = Symbol('t')
    ans=solve([(((1 - s) * S1x) + (s * D1x) - ((1 - t) * S2x) - (t * D2x)), (((1 - s) * S1y) + (s * D1y) - ((1 - t) * S2y) - (t * D2y))])
    if ans == []:
        return None, None
    if len(ans)==1:
        return None, None
    return ans[s], ans[t]

def Intersection(seg1x1,seg1y1,seg1x2,seg1y2,seg2x1,seg2y1,seg2x2,seg2y2):
    """
    Find intersection point of 2 line segments
    :param S1x: x coordinate of segment 1's start point
    :param S1y: y coordinate of segment 1's start point
    :param D1x: x coordinate of segment 1's end point
    :param D1y: y coordinate of segment 1's end point
    :param S2x: x coordinate of segment 2's start point
    :param S2y: y coordinate of segment 2's start point
    :param D2x: x coordinate of segment 2's end point
    :param D2y: y coordinate of segment 2's end point
    :return: Intersection point [x,y]
    """
    s,t= findST(seg1x1,seg1y1,seg1x2,seg1y2,seg2x1,seg2y1,seg2x2,seg2y2)
    if s==None and t==None:
        return [None, None]
    d = [seg1x2-seg1x1, seg1y2-seg1y1]
    x = seg1x1+d[0]*s
    y = seg1y1+d[1]*s
    return [float(x),float(y)]

def parallel(seg1,seg2):
    """
    Function to find if 2 segments are parallel
    :param seg1: Segment 1
    :param seg2: Segment 2
    :return: Boolean result
    """
    if Intersection(seg1[0][0],seg1[0][1],seg1[1][0], seg1[1][1], seg2[0][0],seg2[0][1],seg2[1][0], seg2[1][1])==[None,None]:
        return True
    return False

def orient(startP, endP, pt):
    """
    Find orientation of a point w.r.t. a line segment
    :param startP: start point of segment [x,y]
    :param endP: end point of segment [x,y]
    :param pt: point [x,y]
    :return: -1, 0, 1
    """
    orientation= (((startP[0]-pt[0])*(endP[1]-pt[1]))-((startP[1]-pt[1])*(endP[0]-pt[0])))

    if orientation<0:
        return -1
    elif orientation>0:
        return 1
    else:
        return 0

def isOnSeg(startP, endP, pt):
    """
    Function to find if a point on segment
    :param startP: Segment starting point
    :param endP: Segment ending point
    :param pt: Point
    :return: Boolean value
    """
    if startP[0]==endP[0]:
        if pt[0]==startP[0]:
            if startP[1]>=pt[1] and pt[1]>=endP[1]:
                return True
            elif endP[1]>=pt[1] and pt[1]>=startP[1]:
                return True
            else:
                return False
        else:
            return False
    elif startP[1]==endP[1]:
        if pt[1]==startP[1]:
            if startP[0]>=pt[0] and pt[0]>=endP[0]:
                return True
            elif endP[0]>=pt[0] and pt[0]>=startP[0]:
                return True
            else:
                return False
        else:
            return False
    if (isclose(((pt[0] - startP[0]) / (endP[0] - startP[0])),((pt[1] - startP[1]) / (endP[1] - startP[1])))):
        if startP[0] >= pt[0] and pt[0] >= endP[0] and startP[1]>=pt[1] and pt[1]>=endP[1]:
            return True
        elif startP[0] >= pt[0] and pt[0]>= endP[0] and endP[1]>=pt[1] and pt[1]>=startP[1]:
            return True
        if endP[0] >= pt[0] and pt[0] >= startP[0] and startP[1] >= pt[1] and pt[1] >= endP[1]:
            return True
        elif endP[0] >= pt[0] and pt[0] >= startP[0] and endP[1] >= pt[1] and pt[1] >= startP[1]:
            return True
        else:
            return False
    else:
        return False

def distance(p1, p2):
    """
    Distance between 2 points
    :param p1: Point 1
    :param p2: Point 2
    :return: Distance
    """
    return m.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2),1

def midpoint(startPt, endPt):
    """
    Midpoint of segment
    :param startPt: Starting point of segment
    :param endPt: Ending point of segment
    :return:
    """
    return [(startPt[0]+endPt[0])/2, (startPt[1]+endPt[1])/2]

def pointInsidePolygon(pt, edges, vertices):
    """
    Function to check if a point is inside the polygon
    :param pt: Point
    :param edges: Edges of the polygon
    :param vertices: Vertices
    :return: Boolean value
    """
    seg = [pt,[10000, pt[1]]]
    intersCount=0
    inters=[]
    for ei in range(len(edges)):
        inter = Intersection(edges[ei][0][0],edges[ei][0][1],edges[ei][1][0],edges[ei][1][1],seg[0][0],seg[0][1],seg[1][0],seg[1][1])
        if isOnSeg(edges[ei][0],edges[ei][1],pt):
            return True
        if inter!=[None,None]:
            if isOnSeg(seg[0],seg[1],inter) and isOnSeg(edges[ei][0],edges[ei][1],inter):
                if inter not in inters:
                    if inter not in vertices:
                        inters.append(inter)
                        intersCount+=1
                    else:
                        if edges[ei][0]==inter:
                            if (edges[(ei-1)%len(edges)][0][1]>pt[1] and edges[(ei)%len(edges)][1][1]<pt[1])\
                                or (edges[(ei-1)%len(edges)][0][1]<pt[1] and edges[(ei)%len(edges)][1][1]>pt[1]):
                                inters.append(inter)
                                intersCount += 1
                        elif edges[ei][1]==inter:
                            if (edges[(ei+1)%len(edges)][1][1]>pt[1] and edges[(ei)%len(edges)][0][1]<pt[1])\
                                or (edges[(ei-1)%len(edges)][1][1]<pt[1] and edges[(ei)%len(edges)][0][1]>pt[1]):
                                inters.append(inter)
                                intersCount += 1
        else:
            if edges[(ei-1)%len(edges)][0][1]>pt[1] and edges[(ei+1)%len(edges)][1][1]>pt[1]:
                intersCount-=2
            elif edges[(ei-1)%len(edges)][0][1]<pt[1] and edges[(ei+1)%len(edges)][1][1]<pt[1]:
                intersCount-=2
    if intersCount%2==0:
        return False
    else:
        return True


def computeVisibility(vertices, vertex):
    """
    Function to compute visibility of the polygon from a vertex
    :param vertices: Vertices of the polygon
    :param vertex: Vertex for which visibility is to be computed
    :return: Visibility polygon vertices
    """
    iV = vertices.index(vertex)
    VsTemp = []
    VsTemp.extend(vertices[iV+1:len(vertices)])
    VsTemp.extend(vertices[0:iV])
    Vs = VsTemp.copy()
    Es = []
    edges=[]
    visibility = [vertex]
    for i in range(len(vertices)):
        """ Make edge list """
        Es.append([vertices[i],vertices[(i + 1) % len(vertices)]])
        if vertex != vertices[i] and vertex != vertices[(i + 1) % len(vertices)]:
            edges.append([vertices[i],vertices[(i + 1) % len(vertices)]])

    visibility = [vertex]
    prevV = vertex
    flag_invisible = False
    invisilbe_edges = []
    for V in Vs:
        seg = [vertex, V]
        inters = []
        interVs = []
        for e in edges:
            if e[0]!=V and e[1]!=V:
                if not parallel(e,seg):
                    inter = Intersection(seg[0][0],seg[0][1],seg[1][0], seg[1][1], e[0][0], e[0][1], e[1][0], e[1][1])
                    if isOnSeg(e[0],e[1],inter):
                        if inter not in inters:
                            inters.append(inter)

        flag_closest = True
        validInters = []
        all_inters_vertices = True
        for inter in inters:
            if isOnSeg(vertex,V,inter):
                flag_closest=False
                if inter not in vertices:
                    all_inters_vertices = False
                    break
                else:
                    validInters.append(inter)
        flag_visible_vertex = False
        if flag_closest == False and all_inters_vertices == True:
            if V not in validInters:
                validInters.append(V)
            if vertex not in validInters:
                validInters.append(vertex)
            validInters.sort()
            flag_visible_vertex = True
            for i in range(len(validInters)-1):
                if not pointInsidePolygon(midpoint(validInters[i],validInters[i+1]),Es,vertices):
                    flag_visible_vertex = False
                    break
        if (flag_closest==True and pointInsidePolygon(midpoint(vertex,V), Es, vertices)) or flag_visible_vertex==True:
            if flag_invisible == False:
                visibility.append(V)

            else:
                seg1=[vertex, visibility[len(visibility)-1]]
                seg2=[vertex, V]
                interPrev = None
                interNext = None
                invisilbe_edges.append([V,prevV])
                for e in invisilbe_edges:
                    if not parallel(e, seg1):
                        inter = Intersection(seg1[0][0], seg1[0][1], seg1[1][0], seg1[1][1], e[0][0], e[0][1], e[1][0],
                                             e[1][1])
                        if isOnSeg(e[0], e[1], inter):
                            if inter!= visibility[len(visibility)-1]:
                                if distance(vertex, inter) > distance(visibility[len(visibility) - 1], inter):
                                    if interPrev==None:
                                        interPrev = inter
                                    elif distance(vertex,inter)<distance(vertex,interPrev):
                                        interPrev = inter
                            else:
                                i = vertices.index(visibility[len(visibility)-1])
                                if not (orient(vertex, vertices[i], vertices[(i + 1) % len(vertices)]) <= 0 and orient(
                                        vertex,vertices[i], vertices[(i - 1) % len(vertices)]) <= 0) and not (
                                            orient(vertex, vertices[i], vertices[(i + 1) % len(vertices)]) >= 0 and orient(
                                        vertex, vertices[i], vertices[(i - 1) % len(vertices)]) >= 0):
                                    if distance(vertex, inter)>distance(visibility[len(visibility)-1],inter):
                                        interPrev=inter



                    if not parallel(e, seg2):
                        inter = Intersection(seg2[0][0], seg2[0][1], seg2[1][0], seg2[1][1], e[0][0], e[0][1], e[1][0],
                                             e[1][1])
                        if isOnSeg(e[0], e[1], inter):
                            if inter!=V:
                                i = vertices.index(V)
                                if (orient(vertex, vertices[i],
                                               vertices[(i + 1) % len(vertices)]) <= 0 and orient(
                                        vertex, vertices[i], vertices[(i - 1) % len(vertices)]) <= 0) or (
                                                orient(vertex, vertices[i],
                                                       vertices[(i + 1) % len(vertices)]) >= 0 and orient(
                                            vertex, vertices[i], vertices[(i - 1) % len(vertices)]) >= 0):
                                    if distance(vertex, inter) > distance(V, inter):
                                        if interNext==None:
                                            interNext = inter
                                        elif distance(vertex,inter)<distance(vertex,interNext):
                                            interNext = inter
                if interPrev != None:
                    visibility.append(interPrev)
                if interNext != None:
                    visibility.append(interNext)

                visibility.append(V)
                flag_invisible = False
                invisilbe_edges = []
            prevV = V
        else:
            flag_invisible=True
            invisilbe_edges.append([V,prevV])
            prevV = V
    return visibility