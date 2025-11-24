#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

class Node:
    def depth():
        raise NotImplementedError("Abstract method")

class Document(Node):
    def __init__(self, name: str, text: str):
        self._name = name
        self._text = text
    
    def depth(self):
        return 0

class Folder(Node):
    def __init__(self, name: str, subnodes: list[Node]):
        self._name = name
        self._subnodes = subnodes

    def depth(self):
        max_depth = max(node.depth() for node in self._subnodes)
        return 1 + max_depth

def main():
    prod = Document("prod.csv", "1,2,3,4")
    data = Folder("data", [prod])
    a1_0 = Document("a1.txt", "bla bla 0")
    work = Folder("Work", [a1_0, data])
    a1_1 = Document("a1.txt", "a different file")
    personal = Folder("Personal", [a1_1])
    desktop = Folder("Desktop", [work, personal])
    print(desktop.depth())
    
if __name__ == "__main__":
    main()
