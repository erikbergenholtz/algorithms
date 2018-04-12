#!/usr/bin/env python3

import graphviz

BLACK = "lightgrey"
RED   = "red"

class RBTree:
    __NIL = {"key": "NIL", "color": BLACK, "left": None, "right": None, "parent": None}
    dumpid = 0

    def __init__(self):
        self.root = self.__NIL

    def Node(self, k, c=RED, l=__NIL, r=__NIL, p=__NIL):
        return {"key": k, "color": c, "left": l, "right": r, "parent": p}

    def __rotate(self, x, d):
        b = "right" if d == "left" else "left"
        y = x[b]
        x[b] = y[d]
        if y[d] != self.__NIL:
            y[d]["parent"] = x
        y["parent"] = x["parent"]
        if x["parent"] == self.__NIL:
            self.root = y
        elif x == x["parent"][d]:
            x["parent"][d] = y
        else:
            x["parent"][b] = y
        y[d] = x
        x["parent"] = y
        return y

    def left_rotate(self, x):
        y = x["right"]
        x["right"] = y["left"]
        if y["left"] != self.__NIL:
            y["left"]["parent"] = x
        y["parent"] = x["parent"]
        if x["parent"] == self.__NIL:
            self.root = y
        elif x == x["parent"]["left"]:
            x["parent"]["left"] = y
        else:
            x["parent"]["right"] = y
        y["left"] = x
        x["parent"] = y
        return y

    def right_rotate(self, x):
        y = x["left"]
        x["left"] = y["left"]
        if y["left"] != self.__NIL:
            y["left"]["parent"] = x
        y["parent"] = x["parent"]
        if x["parent"] == self.__NIL:
            self.root = y
        elif x == x["parent"]["left"]:
            x["parent"]["left"] = y
        else:
            x["parent"]["right"] = y
        y["left"] = x
        x["parent"] = y
        return y

    def insert_fixup(self, z):
        while z["parent"]["color"] == RED:
            if z["parent"] == z["parent"]["parent"]["left"]:
                y = z["parent"]["parent"]["right"]
                if y["color"] == RED:
                    z["parent"]["color"] = BLACK
                    y["color"] = BLACK
                    z["parent"]["parent"]["color"] = RED
                    z = z["parent"]["parent"]
                else:
                    if z == z["parent"]["right"]:
                        z = z["parent"]
                        z = self.__rotate(z, "left")
                        #z = self.left_rotate(z)
                    print("Got this far")
                    z["parent"]["color"] = BLACK
                    z["parent"]["parent"]["color"] = RED
                    z = self.__rotate(z["parent"]["parent"], "right")
                    #z = self.right_rotate(z["parent"]["parent"])
            else:
                y = z["parent"]["parent"]["left"]
                if y["color"] == RED:
                    z["parent"]["color"] = BLACK
                    y["color"] = BLACK
                    z["parent"]["parent"]["color"] = RED
                    z = z["parent"]["parent"]
                else:
                    if z == z["parent"]["left"]:
                        z = z["parent"]
                        z = self.right_rotate(z)
                    z["parent"]["color"] = BLACK
                    z["parent"]["parent"]["color"] = RED
                    z = self.left_rotate(z["parent"]["parent"])
        self.root["color"] = BLACK

    def insert(self, k):
        z = self.Node(k)
        y = self.__NIL
        x = self.root
        while x != self.__NIL:
            y = x
            if z["key"] < x["key"]:
                x = x["left"]
            else:
                x = x["right"]
        z["parent"] = y
        if y == self.__NIL:
            self.root = z
        elif z["key"] < y["key"]:
            y["left"] = z
        else:
            y["right"] = z
        self.insert_fixup(z)

    def delete(self, val):
        return

    def transplant(self, a, b):
        return

    def __dump(self, n, i):
        s = "{} [label=\"Key :{}\" style=filled fillcolor={}]\n".format(i, n["key"], n["color"])
        if n["left"] != self.__NIL:
            self.dumpid += 1
            s += "{} -- {} [label=\"{}\"]\n".format(i, self.dumpid, "left")
            s += self.__dump(n["left"], self.dumpid)
        if n["right"] != self.__NIL:
            self.dumpid += 1
            s += "{} -- {} [label=\"{}\"]\n".format(i, self.dumpid, "right")
            s += self.__dump(n["right"], self.dumpid)
        return s

    def dump(self):
        graph = "graph G{\n"
        graph += self.__dump(self.root, self.dumpid)
        graph += "}"
        print(graph)
        dot = graphviz.Source(graph)
        dot.render(view=True)





rb = RBTree()
rb.insert(10)
rb.insert(4)
rb.insert(2)
rb.insert(12)
rb.insert(13)
rb.insert(11)
rb.insert(8)

rb.dump()

#dot = Graph()
#dot.node('A')
#dot.node('B')
#dot.edges(["AB"])
#dot.render(view=True)
