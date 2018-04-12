#!/usr/bin/env python

# dijkstra.py
# Worst: O(|E|+|V| log|V|)
# Author: Erik Bergenholtz

import sys

graph = {
        "Start":[("A",7),("B",2),("C",3)],
        "A":[("Start",7),("B",3),("D",4)],
        "B":[("Start",2),("A",3),("D",4),("H",1)],
        "C":[("Start",3),("L",5)],
        "D":[("A",4),("B",4),("F",5)],
        "F":[("D",5),("H",3)],
        "G":[("H",2),("Dest",2)],
        "H":[("B",1),("F",3),("G",2)],
        "I":[("J",6),("K",4),("L",4)],
        "J":[("I",6),("K",4),("L",4)],
        "K":[("I",4),("J",4),("Dest",5)],
        "L":[("C",2),("I",4),("J",4)],
        "Dest":[]
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

def dijkstra(g):
    visited = {}
    unvisited = {}
    for k,v in graph.iteritems():
        w = INF
        if k == "Start":
            w = 0
        unvisited[k] = (w,"")
    cur = smallest(unvisited)
    while not isFinished(visited,unvisited):
        for k,n in graph[cur[0]]:
            if not isVisited(k,visited):
                tw = cur[1][0]+n
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
    printPath(dijkstra(graph))

if __name__ == '__main__':
    main()
