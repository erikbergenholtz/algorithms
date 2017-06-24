#!/usr/bin/env python

# astar.py
# Worst: O(|E|)
# Author: Erik Bergenholtz

import sys

graph = {
        "Start":[("A",7,9),("B",2,7),("C",3,8)],
        "A":[("Start",7,10),("B",3,7),("D",4,8)],
        "B":[("Start",2,10),("A",3,9),("D",4,8),("H",1,30)],
        "C":[("Start",3,10),("L",5,6)],
        "D":[("A",4,9),("B",4,7),("F",5,6)],
        "F":[("D",5,8),("H",3,30)],
        "G":[("H",2,30),("Dest",2,0)],
        "H":[("B",1,7),("F",3,6),("G",2,3)],
        "I":[("J",6,4),("K",4,3),("L",4,6)],
        "J":[("I",6,4),("K",4,3),("L",4,6)],
        "K":[("I",4,4),("J",4,4),("Dest",5,0)],
        "L":[("C",2,8),("I",4,4),("J",4,4)],
        "Dest":[("G",2,3),("K",5,3)]
        }

INF = float("INF")

def smallest(unvisited):
    s = None
    for n,w in unvisited.iteritems():
        if s == None:
            s = (n, w)
        elif w[0] < s[1][0]:
            s = (n, w)
    return s

def isVisited(k,visited):
    for n in visited:
        if n == k:
            return True

def isFinished(visited,unvisited):
    if isVisited("Dest",visited) or smallest(unvisited)[1] == INF:
        return True
    return False

def astar(g):
    visited = {}
    unvisited = {}
    for k,v in graph.iteritems():
        w = INF
        if k == "Start":
            w = 0
        unvisited[k] = (w,"")
    cur = smallest(unvisited)
    while not isFinished(visited,unvisited):
        for k,n,h in graph[cur[0]]:
            if not isVisited(k,visited):
                tw = cur[1][0]+n+h
                if tw < unvisited[k][0]:
                    unvisited[k] = (tw,cur[0])
        visited[cur[0]] = cur[1]
        unvisited.pop(cur[0],None)
        cur = smallest(unvisited)
    return visited

def printPath(visited):
    cur = visited["Dest"]
    path = ["Dest"]
    while cur[1] != "":
        path.insert(0,cur[1])
        cur = visited[cur[1]]
    for p in path:
        sys.stdout.write(p)
        if p != path[-1]:
            sys.stdout.write(" -> ")
    print

def main():
    global visited
    printPath(astar(graph))

if __name__ == '__main__':
    main()
